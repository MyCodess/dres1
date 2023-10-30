____________ exceptions, finally, raise, ....: _______________________
##________________________________________  ___________________________


#####  ==========  tree :
-| Object
-|-------| BaseException
-|-------|-------| Exception
-|-------|-------|-------| TypeError
-|-------|-------|-------| StopAsyncIteration
-|-------|-------|-------| StopIteration
-|-------|-------|-------| ImportError
-|-------|-------|-------|-------| ModuleNotFoundError
-|-------|-------|-------|-------| ZipImportError
-|-------|-------|-------| OSError   ---> also aliased as IOError ! _1kk
-|-------|-------|-------|-------| ConnectionError
-|-------|-------|-------|-------|-------| BrokenPipeError
-|-------|-------|-------|-------|-------| ConnectionAbortedError
-|-------|-------|-------|-------|-------| ConnectionRefusedError
-|-------|-------|-------|-------|-------| ConnectionResetError
-|-------|-------|-------|-------| BlockingIOError
-|-------|-------|-------|-------| ChildProcessError
-|-------|-------|-------|-------| FileExistsError
-|-------|-------|-------|-------| FileNotFoundError
-|-------|-------|-------|-------| IsADirectoryError
-|-------|-------|-------|-------| NotADirectoryError
-|-------|-------|-------|-------| InterruptedError
-|-------|-------|-------|-------| PermissionError
-|-------|-------|-------|-------| ProcessLookupError
-|-------|-------|-------|-------| TimeoutError
-|-------|-------|-------|-------| UnsupportedOperation
-|-------|-------|-------|-------| ItimerError
-|-------|-------|-------| EOFError
-|-------|-------|-------| RuntimeError
-|-------|-------|-------|-------| RecursionError
-|-------|-------|-------|-------| NotImplementedError
-|-------|-------|-------|-------| _DeadlockError
-|-------|-------|-------| NameError
-|-------|-------|-------|-------| UnboundLocalError
-|-------|-------|-------| AttributeError
-|-------|-------|-------| SyntaxError
-|-------|-------|-------|-------| IndentationError
-|-------|-------|-------|-------|-------| TabError
-|-------|-------|-------| LookupError
-|-------|-------|-------|-------| IndexError
-|-------|-------|-------|-------| KeyError
-|-------|-------|-------|-------| CodecRegistryError
-|-------|-------|-------| ValueError
-|-------|-------|-------|-------| UnicodeError
-|-------|-------|-------|-------|-------| UnicodeEncodeError
-|-------|-------|-------|-------|-------| UnicodeDecodeError
-|-------|-------|-------|-------|-------| UnicodeTranslateError
-|-------|-------|-------|-------| UnsupportedOperation
-|-------|-------|-------| AssertionError
-|-------|-------|-------| ArithmeticError
-|-------|-------|-------|-------| FloatingPointError
-|-------|-------|-------|-------| OverflowError
-|-------|-------|-------|-------| ZeroDivisionError
-|-------|-------|-------| SystemError
-|-------|-------|-------|-------| CodecRegistryError
-|-------|-------|-------| ReferenceError
-|-------|-------|-------| MemoryError
-|-------|-------|-------| BufferError
-|-------|-------|-------| Warning
-|-------|-------|-------|-------| UserWarning
-|-------|-------|-------|-------| DeprecationWarning
-|-------|-------|-------|-------| PendingDeprecationWarning
-|-------|-------|-------|-------| SyntaxWarning
-|-------|-------|-------|-------| RuntimeWarning
-|-------|-------|-------|-------| FutureWarning
-|-------|-------|-------|-------| ImportWarning
-|-------|-------|-------|-------| UnicodeWarning
-|-------|-------|-------|-------| BytesWarning
-|-------|-------|-------|-------| ResourceWarning
-|-------|-------|-------| Error
-|-------|-------| GeneratorExit
-|-------|-------| SystemExit
-|-------|-------| KeyboardInterrupt
##________________________________________  ___________________________


#####  ==========  docs:
	docsRF-Tut:  8. Errors and Exceptions
	docsRF-StdLibs:  Built-in Exceptions
##________________________________________  ___________________________


#####  ==========  Allg-excepts:
	- DEFAULT/unnamed-except clause MUST be the LAST (so only "except:" WITHOUT Exception-Type) !! otherwise compiler SyntaxError ! so does NOT run at all!! :
	- ONLY the FIRST matching except clause will be executed out of many except clauses!! so ONLY ONE except-branch will be executed !
	  The very LAST except clause may omit the exception-name to serve as a wildcard.  Use this with extreme caution, since it is easy to mask a real programming error in this way! 
	- so the DEFAULT except clause (WITHOUT Exception-Type) will be ONLY executed, if NO other one is matching !!
	- should always place more concrete/specific/sub-exception-clauses  higher/before more general/base-exceptons-clauses !
	- eg: putting "except BaseException: ..." will make ALL further exception-clauses UNREACHABLE/redundant !!
##________________________________________  ___________________________


#####  ==========  inherited exceptions !!:
	- docsRF_3.9:  8.3. Handling Exceptions :
	A class in an except clause is compatible with an exception if it is the same class or a base class thereof, but NOT the other way around ! !see example-code there ! also in py_dres_1kk !
	So: BaseException will catch all raised exceptions in a try-except-clause !
##________________________________________  ___________________________


#####  ==========  "finally" in try-exception-else-finally :
	-!! see docsRF-Tut: 8.7. Defining Clean-up Actions ! for Details and sequnces ...:
	- If a finally clause is present, the finally clause will execute as the last task before the try statement completes. The finally clause runs whether or not the try statement produces an exception.  docsRF
	- finally clauses are called clean-up or termination clauses, because they must be executed under all circumstances, i.e. a "finally" clause is ALWAYS executed REGARDLESS if an exception occurred in a try block or not !
##________________________________________  ___________________________


#####  ==========  raise :
	-! raise; (with NO-arguments): ONLY in except-clause to forward the SAME except further !! in ALL other cases it needs an argument as: raise OSError; !
	so: The specialized, argumentless variant of the raise instruction can be used only during ongoing exception handling. In other words, it is illegal to execute it outside except branches.
	The instruction is designed to re-raise the same exception which is currently being handled. It allows the programmer to partially handle the exception and explicitly delegate further handling to other parts of the code.
##________________________________________  ___________________________


#####  ==========  Built-in Exceptions
	docsRF-StdLibs:  Built-in Exceptions
##________________________________________  ___________________________


#####  ==========  Custom-/User-defined-Exceptions:
	docsRF-Tut:  8. Errors and Exceptions ---> 8.6. User-defined Exceptions
	- programmers are encouraged to derive new exceptions from the Exception class or one of its subclasses, and not from BaseException.
