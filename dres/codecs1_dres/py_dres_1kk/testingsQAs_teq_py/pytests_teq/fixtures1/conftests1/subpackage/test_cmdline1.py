"""
- sequence of overwriting the cmdline_args:
    - defaults in pa1.cmdline_args < pytest.ini < envvar PYTEST_ADDOPTS < shell-cmdline-arg
    - Note that the environment variable PYTEST_ADDOPTS and the addopts ini option are handled by pytest itself! (pytest-py-run/-interpreter)
    - 
"""
from .. import params1 as pa1

def test_cmdline_args1():
    print("\nparams1-arg1 :: ", pa1.cmdline_args['--arg1'])
    print("params1-arg2 :: ", pa1.cmdline_args['--arg2'])
    print("pa1.cmdline_args--dict:  ", str(pa1.cmdline_args))

