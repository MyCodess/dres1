#- see:  https://docs.pytest.org/en/stable/reference/fixtures.html#conftest-py-sharing-fixtures-across-multiple-files

import pytest
#from pytest import pytestconfig

from . import params1 as pa1

######################## Topic: hierarchical-conftest.py-files : accesing/overwriting these fixtures from lower/subdirs test-files ################
@pytest.fixture
def order():
    return []

@pytest.fixture
def top(order, innermost):
    order.append("top")

######################## Topic: adding cmdline-options-fixture here and use this in subpkg/subdir which himself contains another conftest.py: ######
# - added from: https://docs.pytest.org/en/stable/example/simple.html  :

# 1- register the cmdline-args with pytest:
def pytest_addoption(parser):
    parser.addoption("--arg1", action="store", default=None, help="set arg-value in: code < pytest.ini < envvar < shell-cmdline-arg")
    parser.addoption("--arg2", action="store", default=None, help="set arg-value in: code < pytest.ini < envvar < shell-cmdline-arg")

# 2- parse the cmdline-args and setup relevant vars in code:
@pytest.fixture(scope="session", autouse=True)
def cmdline_args_parser(pytestconfig):
    for argname in pa1.cmdline_args_names:   # -readin all args into pramas1-global-dict:
        if pytestconfig.getoption(argname):
            pa1.cmdline_args[argname] = pytestconfig.getoption(argname)   # -default-val is defined in pytest_addoption ! so here NOT again default=xxx !
# - /OR same with request.config instead pytestconfig :
#   def cmdline_args_parser(request): pa1.cmdline_args['arg1'] = request.config.getoption("--arg1", default=None)
