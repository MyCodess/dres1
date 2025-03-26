"""
- sequence of overwriting the cmdline_args:
    - defaults in pa1.cmdline_args < pytest.ini < envvar PYTEST_ADDOPTS < shell-cmdline-arg
    - Note that the environment variable PYTEST_ADDOPTS and the addopts ini option are handled by pytest itself! (pytest-py-run/-interpreter)
    - 
"""
from .. import params1 as pa1

def test_cmdline_args1():
    print("params1-arg1 :: ", pa1.cmdline_args['arg1'], str(pa1.cmdline_args))

def test_answer(cmdopt):
    print("cmdopt-val: ", cmdopt)

