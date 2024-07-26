
import pytest
"""
    Parametrizing Fixtures:
    pytest will then call the fixture once each for every set of values we provide.
    Then downstream (compared with Parametrizing Functions): every test function that depends on the fixture will be called, once each for every fixture value.
    Fixture parametrization has the benefit of having a fixture run for each setof arguments. This is useful if you have setup or teardown code that needsto run for each test case—maybe a different database connection, or differentcontents of a file, or whatever.
    - see also the other method with marker: @pytest.mark.parametrize: parametrizing test functions : see /how-to/parametrize.html#parametrizemark
"""

@pytest.fixture(params=[1,2,3])
def fx_params1(request):
    return request.param

def test_params1(fx_params1):
    assert fx_params1 % 2 == 0

def test_params3(fx_params1):
    assert fx_params1 % 2 != 0
