# see:  https://docs.pytest.org/en/stable/reference/fixtures.html#conftest-py-sharing-fixtures-across-multiple-files
# - Topic: conftest.py: sharing fixtures across multiple files :
#   multiple nested directories/packages containing your tests, and each directory can have its own conftest.py with its own fixtures, adding on to the ones provided by the conftest.py files in parent directories.

import pytest

@pytest.fixture
def innermost(order):
    order.append("innermost top")

def test_order(order, top):
    print("__order-final1:  ", order)
    assert order == ["innermost top", "top"]


