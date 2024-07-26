# -HotTo: Fixtures can be requested more than once per test (return values are cached)
# - ALL fixtures are already executed BEFORE starting the test_xxx ! and will provide the test_xxx with fixture-results as their parameters!

# contents of test_append.py
import pytest


# Arrange
@pytest.fixture
def first_entry():
    return "a"


# Arrange
@pytest.fixture
def order():
    return []


# Act
@pytest.fixture
def append_first(order, first_entry):
    return order.append(first_entry)


def test_string_only(append_first, order, first_entry):
    # Assert
    assert order == [first_entry]

def test_string_only_2(order, append_first, first_entry):
    # Assert
    assert order == [first_entry]

