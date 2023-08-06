#! /usr/bin/env python
import pytest

import piig as G


PROBE = G.FixedVec[3](addr=5061)


@G.nc_compare2
def test_var_addresses(g):
    add_some_symbols(g)

    p = g.txyz.y
    q = g.Address(p)

    assert g.Address(g.txyz.y) == g.AsAddress(101)

    assert g.Address(g.txyz.x) == g.AsAddress(100)
    # negative assertions are because
    # if constant folding doesn't worke
    # the exp will be a tree, whch will
    # alwasy be true.
    assert not g.Address(g.txyz.z) == g.AsAddress(202)
    assert not g.Address(PROBE) != g.AsAddress(5061)
    assert g.Address(PROBE) == g.AsAddress(5061)


@G.nc_compare2
def test_missing_functions(g):
    T = g.Var()
    T.var = -T.var
    T.var = ~T.var
    T.var = not T.var
    T.var = -7
    T.var = ~7
    T.var = not 7
    # assert g.checkcode(
    #     "#100= -#100",
    #     "#100= #100 XOR 0.",
    #     "#100= #100 NE 0.",
    #     "#100= -7.",
    #     "#100= -8.",
    #     "#100= 0.",
    # )


@G.nc_compare2
def test_simplify0_fail(g):
    dx, dy = -1, -1
    howtosearch = g.Const[2](-1.0, 2.0)
    cursor = G.FixedVec[2](addr=200)
    delta = howtosearch * [dx, dy]

    cursor.xy += delta


@G.nc_compare2
def test_simplify1_fail(g):
    print("P1")
    y = G.FixedVec[1](addr=17)
    x = g.Vec(y[0] + -1 * 1.5)


#    assert g.checkcode("#100=#17 - 1.5")


@G.nc_compare2
def test_prev_errors(g):
    print("IN TPE")

    class S:
        def __init__(self, g):
            self.MAX = g.Vec[3]()
            self.MIN = g.Vec[3]()
            self.delta = 1.0

    s = S(g)

    itsvec = g.Const[2]((s.MAX.xy - s.MIN.xy) / 2.0 / s.delta)
    its = itsvec[0]
    dst = g.Vec(its)
    print("s.delta", s.delta)
    print("s.delta", 2.0 / s.delta)


#    assert g.checkcode("#106=[#100-#103]/2.")


# sys.path.insert(0, "..")


# pylint: disable=attribute-defined-outside-init,unneeded-not
@G.nc_compare2
def test_basic_folding1(g):
    T = g.Var()

    T.var = T * -1.0
    T.var = T * 1.0
    T.var = T * 0.0

    V = g.Const[2](-1, 1)
    U = g.Const[2](1, -1)
    P = g.Vec[2](17, 20)
    Q = g.FixedVec[2](addr=177)

    P.var *= V
    P.var += V - U
    Q.xy += [103, 203]
    Q.xy += [103, 203] * 7


@G.nc_compare2
def test_basic_folding0(g):
    T = g.Var()
    T.var = not 1
    T.var = not (not 1)
    T.var = not (not (not 1))
    T.var = T
    T.var = not T
    T.var = not (not T)
    T.var = not (not (not T))
    T.var = T.var > 9
    T.var = not (T.var > 9)
    T.var = not (not (T.var > 9))
    T.var = not ((T.var > 9) != 0)
    T.var = not (not ((T.var > 9) != 0))
    T.var = not (not ((T.var > 9) != 0)) == 0
    T.var = 99999
    T.var = T == 9
    T.var = (T == 9) == 0
    T.var = ((T == 9) == 0) == 0
    T.var = (((T == 9) == 0) == 0) == 0
    T.var = 88888
    T.var = T != 9

    T.var = (T == 9) == 0
    T.var = (T == 9) != 0
    T.var = ((T == 9) == 0) == 0
    T.var = ((T == 9) != 0) != 0
    T.var = ((T == 9) == 0) != 0
    T.var = ((T == 9) != 0) == 0

    T.var = 9
    T.var = T == 9
    T.var = T != 9
    T.var = not (T == 9)
    T.var = not (T == 9) != 0
    T.var = not ((T == 9) == 0) == 0
    T.var = not ((T == 9) != 0) != 0
    T.var = not ((T == 9) == 0) != 0
    T.var = not ((T == 9) != 0) == 0


@G.nc_compare2
def test_simple_code0(g):
    g.base_addr = 300

    CURSOR = g.Vec(20, 30)
    #    CURSOR = [1, 7]
    CURSOR.xy += [71, 17]
    CURSOR.y = PROBE.y - 10
    CURSOR.x = CURSOR.y

    CURSOR.y = 901
    CURSOR[0:2] = PROBE.xy * 2.0


@G.nc_compare2
def test_constant_arithmetic(g):
    v = PROBE

    v.xy = 9

    zap0 = g.Const(9.2, 12.3, -10.0 - 17.0, 2)
    zap1 = g.Const(9.2, 12.3, -10.0 - 7.0, 2)
    zap2 = g.Const(9.2, 0, -10.0 - 7.0, 2)
    print(zap0)

    sometrue = zap0 == zap1
    # noinspection PyType:Checker

    f1 = zap0 == zap2
    print("F1 is", f1)

    btrue = any(zap0 == zap2)
    cfalse = all(zap0 == zap2)
    dtrue = all(zap0 == zap1)
    print("F2 is", f1)

    print("F3 is", f1)
    assert sometrue.x == 1
    assert sometrue.y == 1
    assert sometrue.z == 0
    print("F3 lkjlkis", f1)

    #        assert (zap == zap2).y == 0

    tmp = zap0.xyz + 1
    #    tmp = round(zap.xyz * 4 - 9, 1)

    print("AAA")

    t1 = tmp.y != 13.3
    assert not t1

    print("AAbbbA")

    assert tmp.y == 13.3
    #    assert not G.zap != [1, 2, 3]

    print("AAbcccbbA")

    assert not any(tmp == [27.8, 40.2, -77.0])

    print("AAbcccbblkjlkjldsA")


def add_some_symbols(g):
    g.txyz = g.Vec(size=3)
    g.txy = g.Vec(size=2)
    g.CURSOR = g.Vec(size=2)
    g.v = g.Vec(size=1)


@G.nc_compare2
def test_const_deref_addresses(g):
    add_some_symbols(g)
    ptrb = g.txyz

    idx = g.FixedVec(
        150,
        addr=20,
    )

    sa = g.FixedVec([1, 2, 3.14, 4, 5, 6], addr=40)
    ptr = g.FixedVec(addr=400, size=100)

    j = g.FixedVar(addr=10)
    for j.var in range(3):
        ptr[j.var + 2] = (j + 2) ** 2 + 17


@G.nc_compare2
def test_simple_arrays(g):
    nw = g.FixedVec[7](2, 2, 2, 2, 3, 3, 1, addr=200)
    nw[2] = 3
    nw[4] = 9
    idx = g.FixedVar(7, addr=220)
    fish = g.FixedVar(addr=300)
    fish.var = nw[idx // 1]


@G.nc_compare2
def test_bad_bounds0(g):
    add_some_symbols(g)

    with pytest.raises(IndexError):
        g.txy.xyz = 0x99


@G.nc_compare2
def test_bad_bounds1(g):
    add_some_symbols(g)

    with pytest.raises(IndexError):
        g.txyz.xy = g.txy.z

    print("BBOUT")


@G.nc_compare2
def test_var_deref_addresses(g):
    j = g.Var()
    print("J IS ", j)
    ptr = g.FixedVec(size=10, addr=300)

    for j.var in range(7, 10):
        ptr[j] = 12

    add_some_symbols(g)

    ptr1 = g.Address(g.txyz.xyz)

    ptr2 = g.txyz

    assert ptr1 == ptr2
    assert ptr2 == g.txyz

    assert not (g.Address(ptr2.x) != g.Address(g.txyz.x))
    assert ptr1 == g.txyz

    assert g.Address(g.txyz.xyz) == g.txyz

    for j.var in range(7, 10):
        ptr[j] = j

    for j.var in range(2, 7):
        ptr[j] = (j + 2) ** 2 + 17


@G.nc_compare2
def test_bad_attribute(g):
    with pytest.raises(AttributeError):
        add_some_symbols(g)
        g.txyz.pop


@G.nc_compare2
def test_variable_assignment(g):
    add_some_symbols(g)
    g.txyz.xy = [1, 3 + 9]

    g.txyz.z = g.txyz.y + 1

    g.txyz.y = 9

    g.txyz.x = [1]

    g.txyz.xyz = [1, 2, 3]
    g.txyz.xyz = [g.txy.x + 1, g.txy.y * 34, 99]


@G.nc_compare2
def test_operator_precedence(g):
    add_some_symbols(g)

    src = PROBE

    tmp = g.FixedVar(addr=100)
    a = g.FixedVar(addr=1)
    b = g.FixedVar(addr=2)
    c = g.FixedVar(addr=3)
    d = g.FixedVar(addr=4)

    #        sac.ob(g)

    print(PROBE.y)

    print(a + 3)
    # gcode has unusal precedence for %
    # make sure translated from python to gcode
    # nicely

    tmp.var = a.var / b.var % 7
    tmp.var = a.var % b.var / 8
    tmp.var = (a.var / b.var) % 9
    tmp.var = (a.var % b.var) / 10

    # same as python
    tmp.var = a.var | b.var ^ c.var & d.var
    tmp.var = a.var & b.var ^ c.var | d.var

    # goes ((pointer to (float)*1):100)
    # [(contents of ((pointer to (float)*1):100))]
    tmp.var = 12
    src.y = 3

    src.xy = 90
    foo = g.FixedVar(addr=333)
    foo.var = 19

    g.txyz.x = 1 + 2 * 20 + 7 * 2
    ct = g
    src = ct.txyz.y

    ct.txyz.z = (src + 2) * 20
    ct.txyz.z = (ct.txyz.y + 2) * 20

    ct.txyz.y = ct.txyz.z + 2 + 3
    ct.txyz.y = ct.txyz.z + 2 * 20 + 3  # ct.txyz.z +
    p2 = 17.0
    ct.txyz.y = ct.txyz.z + p2 * 2
    ct.txyz.y = (ct.txyz.z + p2) * 2
    ct.txyz.y = ct.txyz.z + 3 - p2 * 2


@G.nc_compare2
def test_wibble(g):
    CURSOR = g.FixedVec(1, 2, 3, addr=100)
