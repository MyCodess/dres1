_________________ * and ** in methods-params and their invocations ... : ______________________
##________________________________________  ___________________________


#####  ==========  docs/WPs/helps:
-!! https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/  :  Asterisks in Python: what they are and how to use them
-! RefDocsPy_Tutorial:  4.7. More on Defining Functions
- https://www.python.org/dev/peps/pep-3102/ : PEP 3102 -- Keyword-Only Arguments
- PEP 3132 -- Extended Iterable Unpacking
- PEP 448 -- Additional Unpacking Generalizations
- in functions-params:  /python-course.eu/python3_functions.php.html
##________________________________________  ___________________________


#####  ==========  */**-params , stars-params (are NOT pointer!) :
-!! */** in funcs-params : simply unpack/singularize the list/dict and übergeben an func1 as individual values! that is all! nothing with pointer/Refs/... !

	_______:  *-params :
	-!! *-params are handed over to the func as a TUPLE !!

	_______:  **-params :
	-!! **-params eg in str.fromat(**dic1) turns dic1 into the form:  k1=v1, k2=v2,...
	"**" in str.fromat(**dic1) turns dic1 automatically into the form 'province="Ontario",capital="Toronto"' ! py1var/docsvar/python-course.eu/python3_formatted_output.php.html
##________________________________________  ___________________________


#####  ==========  in functions-params as in f1(p1, *list1) ... :
	- /python-course.eu/python3_functions.php.html
	- /python-course.eu/python3_passing_arguments.php.html  : * in Function Calls
	--- in functions definitions (as param-declaration) :
	- * is NOT pointer!  is just for: "Arbitrary Number of Parameters" :
	- ** is NOT pointer!  is just for: "Arbitrary Number of Keyword Parameters" :
	--- in functions calls (as param-uebergabe):
	- * will just "unpack" or singularize the list as in f1(5, *l1)
	- ** will just "unpack" or singularize the dic1 in key1=val1, .... as in:  f1(5, **dic1)
##________________________________________  ___________________________


#####  ==========  
