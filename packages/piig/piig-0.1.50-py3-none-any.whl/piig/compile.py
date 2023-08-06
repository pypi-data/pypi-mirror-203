import sys

import docopt

import piig

from piig import function
from piig import gbl
from piig import lib

import pathlib


def generate(fn, output_filename=None):
    assert isinstance(fn, function.InlineDefinition)

    src_filename = fn.fn.__code__.co_filename
    if output_filename is None:
        output_filename = pathlib.Path(src_filename).with_suffix(".nc")

    with open(output_filename, "w", encoding="utf-8") as outf:
        newctx = fn.call_from_outside(create_ctx=True)
        for line in newctx():
            outf.write(line)
    return output_filename


doc = """
Turns a python program into a gcode program.

Usage:
   prog [options] [--out=<file>]

Options:
    -o <file> --out=<file>   Output file, [default: -]
    -h --help                This.
    -v --verbose             Make verbose
    --version                Print version and quit.

"""


def p2git(idfn: function.InlineDefinition, **kwargs):
    fn = idfn.fn
    jobname = fn.__name__
    newdoc = doc.replace("PROG", jobname)
    args = docopt.docopt(newdoc)

    if args["--version"]:
        print(f"Version: P2G {piig.__version__}")
        sys.exit(0)

    if args["--verbose"]:
        gbl.VERBOSE = True

    with lib.openout(args["--out"]) as outf:
        newctx = idfn.call_from_outside(create_ctx=True)
        for line in newctx():
            outf.write(line)
        outf.write(f"(Version: P2G {piig.__version__})")
