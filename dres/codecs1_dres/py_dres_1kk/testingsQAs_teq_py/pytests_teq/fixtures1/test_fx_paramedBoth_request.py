import inspect
from pprint import pprint
import pytest

"""
fixtures with argument</params! And
pytest "request" builtin-fixture inspect !
---
two approaches to forward parameters/args to a fixture:
1- statitically: directly fixture-decorator-params
2- dynamically:  indirectly through test-method parametrize.
- !! if you do both, the dynamic/test-method-parametrize will OVERWRITE the static/fixture-method-params ones!
    so they will NOT be added, but overwrite!
---
-! So: you can define default params in fixture-decorator with @pytest.fixture(params=[50,60,70])
  and customize them with dynamic/test-method-deco @pytest.mark.parametrize(...)
---
- to inspect "request" fixture, forward 0 as param to the fixture!
"""

# --- fixture with default/static params:
@pytest.fixture(params=[50,60])
def fixt1(request):
    v1 = 5
    print("\n--- pre-yield---fixt1 started !")
    # -print debug/dict output only if param=0 !
    if request.param == 0:
        print("\n===== request-members1:  =======", str(request))
        for ii in inspect.getmembers(request):
            if ii[0] == '__dict__':
                print("\n----- request-dict1:  -----")
                pprint(ii[1], indent=4)
                print("----- END--request-dict1:  -----\n")
            else: print(ii)
    yield v1 + request.param
    print("\n----------  pos-yield- e.g. for teardown! ---fixt1 ended   !")


# --- test-method with custom/dynamic
# -2try: comment out following decorator to get the default params of the fixture:
# -2try: to inspect request builtin fixture:   @pytest.mark.parametrize("fixt1", [0, 20], indirect=True)
@pytest.mark.parametrize("fixt1", [10, 20], indirect=True)
def test_req1(fixt1):
    print("- test_req1: fixt1-value/v1 is:  ", fixt1)
    assert fixt1 in [5, 15, 25]
    # for default/static values:  assert fixt1 in [55, 65]

