import pytest
"""
    Parametrizing Functions:
    with function parametrization, pytest calls test-functions once each for every set of argument values we provided.
    ! the test_xx requires always as the first parameter a real fixture!! not directly/only mark-parametrization ! so here the dummy-fixture !
"""

@pytest.fixture
def fx_dummy1():
    return 0

@pytest.mark.parametrize(["p11","p12"],[(1,1),(1,2),(1,3)])
def test_params2(fx_dummy1, p11, p12):
    assert p11 == p12
