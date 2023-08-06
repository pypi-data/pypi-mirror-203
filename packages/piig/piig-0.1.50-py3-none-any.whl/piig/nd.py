import abc
import ast
import contextlib
import dataclasses
import enum
import inspect
import sys
import typing

from itertools import zip_longest
from pathlib import Path

from piig import axis
from piig import coords
from piig import exception as ex
from piig import gbl
from piig import lib
from piig import sandl


COMMENT_INDENT = 30
CODE_INDENT = 30

USE_RELATIVE_FILENAMES = True

USE_RELATIVE_FILENAMES = False
CODECOMMENT = 0
COMMENTCODE = 1
LINDENT = 0
CINDENT = 2
DECIMALS = 4


class N(abc.ABC):
    pass


class Exp(N):
    pass


# remebers things like where ebss was at the entrance to
# a function so it can be restored, so new calls get the same
# address - like F66 - in the absense of recursion.


class ScopeData:
    ebss: int

    def __init__(self, ebss):
        self.ebss = ebss


class Label_Genoff:
    _next: int

    def __init__(self, first=1000):
        self._next = first

    def next(self):
        res = Label(self._next)
        self._next += 1
        return res


def to_gcode_from_float(thing):
    with ex.expect_no_errors():
        c = str(round(float(thing), DECIMALS))
        if c.endswith(".0"):
            c = c[:-1]
        return c


def to_gcode(thing, need_int=False):
    if isinstance(thing, (float, int)):
        if need_int:
            return str(int(thing))
        return to_gcode_from_float(thing)

    if thing is None:
        return "none"
    with ex.try_this():
        return thing.to_gcode(need_int)
    if isinstance(thing, (float, int)):
        return to_gcode_from_float(thing)
    with ex.try_this():
        breakpoint()
        return thing.to_gcode(need_int)
    if need_int:
        return str(int(thing))

    return to_gcode_from_float(thing)


chmap = {
    "(": "[",
    ")": "]",
    "+": "+",
    "/": "/",
    "-": "-",
    "=": "=",
    ":": ":",
    "*": "*",
    ".": ".",
    ">": ">",
    "<": "<",
    ",": ",",
    " ": " ",
    "#": "#",
    "_": "_",
    "[": "[",
    "]": "]",
    "!": "!",
    "~": "~",
    "%": "%",
    "|": "|",
    "^": "^",
    "&": "&",
    **{chr(x): chr(x) for x in range(0, 127) if chr(x).isalnum()},
}


# remove bad chars from a comment.
def clean_comment_chars(txt):
    res = ""
    for ch in txt:
        match ch:
            case "(":
                ch = "["
            case ")":
                ch = "]"

        res += ch
    return res


prev_line = ""

# auto comment is a comment which comes from
# the source, rather than being typed.
# we take liberties to increase information density.


def compress_comment(lines: list[str]):
    for line in lines:
        guts = clean_comment_chars(line)
        for too_talky in ["cin.", "ctx.", "g.", "goto"]:
            guts = guts.replace(too_talky, "")

        if guts.startswith("    "):
            guts = guts[4:]

        global prev_line
        if guts != prev_line:
            yield "( " + guts.ljust(30) + ")"
            prev_line = guts


class B(abc.ABC):
    def __init__(self):
        self.node = gbl.last_node

    def to_gcode_lines(self) -> list[str]:
        return ["NO"]

    def __repr__(self):
        res = []
        for line in self.to_gcode_lines():
            res.append(line)
        return "\n".join(res)

    def to_gcode_comment(self):
        return compress_comment(get_lines_at(self.node))

    def to_full_lines(self):
        for code, comment in zip_longest(
            self.to_gcode_lines(),
            self.to_gcode_comment(),
            fillvalue="",
        ):
            if COMMENTCODE:
                if comment:
                    if len(code) > COMMENT_INDENT:
                        yield " " * COMMENT_INDENT + comment + "\n"
                        comment = ""

                if code:
                    if code[0] == "!":
                        breakpoint()
                        code = "( " + clean_comment_chars(code[1:]) + " )"
                        comment = ""
                        indent = 0
                    else:
                        if code[0] == "L":
                            indent = LINDENT
                        elif code[0] == "(":
                            indent = 0
                            comment = code
                            code = ""
                        else:
                            indent = CINDENT
                    if comment:
                        yield (" " * indent) + code.ljust(
                            COMMENT_INDENT - indent
                        ) + comment + "\n"
                    else:
                        yield (" " * indent) + code + "\n"


class Label:
    _n: int
    _read: bool
    _written: bool

    def __init__(self, idx: int):
        self._n = idx
        self._read = False
        self._written = False

    def as_gcode_ref(self):
        self._read = True
        return f"{self._n}"

    def as_gcode_definition(self):
        self._written = True
        return f"L{self._n}"

    def used(self):
        return self._read or self._written


@dataclasses.dataclass
class LabelDef(B):
    v: Label

    def __init__(self, v: Label):
        super().__init__()
        self.v = v

    def to_gcode_lines(self):
        yield f"{self.v.as_gcode_definition()}"


class Label_Gen:
    def reset(self):
        self.next_label = 1000

    def __init__(self):
        self.next_label = 1000

    def next(self):
        r = self.next_label
        self.next_label += 1
        return Label(r)


@dataclasses.dataclass
class Block(B):
    guts: list[B]

    def __init__(self, v):
        super().__init__()
        self.guts = v

    def to_gcode_lines(self):
        for line in self.guts:
            yield line.to_gcode_lines()


@dataclasses.dataclass
class Goto(B):
    v: Label

    def __init__(self, v: Label):
        super().__init__()
        self.v = v

    def to_gcode_lines(self):
        yield f"GOTO {self.v.as_gcode_ref()}"


@dataclasses.dataclass
class Return(B):
    v: Label

    def __init__(self, v: Label):
        super().__init__()

        self.v = v

    def to_gcode_lines(self):
        yield f"RETURN {self.v}"


@dataclasses.dataclass
class If(B):
    exp: typing.Any
    on_t: Label

    def __init__(self, exp, on_t: Label):
        super().__init__()

        self.exp = exp
        self.on_t = on_t

    def to_gcode_lines(self):
        yield f"IF [{to_gcode(self.exp)}] GOTO {self.on_t.as_gcode_ref()}"


class CommentLines(B):
    def __init__(self, lines):
        super().__init__()
        self.lines = lines

    def to_full_lines(self):
        lines = list(map(str, self.lines))
        lines = lib.pad_to_same_width(lines)

        for line in lines:
            if line:
                yield "( " + clean_comment_chars(line) + " )\n"
            else:
                yield "\n"

    @classmethod
    def emit(cls, lines):
        emit_stat(CommentLines(lines))


@dataclasses.dataclass
class Comment(B):
    def __init__(self, txt):
        super().__init__()
        self.txt = txt

    def to_gcode_lines(self):
        yield self.txt

    def to_full_lines(self):
        # lhs comment.
        if len(self.txt) < 3:
            yield "\n"
        elif self.txt[0] == "!":
            yield "(" + self.txt[1:] + " )\n"
        else:
            yield " " * COMMENT_INDENT + self.txt + " )\n"


@dataclasses.dataclass
class Code(B):
    def to_gcode_comment(self):
        # got explicit comment, use it
        if self.comment:
            yield from compress_comment([self.comment])
        else:
            yield from super().to_gcode_comment()

    def __init__(self, txt, comment):
        super().__init__()
        self.txt = txt
        self.comment = comment

    def to_gcode_lines(self):
        yield self.txt


def makeCode(src, comment=None):
    #    if isinstance(src, list):
    #        breakpoint()
    if isinstance(src, str):
        yield Code(src, comment)
    else:
        for line in src:
            yield Code(line, comment)


@dataclasses.dataclass
class ByMethod(B):
    def __init__(self, method):
        super().__init__()
        self.method = method

    def to_full_lines(self):
        yield from self.method.to_full_lines()


class Set(B):
    def __init__(self, lhs, rhs):
        super().__init__()
        self.lhs = lhs
        self.rhs = rhs

    def to_gcode_lines(self):
        l = to_gcode(self.lhs)
        r = to_gcode(self.rhs)

        res = f"{to_gcode(self.lhs)}= {to_gcode(self.rhs)}"
        if "##" in res:
            breakpoint()
        if l == r:
            breakpoint()

        yield f"{to_gcode(self.lhs)}= {to_gcode(self.rhs)}"


# def source_lines_at(
#     filename, rel_linenumber, col_offset, end_col_offset, show_caret=False
# ):
#     rel_linenumber = spos.node.lineno - 1
#     #    filename = pathlib.Path(filename).relative_to(pathlib.Path.cwd())
#     if filename is None:
#         return ["no filename"]

#     src = inspect.getsource(spos.fn)
#     lines = src.split("\n")

#     result = []
#     result.append(lines[rel_linenumber])

#     if show_caret:
#         indent = spos.node.col_offset
#         length = spos.node.end_col_offset - indent
#         result.append(" " * indent + "^" * length)


class Show(enum.IntFlag):
    file = enum.auto()
    line = enum.auto()
    column = enum.auto()
    caret = enum.auto()
    traceback = enum.auto()


class Linfo:
    def __init__(self, file=None, line=None, c1=0, cwidth=0, txt=None):
        self.file = file
        self.line = line
        self.c1 = c1
        self.cwidth = cwidth
        self.txt = txt

        self.parts = []
        if self.file:
            self.parts.append(self.file)
        if self.line:
            self.parts.append(str(self.line))
        if self.c1:
            self.parts.append(str(self.c1))
            self.parts.append(str(self.cwidth))

    def __eq__(self, other):
        return (
            self.file == other.file
            and self.line == other.line
            and self.c1 == other.c1
            and self.cwidth == other.cwidth
            and self.txt == other.txt
        )


def get_Linfo(node):
    filename = inspect.getsourcefile(node.fn)

    if USE_RELATIVE_FILENAMES:
        try:
            filename = str(Path(filename).relative_to(Path.cwd()))
        except ValueError:
            pass

    first_linenumber = node.fn.__code__.co_firstlineno
    rel_linenumber = getattr(node, "lineno", 1) - 1
    col_offset = getattr(node, "col_offset", 0)
    col_width = getattr(node, "end_col_offset", 0) - col_offset

    #    filename = pathlib.Path(filename).relative_to(pathlib.Path.cwd())

    src = inspect.getsource(node.fn)
    lines = src.split("\n")

    return Linfo(
        filename,
        first_linenumber + rel_linenumber,
        col_offset,
        col_width,
        lines[rel_linenumber],
    )


def interp_traceback():
    prev_linfo = None
    if gbl.interp is None:
        return
    for node in gbl.interp.last_place:
        linfo = get_Linfo(node)

        if prev_linfo and linfo == prev_linfo:
            continue

        prev_linfo = linfo
        prefix = ":".join(linfo.parts)
        print(prefix + ": " + linfo.txt)
        # +2 cause : space
        print(" " * (len(prefix) + linfo.c1 + 2) + "^" * linfo.cwidth)


def python_traceback():
    exc_type, exc_obj, exc_tb = sys.exc_info()

    res = sandl.relevant_traceback(exc_tb)
    res.reverse()
    print("python traceback", str(exc_obj))

    def oneel(tup):
        print(f"{tup[0]}:{tup[1]}: {tup[2]}")

    if len(res) > 10:
        for el in res[:5]:
            oneel(el)
        print("...")
        for el in res[-5:]:
            oneel(el)
    else:
        for el in res:
            oneel(el)


def show_error_at(message):
    print(message)
    interp_traceback()
    show_locals()
    python_traceback()


def show_line_at(node):
    linfo = get_Linfo(node)
    print(linfo.txt)
    print(" " * linfo.c1 + "^" * linfo.cwidth)


def get_lines_at(ctx):
    linfo = get_Linfo(ctx)
    return [linfo.txt]


# def i_traceback(imessage):
#     print(
#         "\n".join(
#             source_lines_with_error_at(SPos.last_known(), imessage, show_caret=True)
#         )
#     )


def show_locals():
    interp = gbl.interp
    if interp.ns.d is None:
        print("NO LOCALS YET")
        return
    print("LOCALS")
    for k, v in interp.ns.d.items():
        vstr = str(v)
        if "<class '" in vstr:
            continue
        if "object" in vstr:
            continue
        if len(str(v)) < 30:
            print(f"{k} = {v}")


def show_error_at_lastpos_tb(interp, exception, message):
    breakpoint()
    if isinstance(exception, ex.ErrorHere):
        imessage = message
        pmessage = ""
    else:
        pmessage = message
        imessage = "last interpreted location"

    i_traceback(imessage)
    show_locals(interp)
    py_traceback(exception, pmessage)

    sys.exit(1)


@contextlib.contextmanager
def catch_running_errors():
    try:
        yield

    except AssertionError as err:
        show_error_at_lastpos_tb(err)
        raise err
    except (
        AssertionError,
        IndexError,
        AttributeError,
        NameError,
        ex.ErrorHere,
        TypeError,
    ) as err:
        show_error_at_lastpos_tb(err)


@contextlib.contextmanager
def catch_errors():
    #    yield

    print("CATCH ERRORRS")

    try:
        yield

    except (IndexError, AssertionError) as err:
        show_error_at(
            str(err) + repr(err),
        )
        raise ex.AllDone

    except (
        #        AttributeError,
        NameError,
        ex.ErrorHere,
        TypeError,
    ) as err:
        show_error_at(str(err))
        raise ex.AllDone

    except Exception as err:
        print("big deal !", err)
        show_error_at(str(err))
        breakpoint()
        print("big deal !", err)


def slice_to_index_list(idx, size=None):
    res = []
    if isinstance(idx, slice):
        f = idx.start if idx.start is not None else 0
        t = idx.stop if idx.stop is not None else size
        if t is None:
            breakpoint()
        i = idx.step if idx.step is not None else 1

        for el in range(f, t, i):
            res.append(can(el))
    else:
        res.append(can(idx))
    return res


class Glist(Exp, list):
    def __init__(self):
        super().__init__()


# only associated with things with multiple elements, ie Glist and ARRAY
# used when not running inside interpreter
class Dots(Exp):
    def __init__(self):
        super().__init__()

    def byslice_to_list(self, idx):
        res = []
        for elidx in slice_to_index_list(idx, len(self)):
            res.append(self[elidx])
        return res

    def byname_to_list(self, name):
        return axis.name_to_indexes(name)

    def __setattr__(self, key, value):
        if key[0] == "_":
            object.__setattr__(self, key, value)
            return

        if key == "var":
            axes_list = range(0, self._size)
        else:
            axes_list = self.byname_to_list(key)
        for dst, src in zip(axes_list, one_is_forever(value)):
            self[dst] = src

    def __getattr__(self, key):
        if key[0] == "_":
            return object.__getattr__(self, key)

        if key == "var":
            axes_list = range(0, self._size)
        else:
            axes_list = self.byname_to_list(key)

        res = Glist()
        for idx in axes_list:
            res.append(self[idx])
        return res

        return Gvalue([self[idx] for idx in axes_list])

        raise AttributeError

    # @property
    # def x(self):
    #     return self[0]

    # @x.setter
    # def x(self, src):
    #     self[0] = src

    # @property
    # def y(self):
    #     return self[1]

    # # @y.setter
    # # def y(self, src):
    # #     self[1] = src

    # @property
    # def z(self):
    #     return self[2]

    # # @z.setter
    # # def z(self, src):
    # #     self[2] = src

    # @property
    # def xyz(self):
    #     return self[0:3]

    # # @xyz.setter
    # # def xyz(self, src):
    # #     self.do_set(slice(0, 3), src)

    # @property
    # def xy(self):
    #     return self[0:2]

    # # @xy.setter
    # # def xy(self, src):
    # #     self.do_set(slice(0, 2), src)

    # # @property
    # # def ab(self):
    # #     return self[0:2]

    # @property
    # def var(self):
    #     return self[:]

    # # @var.setter
    # def var(self, src):
    #     self.do_set(slice(0, len(self)), src)

    # @property
    # def tvar(self):
    #     return self[:]

    # @tvar.setter
    # def tvar(self, src):
    #     self.do_set(slice(0, len(self)), src)

    # def do_set(self, dst_slice, src):
    #     self[dst_slice] = src

    # def gcode(self):
    #     idx = 0
    #     if self[idx]:
    #         return self[idx].gcode()
    #     return "NOTHING"


# one element will repeat, more will run to end.
# always unwraps, never return gvalue or array
def one_is_forever(gvalue):
    try:
        for idx, el in enumerate(gvalue):
            yield unwrap(el)

        if idx == 1:
            while True:
                yield unwrap(el)
    except TypeError:
        while True:
            yield unwrap(gvalue)


# take whatever it is out of any list or gvalue
def unwrap(value):
    return scalarify(value)


# return first element in x, digging till atom.
def scalarify(x):
    if isinstance(x, (int, float)):
        return x
    if "Op" in str(x.__class__):
        breakpoint()
        return x
    if "Unop" in str(x.__class__):
        return x
    if "Binop" in str(x.__class__):
        return x
    if isinstance(x, coords.ARRAY):
        return x[0]
    try:
        return x.get_element(0)
    except AttributeError:
        return scalarify(x[0])


# a dots item can have a subscript, or attribute.
class Gvalue(Dots):
    def __not__(self):
        breakpoint()

    def get_element(self, idx):
        return self._guts[idx]

    def same(self, other):
        if not isinstance(other, Gvalue):
            return False
        if self._guts != other.g:
            return False
        return True

    def to_symtab_entry(self):
        r = []
        for el in self._guts:
            r.append(to_gcode(el))
        return ",".join(r)

    #        yield lib.in_bcommas("", self.g)

    def __init__(self, co, *, size=None):
        #        breakpoint()

        for el in co:
            if isinstance(el, Gvalue):
                breakpoint()
        super().__init__()

        self._guts = co

        if size is None:
            self._size = len(self._guts)
        else:
            self._size = size

    @classmethod
    def make(cls, src):
        if isinstance(src, list) and len(src) == 1:
            return src[0]

        if isinstance(src, Exp):
            return cls([src])
        if lib.is_iterable(src):
            return cls(src)
        return cls([src])

    def __iter__(self):
        yield from self._guts

    def __len__(self):
        return self._size

    def __getitem__(self, i):
        return Gvalue.make(self._guts[i])

        # if isinstance(i, slice):
        #     return Glist(co=self.g[i])
        # try:
        #     return self.g[i]
        # except IndexError:
        #     raise IndexError
        # except Exception as e:
        #     breakpoint()
        #     print(e)

        #     print(e)

    def __setitem__(self, indexes, src):
        for lhs, rhs in zip(self.byslice_to_list(indexes), one_is_forever(src)):
            if lhs is not rhs:
                emit_single_set(lhs, rhs)

    # def __setitem__(self, i, val):
    #     breakpoint()
    #     if isinstance(i, slice):
    #         return Glist(self.g[i])

    #     return self.g[i]

    def to_gcode(self, need_int):
        if self._size != 1:
            ex.rErrorHere(f"Expected a scalar, but got a vector.. {self}")
        return to_gcode(self._guts[0], need_int)

    def __repr__(self):
        return lib.in_aspace("", self._guts)

        breakpoint()

    def precedence(self):
        return get_precedence(self._guts[0])


def flatten(args):
    if "Op" in str(args.__class__):
        return [args]
    if "ARRAY" in str(args.__class__):
        res = []

        for el in args:
            res.append(el)
        return res

    if isinstance(args, Gvalue):
        return args._guts
        for el in args:
            res.append(el)
        return res

    elif isinstance(args, (int, str, float)):
        return [args]
    elif lib.is_iterable(args):
        args = list(args)
        res = []
        for x in args:
            res += flatten(x)
        return res
    else:
        return [args]


def emit_stat(stat):
    if gbl.ctx:
        gbl.ctx.block_context.statements.emit_stat(stat)


def can(x):
    if isinstance(x, Gvalue):
        if len(x) == 1:
            return x[0]
    if isinstance(x, list):
        return x[0]
    return x


def is_constant(v):
    return isinstance(v, (int, float, bool))


def emit_single_set(dst, src):
    if not same(dst, src):
        emit_stat(Set(dst, src))


def same(lhs, rhs):
    if type(lhs) is not type(rhs):
        return False
    try:
        if is_constant(lhs):
            if is_constant(rhs):
                return lhs == rhs
            return False
        #    with ex.expect_no_errors():
        return lhs.same(rhs)

    except Exception:
        breakpoint()
        return lhs.same(rhs)
    return False


def just(values):
    res = flatten(values)

    return res


def forever(values):
    part = flatten(values)
    while True:
        yield from part


def only(maybe):
    if isinstance(maybe, Gvalue) and len(maybe) == 1:
        return maybe[0]

    if isinstance(maybe, typing.Iterator):
        return next(maybe)

    if isinstance(maybe, typing.Iterable):
        return maybe[0]
    return maybe


def comment(*lines):
    emit_stat(CommentLines(lines))
