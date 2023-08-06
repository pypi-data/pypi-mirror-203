#! /usr/bin/env python

# make sure the testing is working.

import piig as G


# @conftest.nc_compare
@G.nc_compare2
def test_ok(g):
    g.checkcode()
    print("IN TESTOK")
    zz = g.Vec[200]()
    zz[0] = 3
    g.insert_symbol_table(show_names=False)


#    z = g.FixedVec[200](addr=123)


@G.nc_compare2
def test_ok2(g):
    g.checkcode()
    print("IN TESTOK")
    z = g.FixedVec[200](addr=123)
    g.FixedVar(2, addr=100)
    assert g.checkcode("#100=2.")
