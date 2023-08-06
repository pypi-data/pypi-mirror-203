import typing
import dataclasses


from piig import axis
from piig import exception as ex
from piig import gbl, coords

from piig import nd
from piig import op

# fast and slow and neither look up params.
# can be changed by using explicit feed.
# kwargs could contain x,y,z,feed ec
# as could extras

import enum


class MovementSpace(enum.IntEnum):
    WORK = enum.auto()
    MACHINE = enum.auto()
    RELATIVE = enum.auto()


def do_goto(self, *args, **kwargs):
    default_modifiers = {
        "relative": False,
        "feed": None,
        "probe": None,
        "work": None,
        "machine": False,
        "bp": False,
    }

    # split out arguments we understand from
    # ones for coordinates.
    co_args = {}
    for key, value in kwargs.items():
        match key:
            case "work":
                self._space = MovementSpace.WORK
            case "relative":
                self._space = MovementSpace.RELATIVE
            case "machine":
                self._space = MovementSpace.MACHINE
            case "feed":
                self._feed = value
            case "probe":
                self._probe = value
            case _:
                co_args[key] = value

    if self._bp:  # pragma: no cover
        breakpoint()

    values, l, sz = coords.unpack_cos_inner(args, co_args)

    res = ["G01"]

    match self._space:
        case MovementSpace.MACHINE:
            res.append("G90")
            res.append("G53")

        case MovementSpace.RELATIVE:
            res.append("G91")
        case MovementSpace.WORK:
            res.append("G90")
    if self._probe:
        res.append("G31")
        res.append(gbl.ctx.st.MUST_SKIP)

    if self._feed is None:
        raise SyntaxError("Need feed rate.")

    res.append(f"F{nd.to_gcode(self._feed)}")

    for aname, value in zip(axis.lnames, values):
        if value is not None:
            res.append(f"{aname}{nd.to_gcode(value)}")

    r = " ".join(res)

    nd.emit_stat(nd.makeCode(r))


@dataclasses.dataclass
class Goto:
    _bp: bool
    _space: MovementSpace
    _probe: bool
    _feed: float

    def __init__(self):
        self._bp = False
        self._probe = False
        self._space = MovementSpace.WORK
        self._feed = None

    def copy(self):
        res = Goto()
        res._bp = self._bp
        res._probe = self._probe
        res._space = self._space
        res._feed = self._feed
        return res

    @property
    def work(self):
        n = self.copy()
        n._space = MovementSpace.WORK
        return n

    @property
    def machine(self):
        n = self.copy()
        n._space = MovementSpace.MACHINE
        return n

    # pragma: no cover
    @property
    def bp(self):
        n = self.copy()
        n._bp = True
        return n

    @property
    def probe(self):
        n = self.copy()
        n._probe = True
        return n

    @property
    def relative(self):
        n = self.copy()
        n._space = MovementSpace.RELATIVE
        return n

    def feed(self, feed):
        n = self.copy()
        n._feed = feed
        return n

    def __call__(self, *args, **kwargs):
        do_goto(self, args, **kwargs)
