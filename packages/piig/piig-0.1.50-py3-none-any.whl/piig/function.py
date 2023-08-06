# any function inlined is part of a code generation tree.
# when finally run, gets own interpreter instance, and set of globals as seen
# when function was defined.
import functools
import inspect

from piig import deb
from piig import exception as ex
from piig import gtype
from piig import interp
from piig import ity
from piig import lib
from piig import nd
from piig import support


def prepare_func(self, node):
    """Prepare function AST node for future interpretation: pre-calculate
    and cache useful information, etc."""

    func = ity.InterpFuncWrap(node, self)
    args = node.args
    num_required = len(args.args) - len(args.defaults)
    all_args = set()
    d = {}
    for i, a in enumerate(args.args):
        all_args.add(a.arg)
        if i >= num_required:
            d[a.arg] = self.visit(args.defaults[i - num_required])
    for a, v in zip(args.kwonlyargs, args.kw_defaults):
        all_args.add(a.arg)
        if v is not None:
            d[a.arg] = self.visit(v)
    # We can store cached argument names of a function in its node -
    # it's static.
    node.args.all_args = all_args
    # We can't store the values of default arguments - they're dynamic,
    # may depend on the lexical scope.
    func.defaults_dict = d

    return ity.InterpFunc(func)


class Runnable:
    def __init__(self):
        pass


class InlineDefinition(Runnable):
    def __init__(self, fn, ast):
        super().__init__()
        self.fn = fn
        ast.fn = fn
        self.ast = ast

        self.it = interp.Interpreter("FISH", fn, ast)

    # was interpreting something and came to a call,
    # so go in there.
    def call_from_inside(self, interp, args, kwargs):
        self.call_worker(interp.ctx, args, kwargs)

    def call_worker(self, ctx, args, kwargs):
        deb.interp = self.it
        self.it.push_ns(ity.FunctionNS())
        sig = inspect.signature(self.fn)
        arguments = sig.bind(*args, **kwargs)
        arguments.apply_defaults()
        self.it.ns.update(arguments.arguments)
        self.it.start(ctx, self.ast.body[0].body)
        self.it.pop_ns()

    def call_from_outside(
        self, args=None, kwargs=None, create_ctx=False, with_version=True
    ) -> gtype.CompiledCode:
        if args is None:
            args = []
        if kwargs is None:
            kwargs = {}
        if create_ctx:
            ctx = support.CTX(None)
            args = list(args)
            args.insert(0, ctx)
        else:
            breakpoint()
            ctx = args[0]
        try:
            self.call_worker(ctx, args, kwargs)
            return ctx.to_compiled_code(with_version)
        except AssertionError as err:
            #            breakpoint()
            nd.show_error_at(str(err))
            raise err
        except ex.ErrorHere as err:
            nd.show_error_at(str(err))
        return None

    def __call__(self, *args, **kwargs):
        return self.fn(*args, **kwargs)


# at definition of an inline function,
# just remember the tree.
def inline(fn):
    if isinstance(fn, InlineDefinition):
        print(f"ALREADY INLINE {fn.fn}")
        breakpoint()
        return fn

    return InlineDefinition(fn, interp.just_ast(fn))


# this is the head of a gcode trace to be emitted.
def to_macro(fn, *args, **kwargs):
    lib.trygetarg("outfile", kwargs)

    return inline(fn).call_from_outside(args, kwargs, create_ctx=True)


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


def macro(fn):
    @functools.wraps(fn)
    def macro_(*args, **kwargs):
        to_macro(fn, *args, **kwargs)

    return macro_


@inline
def foop(ctx, output, idx):
    print(output)

    CURSOR = ctx.Vec(20, 30)
    CURSOR.xy += [71, 17]


def output_macro(fn, outfile):
    assert isinstance(fn, InlineDefinition)

    with open(outfile, "w") as outf:
        newctx = fn.call_from_outside(create_ctx=True)
        newctx.write(outf)


def to_full_lines(fn):
    yield from inline(fn).call_from_outside(create_ctx=True).to_full_lines()


def emoty():
    pass


@for_test
def doit1(g):
    zap = g.Var[2]()

    zap.xy = 1

    #        assert (zap == zap2).y == 0


def doit():
    doit1()
