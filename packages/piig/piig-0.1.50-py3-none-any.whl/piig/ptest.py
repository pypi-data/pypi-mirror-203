import functools
import logging
import pathlib

import itertools
from piig import function, lib
from piig import support


LESS_TESTY_STUFF = True


# takes fn, works out where it lives, where to find golden output and
# where to put test output


def make_file_paths(fn) -> tuple[str, str]:
    pathlib.Path(fn.__code__.co_filename)
    this_file_directory = pathlib.Path(__file__).parent

    generated_dir = this_file_directory / "tests" / "golden"
    generated_dir.mkdir(exist_ok=True)

    common_path = generated_dir / (fn.__name__.replace("test_", ""))
    golden_path = common_path.with_suffix(".nc")
    callow_path = common_path.with_suffix(".new")

    return golden_path, callow_path


# decorator for pytests
# expand fn to inline, and compare outputs.


def look_in_log():
    assert False


def strip_comments(txt):
    txt = txt.strip()
    idx = txt.find("(")
    if idx >= 0:
        return txt[:idx]
    return txt


def compare_with_golden(fn, got):
    # make paths and write the output.
    golden_path, callow_path = make_file_paths(fn)
    with open(callow_path, "w", encoding="utf-8") as gotf:
        for line in got():
            gotf.write(line)

    if not golden_path.exists():
        logging.info(f"Making {golden_path}.")
        callow_path.rename(golden_path)
        return

    error_place, markers = find_differences(callow_path, golden_path)

    if error_place < 0:
        callow_path.unlink()
        return

    show_differences(error_place, markers, callow_path, golden_path)
    look_in_log()
    # read back in and compare to golden


# find differences between two files, return
# line where error found, and a list of *s assocaited with
# broken lines.


def find_differences(callow_path, golden_path) -> tuple[int, list[str]]:
    first_bad = -1
    line_number = 0
    line_marker = []

    with (
        open(callow_path, encoding="utf-8") as gotf,
        open(golden_path, encoding="utf-8") as wantf,
    ):
        for want, got in itertools.zip_longest(
            wantf.readlines(), gotf.readlines(), fillvalue=""
        ):
            want = strip_comments(want)
            got = strip_comments(got)
            if want != got:
                line_marker.append(" * ")
                if first_bad < 0:
                    first_bad = line_number
            else:
                line_marker.append(" | ")

            line_number += 1
    return first_bad, line_marker


def show_differences(first_bad, line_marker, callow_path, golden_path):
    with (
        open(callow_path, encoding="utf-8") as gotf,
        open(golden_path, encoding="utf-8") as wantf,
    ):
        wlist = ["WANT"]
        mlist = [""]
        glist = ["GOT"]

        line_number = 0
        for want, middle, got in itertools.zip_longest(
            wantf.readlines(),
            line_marker,
            gotf.readlines(),
            fillvalue="",
        ):
            if line_number - 10 < first_bad < line_number + 10:
                wlist.append(strip_comments(want))
                mlist.append(middle)
                glist.append(strip_comments(got))
            line_number += 1

        wlist = lib.pad_to_same_width(wlist)
        for want, middle, got in zip(wlist, mlist, glist):
            logging.error(want + middle + got)
    look_in_log()


def nc_compare(fn):
    also_native = fn.__name__.endswith("n2")
    return gcoded_output_tester(function.inline(fn), also_native=also_native)


def nc_compare2(fn):
    return gcoded_output_tester(function.inline(fn), also_native=True)


# nc_compare, but for things which aren't tests so are
# already inlined


def example_compare(fn):
    return gcoded_output_tester(fn, also_native=False)


# fortest just remembers the function node until a bit later
def for_test(fn):
    @functools.wraps(fn)
    def macro_(*args, **kwargs):
        dellist = []

        for k, v in kwargs.items():
            if v == "<REPLACEWITHCTX>":
                dellist.append(k)
        for k in dellist:
            del kwargs[k]

        to_macro(fn, *args, **kwargs)

    return macro_


def example_tester(test_hook):
    def example_tester_():
        breakpoint()
        #        mod = __import__("piig.examples." + mod_name)
        got = function.inline(test_hook).call_from_outside(create_ctx=True)

        with open("/tmp/also.nc", "w", encoding="utf-8") as outf:
            with open(wantfilename, encoding="utf-8") as wantf:
                for want, got in zip(wantf.readlines(), got):
                    outf.write(got)
                    assert want == got

    return example_tester_


def do_native_compile(fn):
    ctx = support.CTX()
    got = fn(ctx)


def gcoded_output_tester(gcoded, *, also_native):
    def output_tester_():
        if also_native:
            do_native_compile(gcoded.fn)

        got = gcoded.call_from_outside(create_ctx=True, with_version=False)

        compare_with_golden(gcoded.fn, got)

    return output_tester_
