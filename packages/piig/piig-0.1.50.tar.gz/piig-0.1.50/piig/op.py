import ast
import typing

from piig import exception as ex
from piig import lib
from piig import nd
from piig import support


def known_zero(x):
    if x == 0:
        return True
    if nd.is_constant(x):
        return False
    breakpoint()
    return False


def is_multi(arg):
    return isinstance(arg, (list, nd.Gvalue))


def make_scalar_binop(pyname, lhs, rhs):
    return make_scalar_binop_by_opinfo(allops[pyname], lhs, rhs)


def make_scalar_unop(pyname, child):
    return make_scalar_unop_by_opinfo(allops[pyname], child)


def make_scalar_binop_by_opinfo(opinfo, lhs, rhs):
    assert not is_multi(lhs), "a"
    assert not is_multi(rhs), "b"

    if isinstance(rhs, list):
        breakpoint()
        return perform_list_op(opinfo, lhs, rhs)

    # can it be done right now?
    if nd.is_constant(lhs) and nd.is_constant(rhs):
        with ex.try_this():
            if isinstance(lhs, float) or isinstance(rhs, float):
                lhs = float(lhs)
                rhs = float(rhs)
            if opinfo.pyname == "round":
                rhs = int(rhs)
            if opinfo.mth is None:
                breakpoint()
            else:
                return lhs.__getattribute__(opinfo.mth)(rhs)

    # put contant on rhs if we can
    if opinfo.commutative and nd.is_constant(lhs) and not nd.is_constant(rhs):
        lhs, rhs = rhs, lhs

    if opinfo.opt_sbinop:
        with ex.try_this():
            return opinfo.opt_sbinop(opinfo, lhs, rhs)

    return Binop(opinfo, lhs, rhs)


def make_scalar_unop_by_opinfo(opinfo, child):
    if isinstance(child, list):
        breakpoint()
        return perform_list_op(opinfo, child, 0)

    # can it be done right now?
    if nd.is_constant(child):
        with ex.try_this():
            return getattr(child, opinfo.mth)()

    if opinfo.opt_unop:
        with ex.try_this():
            return opinfo.opt_unop(opinfo, child)

    return Unop(opinfo, child)


def make_unop(optyp, lhs):
    oinfo = op_byclass[optyp]
    return make_unop_withopinfo(oinfo, lhs)


def make_binop(optyp, lhs, rhs):
    oinfo = op_byclass[optyp]

    return make_binop_withopinfo(oinfo, lhs, rhs)


def make_unop_withopinfo(oinfo, arg):
    try:
        res = []
        lgen = nd.just(arg)
        for litem in lgen:
            res.append(make_scalar_unop_by_opinfo(oinfo, litem))
        return nd.Gvalue.make(res)
    except ex.CantBeDone:
        return Unop(oinfo, arg)


def make_binop_withopinfo(oinfo, lhs, rhs):
    try:
        res = []
        lgen = nd.just(lhs)
        #        breakpoint()

        rgen = nd.one_is_forever(rhs)

        for litem, ritem in zip(lgen, rgen):
            res.append(make_scalar_binop_by_opinfo(oinfo, litem, ritem))

        return nd.Gvalue.make(res)
    except ex.CantBeDone:
        return Binop(oinfo, lhs, rhs)


def parensif(cond, thing):
    if cond:
        return "[" + thing + "]"
    return thing


class Op(nd.Exp):
    #    def __iter__(self):
    #        yield self

    def __init__(self, opinfo):
        super().__init__()
        self.opinfo = opinfo

    def precedence(self):
        return self.opinfo.precedence

    def to_symtab_entry(self):
        return str(self)


class Binop(Op):
    def same(self, other):
        return (
            self.opinfo == other.opinfo
            and nd.same(self.lhs, other.lhs)
            and nd.same(self.rhs, other.rhs)
        )

    def __init__(self, opinfo, lhs, rhs):
        super().__init__(opinfo)
        self.lhs = lhs
        self.rhs = rhs

    def to_gcode(self, need_int: bool = False):
        if self.opinfo.g_func:
            res = [nd.to_gcode(self.lhs, need_int), nd.to_gcode(self.rhs, need_int)]
            return f"{self.opinfo.gname}[{','.join(res)}]"

        res = []

        outer_prec = self.opinfo.precedence

        def handle_term(node):
            return parensif(
                get_precedence(node) < outer_prec, nd.to_gcode(node, need_int)
            )

        res.append(handle_term(self.lhs))
        res.append(self.opinfo.gname)
        res.append(handle_term(self.rhs))

        return " ".join(res)

    def __repr__(self):
        return f"({self.lhs}{self.opinfo.pyname}{self.rhs})"


def known_equal(lhs, rhs):
    return nd.same(lhs, rhs)


def get_precedence(thing):
    with ex.try_this():
        return thing.precedence()
    return 20


ctx: support.CTX = typing.cast(support.CTX, None)


class Unop(Op):
    def same(self, other):
        return self.opinfo == other.opinfo and nd.same(self.child, other.child)

    def __init__(self, opinfo, child):
        super().__init__(opinfo)
        self.child = child

    def to_gcode(self, need_int: bool = False):
        res = []

        if self.opinfo.pyname == "#":
            ctx.varref(self.child)

        outer_prec = self.opinfo.precedence
        assert self.opinfo.nargs == 1

        res.append(self.opinfo.gname)
        # at least # is left right associative.
        inside_prec = get_precedence(self.child)

        res.append(
            parensif(
                outer_prec >= inside_prec,
                nd.to_gcode(self.child, self.opinfo.force_int or need_int),
            )
        )

        return "".join(res)

    def __repr__(self):
        return f"({self.opinfo.pyname} {self.child})"


class Opinfo:
    ast_class: typing.Any
    cls: str
    pyname: str
    mth: str
    gname: str
    precedence: int
    extra: str

    commutative: bool
    nargs: int
    # if argument should be forced to int - as in '#'
    force_int: bool
    opt_sbinop: typing.Callable
    opt_unop: typing.Callable

    def __repr__(self):
        return self.pyname

    def __init__(self, ast_class, pyname, **kwargs):
        self.ast_class = ast_class
        lib.apply(
            lambda kv: setattr(self, kv[0], kwargs.get(*kv)),
            [
                ("precedence", 20),
                ("g_func", False),
                ("cls", ""),
                ("pyname", pyname),
                ("nargs", 1 if pyname[0].isalpha() else 2),
                ("mth", None),
                ("opt_unop", None),
                ("opt_sbinop", None),
                ("commutative", False),
                ("gname", pyname),
                ("force_int", False),
                ("extra", pyname),
            ],
        )

        assert isinstance(self.precedence, int), "A"


allops: typing.Dict[str, Opinfo] = {}


def perform_list_op(opinfo, lhs, rhs):
    if opinfo.pyname == "+":
        return lhs + rhs

    if opinfo.pyname == "*":
        return lhs * rhs

    ex.rErrorHere("Bad list operation")


def opinfo_install(opinfo: Opinfo):
    def make_multi_binop_tramp(lhs, rhs):
        return make_binop_withopinfo(opinfo, lhs, rhs)

    def make_multi_unop_tramp(child):
        return make_unop_withopinfo(opinfo, child)

    # if opinfo.mth:
    #     setattr(nd.Exp, opinfo.mth, op_maker)
    #     opinfo.op_maker = op_maker
    if opinfo.mth:
        if opinfo.nargs == 1:
            setattr(nd.Exp, opinfo.mth, make_multi_unop_tramp)
        else:
            setattr(nd.Exp, opinfo.mth, make_multi_binop_tramp)


#    setattr(ScalarOps, opinfo.mth, mp)
#    setattr(ArrayOps, opinfo.mth, mp)


revop = {
    "+": "+",
    "-": "+",
    "*": "*",
    "/": "*",
}


def opt_sbinop_fold(opinfo, lhs, rhs):
    rop = revop.get(opinfo.pyname)

    if rop and lhs.opinfo == opinfo and nd.is_constant(lhs.rhs) and nd.is_constant(rhs):
        return make_scalar_binop_by_opinfo(
            opinfo, lhs.lhs, make_scalar_binop(rop, lhs.rhs, rhs)
        )

    raise ex.CantBeDone


def get_float(arg):
    if isinstance(arg, (int, float)):
        return float(arg)
    return None


def opt_sbinop_mul(opinfo, lhs, rhs):
    match get_float(rhs):
        case 0.0:
            return 0.0
        case 1.0:
            return lhs
        case -1.0:
            return make_scalar_unop("un-", lhs)

    return opt_sbinop_fold(opinfo, lhs, rhs)


def opt_sbinop_div(opinfo, lhs, rhs):
    match get_float(rhs):
        case 0.0:
            ex.rErrorHere(f"Divide by zero {lhs}/{rhs}")
        case 1.0:
            return lhs
        case -1.0:
            return make_scalar_unop("un-", lhs)

    return opt_sbinop_fold(opinfo, lhs, rhs)


def opt_unop_fold(opinfo, child):
    raise ex.CantBeDone


not_compop = {
    "==": "!=",
    "!=": "==",
    "<": ">=",
    ">": "<=",
    "<=": ">",
    ">=": "<",
}


def opt_unop_not(opinfo, arg):
    if nd.is_constant(arg):
        return not arg

    if arg.opinfo == opinfo:
        return arg.child

    # got not(comop, turn into (inverted compop))

    if notted := not_compop.get(arg.opinfo.pyname):
        return make_scalar_binop(notted, arg.lhs, arg.rhs)

    return make_scalar_binop("!=", arg, 0)


def opt_unop_plus(_, arg):
    return arg


# don't have binary not operator, make from xor.
def opt_unop_invert(_, arg):
    return make_scalar_binop("^", arg, 0)


def opt_sbinop_comp(opinfo, lhs, rhs):
    raise ex.NotThisWay


# (a1 > a2)  == 0
# => (a1 <= a2)
# etc


def opt_sbinop_eq(opinfo, lhs, rhs):
    if not known_zero(rhs):
        raise ex.CantBeDone

    if rev := not_compop.get(lhs.opinfo.pyname):
        if opinfo.pyname == "==":
            return make_scalar_binop(rev, lhs.lhs, lhs.rhs)
        if opinfo.pyname == "!=":
            return lhs
        assert False
    raise ex.CantBeDone()


def opt_sbinop_add(opinfo, lhs, rhs):
    with ex.try_this():
        return opt_sbinop_fold(opinfo, lhs, rhs)

    if isinstance(rhs, Op) and rhs.opinfo.pyname == "un-":
        return make_scalar_binop("-", lhs, rhs.child)

    if not nd.is_constant(rhs):
        raise ex.NotThisWay

    rv = float(rhs)
    if rv < 0.0:
        t1 = make_scalar_binop("-", lhs, -rv)
        return t1

    with ex.try_this():
        if float(rhs) == 0.0:
            return lhs

    raise ex.NotThisWay


op_byclass = {}


def xx(precedence, astclass, pyname, com=False, **kwargs):
    opinfo = Opinfo(
        astclass,
        pyname,
        precedence=precedence,
        commutative=com,
        **kwargs,
    )
    allops[pyname] = opinfo
    op_byclass[astclass] = opinfo
    opinfo_install(opinfo)


# def make_round(val, precision):
#     if ex.try_this():
#         return round(val,precision)

#     tens = Glist(typ=typ.Float, co=[10**precision]*len(lhs))
#     # turn round(a,b) into (round (a/(10**b))) *(10**b)


# flake8:  noqa
xx(4, ast.BitOr, "|", mth="__or__", gname="OR", com=True)
xx(5, ast.BitXor, "^", mth="__xor__", gname="XOR", com=True)
xx(6, ast.BitAnd, "&", mth="__and__", gname="AND", com=True)

xx(10, ast.Lt, "<", mth="__lt__", opt_sbinop=opt_sbinop_comp, gname="LT", cls="compare")
xx(
    10,
    ast.LtE,
    "<=",
    mth="__le__",
    opt_sbinop=opt_sbinop_comp,
    gname="LE",
    cls="compare",
)
xx(
    10,
    ast.NotEq,
    "!=",
    mth="__ne__",
    gname="NE",
    opt_sbinop=opt_sbinop_eq,
    cls="eq",
    com=True,
)
xx(
    10,
    ast.Eq,
    "==",
    mth="__eq__",
    gname="EQ",
    opt_sbinop=opt_sbinop_eq,
    cls="eq",
    com=True,
)
# xx(10, ast.Is, "is", mth="__is__", nargs=2, opt_sbinop=opt_sbinop_equality, gname="EQ", com=True)
# xx(
#     10,
#     ast.IsNot,
#     "isnot",
#     mth="__isnot__",
#     nargs=2,
#     opt_sbinop=opt_sbinop_comp,
#     gname="NE",
#     com=True,
# )
xx(10, ast.Gt, ">", mth="__gt__", opt_sbinop=opt_sbinop_comp, gname="GT", cls="compare")
xx(
    10,
    ast.GtE,
    ">=",
    mth="__ge__",
    opt_sbinop=opt_sbinop_comp,
    gname="GE",
    cls="compare",
)
xx(12, ast.Sub, "-", mth="__sub__")
xx(12, None, "-rev", mth="__rsub__")
xx(12, ast.Add, "+", mth="__add__", opt_sbinop=opt_sbinop_add, com=True)
xx(12, None, "round", nargs=2, mth="__round__")
xx(13, ast.Mult, "*", mth="__mul__", com=True, opt_sbinop=opt_sbinop_mul)
xx(13, ast.Div, "/", mth="__truediv__", opt_sbinop=opt_sbinop_div)
xx(13, ast.FloorDiv, "//", mth="__floordiv__", opt_sbinop=opt_sbinop_div)
xx(14, ast.Mod, "%", mth="__mod__", gname="MOD")

xx(14, ast.USub, "un-", gname="-", mth="__neg__")
xx(14, ast.UAdd, "un+", gname="+", opt_unop=opt_unop_plus, mth="__pos__")
xx(14, ast.Invert, "un~", mth="__invert__", opt_unop=opt_unop_invert)
xx(14, ast.Not, "unot", opt_unop=opt_unop_not)
xx(15, ast.Pow, "**", gname="POW", g_func=True, mth="__pow__")
xx(15, None, "abs", gname="ABS", g_func=True, nargs=1, mth="__abs__")

xx(19, None, "#", gname="#", nargs=1, force_int=True)


def hashop(arg):
    return Unop(allops["#"], arg)
