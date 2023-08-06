import pytest

import piig as G


PROBE = G.FixedVec[3](addr=5061)


@G.nc_compare2
def test_some_errors0(g):
    with pytest.raises(AttributeError):
        PROBE.fish = 100
