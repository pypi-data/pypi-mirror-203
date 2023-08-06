# from m1.gtypes import *
from pathlib import Path

from piig import gbl
from piig import lib


# BASE_OIDX = 1


root = Path("/home/sac/vf3/_nc_/")
root_for_compare = Path("/home/sac/vf3/progs/piig/piig/n")


def oidx_to_o(x):
    if x is None:
        return ""
    idx = int(x)
    return f"O{idx:04}"


def oidx_to_filename(x):
    try:
        return oidx_to_o(x) + x.name

    except AttributeError:
        return oidx_to_o(x)


class FILEOUT:
    def __init__(self, proc_number):
        dirname = root_for_compare
        file_name = oidx_to_filename(proc_number)
        file_name = file_name.replace(" ", "-").replace("_", "-").upper()
        self.fpath = dirname / file_name
        self.handle = open(self.fpath, "w", encoding="utf-8")

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.handle.close()

    def write(self, lines):
        pending = []
        lhs_lens = []
        rhs_lens = []
        for code, comment in lines:
            if comment:
                lhs_lens.append(len(code))
            rhs_lens.append(len(comment))
            pending.append((code, comment))

        pad_left = lib.give86(lhs_lens)
        pad_right = lib.give86(rhs_lens)

        for code, comment in pending:
            if comment:
                comment = "( " + comment.ljust(pad_right) + ")"
            s = code.ljust(pad_left) + comment
            print(s)
            self.handle.write(s + gbl.NEWLINE)


def human(v: float):
    return f"{round(v,1)}"
