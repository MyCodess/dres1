__________________ pytests_dnts ___________________________________________

#####  ==========  setup/urls/nts pytest : ===================================

    ---
    - python -m venv venv1 ; activate.ps1;  pip list | grepi pytest ;  pip install pytest ;
    - /OR sys-pkg:  pacman -Syu community/python-pytest
    --- docs/urls/...:
    - https://docs.pytest.org/
    - pytest --help    ##no-manpage , also on wins!
    - pydoc pytest
    - BK1  ==  BK-Python-Testing-with-Pytest_2Ed_Y2022_BrianOkken.pdf
##________________________________________  ___________________________


#####  ==========  runs/calls tests:

    --- defaults of "test discovery":  see BK1--p.7--"test discovery" :
        - default namings:  test_file1.py / file1_test.py , methods: test_method1() , TestClass1
        - no-args as: pytest  ==  in cu-dir-Tree : run all files named: test_xx.py /OR  xx_test.py  and look for test-methods/classes as:
        - no arguments: pytest looks at your current directory and all subdirectories for test files and runs the test code it finds, named as following:
        - Test files should be named test_<something>.py or <something>_test.py.
        - Test methods and functions should be named test_<something>.
        - Test classes should be named Test<Something>.
    ---
    - run All tests in "./dir1/" tree (incl. subdirs):    pytest  ./dir1/
    - certain-method only run:   pytest -v ch1/test_one.py::test_passing
##________________________________________  ___________________________



#####  ==========  outputs:
    - control-pytest-outputs:   pytest  --tb=XX  ##--as: --tb=style  :  Traceback print mode (auto/long/short/line/native/no) ;eg no tracebacks: --tb=no
    - more outputs:  pytest -v ...
##________________________________________  ___________________________

