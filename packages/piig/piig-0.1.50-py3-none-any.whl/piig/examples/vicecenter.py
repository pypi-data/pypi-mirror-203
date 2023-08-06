#! /usr/bin/env python

import piig as g

from piig import csearch
from piig.examples import defs


class TOOL:
    def __init__(self, number, name, code=None):
        self.number = number
        self.name = name
        self.code = code if code is not None else number


#    def to_file_name(self):
#        return f"O{self.value:04}-{self.name}.nc"


# map of coords to DirectionInfo
# DIRECTION_INFO: Dict[str, "DirectionInfo"] = {}

MACHINE_ABS_HOME2 = g.Const(x=-15.0, y=-15.0, z=-2.0)

PROBE_RING_DIAMETER = 0.7
MACHINE_ABS_HOME2 = g.Const(x=-15.0, y=-15.0, z=-2.0)

MACHINE_ABS_Z0 = g.Const(z=0.0)
MACHINE_ABS_ZMIN = g.Const(z=-22.0)

MACHINE_ABS_KNOWN_LENGTH_CALIBRATE = g.Const(x=-1.16, y=-7.5, z=-8.0)

MACHINE_ABS_CLOSE_ABOVE_TOOL_TOUCH = g.Const(x=-1.16, y=-7.5, z=-7.6)

MACHINE_ABS_ABOVE_RING = g.Const(x=-16.46, y=-3.5, z=-22.7)
MACHINE_ABS_ABOVE_ROTARY = g.Const(x=-12.5214, y=-12.9896, z=-7.0)
MACHINE_ABS_ABOVE_SEARCH_ROTARY_LHS_5X8 = g.Const(x=-15.5, y=-17.50, z=-14.0)
m1 = g.Const(x=0.0, y=0.0, z=-0.7)
MACHINE_ABS_SEARCH_ROTARY_LHS_5X8 = [MACHINE_ABS_ABOVE_SEARCH_ROTARY_LHS_5X8, "+", m1]

MACHINE_ABS_ROTARY_HOME = g.Const(x=-12, y=0.0, z=-3.0)

MACHINE_ABS_ABOVE_VICE = g.Const(x=-28.0, y=-10.0, z=-16.00)
KNOWN_LENGTH_TOOL = 2

ORIGIN = g.Const(x=0, y=0, z=0)
DEBUG = False


@g.inline
def runit(ctx, var, sch):
    var.WCS = var.G55

    ctx.comment(
        "Find center of plate in vice,",
        f" result in {var.WCS}",
        *sch.comment,
    )

    ctx.insert_symbol_table(show_names=False)
    g.setup_probing(defs.Tool.PROBE)

    find_surface_before(ctx, var, sch)


class DInfo:
    name: str
    dxdy: list[float]
    opposite: str
    active_axis: int

    def __init__(self, name, opposite, axis, dxdy):
        self.name = name
        self.opposite = opposite
        self.active_axis = axis
        self.dxdy = dxdy


dinfo = {
    "left": DInfo("left", "right", 0, (-1, 0)),
    "right": DInfo("right", "left", 0, (1, 0)),
    "far": DInfo("far", "near", 1, (0, 1)),
    "near": DInfo("near", "far", 1, (0, -1)),
}


@g.inline
def prod_surface(ctx, var, sch, di, output):
    ctx.comment(
        "",
        f"Quickly move probe to find {di.name} edge",
    )

    addr = ctx.base_addr
    start_search = ctx.Const[2](sch.amin.xy * di.dxdy / 2.0)
    stop_search = ctx.Const[2](sch.amax.xy * di.dxdy / 2.0)
    delta = sch.delta * di.dxdy

    its = ctx.Var(
        (abs(stop_search - start_search) / sch.delta)[di.active_axis] + 1,
    )
    cursor = var.cursor

    cursor[di.active_axis] = start_search[di.active_axis]

    while its > 0:
        sch.goto(cursor)
        sch.fast_probe(z=sch.search_depth)
        if var.SKIP_POS.z < sch.search_depth + sch.iota:
            break
        cursor.xy += delta
        its.var -= 1
    else:
        ctx.error(f"Search for {di.name} failed")

    ctx.comment(
        f"back off a bit to the {di.name}, then slowly probe ",
        f"{di.opposite}wards for precise measurement.",
    )
    cursor.xy += sch.backoff * di.dxdy
    sch.goto(cursor.xy)
    sch.fast_probe([0, 0])
    output[di.active_axis] = (var.SKIP_POS + var.PROBE_R * di.dxdy)[di.active_axis]

    cursor.xy = var.SKIP_POS + var.PROBE_R * di.dxdy

    ctx.comment(
        "reposition above surface skim height,",
        f"just inside {di.name} edge",
    )

    sch.goto.relative(sch.backoff.xy * di.dxdy)
    sch.goto(z=sch.skim_distance)
    cursor.xy += -sch.indent.xy * di.dxdy
    sch.goto(cursor)
    ctx.base_addr = addr


@g.inline
def find_surface_before(ctx, var, sch):
    ctx.wcs = var.WCS

    print("FSB")
    sch.goto.machine(z=0)
    sch.goto.machine(xy=sch.above.xy)
    sch.goto.machine(z=sch.above.z)

    ctx.comment(f"Find top z roughly set {var.WCS}.z.")

    var.WCS.xyz = var.MACHINE_POS.xyz

    # fast find move down to min search distance
    sch.fast_probe(z=sch.amin.z)

    # make work offset z make rough top 0.
    var.WCS.z = var.MACHINE_POS.z
    ctx.alert("CHECK  G55 z")

    ctx.comment(
        "Now work.z should be 0 at surface",
        "and work.xy roughly middle",
    )
    sch.goto(z=sch.skim_distance)

    var.tlc = ctx.Vec[2]()
    var.brc = ctx.Vec[2]()

    var.cursor = ctx.Vec[2](0, 0)
    prod_surface(ctx, var, sch, dinfo["left"], var.tlc)
    prod_surface(ctx, var, sch, dinfo["near"], var.brc)
    prod_surface(ctx, var, sch, dinfo["far"], var.tlc)

    # move back to centerline
    sch.goto(0, 0)
    prod_surface(ctx, var, sch, dinfo["right"], var.brc)

    ctx.comment(
        " the 'error' between 0,0 and where we",
        " calculate the center to be gets",
        " added to cos and voila.",
    )

    var.error = ctx.Vec[2]((var.tlc + var.brc) / 2.0)
    var.WCS.xy += var.error.xy
    sch.goto(0, 0)

    ctx.comment(" final slow probe to find the surface z")
    sch.slow_probe(z=sch.search_depth)
    var.WCS.z = var.SKIP_POS.z

    sch.goto.machine(z=sch.above.z)
    ctx.alert("WHAT CHANGED")
    g.code("M99")


@g.inline
def vicecenter(ctx):
    print("TOP")
    g.haas_names(ctx.st)
    sch = csearch.SearchConstraint(
        # minimum size expected
        amin=g.Const(x=7.0, y=4.0, z=-5.0),
        # maximum size expected
        amax=g.Const(x=14.0, y=8.0, z=3.0),
        delta=g.Const(x=0.75, y=0.4),
        above=MACHINE_ABS_ABOVE_VICE + g.Const(x=0.0, z=0.0, y=-3.0),
    )
    sch.goto = ctx.goto.work.feed(650)
    sch.slow_probe = sch.goto.probe.feed(10)
    sch.fast_probe = sch.goto.probe.feed(50)
    runit(ctx, ctx.st, sch)


def main():
    g.p2git(vicecenter)


if __name__ == "__main__":
    main()
