___________________ TestingsQA_py _________________________________________

    -! abbrv:  teq == TEstingsQA ,  FNs-label:  _teq  bzw.  _teq[1/3/5].txt eg in f1.py + f1_teq.txt  (old/Anfang/hardly-used: teqa  ==  TestingsQA)


#####  ==========  docs/refs for  TestingsQA_py

	_______:  urls/refs...:
	- py_Ref_docs:  "Standard Library" ---> Development Tools : Listings there !!   https://docs.python.org/3/library/development.html
	- py_RefDocs    "Standard Library" ---> Development Tools ---> doctest + unittest +  test , see: https://docs.python.org/3/library/development.html  and search "test"
    - py_RefDocs:   listing-of-test-alternatives in py_RefDocs ! :  https://wiki.python.org/moin/PythonTestingToolsTaxonomy  + https://docs.python.org/3.11/library/unittest.html  +  
    - listing-of-test-alternatives :  https://www.softwaretestinghelp.com/python-testing-frameworks/  + https://wiki.python.org/moin/PythonTestingToolsTaxonomy
	- alternatives TestingsQA_py : docstring/doctest/unittest , unittest pkg, pytest , robot , Nose2, Robot Framework, ...
	- https://www.python-course.eu/python3_pytest.php  ,  https://www.python-course.eu/python3_tests.php
    - assert / __debug__  :  see extra dnts !

	_______:  learn-urls/...:
    https://realpython.com/python-testing/
	https://realpython.com/python-code-quality/
##________________________________________  ___________________________


########################### testing-frameworks_py: ################################################
#####  ==========  main-testing-framewokrs_py /StdLib-testings  : see extra dnts:
    - doctests_docstrings_dnts_py.md
    - unittests_dnts_py.md
    - pytests_dnts_py.md
    - Listing of all py-test-frameworks in pyRefDocs :    https://www.softwaretestinghelp.com/python-testing-frameworks/ 
##________________________________________  ___________________________

#####  ==========  Robot-Framework: =============================================================
    - https://robotframework.org/
##________________________________________  ___________________________

#####  ==========  Nose2 : unittest successor, with plugins :======================================
    - based on unittest hence it is referred to as extend unittest or unittest with the plugin
    - https://docs.nose2.io/en/latest/
    - https://nose2.readthedocs.io/en/release-0.3/plugins.html
    - nose2 is the successor to nose (and unittest). It’s unittest with plugins.
    - nose2’s purpose is to extend unittest to make testing nicer and easier to understand.
##________________________________________  ___________________________

#####  ==========  Testify (geplant was as Nachfolger of unittest and nose !?) ===================
    - Testify was designed to replace unittest and nose. Testify has more advanced features over unittest.
    - https://pkg.go.dev/github.com/stretchr/testify
    - Initially Testify was developed to replace unittest and Nose but the process of transiting it to pytest is on, so it is recommended for the users to avoid using Testify for few upcoming projects.
##________________________________________  ___________________________



#################### BDD (Behavior Driven Development) #####################################
#####  ==========  BDD (Behavior Driven Development):
	_______:  Behave 	:  https://behave.readthedocs.io/en/latest/ , It only supports black box testing.
	_______:  Lettuce :  http://lettuce.it/tutorial/simple.html
##________________________________________  ___________________________


############################  QA-code / linters/ STATIC-checkers / typings, type-hints / Type-Checkers : ########################################
#####  ==========  typings-TypeCheckers_dnts_py:  see extra typings_dnts_py.md  !
##________________________________________  ___________________________

#####  ==========  linters : Static-Code-checkers/-Analyzers) :
	_______:  pylint,...:
	- !!  https://realpython.com/python-code-quality/
	- ! Pylint , https://pylint.pycqa.org/en/latest/
	- ! pycqa.org  :  py automatic style and quality reporting : Astroid and Pylint

	_______:  more:
	- https://realpython.com/python-code-quality/ :
        : Linter	Category	Description  :
	- Pylint	Logical & Stylistic	Checks for errors, tries to enforce a coding standard, looks for code smells
	- PyFlakes	Logical	Analyzes programs and detects various errors
	- Bandit	Logical	Analyzes code to find common security issues
    - SonarQube  : all-langs!
    - ?  sphinx.ext.coverage
##________________________________________  ___________________________

#####  ==========  QA-packages (coll of several linters/checkers/...):
	_______:  
	Mccabe	Analytical	Checks McCabe complexity
	Radon	Analytical	Analyzes code for various metrics (lines of code, complexity, and so on)
##________________________________________  ___________________________


#####  ==========  StyleGuides/Formatters/...:  ---> see extra_dnts here !
##________________________________________  ___________________________


####################  Utils/Tools/Envs testing/QAs py : ###########################################
#####  ==========  tox
    tox aims to automate and standardize testing in Python. https://tox.wiki/en/latest/
##________________________________________  ___________________________


#####  ==========  devpi :   https://www.devpi.net  :
    devpi : complementary command line tool to drive packaging, testing and release activities with Python. 
##________________________________________  ___________________________

