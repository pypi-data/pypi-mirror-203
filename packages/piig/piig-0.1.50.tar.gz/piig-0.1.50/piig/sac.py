# watch function calls using
# @pa
# then use @break_at to stop when..

import ast
import dataclasses
import enum
import inspect
import re
import sys


# first run: find out which modules were initially loaded
init_modules = sys.modules.keys()


def shorten_tname(tname):
    if g := re.match("<class '(.*)'", tname):
        tname = g.group(1)
    if g := re.match("<enum '(.*)'", tname):
        tname = g.group(1)
    tname = tname.removeprefix("s.")
    if tname == "Node":
        return "N:"
    r = tname.rfind(".")
    if r >= 0:
        tname = tname[r + 1 :]

    return tname


class CantPrint(Exception):
    pass


class TooDeep(Exception):
    pass


class _C:
    pass


# if self can be described in a few bits, do so.


def chooseseps(thing):
    if isinstance(thing, list):
        return "[", "]", ","
    if isinstance(thing, tuple):
        return "(", ")", ""
    return "{", "}", ":"


def try_well_known(prefix, tname, thing, deeper):
    if prefix.endswith("stats"):
        yield "WK" + prefix + "ignore"
        return

    match tname:
        case "Opinfo":
            yield "WK" + prefix + " " + thing.pyname
            return
    raise CantPrint()


def try_format(prefix, tname, thing, deeper):
    try:
        ret = str(thing)
        if ret[0] == "<":
            raise CantPrint()
        yield f"TF{prefix} {ret}"
    except TypeError:
        raise CantPrint()
    except ValueError:
        raise CantPrint()


#    except Exception as e:
#        return None


def try_list(_prefix, _tname, thing, deeper):
    if isinstance(thing, list):
        for idx, value in enumerate(thing):
            if idx < 10:
                try:
                    yield from deeper(idx, value)
                except CantPrint:
                    yield "hnn"


def try_alist(prefix, tname, thing, deeper):
    if isinstance(thing, list):
        for idx, value in enumerate(thing):
            if idx < 10:
                try:
                    if len(value) == 2 and isinstance(value[0], str):
                        yield from deeper(value[0], value[1])
                except CantPrint:
                    yield "hnn"


def try_with_items(keylambda, prefix, tname, thing, deeper):
    #    yield "TI" + prefix + ": " + tname
    try:
        for row, (key, value) in enumerate(thing.items()):
            if row < 10:
                try:
                    yield from deeper(keylambda(key), value)
                except CantPrint:
                    yield "hnn"
            else:
                yield "TI" + prefix + "...."
                break

    except AttributeError:
        raise CantPrint()


def try_with_dict(prefix, tname, thing, deeper):
    if hasattr(thing, "__dict__"):
        title = "DI" + prefix + "<" + tname + ">"

        if title.endswith("typ<Type>"):
            yield "WK" + prefix + "<Type>" + thing.tstr
            return

        if title.endswith("ctx<CTX>"):
            yield title + ".."
            return
        yield title
        list(thing.__dict__.items())
        yield from try_with_items(
            lambda key: "." + key, prefix, tname, thing.__dict__, deeper
        )
    else:
        raise CantPrint()


def try_as_dict(prefix, tname, thing, deeper):
    yield "TA" + prefix + "<" + tname + ">"
    try:
        if len(thing) > 30:
            yield "TA" + prefix + "<" + tname + "> ..... big ..."
        else:
            yield from try_with_items(
                lambda key: "[" + key + "]", prefix, tname, thing, deeper
            )
    except AttributeError:
        raise CantPrint()
    except TypeError:
        raise CantPrint()


def str_atom_el(thing):
    if thing is None:
        return "-"
    if isinstance(thing, list) and len(thing) == 0:
        return "[]"
    if isinstance(thing, dict) and len(thing) == 0:
        return "{}"
    if isinstance(thing, bool):
        return f"{thing}"

    if isinstance(thing, tuple) and len(thing) == 2:
        return f"{str_atom_el(thing[0])} {str_atom_el(thing[1])}"

    if isinstance(thing, float):
        return f"{thing}f1"
    if isinstance(thing, int):
        return f"{thing}i"
    if isinstance(thing, str):
        return f"'{thing}'"
    raise CantPrint()


def try_atom(prefix, _tname, thing, _deeper=None):
    yield f"AT{prefix} x= {str_atom_el(thing)}"


def try_empty_list(prefix, tname, thing, _deeper=None):
    if isinstance(thing, list) and len(thing) == 0:
        yield f"EL{prefix} = []"
        return
    raise CantPrint()


def try_empty_dict(prefix, tname, thing, deeper=None):
    if isinstance(thing, dict) and len(thing) == 0:
        yield f"ED{prefix} = " + "{}"
        return
    raise CantPrint()


def try_none(prefix, tname, thing, deeper=None):
    if thing is None:
        yield f"NO{prefix} = -"
        return
    raise CantPrint()


def try_enum(prefix, tname, thing, deeper=None):
    if isinstance(thing, enum.Enum):
        yield f"EN{prefix} = {thing.name}"
        return
    raise CantPrint()


def try_property(prefix, tname, thing, deeper):
    if thing.__class__ == property:
        yield f"PR{prefix} = property"
        return
    raise CantPrint()


def try_member_descriptor(prefix, tname, thing, deeper):
    try:
        q = thing.__qualname__
        yield f"MB{prefix} = {q}"
    except:
        raise CantPrint()


def try_checksame_(self, prefix, tname, thing, print_deeper):
    seeninstances = self.seeninstances
    seenhardinstances = self.seenhardinstances

    try:
        if (v := seeninstances.get(thing, None)) is not None:
            yield f"CC{prefix} SAME {v}"
            return
        seeninstances[thing] = self.idx
        raise CantPrint()
    except TypeError:
        pass
    try:
        seenhardinstances.index(thing)
        yield f"CC{prefix} SAMEL"
        return
    except ValueError:
        seenhardinstances.append(thing)
    raise CantPrint()


class PX:
    def __init__(
        self,
        max_depth=5,
        withlg=True,
        with_debug=False,
        withls=False,
        noscope=False,
        with_shortclass=True,
        with_try_checksame=True,
        with_try_format=True,
    ):
        self.with_shortclass = with_shortclass
        self.seenhardinstances = []
        self.seeninstances = {}
        self.filter = ""
        self.max_depth = max_depth
        self.with_try_format = with_try_format
        self.idx = 0
        self.withls = withls
        self.withlg = withlg
        self.with_try_checksame = with_try_checksame
        self.with_debug = with_debug
        self.noscope = noscope
        self.with_try_checksame = with_try_checksame

    def pri(self, thing, name="", depth=0):
        self.idx += 1
        prefix = f"{self.idx:3}{name}"

        def print_deeper(name_suffix, inner_thing):
            if name_suffix == "__doc__":
                return
            if isinstance(name_suffix, int):
                name_suffix = f"[{name_suffix}]"
            elif isinstance(name_suffix, str):
                name_suffix = f"{name_suffix}"

            yield from self.pri(inner_thing, name + name_suffix, depth + 1)

        tname = f"{type(thing)}"
        tname = shorten_tname(tname)

        def try_maxdepth(prefix, tname, thing, deeper):
            if depth > self.max_depth:
                raise StopIteration()
            raise CantPrint()

        def try_checksame(prefix, tname, thing, deeper):
            return try_checksame_(
                self,
                prefix,
                tname,
                thing,
                deeper,
            )

        def fls():
            #            if self.with_try_checksame:
            #                yield try_checksame
            if self.with_try_format:
                yield try_format
            if self.with_shortclass:
                yield try_well_known
            yield try_atom
            yield try_enum

            yield try_maxdepth
            yield try_with_dict
            yield try_as_dict
            yield try_list

            yield try_property
            yield try_member_descriptor

        #        if self.with_debug:
        #            pdb.set_trace()

        try:
            for func in fls():
                try:
                    #                    if self.with_debug:
                    #                        print(func)
                    #                        breakpoint()
                    yield from func(prefix, tname, thing, print_deeper)
                    return
                except CantPrint:
                    if self.with_debug:
                        print("fail")
                    pass
        except StopIteration:
            yield f"MD{prefix}..."
            return

        yield "DONE"
        return

        breakpoint()
        yield f"{prefix}{name}={thing}"


def printit(gen):
    for line in gen:
        assert line[0:2].isalpha()
        assert line[0:2].isupper()
        print(line)


#        print(line[2:])


def o(thing):
    pxo = PX(noscope=True)
    printit(pxo.pri(thing))


# o bland - no clever shortclass.
def ob(thing):
    pxo = PX(
        with_try_format=False,
        with_shortclass=False,
        with_try_checksame=True,
        with_debug=False,
    )
    printit(pxo.pri(thing))


def xl(thing):
    pxo = PX(withls=True)
    printit(pxo.pri(thing))


def xnog(thing):
    pxo = PX(withlg=False)
    printit(pxo.pri(thing))


def pl(thing):
    pxo = PX(max_depth=20)
    printit(pxo.pri(thing))


def od(thing):
    pxo = PX(
        with_try_format=False,
        with_shortclass=False,
        with_try_checksame=False,
        with_debug=True,
    )

    printit(pxo.pri(thing))


def xx(src):
    o(src)


#    print(">>>>", object.__repr__(x))


def spoff(fn):
    return fn


global DEPTH
DEPTH = 1


def betterrep(v):
    tname = type(v)
    if tname == "s.Node":
        return "*"
    if isinstance(v, int):
        return f"i{v}"
    if isinstance(v, float):
        return f"f{v}"

    if tname.__name__.endswith("Constant"):
        return f"c{v._value}"
    return v.__repr__()


def asg(x):
    print(x.as_gcode)

    ######################################################################


# saved arg printing, incase we can to ret and call on same line


@dataclasses.dataclass
class Pending:
    prefix: str
    args: str
    res: str
    index: int

    def print_args(self):
        assert not self.res
        print(self.prefix + self.args)
        self.args = ""

    def print_res(self):
        assert not self.args
        print(self.prefix + self.res)
        self.res = ""
        self.index = 0
        self.prefix = ""
        self.index = None

    def print_argsandres(self):
        assert self.res
        assert self.args
        print(self.prefix + self.res + self.args)
        self.res = ""
        self.args = ""
        self.prefix = ""
        self.index = None

    def set_args(self, index, args):
        assert index == self.index
        assert not self.args
        self.args = args

    def set_res(self, index, res):
        assert index == self.index
        assert not self.res
        self.res = res

    def set_prefix(self, index, prefix):
        assert index == self.index
        self.prefix = prefix

    def set_index(self, index):
        assert not self.args
        assert not self.res
        self.index = index

    def __init__(self, index=0):
        self.args = ""
        self.prefix = ""
        self.res = ""
        self.index = index


global Pends
Pends = Pending()


# frameinfo = getframeinfo(currentframe())

# print(frameinfo.filename, frameinfo.lineno)


PAON = False


def look_back(count):
    cursor = inspect.currentframe()
    while count:
        if cursor is not None:
            cursor = cursor.f_back
        count -= 1

    ifra = inspect.getframeinfo(cursor)
    return ifra


def nothing(x):
    return x


# pa = nothing


""" break when passed this number of times,
and all other funcs break too """


global ALLBREAK
ALLBREAK = 0


# def break_at(count):
#     def decorate(fn):
#         @wraps(fn)
#         def wrapper(*args, **kwargs):
#             global ALLBREAK
#             if ALLBREAK or pacount[fn.__qualname__] >= count:
#                 ALLBREAK = 1
#                 breakpoint()
#             return fn(*args, **kwargs)

#         return wrapper

#     return decorate


######################################################################
## prrotect reprs
def save(fn):
    def worker(x):
        try:
            res = fn(x)
        except AttributeError as e:
            res = f"<<<<{e.args}>>>>>"
        return res

    return worker


def dast(node):
    import ast

    for x in ast.dump(node, indent=3).split("\n"):
        print(x)


COUNT = 1


def K(l=0):
    global COUNT
    print("K", COUNT)
    COUNT += 1
    if l != 0 and COUNT > l:
        breakpoint()


def ba(x):
    if not x:
        breakpoint()


def dn(tree):
    for x in ast.dump(tree, indent=4, include_attributes=False).split("\n"):
        print(x)


def pand(line):
    tree = ast.parse(line)
    dn(tree)
