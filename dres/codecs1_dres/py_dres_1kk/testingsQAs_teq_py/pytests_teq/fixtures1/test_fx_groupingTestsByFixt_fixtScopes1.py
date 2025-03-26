"""
    PyTests_dc/REFs-pytests_p/pytest-main/doc/en/_build/html/how-to/fixtures.html#automatic-grouping-of-tests-by-fixture-instances
    Automatic grouping of tests by fixture instances (scopes compares!) -pytestRefs !
    call:  pytest -s ...
    ---
    -! pytest minimizes the number of active fixtures during test runs. If you have a parametrized fixture, then all the tests using it will first execute with one instance and then finalizers are called before the next fixture instance is created.
    !! check the sequences of tests+fixtures ab-/aufbau for diffenren fx-scopes!
    !! parametrized module-scoped modarg resource caused an ordering of test execution that lead to the fewest possible “active” resources.  .... see docsRef there!
"""
# content of test_module.py
import pytest


@pytest.fixture(scope="module", params=["mod1", "mod2"])
def modarg(request):
    print("\n======---------------------------------=======")
    param = request.param
    print("  -- SETUP MOD-arg", param)
    yield param
    print("  >>>>> TEARDOWN MOD-arg", param)
    print("==============================================")


@pytest.fixture(scope="function", params=[1, 2])
def otherarg(request):
    print("\n______---------------------------------_______")
    param = request.param
    print("  ---- SETUP FUNC-arg", param)
    yield param
    print("  >>>>>>>>>> TEARDOWN FUNC-arg", param)
    print("______________________________________________")

##################### tests: ###############################
def test_0(otherarg):
    print("  RUN test_0 with FUNC-arg", otherarg)


def test_1(modarg):
    print("  RUN test_1 with MOD-arg", modarg)


def test_2(otherarg, modarg):
    print(f"  RUN test_2 with FUNC-arg {otherarg} and MOD-arg {modarg}")
