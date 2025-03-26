# --Note on yields order in fixtures:
# - yield fixtures, the first teardown code to run is from the right-most fixture, i.e. the last test parameter.
# - but Finalizers in fixtures are executed in a first-in-last-out order.
# - call it:  pytest  --capture=no ...

# content of test_finalizers.py
import pytest


@pytest.fixture
def fix_w_yield1():
    print("\n--- S1: ------------")
    # print("before_yield_1")
    yield
    # print("after_yield_1")
    print("--- E1_-------------")


@pytest.fixture
def fix_w_yield2():
    print("--- S2: ")
    # print("before_yield_2")
    yield
    # print("\nafter_yield_2")
    print("\n--- E2: ")


def test_bar(fix_w_yield1, fix_w_yield2):
    print("__ test......")
    print("__ test......")

