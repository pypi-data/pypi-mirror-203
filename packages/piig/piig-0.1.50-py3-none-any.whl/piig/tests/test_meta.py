#! /usr/bin/env python

# make sure the testing is working.
import pytest

import piig as G


@G.nc_compare2
def test_simple_ok(g):
    g.FixedVar(2, addr=100)


@pytest.mark.xfail
@G.nc_compare2
def test_simple_xfail1(g):
    CURSOR = g.FixedVar(addr=100)
    CURSOR.x = 1


#    assert False


# expected fail        test_broken()
