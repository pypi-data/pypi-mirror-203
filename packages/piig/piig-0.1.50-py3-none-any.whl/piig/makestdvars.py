#! /usr/bin/env python

"""
This program maintains the macro variable name to index and type
mapping.

Option --pretty lists the variables an easy to compare with the
vendor's manuals way.

Import the generated stdg.py to get classes which describe the macro
variables.

Option --reprint regenerrates data for mvars's own consumption; to
deal with format changes.

Option --regen is what it's all about, makes a new <foo>.py from data 
here.

Usage:
  mvars.py --regen <OUTFILE>
  mvars.py --pretty
  mvars.py --reprint


"""
import re

from itertools import zip_longest
from pathlib import Path

import docopt
import rich.console

from rich.table import Table


FIXED_OUTPUT = False
ASCLASS = 1
# instance name to write to.

if ASCLASS:
    #    DEF_PREFIX = "CTX."
    DEF_PREFIX = "dst."
    MAKER_PREFIX = "g."
    INDENT = "    "
else:
    MAKER_PREFIX = "G."
    DEF_PREFIX = ""
    INDENT = ""


class MV:
    def __lt__(self, other):
        return self.addr < other._addr

    def __init__(
        self, *, key, addr, alias=None, isrel=None, size=None, name="", typ=""
    ):
        self.typ = typ
        self.isrel = isrel
        self.key = key
        self.addr = addr

        self.name = name
        self.alias = alias
        self.size = size

        suffix = ""
        self.last = None
        if self.size:
            self.last = self.addr + self.size - 1
            if self.last != self.addr:
                suffix = f"..#{self.last}"

        self.range_as_text = f"#{self.addr}{suffix}"

    def for_reprint(self):
        funcname = self.__class__.__qualname__
        res = [str(self.addr)]
        if self.size is not None:
            res.append(f"size={self.size}")
        res = ", ".join(res)
        return f"dst.{self.name.ljust(20)} = {funcname}({res})"

    def for_pretty(self):
        return (
            self.range_as_text,
            str(self.size),
            self.key,
            self.typ,
            self.name,
        )

    def for_regen(self):
        return f"# {self.addr} .. {self.last} {self.name} .."


def one(addr, typ="Float"):
    return Gen(
        exp_name=f"Fixed{typ}",
        id_char="v" + typ[0],
        addr=addr,
        size=1,
        typ=typ,
    )


def IOne(addr):
    return one(addr, typ="Int")


class Alias(MV):
    def __init__(self, src):
        super().__init__(key="A", addr=src._addr, size=src.size, alias=src)

    def for_reprint(self):
        lhs = f"{DEF_PREFIX}{self.name.ljust(20)}"
        return f"{lhs} = Alias({DEF_PREFIX}{self.alias.name})"

    def for_regen(self):
        return f"{DEF_PREFIX}{self.name} = {DEF_PREFIX}{self.alias.name}"

    def for_pretty(self):
        return (
            self.range_as_text,
            str(self.size),
            self.key,
            self.typ,
            " also " + self.name,
        )


def Fixed(addr, size, typ="Float"):
    return Gen(
        exp_name="Fixed",
        id_char="V",
        addr=addr,
        size=size,
        typ=typ,
    )


class Gap(MV):
    C = 0

    def __init__(self, addr, size=None):
        super().__init__(key="_", addr=addr, size=size)
        self.name = "-"

    def for_reprint(self):
        self.name = f"gap{Gap.C:02}"
        Gap.C += 1
        return super().for_reprint()


class Gen(MV):
    def __init__(
        self,
        *,
        exp_name,
        id_char,
        addr,
        size=None,
        typ,
        isrel=None,
    ):
        self.exp_name = exp_name

        super().__init__(
            key=id_char,
            isrel=isrel,
            addr=addr,
            size=size,
            typ=typ,
        )

    def for_regen(self):
        rs = ""
        if self.isrel is not None:
            rs = f"isrel={self.isrel}, "
        sstr = ""
        if self.size is not None and self.size != 1:
            sstr = f"[{self.size}]"
        lhs = f"{DEF_PREFIX}{self.name}"
        return f"{lhs} = {MAKER_PREFIX}{self.exp_name}{sstr}({rs}addr={self.addr})"


def CWCPos(addr):
    return Gen(
        exp_name="CWCPos",
        id_char="m",
        addr=addr,
        size=20,
        typ="Float",
    )


def MachinePos(addr):
    return Gen(
        exp_name="MachinePos",
        id_char="m",
        addr=addr,
        size=20,
        typ="Float",
    )


def WorkOffsetTable(addr):
    return Gen(
        exp_name="WorkOffsetTable",
        id_char="W",
        addr=addr,
        typ="Float",
    )


def ToolTable(addr, size, typ="Float"):
    return Gen(
        exp_name="ToolTable",
        id_char="T",
        addr=addr,
        size=size,
        typ=typ,
    )


class PalletTable(MV):
    def __init__(self, addr, size):
        super().__init__(key="L", addr=addr, size=size, typ="Int")


class Names:
    interesting: list[MV]

    def __init__(self):
        object.__setattr__(self, "interesting", [])

    def write_to(self, out):
        for v in self.interesting:
            if "gap" in v.name:
                continue

            out.write(INDENT + v.for_regen() + "\n")

    def __setattr__(self, key, value):
        if key == "GAP":
            value = Gap(value)

        if key[0].isupper():
            if isinstance(value, int):
                value = one(value)
            value.name = key

            object.__setattr__(self, key, value)

        self.interesting.append(value)


class HaasNames(Names):
    title = "HAAS"

    def __init__(self):
        super().__init__()
        # pylint: ignore=R0902
        # pylint: ignore=R0915
        self.NULL = one(0)
        self.MACRO_ARGUMENTS = Fixed(1, size=33)
        self.gap01 = Gap(34, size=66)
        self.GP_SAVED1 = Fixed(100, size=100)
        self.gap02 = Gap(200, size=300)
        self.GP_SAVED2 = Fixed(500, size=50)

        self.PROBE_CALIBRATION1 = Fixed(550, size=6)
        self.PROBE_R = Fixed(556, size=3)
        self.PROBE_CALIBRATION2 = Fixed(559, size=22)

        self.GP_SAVED3 = Fixed(581, size=119)
        self.gap03 = Gap(700, size=100)
        self.GP_SAVED4 = Fixed(800, size=200)
        self.INPUTS = Fixed(1000, size=64)
        self.MAX_LOADS_XYZAB = Fixed(1064, size=5)
        self.gap04 = Gap(1069, size=11)
        self.RAW_ANALOG = Fixed(1080, size=10)
        self.FILTERED_ANALOG = Fixed(1090, size=8)
        self.SPINDLE_LOAD = one(1098)
        self.gap05 = Gap(1099, size=165)
        self.MAX_LOADS_CTUVW = Fixed(1264, size=5)
        self.gap06 = Gap(1269, size=332)
        self.TOOL_TBL_FLUTES = ToolTable(1601, size=200, typ="Int")
        self.TOOL_TBL_VIBRATION = ToolTable(1801, size=200)
        self.TOOL_TBL_OFFSETS = ToolTable(2001, size=200)
        self.TOOL_TBL_WEAR = ToolTable(2201, size=200)
        self.TOOL_TBL_DROFFSET = ToolTable(2401, size=200)
        self.TOOL_TBL_DRWEAR = ToolTable(2601, size=200)
        self.gap07 = Gap(2801, size=199)
        self.ALARM = one(3000, typ="Int")
        self.T_MS = one(3001, typ="Time")
        self.T_HR = one(3002, typ="Time")
        self.SINGLE_BLOCK_OFF = IOne(3003)
        self.FEED_HOLD_OFF = IOne(3004)
        self.gap08 = Gap(3005, size=1)
        self.STOP_WITH_MESSAGE = IOne(3006)
        self.gap09 = Gap(3007, size=4)
        self.YEAR_MONTH_DAY = one(3011, typ="Time")
        self.HOUR_MINUTE_SECOND = one(3012, typ="Time")
        self.gap10 = Gap(3013, size=7)
        self.POWER_ON_TIME = one(3020, typ="Time")
        self.CYCLE_START_TIME = one(3021, typ="Time")
        self.FEED_TIMER = one(3022, typ="Time")
        self.CUR_PART_TIMER = one(3023, typ="Time")
        self.LAST_COMPLETE_PART_TIMER = one(3024, typ="Time")
        self.LAST_PART_TIMER = one(3025, typ="Time")
        self.TOOL_IN_SPIDLE = IOne(3026)
        self.SPINDLE_RPM = IOne(3027)
        self.PALLET_LOADED = IOne(3028)
        self.gap11 = Gap(3029, size=1)
        self.SINGLE_BLOCK = IOne(3030)
        self.AGAP = one(3031)
        self.BLOCK_DELETE = IOne(3032)
        self.OPT_STOP = IOne(3033)
        self.gap12 = Gap(3034, size=162)
        self.TIMER_CELL_SAFE = one(3196, typ="Time")
        self.gap13 = Gap(3197, size=4)
        self.TOOL_TBL_DIAMETER = ToolTable(3201, size=200)
        self.TOOL_TBL_COOLANT_POSITION = ToolTable(3401, size=200)
        self.gap14 = Gap(3601, size=300)
        self.M30_COUNT1 = IOne(3901)
        self.M30_COUNT2 = IOne(3902)
        self.gap15 = Gap(3903, size=98)
        self.LAST_BLOCK_G = Fixed(4001, size=21)
        self.gap16 = Gap(4022, size=79)
        self.LAST_BLOCK_ADDRESS = Fixed(4101, size=26)
        self.gap17 = Gap(4127, size=874)
        self.LAST_TARGET_POS = CWCPos(5001)
        self.MACHINE_POS = MachinePos(5021)
        self.WORK_POS = CWCPos(5041)
        self.SKIP_POS = CWCPos(5061)
        self.TOOL_OFFSET = Fixed(5081, size=20)
        self.gap18 = Gap(5101, size=100)
        self.G52 = WorkOffsetTable(5201)
        self.G54 = WorkOffsetTable(5221)
        self.G55 = WorkOffsetTable(5241)
        self.G56 = WorkOffsetTable(5261)
        self.G57 = WorkOffsetTable(5281)
        self.G58 = WorkOffsetTable(5301)
        self.G59 = WorkOffsetTable(5321)
        self.gap19 = Gap(5341, size=60)
        self.TOOL_TBL_FEED_TIMERS = ToolTable(5401, size=100, typ="Secs")
        self.TOOL_TBL_TOTAL_TIMERS = ToolTable(5501, size=100, typ="Secs")
        self.TOOL_TBL_LIFE_LIMITS = ToolTable(5601, size=100, typ="Int")
        self.TOOL_TBL_LIFE_COUNTERS = ToolTable(5701, size=100, typ="Int")
        self.TOOL_TBL_LIFE_MAX_LOADS = ToolTable(5801, size=100)
        self.TOOL_TBL_LIFE_LOAD_LIMITS = ToolTable(5901, size=100)
        self.gap20 = Gap(6001, size=197)
        self.NGC_CF = IOne(6198)
        self.gap21 = Gap(6199, size=802)
        self.G154_P1 = WorkOffsetTable(7001)
        self.G154_P2 = WorkOffsetTable(7021)
        self.G154_P3 = WorkOffsetTable(7041)
        self.G154_P4 = WorkOffsetTable(7061)
        self.G154_P5 = WorkOffsetTable(7081)
        self.G154_P6 = WorkOffsetTable(7101)
        self.G154_P7 = WorkOffsetTable(7121)
        self.G154_P8 = WorkOffsetTable(7141)
        self.G154_P9 = WorkOffsetTable(7161)
        self.G154_P10 = WorkOffsetTable(7181)
        self.G154_P11 = WorkOffsetTable(7201)
        self.G154_P12 = WorkOffsetTable(7221)
        self.G154_P13 = WorkOffsetTable(7241)
        self.G154_P14 = WorkOffsetTable(7261)
        self.G154_P15 = WorkOffsetTable(7281)
        self.G154_P16 = WorkOffsetTable(7301)
        self.G154_P17 = WorkOffsetTable(7321)
        self.G154_P18 = WorkOffsetTable(7341)
        self.G154_P19 = WorkOffsetTable(7361)
        self.G154_P20 = WorkOffsetTable(7381)
        self.gap22 = Gap(7401, size=100)
        self.PALLET_PRIORITY = PalletTable(7501, size=100)
        self.PALLET_STATUS = PalletTable(7601, size=100)
        self.PALLET_PROGRAM = PalletTable(7701, size=100)
        self.PALLET_USAGE = PalletTable(7801, size=100)
        self.gap23 = Gap(7901, size=599)
        self.ATM_ID = IOne(8500)
        self.ATM_PERCENT = one(8501, typ="Percent")
        self.ATM_TOTAL_AVL_USAGE = IOne(8502)
        self.ATM_TOTAL_AVL_HOLE_COUNT = IOne(8503)
        self.ATM_TOTAL_AVL_FEED_TIME = one(8504, typ="Secs")
        self.ATM_TOTAL_AVL_TOTAL_TIME = one(8505, typ="Secs")
        self.gap24 = Gap(8506, size=4)
        self.ATM_NEXT_TOOL_NUMBER = IOne(8510)
        self.ATM_NEXT_TOOL_LIFE = one(8511, typ="Percent")
        self.ATM_NEXT_TOOL_AVL_USAGE = IOne(8512)
        self.ATM_NEXT_TOOL_HOLE_COUNT = IOne(8513)
        self.ATM_NEXT_TOOL_FEED_TIME = one(8514, typ="Secs")
        self.ATM_NEXT_TOOL_TOTAL_TIME = one(8515, typ="Secs")
        self.gap25 = Gap(8516, size=34)
        self.TOOL_ID = IOne(8550)
        self.TOOL_FLUTES = IOne(8551)
        self.TOOL_MAX_VIBRATION = one(8552)
        self.TOOL_LENGTH_OFFSETS = one(8553)
        self.TOOL_LENGTH_WEAR = one(8554)
        self.TOOL_DIAMETER_OFFSETS = one(8555)
        self.TOOL_DIAMETER_WEAR = one(8556)
        self.TOOL_ACTUAL_DIAMETER = one(8557)
        self.TOOL_COOLANT_POSITION = IOne(8558)
        self.TOOL_FEED_TIMER = one(8559, typ="Secs")
        self.TOOL_TOTAL_TIMER = one(8560, typ="Secs")
        self.TOOL_LIFE_LIMIT = one(8561)
        self.TOOL_LIFE_COUNTER = one(8562)
        self.TOOL_LIFE_MAX_LOAD = one(8563)
        self.TOOL_LIFE_LOAD_LIMIT = one(8564)
        self.gap26 = Gap(8565, size=435)
        self.THERMAL_COMP_ACC = one(9000)
        self.gap27 = Gap(9001, size=15)
        self.THERMAL_SPINDLE_COMP_ACC = one(9016)
        self.gap28 = Gap(9017, size=983)
        self.GVARIABLES3 = Fixed(10000, size=1000)
        self.INPUTS = Fixed(11000, size=256)
        self.gap29 = Gap(11256, size=744)
        self.OUTPUT = Fixed(12000, size=256)
        self.gap30 = Gap(12256, size=744)
        self.FILTERED_ANALOG = Fixed(13000, size=13)
        self.COOLANT_LEVEL = one(13013)
        self.FILTERED_ANALOG = Fixed(13014, size=50)
        self.gap31 = Gap(13064, size=936)
        self.SETTING = Fixed(20000, size=10000)
        self.PARAMETER = Fixed(30000, size=10000)

        self.TOOL_TYP = Fixed(50001, size=200)
        self.TOOL_MATERIAL = Fixed(50201, size=200)
        self.gap32 = Gap(50401, 50600)
        self.gap32 = Gap(51001, 51300)
        self.CURRENT_OFFSET = Fixed(50601, size=200)
        self.CURRENT_OFFSET2 = Fixed(50801, size=200)
        self.VPS_TEMPLATE_OFFSET = Fixed(51301, size=100)
        self.WORK_MATERIAL = Fixed(51401, size=200)
        self.VPS_FEEDRATE = Fixed(51601, size=200)

        self.APPROX_LENGTH = Fixed(51801, size=200)
        self.APPROX_DIAMETER = Fixed(52001, size=200)
        self.EDGE_MEASURE_HEIGHT = Fixed(52201, size=200)
        self.TOOL_TOLERANCE = Fixed(52401, size=200)
        self.PROBE_TYPE = Fixed(52601, size=200)

        self.PROBE = Alias(self.SKIP_POS)
        self.WORK = Alias(self.WORK_POS)

        self.MACHINE = Alias(self.MACHINE_POS)
        self.G53 = Alias(self.MACHINE_POS)


def print_pretty_table(names):
    guts = Table(
        title=f"{names.title} Macro Variables",
        caption=f"Generated by {__file__}",
    )
    #    toptable.add_column(justify="center")

    guts.add_column("Range", justify="right")
    guts.add_column("N", justify="right")
    guts.add_column("K", justify="right")
    guts.add_column("Type", justify="center")
    guts.add_column("Name", justify="left")

    predicted_addr = 0
    snames = sorted(names.interesting)
    for el, nextel in zip_longest(snames, snames[1:]):
        # if not provided a size, workout from next one in list.
        if el.size is None:
            el.size = nextel._addr - el._addr
            el.last = el._addr + el.size - 1
        guts.add_row(*el.for_pretty())
        src_el = el
        if el.alias:
            src_el = el.alias
            predicted_addr = src_el._addr

        # not hitting predicted _addr means i've missed out a row.
        if src_el._addr != predicted_addr:
            gap = src_el._addr - predicted_addr
            guts.add_row(
                f"{predicted_addr}..{src_el._addr - 1}",
                str(gap),
                "G",
                "-",
            )
        predicted_addr = src_el.last + 1

    if FIXED_OUTPUT:
        outname = names.title + ".txt"
        with open(outname, "w", encoding="utf-8") as out:
            console = rich.console.Console(file=out)
            console.print(guts, style=None)
            print("Generated ", outname)
    else:
        console = rich.console.Console()
        console.print(guts, style=None)


def reprint_these_definitions(defs):
    for el in sorted(defs.interesting):
        print("        " + el.for_reprint())


def regen(defs, output_filename):
    filepath = Path(output_filename)
    tmp_filepath = filepath.with_suffix(".tmp")

    with open(filepath, encoding="utf-8") as inf:
        repl = re.match(
            "(.*?# MACHINE GEN BELOW.*?).*(.*?# MACHINE.*)",
            inf.read(),
            flags=re.DOTALL,
        )
        if repl is not None:
            with open(tmp_filepath, "w", encoding="utf-8") as out:
                out.write(repl.group(1) + "\n")
                defs.write_to(out)
                out.write(INDENT + repl.group(2))
            tmp_filepath.rename(filepath)


def main():
    args = docopt.docopt(__doc__)
    for names in [HaasNames()]:
        if args["--pretty"]:
            print_pretty_table(names)

        #    if args["--version"]:
        #        print(gbl.VERSION)

        elif args["--reprint"]:
            reprint_these_definitions(names)
        elif args["--regen"]:
            try:
                regen(names, args["<OUTFILE>"])
            except FileNotFoundError as exc:
                print(f"FAIL {exc.args[1]} '{exc.filename}'")


if __name__ == "__main__":
    main()
