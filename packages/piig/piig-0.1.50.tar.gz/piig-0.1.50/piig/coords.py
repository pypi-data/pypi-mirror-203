# magic for things like

# g.goto.fast ([1,2])
# foo = g.probe.slow
# foo(z=12)
import typing


from piig import axis, gbl
from piig import exception as ex


from piig import nd
from piig import op


class ARRAY(nd.Dots):
    def to_symtab_entry(self, hit_indexes):
        fwidth = 7

        if max(hit_indexes) >= len(axis.lnames):
            return f"#{self._addr}[{self._size}]".rjust(fwidth)
        res = []

        for idx in range(self._size):
            if idx not in hit_indexes:
                continue

            res.append(
                f"#{self._addr + idx}.{axis.lnames[idx]}".rjust(fwidth),
            )
        return " ".join(res)

    def __init__(self, addr=None, size=None):
        #        breakpoint()
        self._addr = addr
        self._size = size
        super().__init__()

    def __len__(self):
        return self._size

    def __getitem__(self, i):
        res = []
        indexes = list(nd.slice_to_index_list(i, self._size))
        if len(indexes) != 1:  # pragma: no cover
            breakpoint()
        #            for idx in indexes:
        #                res.append(self[idx])
        #            return res

        idx = nd.unwrap(indexes[0])
        if isinstance(idx, int):
            if idx >= self._size or idx < 0:
                raise IndexError(f"Index error, index={idx} size={self._size}")

        return op.hashop(
            op.make_scalar_binop("+", self._addr, nd.scalarify(idx)),
        )

    def __setitem__(self, indexes, src):
        #        breakpoint()

        for lhs, rhs in zip(
            self.byslice_to_list(indexes),
            nd.one_is_forever(src),
        ):
            if not nd.same(lhs, rhs):
                nd.emit_single_set(lhs, rhs)

    def __repr__(self):
        return f"(array  {self._addr} {self._size})"


def AddressedArray(*, addr=None, size=1):
    return ARRAY(addr, size)


def unpack_cos_inner(
    args,
    kwargs,
) -> tuple[list[typing.Any], int, typing.Optional[int]]:
    resmap = {}
    if args:
        for idx, value in enumerate(nd.flatten(args)):
            resmap[idx] = value

    rexplicit_size = 0
    # can have x=1,y=1 or xy=(somthing)
    for axis_string, values in kwargs.items():
        axis_indexes = axis.name_to_indexes(axis_string)
        # don't forever the inits ?
        for axis_idx, value in zip(axis_indexes, nd.one_is_forever(values)):
            if axis_idx in resmap:
                raise IndexError(f"Overlapping axes {args} {kwargs}")
            resmap[axis_idx] = value

    # fill any holes.
    coord_size = 0
    if resmap:
        coord_size = max(resmap) + 1

    # rules:
    # everthing in the input gets packed into
    # the output in the right order.
    # if something is a nan in the input, and
    # we've got gap_default, then the nan is
    # turned into that.

    def suck(idx):
        got = resmap.get(idx)
        return got

    min_size = 0
    raddr = None
    res = [suck(x) for x in range(max(min_size, coord_size))]
    return res, max(coord_size, rexplicit_size), raddr


# build things like AABuilder(size=9, _addr=123) and AABuilder[8](_addr=123)
class _TypeBuilder:
    def __init__(
        self,
        addr=None,
        size=None,
        test=False,
        const=False,
        ctx=None,
    ):
        self.addr = addr
        self.size = size
        self.test = test
        self.const = const
        self.ctx = ctx

    def __getitem__(self, el):
        return _TypeBuilder(
            addr=self.addr,
            size=el,
            test=self.test,
            const=self.const,
            ctx=self.ctx,
        )

    def __call__(
        self,
        *args,
        addr=None,
        size=None,
        bp=False,
        **kwargs,
    ):
        if bp:  # pragma: no cover
            breakpoint()

        if self.size is not None and size is not None:
            raise SyntaxError("Two sizes.")
        if size is None:
            size = self.size
        if addr is None:
            addr = self.addr
        if addr is not None and self.const:
            raise SyntaxError("Const can't have an address.")
        values, sz, _addr = unpack_cos_inner(args, kwargs)

        if size is not None and sz != 0 and size != sz:
            values, sz, _addr = unpack_cos_inner(args, kwargs)
            raise SyntaxError(f"Conflicting sizes {size} and {sz}")
        if sz > 0:
            size = sz

        if self.const:
            return nd.Gvalue(values)

        if size is None:
            size = 1

        if addr is None:
            addr = gbl.ctx.block_context.ebss
            self.ctx.block_context.ebss += size

        res = AddressedArray(addr=addr, size=size)
        if values:
            gbl.ctx.emit_multi_set(res, values)
        return res


class TypeBuilderFixedAddr(_TypeBuilder):
    def __init__(self, addr=None, size=None, test=False):
        super().__init__(addr=addr, size=size, test=test, ctx=None)


class TypeBuilderAutoAddr(_TypeBuilder):
    def __init__(self, ctx, addr=None, size=None, test=False):
        super().__init__(addr=addr, size=size, test=test, ctx=ctx)


class TypeBuilderConst(_TypeBuilder):
    def __init__(self, size=None, test=None):
        super().__init__(const=True, size=size, test=test)


Fixed = TypeBuilderFixedAddr()
FixedVec = Fixed
FixedInt = Fixed
FixedFloat = Fixed
FixedTime = Fixed
FixedSecs = Fixed
FixedPercent = Fixed
ToolTable = Fixed
Const = TypeBuilderConst()
MachinePos = Fixed
CWCPos = Fixed


def WorkOffsetTable(addr):
    return AddressedArray(addr=addr, size=6)
