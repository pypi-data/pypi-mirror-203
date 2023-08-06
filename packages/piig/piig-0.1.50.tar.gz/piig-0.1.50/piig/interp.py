# Python AST interpreter written in Python
#
# This module is part of the Pycopy https://github.com/pfalcon/pycopy
# project.
#
# Copyright (c) 2019 Paul Sokolovsky
#
# The MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#   (pycoverage-mode)
import ast
import builtins
import inspect
import sys
import typing

from typing import Optional

from piig import exception as ex
from piig import function
from piig import gbl
from piig import ity
from piig import nd
from piig import op


SOURCE = 0


class StrictNodeVisitor(ast.NodeVisitor):
    def generic_visit(self, node):
        n = node.__class__.__name__
        raise NotImplementedError("Visitor for node {} not implemented".format(n))


# (coverlay--switch-mode t)


# Pycopy by default doesn't support direct slice construction, use helper
# object to construct it.
class SliceGetter:
    def __getitem__(self, idx):
        return idx


slice_getter = SliceGetter()


class TargetNonlocalFlow(Exception):
    """Base exception class to simulate non-local control flow transfers in
    a target application."""

    pass


class TargetBreak(TargetNonlocalFlow):
    pass


class TargetContinue(TargetNonlocalFlow):
    pass


class TargetReturn(TargetNonlocalFlow):
    pass


class VarScopeSentinel:
    def __init__(self, name):
        self.name = name


NO_VAR = VarScopeSentinel("no_var")
GLOBAL = VarScopeSentinel("global")
NONLOCAL = VarScopeSentinel("nonlocal")


# Python don't fully treat objects, even those defining __call__() special
# method, as a true callable. For example, such objects aren't automatically
# converted to bound methods if looked up as another object's attributes.
# As we want our "interpreted functions" to behave as close as possible to
# real functions, we just wrap function object with a real function. An
# alternative might have been to perform needed checks and explicitly
# bind a method using types.MethodType() in visit_Attribute (but then maybe
# there would be still other cases of "callable object" vs "function"
# discrepancies).


class InterpWith:
    def __init__(self, ctx):
        self.ctx = ctx

    def __enter__(self):
        return self.ctx.__enter__()

    def __exit__(self, tp, exc, tb):
        # Don't leak meta-level exceptions into target
        if isinstance(exc, TargetNonlocalFlow):
            tp = exc = tb = None
        return self.ctx.__exit__(tp, exc, tb)


class InterpModule:
    def __init__(self, ns):
        self.ns = ns

    def __getattr__(self, name):
        try:
            return self.ns[name]
        except KeyError:
            raise AttributeError

    def __dir__(self):
        return list(self.ns.d.keys())


def geniter(self, *, whileexp=None, target=None, itr=None, body=None, orelse=None):
    self.loop = LoopContext(self.ctx, self.loop)

    if whileexp:
        nd.emit_stat(nd.LabelDef(self.loop.lcontinue))
        test = op.make_unop(ast.Not, self.visit(whileexp))
        nd.emit_stat(nd.If(test, self.loop.lorelse))
    else:
        assert itr
        self.handle_assign(target, itr.start)
        nd.emit_stat(nd.LabelDef(self.loop.lcontinue))
        nd.emit_stat(
            nd.If(
                op.make_binop(
                    ast.Eq,
                    self.force_load(target),
                    itr.stop,
                ),
                self.loop.lorelse,
            )
        )

    self.visit_x(body)
    nd.emit_stat(nd.Goto(self.loop.lcontinue))
    if orelse:
        nd.emit_stat(nd.LabelDef(self.loop.lorelse))
        self.visit_x(orelse)
        if self.loop.lbreak.used():
            nd.emit_stat(nd.LabelDef(self.loop.lbreak))
    else:
        if self.loop.lbreak.used():
            nd.emit_stat(nd.LabelDef(self.loop.lbreak))
        nd.emit_stat(nd.LabelDef(self.loop.lorelse))
    self.loop = self.loop.prev


# class StoredInline:
#     def __init__(self, inline=False):
#         pass

#     def __call__(self, interp, *args, **kwargs):
#         call_func_with_interpreter(interp, *args, **kwargs)
#     def call_func_with_interpreter(self, node, interp_func, *args, **kwargs):


class LoopContext:
    lcontinue: nd.Label
    lbreak: nd.Label
    lorelse: nd.Label
    ivariable: nd.N
    prev: "LoopContext"
    depth: int

    def __init__(self, ctx, prev):
        self.prev = prev
        if prev is None:
            self.depth = 0
        else:
            self.depth = prev.depth + 1

        self.lcontinue = ctx.next_label()
        self.lbreak = ctx.next_label()
        self.lorelse = ctx.next_label()


class Interpreter(StrictNodeVisitor):
    ns: Optional[ity.ANamespace]
    module_ns: Optional[ity.ModuleNS]
    #    exit_label: nd.Label_Gen
    inline: bool
    fname: str
    inside: bool
    store_val: typing.Any
    cur_exc: list
    last_place: list

    def __init__(self, ctx, fn, node, inline=False):
        #        self.exit_label = iface.face.next_label()
        self.ctx = None
        self.inline = inline
        self.last_place = [node, node, node]
        self.module_ns = ity.ModuleNS()
        self.ns = self.module_ns
        self.fn = fn
        self.inside = False
        self.loop = None
        self.module_ns = None
        self.store_val = None
        self.cur_exc = []

    def push_ns(self, new_ns):
        new_ns.parent = self.ns
        self.ns = new_ns

    def pop_ns(self):
        self.ns = self.ns.parent

    def stmt_list_visit(self, lst):
        res = None
        for s in lst:
            res = self.visit(s)
        return res

    def start(self, ctx, ast):
        self.ctx = ctx
        #        self.exit_label = ctx.next_label()
        #        nd.emit_stat(nd.Comment(self.fn))
        self.visit_x(ast)

    #        nd.emit_stat(nd.LabelDef(self.ctx, self.exit_label))

    def visit_x(self, lst):
        if isinstance(lst, list):
            return self.stmt_list_visit(lst)
        return self.visit(lst)

    def wrap_decorators(self, obj, node):
        for deco_n in reversed(node.decorator_list):
            deco = self.visit(deco_n)
            obj = deco(obj)
        return obj

    def visit_Module(self, node):
        self.ns = self.module_ns = ity.ModuleNS()

        #        self.ns.d.update(**self.fn.__globals__)
        self.ns["__file__"] = self.fn.__name__
        self.ns["__name__"] = "__main__"
        sys.modules["__main__"] = InterpModule(self.ns)
        self.stmt_list_visit(node.body)

    def visit_Expression(self, node):
        return self.visit(node.body)

    def visit_ClassDef(self, node):
        self.push_ns(ity.ClassNS())
        try:
            self.stmt_list_visit(node.body)
        except:
            self.pop_ns()
            raise
        ns = self.ns
        self.pop_ns()
        cls = type(node.name, tuple([self.visit(b) for b in node.bases]), ns.d)
        cls = self.wrap_decorators(cls, node)
        self.ns[node.name] = cls
        # Store reference to class object in the namespace object
        ns.cls = cls

    def visit_Lambda(self, node):
        node.name = "<lambda>"
        assert False
        # return self.prepare_func(node)

    def visit_FunctionDef(self, node):
        if hasattr(node, "fn"):
            self.fn = node.fn

        # Defaults are evaluated at function definition time, so we
        # need to do that now.

        func = function.prepare_func(self, node)
        #        func = self.wrap_decorators(func, node)
        self.ns[node.name] = func

        return func

    def prepare_func_args(self, node, interp_func, *args, **kwargs):
        def arg_num_mismatch():
            ex.rErrorHere("bad arguments")

        argspec = node.args

        # If there's vararg, either offload surplus of args to it, or init
        # it to empty tuple (all in one statement). If no vararg, error on
        # too many args.
        if argspec.vararg:
            self.ns[argspec.vararg.arg] = args[len(argspec.args) :]
        else:
            if len(args) > len(argspec.args):
                arg_num_mismatch()

        for i in range(min(len(args), len(argspec.args))):
            self.ns[argspec.args[i].arg] = args[i]

        # Process incoming keyword arguments, putting them in namespace if
        # actual arg exists by that name, or offload to function's kwarg
        # if any. All make needed checks and error out.
        func_kwarg = {}
        for key, value in kwargs.items():
            if key in argspec.all_args:
                if key in self.ns:
                    ex.rErrorHere("bad arguments.")

                self.ns[key] = value
            elif argspec.kwarg:
                func_kwarg[key] = value
            else:
                ex.rErrorHere("bad arguments.")

        if argspec.kwarg:
            self.ns[argspec.kwarg.arg] = func_kwarg

        # Finally, overlay default values for arguments not yet initialized.
        # We need to do this last for "multiple values for the same arg"
        # check to work.
        for k, v in interp_func.defaults_dict.items():
            if k not in self.ns:
                self.ns[k] = v

        # And now go thru and check for any missing arguments.
        for a in argspec.args:
            if a.arg not in self.ns:
                raise TypeError(
                    "{}() missing required positional argument: '{}'".format(
                        node.name, a.arg
                    )
                )
        for arg in argspec.kwonlyargs:
            if arg.arg not in self.ns:
                raise TypeError(
                    "{}() missing required keyword-only argument: '{}'".format(
                        node.name, arg.arg
                    )
                )

    def call_func(self, node, interp_func, *args, **kwargs):
        if hasattr(node, "fn"):
            self.fn = node.fn

        # We need to switch from dynamic execution scope to lexical scope
        # in which function was defined (then switch back on return).
        dyna_scope = self.ns
        self.ns = interp_func.lexical_scope
        self.push_ns(ity.FunctionNS())

        try:
            with nd.catch_errors():
                self.prepare_func_args(node, interp_func, *args, **kwargs)
                if isinstance(node.body, list):
                    res = self.stmt_list_visit(node.body)
                else:
                    res = self.visit(node.body)
        except TargetReturn as e:
            res = e.args[0]
        finally:
            self.pop_ns()
            self.ns = dyna_scope

        return res

    def visit_Return(self, node):
        if self.inline:
            breakpoint()
            rv = self.visit(node.value)
            nd.emit_stat(nd.Return(rv))
            #            nd.emit_stat(nd.Goto(self.exit_label))
            return rv

        if not isinstance(self.ns, ity.FunctionNS):
            raise SyntaxError("'return' outside function")
        raise TargetReturn(node.value and self.visit(node.value))

    def visit_With(self, node):
        assert len(node.items) == 1
        ctx = self.visit(node.items[0].context_expr)
        with InterpWith(ctx) as val:
            if node.items[0].optional_vars is not None:
                self.handle_assign(node.items[0].optional_vars, val)
            self.stmt_list_visit(node.body)

    def visit_Try(self, node):
        try:
            self.stmt_list_visit(node.body)
        except TargetNonlocalFlow:
            raise
        except Exception as e:
            self.cur_exc.append(e)
            try:
                for h in node.handlers:
                    if h.type is None or isinstance(e, self.visit(h.type)):
                        if h.name:
                            self.ns[h.name] = e
                        self.stmt_list_visit(h.body)
                        if h.name:
                            del self.ns[h.name]
                        break
                else:
                    raise
            finally:
                self.cur_exc.pop()
        else:
            self.stmt_list_visit(node.orelse)
        finally:
            self.stmt_list_visit(node.finalbody)
        # Could use "finally:" here to not repeat
        # stmt_list_visit(node.finalbody) 3 times

    def visit_For(self, node):
        itr = self.visit(node.iter)
        if not isinstance(itr, range):
            raise NotImplementedError
        return geniter(
            self, target=node.target, itr=itr, body=node.body, orelse=node.orelse
        )

    def oldvisit_For(self, node):
        itr = self.visit(node.iter)
        for item in itr:
            self.handle_assign(node.target, item)
            try:
                self.stmt_list_visit(node.body)
            except TargetBreak:
                break
            except TargetContinue:
                continue
        else:
            self.stmt_list_visit(node.orelse)

    def visit_While(self, node):
        geniter(self, whileexp=node.test, body=node.body, orelse=node.orelse)

    def oldvisit_While(self, node):
        while self.visit(node.test):
            try:
                self.stmt_list_visit(node.body)
            except TargetBreak:
                break
            except TargetContinue:
                continue
        else:
            self.stmt_list_visit(node.orelse)

    def visit_Break(self, node):
        nd.emit_stat(nd.Goto(self.loop.lbreak))

    def oldvisit_Break(self, node):
        raise TargetBreak

    def update_lastplace(self, node):
        gbl.interp = self
        self.last_place[2] = self.last_place[1]
        self.last_place[1] = self.last_place[0]
        self.last_place[0] = node
        gbl.last_node = node

    # overloading  for extra info.
    def visit(self, node):
        node.fn = self.fn
        self.update_lastplace(node)

        if SOURCE:
            nd.show_line_at(node)

        method = "visit_" + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)

        return visitor(node)

    def visit_Continue(self, node):
        raise TargetContinue

    def visit_If(self, node):
        #   for nicer looking code
        if isinstance(node.body[0], ast.Break):
            exp = op.make_unop(ast.UAdd, self.visit(node.test))

            nd.emit_stat(nd.If(exp, self.loop.lbreak))
            return

        elsepart = self.ctx.next_label()
        donepart = self.ctx.next_label()

        exp = op.make_unop(ast.Not, self.visit(node.test))
        nd.emit_stat(nd.If(exp, on_t=elsepart))
        self.visit_x(node.body)
        nd.emit_stat(nd.Goto(donepart))
        nd.emit_stat(nd.LabelDef(elsepart))
        self.visit_x(node.orelse)

        nd.emit_stat(nd.LabelDef(donepart))

    def oldvisit_If(self, node):
        test = self.visit(node.test)
        if test:
            self.stmt_list_visit(node.body)
        else:
            self.stmt_list_visit(node.orelse)

    def visit_Import(self, node):
        for n in node.names:
            self.ns[n.asname or n.name] = __import__(n.name)

    def visit_ImportFrom(self, node):
        mod = __import__(
            node.module, None, None, [n.name for n in node.names], node.level
        )
        for n in node.names:
            self.ns[n.asname or n.name] = getattr(mod, n.name)

    def visit_Raise(self, node):
        if node.exc is None:
            if not self.cur_exc:
                raise RuntimeError("No active exception to reraise")
            raise self.cur_exc[-1]
        if node.cause is None:
            raise self.visit(node.exc)
        else:
            raise self.visit(node.exc) from self.visit(node.cause)

    # briefly turns a store(or anything) node into a load node.
    def force_load(self, node):
        save_ctx = node.ctx
        node.ctx = ast.Load()
        res = self.visit(node)
        node.ctx = save_ctx
        return res

    def visit_AugAssign(self, node):
        self.store_val = op.make_binop(
            type(node.op),
            self.force_load(node.target),
            self.visit(node.value),
        )
        self.visit(node.target)

    def oldvisit_AugAssign(self, node):
        assert isinstance(node.target.ctx, ast.Store)
        # Not functional style, oops. Node in AST has store context, but we
        # need to read its value first. To not construct a copy of the entire
        # node with load context, we temporarily patch it in-place.
        save_ctx = node.target.ctx
        node.target.ctx = ast.Load()
        var_val = self.visit(node.target)
        node.target.ctx = save_ctx

        rval = self.visit(node.value)

        # As augmented assignment is statement, not operator, we can't put them
        # all into map. We could instead directly lookup special inplace methods
        # (__iadd__ and friends) and use them, with a fallback to normal binary
        # operations, but from the point of view of this interpreter, presence
        # of such methods is an implementation detail of the object system, it's
        # not concerned with it.
        op = type(node.op)
        if op is ast.Add:
            var_val += rval
        elif op is ast.Sub:
            var_val -= rval
        elif op is ast.Mult:
            var_val *= rval
        elif op is ast.Div:
            var_val /= rval
        elif op is ast.FloorDiv:
            var_val //= rval
        elif op is ast.Mod:
            var_val %= rval
        elif op is ast.Pow:
            var_val **= rval
        elif op is ast.LShift:
            var_val <<= rval
        elif op is ast.RShift:
            var_val >>= rval
        elif op is ast.BitAnd:
            var_val &= rval
        elif op is ast.BitOr:
            var_val |= rval
        elif op is ast.BitXor:
            var_val ^= rval
        else:
            raise NotImplementedError

        self.store_val = var_val
        self.visit(node.target)

    def visit_AnnAssign(self, node):
        if node.value is not None:
            breakpoint()
            val = self.visit(node.value)
            self.handle_assign(node.target, val)

    def visit_Assign(self, node):
        val = self.visit(node.value)
        for n in node.targets:
            self.handle_assign(n, val)

    def handle_assign(self, target, val):
        if isinstance(target, ast.Tuple):
            it = iter(val)
            try:
                for elt_idx, t in enumerate(target.elts):
                    if isinstance(t, ast.Starred):
                        t = t.value
                        all_elts = list(it)
                        break_i = len(all_elts) - (len(target.elts) - elt_idx - 1)
                        self.store_val = all_elts[:break_i]
                        it = iter(all_elts[break_i:])
                    else:
                        self.store_val = next(it)
                    self.visit(t)
            except StopIteration:
                ex.rErrorHere("not enough values to unpack")
            try:
                next(it)
                ex.rErrorHere("Too many values to unpack.")

            except StopIteration:
                # Expected
                pass
        else:
            self.store_val = val
            self.visit(target)

    def visit_Delete(self, node):
        for n in node.targets:
            self.visit(n)

    def visit_Pass(self, node):
        pass

    def visit_Assert(self, node):
        r = self.visit(node.test)
        if node.msg is None:
            if not r:
                assert r
        else:
            assert r, self.visit(node.msg)

    def visit_Expr(self, node):
        # Produced value is ignored
        self.visit(node.value)

    def enumerate_comps(self, iters):
        """Enumerate thru all possible values of comprehension clauses,
        including multiple "for" clauses, each optionally associated
        with multiple "if" clauses. Current result of the enumeration
        is stored in the namespace."""

        def eval_ifs(iter):
            """Evaluate all "if" clauses."""
            for cond in iter.ifs:
                if not self.visit(cond):
                    return False
            return True

        if not iters:
            yield
            return
        for el in self.visit(iters[0].iter):
            self.store_val = el
            self.visit(iters[0].target)
            for t in self.enumerate_comps(iters[1:]):
                if eval_ifs(iters[0]):
                    yield

    def visit_ListComp(self, node):
        self.push_ns(ity.FunctionNS())
        try:
            return [self.visit(node.elt) for _ in self.enumerate_comps(node.generators)]
        finally:
            self.pop_ns()

    def visit_SetComp(self, node):
        self.push_ns(ity.FunctionNS())
        try:
            return {self.visit(node.elt) for _ in self.enumerate_comps(node.generators)}
        finally:
            self.pop_ns()

    def visit_DictComp(self, node):
        self.push_ns(ity.FunctionNS())
        try:
            return {
                self.visit(node.key): self.visit(node.value)
                for _ in self.enumerate_comps(node.generators)
            }
        finally:
            self.pop_ns()

    def visit_IfExp(self, node):
        if self.visit(node.test):
            return self.visit(node.body)
        else:
            return self.visit(node.orelse)

    def visit_Call(self, node):
        func = self.visit(node.func)

        args = []
        for a in node.args:
            if isinstance(a, ast.Starred):
                args.extend(self.visit(a.value))
            else:
                args.append(self.visit(a))

        kwargs = {}
        for kw in node.keywords:
            val = self.visit(kw.value)
            if kw.arg is None:
                kwargs.update(val)
            else:
                kwargs[kw.arg] = val

        if func is builtins.super and not args:
            if not self.ns.parent or not isinstance(self.ns.parent, ity.ClassNS):
                raise RuntimeError("super(): no arguments")
            # As we're creating methods dynamically outside of class, super()
            # without argument won't work, as that requires __class__ cell.
            # Creating that would be cumbersome (Pycopy definitely lacks
            # enough introspection for that), so we substitute 2 implied
            # args (which argumentless super() would take from cell and
            # 1st arg to func). In our case, we take them from prepared
            # bookkeeping info.
            # args = (self.ns.parent.cls, self.ns["self"])
            assert False

        #        with nd.catch_outside_errors(self.modit):

        self.ctx.last_node = node
        if isinstance(func, function.InlineDefinition):
            return func.call_from_inside(self, args, kwargs)
        return func(*args, **kwargs)

    def visit_Compare(self, node):
        acc = self.visit(node.left)

        for cop, r in zip(node.ops, node.comparators):
            if isinstance(cop, ast.IsNot):
                breakpoint()

            acc = op.make_binop(type(cop), acc, self.visit(r))
        return acc

    def oldvisit_Compare(self, node):
        cmpop_map = {
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
        lv = self.visit(node.left)
        for op, r in zip(node.ops, node.comparators):
            rv = self.visit(r)
            if not cmpop_map[type(op)](lv, rv):
                return False
            lv = rv
        return True

    def visit_BoolOp(self, node):
        if isinstance(node.op, ast.And):
            res = True
            for v in node.values:
                res = res and self.visit(v)
        elif isinstance(node.op, ast.Or):
            res = False
            for v in node.values:
                res = res or self.visit(v)
        else:
            raise NotImplementedError
        return res

    def visit_JoinedStr(self, node):
        res = []

        for value in node.values:
            match value:
                case ast.Constant():
                    res.append(value.value)
                case ast.FormattedValue():
                    va = self.visit(value.value)
                    if value.format_spec is not None:
                        fv = self.visit(value.format_spec)
                        r = va.__format__(fv)
                    else:
                        r = str(va)
                    res.append(r)
                case _:
                    raise NotImplementedError

        return "".join(res)

    def visit_BinOp(self, node):
        return op.make_binop(
            type(node.op),
            self.visit(node.left),
            self.visit(node.right),
        )

    def oldvisit_BinOp(self, node):
        binop_map = {
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
        }
        l = self.visit(node.left)
        r = self.visit(node.right)
        return binop_map[type(node.op)](l, r)

    def visit_UnaryOp(self, node):
        return op.make_unop(type(node.op), self.visit(node.operand))

    def oldvisit_UnaryOp(self, node):
        unop_map = {
            ast.UAdd: lambda x: +x,
            ast.USub: lambda x: -x,
            ast.Invert: lambda x: ~x,
            ast.Not: lambda x: not x,
        }
        val = self.visit(node.operand)
        return unop_map[type(node.op)](val)

    def visit_Subscript(self, node):
        obj = self.visit(node.value)
        idx = self.visit(node.slice)
        # try:
        #     return self.ctx.visit_x_subscript(
        #         obj,
        #         node.ctx,
        #         idx,
        #         self.store_val,
        #     )
        # except ex.NotThisWay:
        if isinstance(node.ctx, ast.Load):
            return obj[idx]
        elif isinstance(node.ctx, ast.Store):
            obj[idx] = self.store_val
        elif isinstance(node.ctx, ast.Del):
            del obj[idx]
        else:
            raise NotImplementedError
        return None

    def visit_Index(self, node):
        return self.visit(node.value)

    def visit_Slice(self, node):
        # Any of these can be None
        lower = node.lower and self.visit(node.lower)
        upper = node.upper and self.visit(node.upper)
        step = node.step and self.visit(node.step)
        slice = slice_getter[lower:upper:step]
        return slice

    def visit_Attribute(self, node):
        obj = self.visit(node.value)
        direction = node.ctx
        attr = node.attr
        val = self.store_val
        match direction:
            case ast.Store():
                setattr(obj, attr, val)
            case ast.Load():
                return getattr(obj, attr)
            case _:
                delattr(obj, node.attr)
        return None

    def visit_Global(self, node):
        for n in node.names:
            if n in self.ns and self.ns[n] is not GLOBAL:
                ex.rErrorHere(f"Name {n} before global")
            # Don't store GLOBAL in the top-level namespace
            if self.ns.parent:
                self.ns[n] = GLOBAL

    def visit_Nonlocal(self, node):
        if isinstance(self.ns, ity.ModuleNS):
            ex.rErrorHere("nonlocal declaration not allowed at module level")
        for n in node.names:
            self.ns[n] = NONLOCAL

    def resolve_nonlocal(self, name, ns):
        while ns:
            res = ns.get(name, NO_VAR)
            if res is GLOBAL:
                return self.module_ns
            if res is not NO_VAR and res is not NONLOCAL:
                if isinstance(ns, ity.ModuleNS):
                    break
                return ns
            ns = ns.parent
        ex.rErrorHere(f"no binding for nonlocal '{name}'")

    def visit_Name(self, node):
        self.update_lastplace(node)
        if isinstance(node.ctx, ast.Load):
            res = NO_VAR
            ns = self.ns
            # We always lookup in the current namespace (on the first
            # iteration), but afterwards we always skip class namespaces.
            # Or put it another way, class code can look up in its own
            # namespace, but that's the only case when the class namespace
            # is consulted.
            skip_classes = False
            while ns:
                if not (skip_classes and isinstance(ns, ity.ClassNS)):
                    res = ns.get(node.id, NO_VAR)
                    if res is not NO_VAR:
                        break
                ns = ns.parent
                skip_classes = True

            if res is NONLOCAL:
                ns = self.resolve_nonlocal(node.id, ns.parent)
                return ns[node.id]
            if res is GLOBAL:
                breakpoint()
                res = self.module_ns.get(node.id, NO_VAR)
            if res is not NO_VAR:
                return res

                # # need to cheat to get the defs in, since
                # # we don't actually interpret the entire module.
                # res = self.fn.__globals__.get(node.id, NO_VAR)
                # if res is not NO_VAR:
            #                return res
            if 1:
                res = self.fn.__globals__.get(node.id, NO_VAR)
                if res is not NO_VAR:
                    return res

            try:
                return getattr(builtins, node.id)
            except AttributeError:
                ex.rErrorHere(f"{node.id} is not defined.")
        elif isinstance(node.ctx, ast.Store):
            res = self.ns.get(node.id, NO_VAR)
            if res is GLOBAL:
                self.module_ns[node.id] = self.store_val
            elif res is NONLOCAL:
                ns = self.resolve_nonlocal(node.id, self.ns.parent)
                ns[node.id] = self.store_val
            else:
                self.ns[node.id] = self.store_val
        elif isinstance(node.ctx, ast.Del):
            res = self.ns.get(node.id, NO_VAR)
            if res is NO_VAR:
                ex.rErrorHere(f"name '{node.id}' is not defined")
            if res is GLOBAL:
                del self.module_ns[node.id]
            elif res is NONLOCAL:
                ns = self.resolve_nonlocal(node.id, self.ns.parent)
                del ns[node.id]
            else:
                del self.ns[node.id]
        else:
            raise NotImplementedError

    def visit_Dict(self, node):
        return {self.visit(p[0]): self.visit(p[1]) for p in zip(node.keys, node.values)}

    def visit_Set(self, node):
        return {self.visit(e) for e in node.elts}

    def visit_List(self, node):
        return [self.visit(e) for e in node.elts]

    def visit_Tuple(self, node):
        return tuple([self.visit(e) for e in node.elts])

    def visit_NameConstant(self, node):
        return node.value

    def visit_Ellipsis(self, node):
        return ...

    def visit_Constant(self, node):
        #        if node.value == 123:
        #            breakpoint()
        return node.value


def just_ast(victim):
    if isinstance(victim, function.InlineDefinition):
        return victim.ast

    src = inspect.getsource(victim)
    tree = ast.parse(src)
    return tree


def call_func_with_interpreter(self, node, interp_func, *args, **kwargs):
    breakpoint()

    # We need to switch from dynamic execution scope to lexical scope
    # in which function was defined (then switch back on return).
    dyna_scope = self.ns
    self.ns = interp_func.lexical_scope
    self.push_ns(ity.FunctionNS())
    try:
        sig = inspect.signature(interp_func.fn)
        arguments = sig.bind(*args, **kwargs)
        arguments.apply_defaults()

        self.ns.d.update(arguments.arguments)

        res = self.start(node.body)
    except TargetReturn as e:
        res = e.args[0]
    finally:
        self.pop_ns()
        self.ns = dyna_scope

    return res


# # @functools.cache
# def read_module(filename):
#     inf = open(filename)
#     all = inf.read()
#     tree = ast.parse(all)

#     interp = Interpreter(filename)
#     interp.start(tree)
#     breakpoint()
#     breakpoint()
#     return interp


class NATIVE:
    def __init__(self, x):
        self.x = x
        print(f"native {x}")

    def __call__(self, *args, **kwargs):
        print("NATIVE CALL")
        breakpoint()


def native(x):
    return NATIVE(x)


# def generate(fn, outfile):
#     to_macro(fn)

#     #    tree = read_module(fn.__code__.co_filename)

#     if outfile:
#         with open(outfile, "w") as outf:
#             iface.face.statements.write(outf)


#    print(tree)


# support.generate = generate
# support.Interpreter = Interpreter
# support.inline = inline
# support.to_macro = to_macro
# support.native = native
# support.for_test = for_test
