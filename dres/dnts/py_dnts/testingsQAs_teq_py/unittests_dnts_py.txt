___________________ unittest of StdLib_py : _______________________________________

#####  ==========  urls/docs:
    - JUnit-like modules (in Std-Libs of py) :
    - Intro-short + Vorlage:  RefDocs--firstPart: basic-example ,  /library/unittest.html#basic-example
    - RefDocs unittest      :  /library/unittest.html  bzw.  https://docs.python.org/3/library/unittest.html
    - RefDocs unittest.mock :  /library/unittest.mock.html  +  https://realpython.com/python-mock-library/
    - pydoc unittest
    - see dres_1kk
    ---
    - Intro-short:  https://www.dataquest.io/blog/unit-tests-python/
##________________________________________  ___________________________

#####  ==========  naming-conventions for test-routines of unittest_py :
    - test-module-names:  testXXX.py
    - test-method-names:  testXXX(...)
    - src + test modules must be importable modules ! so in sys.path bzw. PYTHONPATH !
    - methods whose names start with the letters "test": This naming convention informs the test runner of unittests about which methods represent tests.
    - unittest-assert-methods /assertXXX methods are used instead of the "builtin assert statement" so the test runner can accumulate all test results and produce a report.
##________________________________________  ___________________________

#####  ==========  setup-/tearDown-test-data/...,  test-fixture :
    - /library/unittest.html#organizing-tests
    - setUp() , tearDown() , setUpClass()
    --- nts to  test-fixture :
    - !! per each **Test-Method** : setUp(), tearDown(), and __init__() will be called once per each test. A new TestCase instance is created as a unique test fixture used to execute each individual test method ! see RefDocs !
    - !! isolated test-cases !!: The testing code of a TestCase instance should be entirely self contained, such that it can be run either in isolation or in arbitrary combination with any number of other test cases.  The order in which the various tests will be run is NOT the same as in your module or as you think ! RefDocs !
    - but you can arrange/order your test-cases yourself as a unittest.TestSuite !
    --- setup() :
    1- per-test-method-executed-setups:  setUp(self): ... ;
    2- per-test-class-executed-setups:   @classmethod ; def setUpClass(self): ... ;
    --- tearDown() :
    - tearDown() :  If setUp() succeeded, tearDown() will be run whether the test method succeeded or not.
##________________________________________  ___________________________

#####  ==========  Impl/code:  https://www.dataquest.io/blog/unit-tests-python/ :
    --- steps for a test-case-impl of unittest.TestCase :
    1- class TestXXX  (unittest.TestCase):
    2- setUp(self) /OR @classmethod def setUpClass(self)
    3- test_method_xxx(self)
    3b- if needed: tearDown() to clear setup steps ... !
    4- /either if __name__ == '__main__': unittest.main();  /OR  pyhon -m unittest
    - see eg:  https://www.dataquest.io/blog/unit-tests-python/ :
    --- nts testcases:
##________________________________________  ___________________________

#####  ==========  run-tests / calls-test-modules+methods

    - !!  python -m unittest -h  ##--listing of all running variations ... !
    - /either if __name__ == '__main__': unittest.main();  /OR  pyhon -m unittest <test-modules, ...>
    - eg: cd prj1;  PYTHONPATH=./src:./tests:$PYTHONPATH  python   ./tests/test_my_calculations.py  ##--requires call of: unittest.main();
    - eg: cd prj1;  PYTHONPATH=./src:./tests:$PYTHONPATH  python  -m unittest  ./tests/test_my_calculations.py  ##--then not needed call of: unittest.main()
    - eg: cd prj1;  PYTHONPATH=./src:./tests:$PYTHONPATH  python -m unittest discover  -s  ./tests/  -v    ##--runs/discover ALL tests/test-modules/.. in ./tests/ ; default-search-for:  test*.py
    - eg: cd prj1;  PYTHONPATH=./src:./tests:$PYTHONPATH  python -m unittest discover  -s  ./tests/  -v  --pattern "*_test.py"   ##--runs/discover ALL tests/test-modules/.. in ./tests/ by filenames-patterns of "*_test.py" ; default-search-for:  test*.py
    - discovery of test modules:  /library/unittest.html#test-discovery  +   /library/unittest.html#command-line-options
    --- cmdline calls + Options :
        - python -m unittest -h
        - cmdline-calls:    /library/unittest.html#command-line-interface , bzw.  
        - cmdline-options:  /library/unittest.html#command-line-options
        - eg:
        python -m unittest  -v  test_module.TestClass.test_method   ##--method
        python -m unittest  -v  test_module1  test_module2    ##--modules
        python -m unittest  -v  test_module.TestClass         ##--class
        python -m unittest  -v  tests/test_something.py       ##--file-path
        python -m unittest  -v  [discover]                    ##---> "Test Discovery" runs, if no arguments !
        - -k  :  Only run test methods and classes that match the pattern or substring !
        - -f, --failfast  :  Stop the test run on the first error or failure.
##________________________________________  ___________________________


#####  ==========  mock / unittest.mock in Python > 3.3 :

	- unittest.mock RefDocs :  /library/unittest.mock.html  + /library/unittest.mock-examples.html  +  https://pypi.org/project/mock/
	- unittest.mock :  https://opensource.com/article/23/4/using-mocks-python +  https://realpython.com/python-mock-library/ + https://www.pythontutorial.net/python-unit-testing/python-unittest-mock/
	- date-time-mocking-lib (from realplay-dc):  https://github.com/spulec/freezegun

	_______:  mock / patch:
	https://www.pythontutorial.net/python-unit-testing/python-unittest-mock/
	- https://realpython.com/python-mock-library/
	--- patching:
	https://www.pythontutorial.net/python-unit-testing/python-patch/
	! Because of the @patch decorator, the decorated method has an additional argument mock_read which is an instance of the MagicMock.
##________________________________________  ___________________________


#####  ========== unittest: patch /mock:
##________________________________________  ___________________________


