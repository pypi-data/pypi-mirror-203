import pytest
import piig as G


@G.nc_compare2
def test_coord_goto_rel(g):
    mgoto = g.goto.feed(20)
    mgoto.relative(1, 2)
    g.comment(mgoto)
