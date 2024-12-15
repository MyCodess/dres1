######### 1kk : ####################
import pytest

##--should fail:
def test_f1():
    assert 1 == 2

##--should pass: XFAIL
@pytest.mark.xfail(reason="1-not-2-fa", strict=False)
def test_xp1():
    assert 1 == 2

##--should pass: XFAIL
@pytest.mark.xfail(reason="1-not-2-tr", strict=True)
def test_xf1():
    assert 1 == 2

##--should fail: XPASS : no-exception--and-not-strict:
@pytest.mark.xfail(reason="expected-EXCEP-fa", strict=False)
def test_pf2():
    assert 1 == 1

##--should fail: FAILED : : no-exception--and-strict
@pytest.mark.xfail(reason="expected-EXCEP-tr", strict=True)
def test_pf1():
    assert 1 == 1