import pytest
import piig as G


@G.nc_compare2
def test_coord_symtab1(g):
    g.st.p = G.Fixed[90](addr=100)
    g.st.q = G.Fixed[3](addr=200)
    p = g.st.p
    # too far to get an axis name.
    p[17] = 31
    p[18] = 123
    g.st.q.x = 9
    g.st.q.z = 91
    g.insert_symbol_table()


@G.nc_compare2
def test_coord_symtab(g):
    p = G.Fixed[9](addr=100)
    g.st.fish = 3
    p.x = 3
    g.st.PROBE_R = G.Fixed[3](addr=556)
    g.st.PROBE_R.x = 3
    g.Const[2](1, 2)
    g.insert_symbol_table()


@G.nc_compare2
def test_coord_addr0(g):
    # takes addr from specified.
    v = g.Var[10](addr=20)
    g.comment(v)


@G.nc_compare2
def test_coord_size0(g):
    with pytest.raises(SyntaxError, match="Two sizes.*"):
        g.Var[10](size=20)


@G.nc_compare2
def test_coord_conflicting_sizes(g):
    with pytest.raises(SyntaxError, match="Conflicting sizes.*"):
        g.Var[100](2)


@G.nc_compare2
def test_coord_kwargs(g):
    v = g.Var(x=2, y=3)
    g.comment(v)


@G.nc_compare2
def test_coord_non_kwargs(g):
    v = g.Var(2, 3)
    g.comment(v)


@G.nc_compare2
def test_coord_overlapping(g):
    with pytest.raises(IndexError, match="Overlapping axes.*"):
        g.Var(2, x=3)


@G.nc_compare2
def test_coord_const1(g):
    with pytest.raises(SyntaxError, match="Const.*"):
        g.Const[2](1, 2, addr=123)
