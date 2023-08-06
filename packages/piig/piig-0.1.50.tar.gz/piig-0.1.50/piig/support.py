import ast
import logging
import sys
import typing
import metadict

# from piig import gtype
# from piig import ity
# from piig import axis
from piig import coords, goto
from piig import exception as ex
from piig import fortest
from piig import gbl
from piig import gtype
from piig import lib
from piig import nd
from piig import op


print(sys.path)
# from itertools import zip_longest
# from typing import Any
# from typing import Callable
# from typing import Dict
# from typing import Optional

# import metadict


RERAISE = 1


# class DictList:
#     def __init__(self):
#         self.l = []

#     def append(self, md: "MacroDictionary"):
#         self.l.append(md)

#     def to_gcode_and_comment_lines(self):
#         for el in self.l:
#             yield from el.to_gcode_and_comment_lines()


# dictlist = DictList()


def to_symtab_entry_from_any(thing):
    if isinstance(thing, list):
        return str(thing)
    if isinstance(thing, str):
        return thing
    if nd.is_constant(thing):
        return str(thing)
    return thing.to_symtab_entry()


# see foo=var(...)
# then x+foo, foo means &,
def array_to_reference(x):
    if isinstance(x, coords.ARRAY):
        return op.hashop(x._addr)
    return x

    # class MacroDictionary:
    #     def __init__(self):
    #         self._guts = {}
    #         breakpoint()
    #         dictlist.append(self)

    # def __setattr__(self, variable_name, variable_obj):
    #     #        print(sandl.current_source_line())
    #     if variable_name[0] == "_":
    #         object.__setattr__(self, variable_name, variable_obj)
    #     else:
    #         if variable_name in self._guts:
    #             breakpoint()
    #             ex.rErrorHere(f"Redefinition of '{variable_name}'.")

    #         self._guts[variable_name] = variable_obj

    # #            variable_obj._set_name(variable_name)

    # def __setitem__(self, variable_name, variable_obj):
    #     if variable_name in self._guts:
    #         ex.rErrorHere(f"Redefinition of 2 '{variable_name}'.")
    #     self._guts[variable_name] = variable_obj

    # def __getitem__(self, variable_name):
    #     #        try
    #     print("GI", variable_name)

    #     return self._guts[variable_name]

    # #        except KeyError:
    # #            ex.make_ErrorHere(f"Undefined symbol '{variable_name}'.")

    # def __getattr__(self, key):
    #     if key[0] == "_":
    #         return object.__getattribute__(self, key)

    #     return self._guts[key]

    #    def update(self, incoming):
    #        self._guts = {**self._guts, **incoming._guts}

    # @classmethod
    # def __setattr__(cls, o, v):
    #     print(o)
    #     setattr(cls, o, v)


opmap = {
    ast.Add: lambda x, y: x + y,
    ast.Sub: lambda x, y: x - y,
    ast.Mult: lambda x, y: x * y,
    ast.Div: lambda x, y: x / y,
    ast.FloorDiv: lambda x, y: x // y,
    ast.Mod: lambda x, y: x % y,
    ast.Pow: lambda x, y: x**y,
    ast.LShift: lambda x, y: x << y,
    ast.RShift: lambda x, y: x >> y,
    ast.BitAnd: lambda x, y: x & y,
    ast.BitOr: lambda x, y: x | y,
    ast.BitXor: lambda x, y: x ^ y,
    ast.Eq: lambda x, y: x == y,
    ast.NotEq: lambda x, y: x != y,
    ast.Lt: lambda x, y: x < y,
    ast.LtE: lambda x, y: x <= y,
    ast.Gt: lambda x, y: x > y,
    ast.GtE: lambda x, y: x >= y,
    ast.Is: lambda x, y: x is y,
    ast.IsNot: lambda x, y: x is not y,
    ast.In: lambda x, y: x in y,
    ast.NotIn: lambda x, y: x not in y,
}

unops = {
    ast.UAdd: lambda x: +x,
    ast.USub: lambda x: -x,
    ast.Invert: lambda x: ~x,
    ast.Not: lambda x: not x,
}


# rules
# - where only one cosys, that wins.
#  - otherwise there's trouble.


# canonify into list
# values may come not in out tree, so make sure
# everything is inside only one rvalue
def clist(x):
    if isinstance(x, (list, nd.Gvalue, coords.ARRAY)):
        return x
    return [x]


# turn whatever it is into a flat list.


def listify(x):
    if lib.is_iterable(x):
        return list(x)
    return [x]


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
    ",": ",",
    " ": " ",
    '"': "",
    "'": "",
    "#": "#",
    "_": "_",
    **{chr(x): chr(x) for x in range(0, 127) if chr(x).isalnum()},
}


# clean up a comment so nothing bad is in it.
# and remove words which happen a lot.

counter = 120


#        self._addr = 123


todo: list = []
one_of_ours = {}


# things needed for expressions to evaluate


class Statements:
    stats: list
    total = 0

    def __init__(self):
        self.stats = []

    def checkcode(self, compare):
        sts = self.to_full_lines()
        res = fortest.LG(sts, [*compare])
        return res

    def reset(self):
        self.stats = []

    def emit_stat(self, sl):
        for el in listify(sl):
            for line in el.to_gcode_lines():
                logging.debug("X" + line)

            Statements.total += 1
            if Statements.total > 1000:
                breakpoint()
            self.stats.append(el)

    def to_full_lines(self):
        for line in self.stats:
            yield from line.to_full_lines()

    # def write(self, outf):
    #     for line in self.to_full_lines():
    #         outf.write(line)


# something with an lval is associated with actual  macro variable(s).


# eg , G54 = WorkOffsetTable(_addr=5221)
# foo = G54.XY( 1,2)  - new variable foo, at 1,x relative to G54.

# def __init__(self, ctx, _addr=None):
#     self._addr = _addr
#     self.ctx = ctx
#     self.n = (_addr - 5221) // 20 + 54
#     super().__init__(_addr=_addr, size=6)

# def __repr__(self):
#     return f"TOF {self._addr} {self.n}"

# def __call__(self, *args, **kwargs):
#     co, cosize, _ = unpack_cos_inner(args, kwargs)
#     res = LValue(
#         ctx=self.ctx,
#         _addr=self._addr,
#         size=cosize,
#     )
#     if co:
#         res[:] = forever(co)
#     return res


class Operators:
    def AsAddress(self, src):
        return src

    def Address(self, src):
        src = nd.scalarify(src)
        if src.opinfo.pyname == "#":
            return src.child
        ex.rErrorHere("Can only take address of something with location.")


prev_line = ""


# turn a list of lines into a list of lines surrounded by parens.
# and drop duplicte lines.


#        for line in self.to_gcode_lines():


class E:
    pass


def load_tool(tool):
    code(f"T{tool:02} M06")


def setup_probing(probe):
    load_tool(probe)

    code(gbl.ctx.st.PROBE_ON)
    code(gbl.ctx.st.NO_LOOKAHEAD)


class BlockContext:
    def __init__(self):
        self.ebss = 100
        self.statements = Statements()
        self.label_gen = nd.Label_Gen()

    def reset(self):
        self.ebss = 100
        self.statements.reset()
        self.label_gen.reset()


class FR(lib.AttrDict):
    slow: float
    normal: float
    fast: float

    def __init__(self, slow=10, normal=50, fast=650):
        super().__init__()
        self.slow = slow
        self.normal = normal
        self.fast = fast


def table_of_macro_vars(symbol_table, varrefs, show_names, show_vars):
    lcols = []
    rcols = []

    # go through table of all known macro names,
    # find out if used, and print nicely.

    for k, v in symbol_table.items():
        if isinstance(v, coords.ARRAY):
            if not show_vars:
                continue

            hit_indexes = {}

            for el, addr in enumerate(range(v._addr, v._addr + v._size)):
                if addr in varrefs:
                    hit_indexes[el] = True
            if hit_indexes:
                lcols.append(k)
                rcols.append(v.to_symtab_entry(hit_indexes))

        else:
            if not show_names:
                continue
            lcols.append(k)
            rcols.append(to_symtab_entry_from_any(v))
    lsize = lib.max_str_len(lcols)

    for k, v in zip(lcols, rcols):
        yield k.ljust(lsize) + " : " + v


def to_symbol_table(symbol_table, varrefs, show_names, show_vars):
    yield from table_of_macro_vars(symbol_table, varrefs, show_names, show_vars)


class Params(lib.AttrDict):
    goto_rate: FR
    probe_rate: FR
    probe_tool: int
    wcs: int
    machine: typing.Any

    def __init__(self, **kwargs):
        super().__init__()
        self.goto_rate = FR()
        self.probe_rate = FR(slow=10, normal=10)
        self.probe_tool = 1
        self.wcs = 54
        for k, v in kwargs.items():
            assert hasattr(self, k)
            setattr(self, k, v)


def make_symbol_table(table, varrefs, show_names=True, show_vars=True, outfile=None):
    return to_symbol_table(table, varrefs, show_names, show_vars)


def code(txt):
    nd.emit_stat(nd.makeCode(txt))


# gbl.emit_stat = emit_stat


class CTX(Operators):
    def insert_symbol_table(self, show_names=True, show_vars=True, outfile=None):
        nd.CommentLines.emit(
            make_symbol_table(self.st, self.varrefs, show_names, show_vars)
        )

    @property
    def goto(self):
        return goto.Goto()

    def to_compiled_code(self, with_version):
        return gtype.CompiledCode(
            self.block_context.statements.to_full_lines(), with_version=with_version
        )

    root_block_context = None

    def varref(self, idx):
        self.varrefs[idx] = True

    # def write(self, outf):
    #     self.block_context.statements.write(outf)

    def next_label(self):
        return self.block_context.label_gen.next()

    def emit_multi_set(self, dst, src):
        for lhs, rhs in zip(clist(dst), nd.one_is_forever(src)):
            nd.emit_single_set(lhs, rhs)

    def __init__(self, outer=None):
        super().__init__()

        self._wcs = None
        self.ebss = None
        self.label_gen = None
        self.varrefs = {}
        self.outer = outer
        self.params = Params()
        self.last_node = None
        op.ctx = self
        coords.ctx = self
        gbl.ctx = self

        self.st = metadict.MetaDict()
        if outer is None:
            CTX.root_block_context = BlockContext()
            self.block_context = CTX.root_block_context
        else:
            self.block_context = outer.block_context

    @property
    def Vec(self):
        return coords.TypeBuilderAutoAddr(ctx=self)

    @property
    def Var(self):
        return coords.TypeBuilderAutoAddr(ctx=self)

    @property
    def Const(self):
        return coords.TypeBuilderConst()

    @property
    def FixedVec(self):
        return coords.TypeBuilderFixedAddr()

    @property
    def FixedVar(self):
        return coords.TypeBuilderFixedAddr()

    ex = ex

    def checkcode(self, *compare):
        res = self.block_context.statements.checkcode(compare)
        self.block_context.reset()
        return res

    # def call_function(self, *, newctx, func, args, kwargs):
    #     # a bottled function has already been stored
    #     # as ast. start running it.
    #     if newctx is None:
    #         newctx = CTX()
    #     if isinstance(func, SI):
    #         stored_func = func
    #         logger.debug(f"calling {stored_func.fn}")

    #         res = run_and_catch_errors(newctx, stored_func, args, kwargs)

    #         return res

    #     if isinstance(func, TOCALL1):
    #         return func(self, *args, **kwargs)

    #     return func(*args, **kwargs)

    # def inline(self, fn):
    #     one_of_ours[fn] = fn
    #     return interp.TOCALL(fn, inline=True)

    def alert(self, s):
        nd.emit_stat(
            nd.makeCode(
                f"#{self.st['STOP_WITH_MESSAGE']._addr} = 100",
                comment=s,
            )
        )

    def error(self, s):
        nd.emit_stat(
            nd.makeCode(
                f"#{self.st['ALARM']._addr} = 100", comment=s
            )  # clean_comment(s)})", show_comment=False)
        )

    def dprint(self, s):
        nd.emit_stat(
            nd.makeCode(
                f"#{self.st['STOP_WITH_MESSAGE']._addr} = 100",
                comment=s,
            )
        )

    def comment(self, *lines):
        nd.comment(*lines)

    @property
    def base_addr(self):
        return self.block_context.ebss

    @base_addr.setter
    def base_addr(self, v):
        self.block_context.ebss = v

    @property
    def wcs(self):
        return self._wcs

    @wcs.setter
    def wcs(self, val):
        self._wcs = (val._addr - 5221) // 20 + 54
        code(f"G{self.wcs}")
