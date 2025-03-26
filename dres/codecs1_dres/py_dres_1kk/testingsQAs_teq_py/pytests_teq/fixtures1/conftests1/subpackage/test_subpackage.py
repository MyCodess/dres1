import pytest

@pytest.fixture
def innermost(order, mid):
    order.append("innermost subpackage")

def test_order(order, top):
    print("__order-final1:  ", order)
    assert order == ["mid subpackage", "innermost subpackage", "top"]

