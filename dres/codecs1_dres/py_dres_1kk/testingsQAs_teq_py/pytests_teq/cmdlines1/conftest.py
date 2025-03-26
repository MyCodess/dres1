# content of conftest.py
import pytest

# ############### fixtures for cmdlineArgs_into_tests1.py : ################
def pytest_addoption(parser):
    parser.addoption( "--cmdopt", action="store", default="type1", help="my option: type1 or type2")    # -stricter:  choices=("type1", "type2"),)

@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")

#--- same but: raplace "request.config" with "pytestconfig" : pytestconfig() is Session-scoped fixture that returns the session’s pytest.Config object :
@pytest.fixture
def cmdopt_b(pytestconfig):
    return pytestconfig.getoption("--cmdopt")
#############################################################################
