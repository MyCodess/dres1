______________ devNts to remember for pcap-cert : ___________________________________
- here ONLY DEVnts for PCAP-Cert ! for additional mock-/verw-pcap-nts see its w1-DIR ! /up1/w1/dcIt/Py_dc/Cert_PCAP_py/Mocks_udemy_1kk-pcap-220114/ , ... !
##________________________________________  ___________________________


#####  ==========  package/modules:
	-! a func can NOT be imported!! so NOT-ok:  import math.pow   !!
	-! a package/dir can NOT be imported with "import xxx" ! so, only modules/xx.py !! (/OR elements from modules by from pack1.mod1 import func1 )
##________________________________________  ___________________________


#####  ==========  str :
	- DIFF:  s1.find/rfind("xxx")  <--->  s1.index/rindex("xxx")  : if xxx NOT-found, then find returns -1 ,BUt index: ValueError !!
	-!! comparing-OPs for  str--int ONLY ok for  == and !=  !!but NOT others like: > < <= ... !
	-! ord("x") to know:  ord(" ") 32 , ord("0") 48 , ord("A") 65 , ord("a") 97 ##--so:  ord("a") - ord("A") == ord(" ") == 32  ! so Abstand between A and a exactly 32, so one-space !
	so: ord('x') - ord('X') == ord(' ') :  In ASCII, the distance between the codepoints of upper- andlower-case letters is always equal to 32, which is the codepoint of a space.
	-! slicing a str is exception-SAFE/free !! NO-exception ! so "12345"[2:600]  just returns "345"  !
	so: the slice which breaks string boundaries does not raise an exception – the non-existent characters are replaced by empty strings instead: "string"[2:100] evaluates to "ring"; "string"[-100:-200] evaluates to an empty string.
	-! empty-string is in EVERY string!  so:  "" in "abc"  == True
	" \t\n\r".isspace()  :==  True
	"U-+? ".isupper()    :==  True
	"a-+? ".islower()    :==  True
	str(None) == 'None'
##________________________________________  ___________________________


#####  ==========  assert
	-! assert  0/''/None/False/[]/{}/)()  , then it  raises AssertError! :
	OK/True/No-exc:    assert not None ; assert True == 1 ;
	Not-OK/AssertExc:  assert None ; assert True == 123 ;
	True == 1 ; False == 0 ; (bool() is subclass of int() ! )
##________________________________________  ___________________________


#####  ==========  random :
- DIFF:  randint(1,10) : is [1, 10] , so incl.10   <---> randrange(1,10)  : is [1, 10) , so: excl.10 ; otherwise same!
	so:  random.randint(start, stop)  ==  random.randrange(start, stop+1)
	randrange(start, stop, step) : pick a int-number between [start,stop), so incl. start excl. stop, in steps/increments of step.  all ONLY int !

	_______:  DIFF:  choice <---> choices :
	random.choice(l1) returns int  <--->  
	random.choices(l1 [, k=2]) returns LIST , and "k"  is only NAMED-param !!! also: random.choice(l1,k=2) so: can have two params! so NOT random.choices(l1, 2)
	random.choices()  and  random.sample() similar ! (sample() has also counts -param !)

	_______:  return-types:
	- returns LIST:     random.sample(l1,1) ,  random.choices(l1 [, k=2])
	- returns int/str/... (no-list):   random.choice(l1) , randint(1,10), randrange(1,10)

	_______:  seed:
	-! same seed(x) throws always SAME random-sequence !!
	so: If you use the same seed value twice you will get the same random number twice. : 
	  r1=random.Random() , r2=random.Random() , r1.seed(5) , r2.seed(5) : r1.random() == r2.random()  ##--the same seq of randoms !
	-! re-call again seed(x) on a random-instance:  RESEts the random engine, so again from start an the SAME random-numbers!! so:
	>>> import random >>> random.seed(10) >>> random.random() 0.5714025946899135 >>> random.random() 0.4288890546751146 >>> random.seed(10) >>> random.random() 0.5714025946899135 >>> random.random() 0.4288890546751146
	  so: Initializing a number generator with random.seed(n) twice will set it to exactly the same state, hence the values returned by the two subsequent calls are the SAME !
	- seed() method : is used to initialize the random number generator. The random number generator needs a number to start with (a seed value), to be able to generate a random number. By default the random number generator uses the current system time.
	- seed: r1.seed(5)  : with the same seed initialized, will always produce the same seq. of randoms !! default is using the system-time !
	- chk:  r1.seed(5) ; r2.seed(5) ; r1.random() ; r2.random() ; ...

	_______:  instance:
	- new random-object/instance:   r1=random.Random()
##________________________________________  ___________________________


#####  ==========  platform:
- python-interpreters: platform.python_implementation() : CPython, PyPy, Jython, IronPython, ...
	-!!  CPython (py-interpreter eg on arx)  <--->  Cython : has nothing to do with py-interpreter! is a subset of C-lang used to write irg Python-Code !
##________________________________________  ___________________________


#####  ==========  basics , syntx, ... :

	_______:  prints:
	- sep="xxx" ONLY between arguments of one print-clause! and NO-sep at the end! so if only one print-arg, then NO-sep at all will be printed!!

	_______:  sort :
	-! DIFF:  sort  <---> sorted : list1.sort() in-place modifies l1 and is lists-method ! but  sorted(l1) only output sorted-l1 and is a builtin-func !
	-! str has NO method sort()!! (str is auch not mutable!) but you can do sorted(str1)
	-! sorted() : sorts mathematically! so: -5 < -1 ! so:  sorted([-1, -5, -3])  #--->  [-5, -3, -1]

	_______:  oparators-basics:
	- / division returns  always float !! not-int !! so 2/2 returns 1.0  not 1 !!
	- 2**2**3 == 2**(2**3)  ! so ** is the only right-sided-precedence-operator ! so not the other way round !

	_______:  comparisonsi-operators:
	- str-and-nonStr-comparisons ONLY OK for == , != , BUT NOT for >,< ! so this compile-TypeError: 11 > "10" !
	- X  "in"  Y  : Y MUST be iterable (String, list,...) !

	_______:  lambda specials:
	- calling a lambda-func directly on-place of definition, eg:  (lambda x: 2**x)(3)
	- eg: f1 = lambda : lambda :4 ; f1()() #returns 4 !
##________________________________________  ___________________________


#####  ==========  OOPs:
	- issubclass(C1,C1)  returns True !
	-! ALL-normal(instance)-class-methods require (self) param, so method1(self)!
	BUT if you define a method1() withOUT-params , then as long as it is NOT called by an instance, everythin ok! no compiler-error!
	BUT as soon as an instance calls it, then Error !  (only class-static-methods do NOT rewquire any parameter !)
	--- init:
	-! __init__ : from-Edube_docs:  cannot be invoked directly either from the object or from inside the class – you can only invoke a constructor from any of the object's superclass constructors. (_1kk: really NOT-correct! but so mentioned in edube.org !)
##________________________________________  ___________________________


#####  ==========  datetime/calendar ?? cert??  pydoc datetime :

	_______:  init-params :
	- ALL up-down (see below eg), so:
	- date(year, month, day) --> date object , eg  date(2012, 12, 24)
	- time([hour[, minute[, second[, microsecond[, tzinfo]]]]]) --> a time object
	- datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])

	_______:  formattings:
	-! see refDocs: "strftime() and strptime() Behavior"
	- %w : Weekday 0==Sun, 6==Sat. :  Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.
	- %W : Weekday 0==Mon, 6==Sun. :  Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.

	_______:  -- calendar :
	- printout a calendar-year:  import calendar ; c1 = calendar.TextCalendar() ; print (c1.pryear(2022));
	- default-weekdays:  0==Mon., 6=Sun
##________________________________________  ___________________________


#####  ==========  
