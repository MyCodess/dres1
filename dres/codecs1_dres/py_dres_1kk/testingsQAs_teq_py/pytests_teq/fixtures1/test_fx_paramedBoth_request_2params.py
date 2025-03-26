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
@pytest.fixture(params=[(50,60),(70,80)])
def fixt1(request):
    v1 = 10
    p0 = request.param[0]
    p1 = request.param[1]
    print(f"\n--- pre-yield---fixt1 started with params: {p0} , {p1} !")
    yield v1 + p0 + p1
    print("\n----------  pos-yield---fixt1 ended   !")


# --- test-method with custom/dynamic : ---> so es wird cartesian-cases of all possible combinations of fixture-params x test-params getestet !! so here 4 tests!:
# -2try: comment out following decorator to get the default params of the fixture:
@pytest.mark.parametrize("fixt1", [[5,6],[7,8]], indirect=True)
@pytest.mark.parametrize("n1", [111, 222])  # -!! just a dummy var to show how parametrize both fixture/indirect + test-func/direct seperately!
def test_req1(n1: int, fixt1):
    print(f"- test_req1: fixt1-value is:  {fixt1} ,and test-func-var n1 is {n1}") 
    assert fixt1 in [21, 25, 120, 160]

