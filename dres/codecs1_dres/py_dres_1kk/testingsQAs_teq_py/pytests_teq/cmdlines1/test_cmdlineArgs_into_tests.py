"""
--- Pass different values to a test function, depending on command line options :
    - alternatives to set/change pytest-cmdline-args:   <pytest.ini:addopts> $PYTEST_ADDOPTS <extra command-line arguments>  #-the LAST wins! so cmdline-args overwrite envvar and pytest.ini settings!
    - see:
    /doc/en/_build/html/example/simple.html#pass-different-values-to-a-test-function-depending-on-command-line-options
    https://pytest-with-eric.com/pytest-advanced/pytest-addoption/

--- steps:
    1- register the args-names in pytest-parser in prj-root-dir/conftest.py:  def pytest_addoption(parser): parser.addoption('--arg1', action=..., default=..., ...)
    2- parse now the cmdline-args in your (autouse-)fixture there as:
        2.a) /Either single ones as:  @pytest.fixture; def arg1_read(request): return request.config.getoption('--arg1')
        2.b) /OR setup a global var to keep args:
        import params1; @pytest.fixture(autouse=True, scope='session');
        def command_line_args():; params1.cmd_args = {};  params1.cmd_args['arg1'] =  request.config.getoption('--arg1'); ...; return params1.cmd_args;
    - nts: can raplace "request.config" with "pytestconfig" : pytestconfig() is Session-scoped fixture that returns the session’s pytest.Config object.

    Example:
--- USAGE1: call this with/out args as:  pytest -q [ --cmdopt=type2/xxx ] <myfile::mytest>
"""

# for the rest see in its fixtures here in conftest.py!
# -same effect:  def test_answer(cmdopt):
def test_answer(cmdopt_b):
    if cmdopt == "type1": print("first")
    elif cmdopt == "type2": print("second")
    else: print("invalid arg : ", cmdopt)
    # - assert 0  # to see what was printed

