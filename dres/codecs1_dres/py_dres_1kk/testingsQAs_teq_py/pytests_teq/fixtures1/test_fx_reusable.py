# --HowTo: Fixtures are reusable (can be used as setups !):
# - gives us the ability to define a generic setup step that can be reused over and over!
# - Two different tests can request the same fixture and have pytest give each test their own result from that fixture.
# - the ability to define a generic setup step that can be reused over and over, just like a normal function would be used.
# - Each test here is being given its own copy of that list object, which means the order fixture is getting executed each time (the same is true for the first_entry fixture)
# contents of test_append.py
import pytest


# Arrange
@pytest.fixture
def first_entry():
    return "a"


# Arrange
@pytest.fixture
def order(first_entry):
    return [first_entry]


def test_string(order):
    order.append("b")
    assert order == ["a", "b"]


def test_int(order):
    order.append(2)
    assert order == ["a", 2]
