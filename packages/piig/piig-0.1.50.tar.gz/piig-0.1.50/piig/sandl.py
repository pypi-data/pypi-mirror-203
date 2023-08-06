import inspect
import traceback

from pathlib import Path


def dummy():
    pass


m = inspect.getmodule(dummy)
if m:
    this_package = m.__package__


def current_source_line():
    cursor = inspect.currentframe()
    while cursor is not None:
        module = inspect.getmodule(cursor.f_code)
        if module and module.__package__ != this_package:
            break
        cursor = cursor.f_back

    return inspect.getframeinfo(cursor).code_context


# def show_tb(cursor, inside_only=False, last_only=False, msg=""):
#     #    inside_only = False
#     #    inside_only = False

#     res = []

#     our_parent = Path(show_tb.__code__.co_filename).parent
#     while cursor:
#         full_name = Path(cursor.tb_frame.f_code.co_filename)
#         line_number = cursor.tb_lineno

#         #        fname = Path(fullname).name
#         their_parent = Path(full_name).parent
#         if not inside_only or our_parent == their_parent:
#             res.append(f"{full_name}:{line_number}")
#         cursor = cursor.tb_next
#     if last_only:
#         print(res[-1] + ":" + msg)
#         return res[-1]

#     print("\n".join(res))


def relevant_traceback(exception_traceback):
    #    breakpoint()
    tb = traceback.extract_tb(exception_traceback, limit=50)

    keep = []
    for cursor in tb:
        code_filename = cursor.filename

        if code_filename.endswith("ast.py"):
            continue
    if len(keep) == 0:
        keep = range(len(tb))

    return [(tb[i].filename, tb[i].lineno, tb[i].line) for i in keep]


# always just outside the context
# returns fname:lineno and the actual source line
def find(stop_outside=False):
    #    pdb.set_trace()
    cursor = inspect.currentframe()
    while True:
        if cursor is None:
            break
        cursor = cursor.f_back
        if cursor is None:
            break

        code_filename = cursor.f_code.co_filename

        if code_filename.startswith("<frozen"):
            continue

        fname = Path(code_filename).name
        if fname == "<stdin>":
            return "-", "console"

        # got <us>/<filename> in our path, then we're
        # part of the guts of the library and not
        # the program.

        if stop_outside and Path(code_filename).parts[-2] != __package__:
            l = inspect.getframeinfo(cursor)
            # if l.code_context:
            #     src = "".join(x for x in l.code_context)
            # else:
            #     src = "noithing"
            breakpoint()
            l = inspect.getframeinfo(cursor)
            res = f"{fname}:{l.lineno} ({l.function})"
            return res

    return "?"


def find_sandl():
    sandls = find(stop_outside=True)
    return sandls


class SANDL:
    def __init__(self):
        self.fileandline, self.source = find(stop_outside=True)

    def __eq__(self, other):
        if other is None:
            return False
        l2 = self.fileandline == other.fileandline
        l3 = self.source == other.source
        return l2 and l3
