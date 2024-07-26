_____________ assert + __debug__ : ______________________________
- see also intreospections-dnts ! + tests + logging !


#####  ==========  __debug__  builtin:

    _______:  values/settings of __debug__  builtin-constant :
    - ! https://realpython.com/python-assert-statement/#disabling-assertions-in-production-for-performance :
    - ! Python has a builtin constant called __debug__. This constant is closely related to the assert statement. Python’s __debug__ is a Boolean constant, which defaults to True. It’s a constant because you can’t change its value once your Python interpreter is running !
    - default/normal __debug__  is True !! (so just calling python without -O/-OO or PYTHONOPTIMIZE setting)
    - export PYTHONOPTIMIZE=1  ##--is Equivalent to python -O   --->  __debug__ is False !
    - export PYTHONOPTIMIZE=2  ##--is Equivalent to python -OO  --->  __debug__ is False !
    - export PYTHONOPTIMIZE=0  ##--is Equivalent to just "python" normal call --->  __debug__ is True ! but this setting is then redundant/un-neccessary !
    --- so:
    - __debug__ is builtin-constant with default value "True" ! NOT-changable-value after python-start !
    - __debug__  ==  True  (normal python call)    <--->   __debug__  ==  False  (if:  python -O/-OO  /OR:  export PYTHONOPTIMIZE=1/2 )
    - its value can ONLY be changed BEFORE python-interpreter is started! its value cano NOT be changed/set once python-interpreter was started !
    - setting __debug__ to False:  ONLY by calling: python -O/-OO  /OR:  export PYTHONOPTIMIZE=1/2

    _______:  use for:
    - use it for devel-debugs, eg:  if __debug__: do-XX ; else: do-YY ;  ##-- then in production with "python -O" debug-stmts are disabled, since __debug__ is false, due to -O !
    - assert stmts are ONLY enabled, if __debug__ is True !! otherwise are disabled !
##________________________________________  ___________________________


#####  ==========  "assert"  builtin:
    _______:  see :
	- see docsRF:  7.3. The assert statement
    - ! https://realpython.com/python-assert-statement/

    _______:  nts assert :
    - ! do NOT use assert to validate input-data,... or anything part of core-funtionalities of your app ! since asserts will be disabled outside development !!  so use it ONLY to verify invariants in your app, so as debugging/QA-facilities ! see:  https://realpython.com/python-assert-statement/#running-python-with-the-o-or-oo-options

    _______: assert and __debug__ relation: 
	- Assert statements are a convenient way to insert debugging assertions into a program:
    -  __debug__  ==  True : asserts are executed /enabled !  <--->    __debug__  ==  False  : asserts are disabled/not-executed/ignored !
	- assert condition1, "msg1"   ==   if __debug__:  if not condition1 raise AssertionError("msg1")
    - The __debug__ constant is closely related to the assert statement. In short, if __debug__ is True, then all your assert statements will run. If __debug__ is False, then your assert statements will be disabled and won’t run at all.
	- disabling assert-stmts by setting __debug__ to False ,eg with:  python -O / -OO : man python ##--see __debug__ section here !

    _______:  usage assert :
    - NO-Paranthesis !! NO: assert (...) ! but just:  assert condition1, "msg1"
	- assert Expression  [, Arguments]   #eg:  assert 0 == 1 , "assert-msg1"  ##without ()
	- assert is a statement and not a function ! So do NOT use assert (...) ,but just WITHOUT () !! so eg assert a=2, "a-bad-value" !
	- AssertionError exceptions can be caught and handled like any other exception using the try-except statement, but if not handled, they will terminate the program and produce a traceback
	- !! assert "abc" does NOT raise AssertionError ,since: assert raises exception/AssertionError only if its condition1 evaluates to False: '' , 0, False, [], (), ... ! 
    - ! Pitfalls /Mis-Usages :  https://realpython.com/python-assert-statement/#understanding-common-pitfalls-of-assert
##________________________________________  ___________________________


