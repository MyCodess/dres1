# - HowTo: Autouse fixtures (fixtures you don’t have to request)
# - autouse=True to the fixture’s decorator :  convenient way to make all tests automatically request them!
# contents of test_append.py
import pytest


@pytest.fixture
def first_entry():
    print("\n__entry()--done1")
    return "a"


@pytest.fixture
def order(first_entry):
    print("__order()--done1")
    return []


@pytest.fixture(autouse=True)
def append_first(order, first_entry):
    print("__append()--done1")
    return order.append(first_entry)


def test_string_only(order, first_entry):
    print("__test_string_only()--done1")
    assert order == [first_entry]


def test_string_and_int(order, first_entry):
    order.append(2)
    print("__test_string_and_int()--done1")
    assert order == [first_entry, 2]
