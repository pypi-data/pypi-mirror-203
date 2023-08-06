import pytest

# fixture which makes a placeholder argument which is replaced
# by the stuff in function.py with the interp context.


@pytest.fixture
def g():  # pragma: no cover
    return "<REPLACEWITHCTX>"
