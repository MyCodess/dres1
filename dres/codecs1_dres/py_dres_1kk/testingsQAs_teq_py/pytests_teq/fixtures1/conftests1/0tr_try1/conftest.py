#- see:  https://docs.pytest.org/en/stable/reference/fixtures.html#conftest-py-sharing-fixtures-across-multiple-files

import pytest
#from pytest import pytestconfig

from . import params1 as pa1

@pytest.fixture
def order():
    return []

@pytest.fixture
def top(order, innermost):
    order.append("top")

######################## kk: adding cmdline-options-fixture here and use this in subpkg/subdir which himself contains another conftest.py: ######
# - added from: https://docs.pytest.org/en/stable/example/simple.html  :
def pytest_addoption(parser):
    parser.addoption( "--cmdopt", action="store", default="def_opt1", help="my option: type1/type2/...")  # -stricter: , choices=("type1", "type2"))
    parser.addoption( "--arg1", action="store", default=None, help="check argument, set to int")

@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")

@pytest.fixture(scope="session", autouse=True)
# - /OR with request.config : def cmdline_args_parser(request): pa1.cmdline_args['arg1'] = request.config.getoption("--arg1", default=None)
def cmdline_args_parser(pytestconfig):
    pa1.cmdline_args['arg1'] = pytestconfig.getoption("--arg1") or pa1.cmdline_args['arg1']  # -default is defined in pytest_addoption ! so here NOT again default=xxx !
