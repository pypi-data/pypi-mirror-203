import collections.abc
import contextlib
import os
import sys


def ignore(_x):
    pass


def flatten(thing):
    if isinstance(thing, (tuple, list)):
        for x in thing:
            yield from flatten(x)
        return
    yield thing


def in_pytest():
    script_name = os.path.basename(sys.argv[0])
    if script_name in ["pytest"]:
        return True

    return False


def in_bcommas(prefix, lis):
    return f"({prefix}{', '.join(map(str, lis))})"


def in_aspace(prefix, lis):
    return f"<{prefix}{' '.join(map(str, lis))}>"


PDEPTH = 0


def apply(fn, seq):
    for el in seq:
        fn(el)


def listify(src):
    if isinstance(src, collections.abc.Iterable):
        return src
    return [src]


def maybe_solo(src):
    if isinstance(src, list):
        if len(src) == 1:
            return src[0]
        return None
    return src


def is_iterable(x):
    return isinstance(x, collections.abc.Iterable)


def is_str(x):
    return isinstance(x, str)


def is_int(x):
    return isinstance(x, int)


# def is_list(self):
#    return isinstance(self, list)


def checkaxis(axes):
    if axes == "var":
        return
    if axes == "pop":
        return
    for c in axes:
        if c not in "xyza":
            breakpoint()

        if axes == "typ":
            breakpoint()


# give a number bigger than ~80 something of the contents.
# def give86(lens):
#     mean = sum(lens) / len(lens)
#     variance = sum([((x - mean) ** 2) for x in lens]) / len(lens)
#     return int(mean + variance**0.5 * 2)


class AttributeDict(dict):
    __slots__ = ()
    __getattr__ = dict.__getitem__


#    __setattr__ = dict.__setitem__


class getset:
    def __init__(self, getse):
        self.getset = getse
        self._name = ""

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return self.getset(obj, None)

    def __set__(self, obj, value):
        self.getset(obj, value)


class X:
    def __init__(self):
        self.q = 123
        self.u = 1223

    @getset
    def zap(self, a=None):
        print("A", a, self.q)
        if a:
            self.q = a

    @getset
    def pop(self, a=None):
        print("A", a, self.u)
        if a:
            self.u = a
        return self.u


FF = X()


def trygetarg(
    key,
    kwargs,
    default=None,
):
    if key in kwargs:
        res = kwargs[key]
        del kwargs[key]
        return res
    return default


def catchany():
    try:
        yield
    except Exception as e:
        breakpoint()
        print(e)
        print(e)
        print(e)


def max_str_len(lines):
    if lines:
        return max(map(len, lines))
    return 0


def pad_to_same_width(lines):
    wid = max_str_len(lines)
    res = []
    for line in lines:
        res.append(line.ljust(wid))
    return res


def count(pred, seq):
    return sum(1 for v in seq if pred(v))


class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__ = self


# open a file which may be stdout for output.


@contextlib.contextmanager
def openout(outfile):
    if outfile == "-":
        yield sys.stdout
    else:
        with open(outfile, "w", encoding="utf-8") as of:
            yield of
