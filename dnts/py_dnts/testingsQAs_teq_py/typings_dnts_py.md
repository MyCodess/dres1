___________________ typings-TypeCheckers_dnts_py : _________________________


############################## Typing /  type-hints in py : #########################################
#####  ==========  typings / type-hints in py (ab ver. 3.5 started! in 3.9+/3.10+ again a jump,....):
    - https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html  :  Type hints cheat sheet
    - https://bernat.tech/posts/the-state-of-type-hints-in-python/
    - PEP 484 – Type Hints  :  https://peps.python.org/pep-0484/
    - ! pydoc  typing  + RefStdLibs :  https://docs.python.org/3.10/library/typing.html
    - Arguments Declarations /Annotations : PEP 483 : simplified introduction ; PEP 484:  full specification of types-hints !  https://peps.python.org/pep-0483/  +  https://peps.python.org/pep-0484/ ; ab Python 3.5 
    - Variables Declarations /Annotations : PEP 526 – Syntax for Variable Annotations ; ab Python 3.6 !
    - type hints for py2 (for checkers): use "Type Comments", so as "# type: (str, int, str) -> str" ! A type comment must start with the "# type:" literal 
    - eg:  def func1(ii: int, lst: List[float]) -> None
##________________________________________  ___________________________



############################## Type-Checkers / Static-Code-Analysers : ################################
#####  ==========  Type-Checkers / Static-Code-Analysers / type-validations Libs ... :
    _______:  Type-Checkers , ...:
    - ! https://realpython.com/python-type-checking/
    - Mypy was arguably the first static type checking system for Python, as work on it began in 2012,
    - Pytype, created by Google, differs from the likes of Mypy in using inference instead of just type descriptors. In other words, Pytype attempts to determine types by analyzing code flow, rather than relying strictly on type annotations.
    - Pyre Created by developers at Facebook and Instagram, Pyre is actually two tools in one: a type checker (Pyre) and a static code analysis tool (Pysa). The two are designed to work hand-in-hand to provide a higher level of checking and analysis than other tools,
    - Pyright is Microsoft’s Python type checker, included as part of the Pylance extension for Visual Studio Code. 
    - pydantic : Data validation and settings management using Python type annotations;  enforces type hints at runtime.  https://docs.pydantic.dev

    _______:  runtime-type-checkers:
    - Have a look at Enforce, Pydantic, or Pytypes for some examples.
##________________________________________  ___________________________


#####  ==========  mypy:  
	- MyPy  :  Logical Checks for optionally-enforced static types
    - ! https://realpython.com/python-type-checking/
    - ! https://mypy.readthedocs.io/en/stable/command_line.html#command-line   bzw.  https://mypy.readthedocs.io/en/stable/index.html
    - mypy  --help    ##-nach:   pip install mypy
    - for ignoring ExtLibs-imports-typing-errors (bzw. not typing defined there), then mypy with:
        either/recommended) in your code-annotations/-comments, eg:  import numpy  # type: ignore   ##--I-The annotation-literal "# type: ignore" tells Mypy to ignore the import of Numpy.
        /OR/not-good/ignorestoo-much)  mypy --ignore-missing-imports  m1.py  ##--but this goes to far /too comprehensive !
        /OR)  mypy.ini in the current directory, add:  [mypy-numpy] ; ignore_missing_imports = True  ##--Mypy reads a file called mypy.ini in the current directory if it is present. This configuration file must contain a section called [mypy] and may contain module specific sections of the form [mypy-module].
        /OR) defining stub-files for not-typed imports /OR use its stb from Typeshed GIthub-Repo ! see:
        !- see  https://realpython.com/python-type-checking/
##________________________________________  ___________________________

