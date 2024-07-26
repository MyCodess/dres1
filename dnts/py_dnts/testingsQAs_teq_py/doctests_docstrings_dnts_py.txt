_________________ docstring / doctest in Std-Libs_py ________________________________

#####  ==========  docstring / doctest in Std-Libs_py , for units-testings :  ===================================

    - very simple test-outputs inserted in the docstring of the funcX, (in Std-Libs of py) for unit-tests !

	_______:  see:
	- pydoc doctest
	- https://docs.python.org/3/library/doctest.html
	- https://www.python-course.eu/python3_tests.php#doctest-Module
	- RefTutDocs--10.11 Quality Control (3.10)

	_______:  dres/exp/nts:
	- !! chk:   pydoc  ./py_dres_1kk/testingsQA_py/docstring1_doctest1.py
	- insrting simple test routines in docstring of source code in same file : basically can copy/paste the terminal-/py-interpreter-output in docstring of the function/module/method/....

	_______:  1.method:   oneFile--source_incl_tests:
	- python -m doctest module1.py  [-v]  ##--/OR:
	- python  module1.py [-v] ##and-then-in-source:    `if __name__ == "__main__":  import doctest; doctest.testmod();`
	- [-v] : print out all test results, also passed+failed ones! detailed report of all examples tried ! withOUT -v : ONLY the failed ones !

	_______:  2.method:   seperateFiles--sourceCode-and-testCode-files:
	- for module1.py must the its testfile module1_1teq.txt  include:  import module1; ....test-routines.... ; then:
	- python -m doctest  module1_1teq.txt  [-v]
	- if __name__ == "__main__": import doctest ;  doctest.testfile("testFile.txt") 
	- /OR more universally generic-filename eg: "sourceFileName"_1teq.txt in the same Dir:
	- if __name__ == "__main__": import doctest, pathlib ; fn1= pathlib.Path(__file__).stem + "_1teq.txt";   doctest.testfile(fn1);  ##--/OR:
	- if __name__ == "__main__": import doctest, os ; fn1= os.path.basename(__file__).removesuffix(".py") + "_1teq.txt";   doctest.testfile(fn1)

	_______:  testSuits of doctest/docstring :
	- pydoc  unittest  +  https://docs.python.org/3.10/library/doctest.html#unittest-api
##________________________________________  ___________________________


