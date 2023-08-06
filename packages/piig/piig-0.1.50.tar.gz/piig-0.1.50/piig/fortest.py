import logging

from itertools import zip_longest



from piig import lib


def remove_comments(line):
    pos = line.find("(")
    if pos >= 0:
        line = line[:pos]
    return line


def fmt_line(wid, want, mid, got):
    return f"{want.ljust(wid)}{mid}{got.ljust(wid)}"


def pytest_report(want, got):
    wid = 0

    def diff_iterator():
        return zip_longest(got, want, fillvalue="")

    # find out widest
    for lhs, rhs in diff_iterator():
        wid = max(wid, len(lhs), len(rhs))

    print("*" * (wid * 2 + 3))
    print(fmt_line(wid, "got", " | ", "want"))

    errorline = ""

    for lhs, rhs in diff_iterator():
        if lhs != rhs:
            middle = " * "
            errorline = f"{lhs} != {rhs}"
        else:
            middle = " | "

        print(fmt_line(wid, lhs, middle, rhs))
        logging.debug(fmt_line(wid, lhs, middle, rhs))
    return errorline


class LG:
    got: list[str]
    want: list[str]

    def __repr__(self):
        return pytest_report(self.want, self.got)

    def __bool__(self):
        return self.want == self.got

    def __init__(self, got, want):
        got = list(got)

        def trimlines(lines):
            lines = list(lines)
            for maybeline in lines:
                for line in maybeline.split("\n"):
                    line = remove_comments(line)
                    line = line.replace(" ", "")
                    if line:
                        yield line

        self.want = list(trimlines(want))
        self.got = list(trimlines(got))

        logging.debug(self.got)
        if self.want != self.got and not lib.in_pytest():
            pytest_report(self.want, self.got)

            print("    g.checkcode(")
            for l in got:
                print('       "' + remove_comments(l.strip()).strip() + '",')
            print("    )")


# run a test which compares golden gcode with generated.
