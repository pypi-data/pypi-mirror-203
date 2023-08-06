#! /usr/bin/env python
import pytest

import piig as G


@G.inline
def ins1(_g, dst):
    dst.var = 99


@G.inline
def inside2(_g, d1, d2, _k=0):
    d1.var = 100
    ins1(_g, d2)


@G.inline
def inside3(g, d1, d2, d3):
    d1.var = 100

    inside2(g, d1, d2, d3)


@G.nc_compare2
def test_nesting_functions1(g):
    T = g.Var()
    ins1(g, T)


@G.nc_compare2
def test_nesting_functions2(g):
    T = g.Var[2]()
    inside2(g, T[0], T[1])


@G.nc_compare2
def test_nesting_functions3(g):
    T = g.Var[2]()
    V = g.Const(1, 2, 3)
    inside3(g, T[0], T[1], V)
