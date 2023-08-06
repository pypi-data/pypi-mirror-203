#! /usr/bin/env python


"""
Turn python into gcode.

Usage:
  piig --test
  piig --version

(flycheck-verify-setup)

"""
import logging
import os
import sys

import docopt
import pytest

import piig


sys.path.insert(0, "..")


LEVEL = "DEBUG"


sys.path.insert(0, ".")

sys.path.insert(0, "../examples")
sys.path.insert(0, "./examples")


TG = 0

# logger.remove(0)
# # format="<level>{message}</level>")
# format = "{time:HH:MM}**{level}***{message}"
# logger.add(sink=sys.stderr, level=LEVEL, format=format)

# logger.add(
#     sink=open("debug.log", "w", encoding="utf-8"),  # pylint: disable=R1732
#     format=format,
#     level="DEBUG",
# )


logging.basicConfig(
    filename="test.log",
    filemode="w",
    level=logging.ERROR,
    format="%(asctime)s %(levelname)s: %(message)s",
    datefmt="%H:%M",
)


os.environ["PYTHONPATH"] = "/home/sac/vf3/progs/piig/"
os.environ["PATH"] = (
    "/home/sac/vf3/progs/piig/piig:/home/sac/vf3/progs/piig/tests" + os.environ["PATH"]
)
if TG:
    try:
        import typeguard

        ih = typeguard.install_import_hook
    except AttributeError:
        import typeguard

        ih = typeguard.importhook.install_import_hook

    print("TURNING ON TYPEGUAR")

    #    typeguard._config.global_config.debug_instrumentation = 1
    #    install_import_hook("piig")
    # ih("gctx")
    # ih("node")
    # ih("astmod")
    # ih("lib")
    # ih("sac")
    # ih("rvalue")
    # ih("lvalue")
    # ih("exception")
    # ih("sandl")
    # ih("g")
    # ih("simple")
    # ih("typ")

    ih("piig")


# from piig import code

# code.doit()

OFF = 0
ON = 1


def run_all_test_(module_name):
    __import__("piig.tests." + module_name)

    modguts = getattr(piig.tests, module_name)
    for key, value in modguts.__dict__.items():
        if key.startswith("test_"):
            xfail = "xfail" in key
            print("K", key)

            try:
                value()
            except AssertionError as e:
                if not xfail:
                    #                    breakpoint()
                    print(e)
            else:
                if xfail:
                    print("ASSERTION EXPECTED")


# sys.exit(0)
def runthem():
    #    with nd.catch_errors():

    if OFF:
        import piig.examples.vicecenter

        piig.examples.vicecenter.main()
    if ON:
        run_all_test_("test_smoke")
        run_all_test_("test_coords")
        sys.exit(0)
    if OFF:
        run_all_test_("test_example")

        run_all_test_("test_error")
        run_all_test_("test_edge")
        run_all_test_("test_meta")
        run_all_test_("test_func")


runthem()

# def main():
#     try:
#         with nd.catch_errors():
#             runthem()
#     except ex.AllDone:
#         pass


def main():
    pytest.main(["tests/test_example.py"])
    args = docopt.docopt(__doc__)
    if args["--version"]:
        print(piig.__version__)
    elif args["--test"]:
        pytest.main([""])
    else:
        runthem()


if __name__ == "__main__":
    main()
