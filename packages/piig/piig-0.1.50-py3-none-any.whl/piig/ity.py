def InterpFunc(fun):
    def func(*args, **kwargs):
        return fun.__call__(*args, **kwargs)

    return func


class InterpFuncWrap:
    """Callable wrapper for AST functions (FunctionDef nodes)."""

    def __init__(self, node, interp):
        #        self.fn = fn
        self.node = node
        self.interp = interp
        self.lexical_scope = interp.ns

    def __call__(self, *args, **kwargs):
        #        self.interp.fn = self.fn
        prev_inside = self.interp.inside
        self.interp.inside = True
        res = self.interp.call_func(self.node, self, *args, **kwargs)
        self.interp.inside = prev_inside
        return res


class ANamespace:
    def __init__(self):
        self.d = {}
        self.parent = None

    def __getitem__(self, k):
        return self.d[k]

    def get(self, k, default=None):
        return self.d.get(k, default)

    def update(self, d):
        self.d.update(d)

    def __setitem__(self, k, v):
        self.d[k] = v

    def __delitem__(self, k):
        del self.d[k]

    def __contains__(self, k):
        return k in self.d

    def __str__(self):
        return f"{self.__class__.__name__} {self.d}"


class ModuleNS(ANamespace):
    pass


class FunctionNS(ANamespace):
    pass


class ClassNS(ANamespace):
    pass


class Sentinel:
    def __init__(self, name):
        self.name = name


NOPE = Sentinel("NOPE")
