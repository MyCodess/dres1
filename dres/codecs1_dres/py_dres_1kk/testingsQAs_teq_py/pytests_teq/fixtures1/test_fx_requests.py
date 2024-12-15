# --HowTo: Fixtures can be requested more than once per test (return values are cached)
# - Fixtures can also be requested more than once during the same test, and pytest won’t execute them again for that test. 
# --------------
# contents of test_append.py
import pytest


# Arrange
@pytest.fixture
def first_entry():
    return "a"


# Arrange
@pytest.fixture
def order():
    print("\n__order-done1")
    return []


# Act
@pytest.fixture
def append_first(order, first_entry):
    return order.append(first_entry)


def test_string_only(append_first, order, first_entry):
    # Assert
    assert order == [first_entry]
    order.append(1)

def test_string_only_2(append_first, order, first_entry):
    # Assert
    assert order == [first_entry]
    order.append(2)

def test_string_only_3(append_first, order, first_entry):
    # Assert
    assert order == [first_entry]

