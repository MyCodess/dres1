___________ collections : lists_dicts_sets_tupels : ____________________________

################### Allg/collections/All-listings...: #############################
#####  ==========  printouts/show-listings:
    - !! beutifyed-printouts-of-listings,  pydoc pprint :  pretty print module   ##--eg  pprint.pp(dir(sys)) ;
##________________________________________  ___________________________


################### LISTs: ########################################################
#####  ==========  !! DIFF:  list1  = list1 + [10,11]   <--->   list1  += [10,11]  bzw. list1.append(10) bzw. l1.append((4,5))

	- the first one (copy-variation): The list1 will be copied in every assignment. The new element will be added to the copy of the list1 and result will be reassigned to the variable liist1. After that, the old list1 will have to be removed by Python, because it is not referenced anymore.
	- the second one (in-place operation: with append/extend /OR as  augmented assignment ("+=") ): new elements will simply added to the end of list1 (fast!)
	--- as func-argument (BIG-DIFF !!):
	- the first assigment in a func is then call-by-value (No-side-effect) AND Very-Expensive/slow, due to first-copying-list1 ! the org-argument is NOT changed, if in a func!!)
	- the second assigment for a func-argument: is call-by-Ref (not first copying of list1 !!)! so the org-list1-argument IS affected/changed, even if assigment inside a func! so take care of side-effects !!
	-! see:
	https://www.python-course.eu/python3_list_manipulation.php#Extending-and-Appending-Lists-with-the-'+'-Operator
	https://www.python-course.eu/python3_passing_arguments.php#Side-effects
##________________________________________  ___________________________


#####  ==========  !! LISTs-copying/shallow/deep/recursive/-DIFFs !!:   Shallow and Deep Copy : 	see!! https://www.python-course.eu/python3_deep_copy.php :
	!! list1 = list2   <    list1=list2.copy()  <  list1=list2.deepcopy() (of: module copy) !!
	- list1 = list2  : absolut shallow! ALL changes in list1 are also in list2 (same references)
	- list1=list2.copy() :  shallow copy (references are copied, BUT NOT recursively!!), so changes in SUB-LISTS are seen in both lists. changes in direct objects are done only for current-list !
	- list1=list2.deepcopy() : absolutly INdependendant references/addresses! any changes in one list do NOT affect the other list !!
##________________________________________  ___________________________


#####  ==========  list comprehensions (in python3) <---> lambda +  map()/filter()/reduce()/.... :
	- /python-course.eu/python3_lambda.php.html
	--- filtering  l1-elements:  filter(lambda ..., l1)    <--->   list-comprehension  ;  eg: with l1 = [0, 1, 2, 3, 4] , looking for only even elements, as l11==[0, 2, 4] :
		- l11 = [x for x in filter (lambda x : x%2==0, l1)]  ##---> [0, 2, 4]    ##/OR same :
		- l11 = [x for x in l1 if x%2==0 ]                   ##---> [0, 2, 4]
	--- mapping  l1-elements:    map(lambda ..., l1)    <--->   list-comprehension  ;  eg: with  l1 = [0, 1, 2, 3, 4] :
		- l5 = list(map(lambda x: x*2, l1))  ##---> [0, 2, 4, 6, 8]
		- l5 = [x*2 for x in l1 ]            ##---> [0, 2, 4, 6, 8]
		-!! map(func1, l1,l2,l3,...) : map() can have several input-lists!!    map(lambda x, y, z : x+y-z,  l1,l2,l3)
	--- reducing  l1-elements to one scalar (eg to one hashCode / sum/.... ):
		- functools.reduce (lambda x,y: x+y , l1)  ##---> 10 /OR:
		- y=0; for x in l1: y +=x ;
##________________________________________  ___________________________


#####  ==========  looping and lists: lists as loop-var :
	-!! do NOT modify the sequence-posiotns (append/del/move/...) while you are iterating over themi in a loop!!
	   modifying the elements itself is no problem (but not their positions)
	-! if modifying positions is needed, then make a copy eg with slice-notation [:] of the list and then reposiotion the elements:
		-! see  ref.tut--Looping Techniques :
		for w in words[:]:   # Loop over a slice copy of the entire list
			if len(w) > 6:  ;  words.insert(0, w) ;
##________________________________________  ___________________________


#####  ==========  converting lists :
	- coverting int-list into str-list:  l5 = [str(x) for x in l1]    #/OR:  l5 = (list(map(str, l1))) ##/OR-inkl-modifs eg:  l5 = ['-- {:.2f} --'.format(x) for x in l1]
	-! file-lines-into-a-list:   fh1=open("t1.txt", "r") ; l5 = list(fh1)
	-! generator into a list:  gen1_iterator = gen1() ; l5 = list(gen1_iterator)
	- list-from-range() (is also finally an iterable, like generators):  list(range(10,20))



################### Dictionarys: #####################################################
#####  ==========  dicts-methods...:
	- pydoc dict ;   syntax: {key1 : val1 , ...}   dict1= {"red" : "rot", "green" : "grün"}
	- copy() is a shallow copy !
	- values(): !! dic1.items() does NOT get a list back, but a so-called items view!! so to a list with: list (dic1.items()) !
##________________________________________  ___________________________


#####  ==========  dicts-convertings  lists <---> dicts :
	- Dict-to-Lists:   l1 = list (d1.items())
	- Lists-1o-Dict:   d1 = dict (zip (l1_keys, l2_values))   ##-detailed:  l1 = list (zip (l1_keys, l2_values)); d1 = dict(l1);
##________________________________________  ___________________________


################### SETs : ###########################################################
#####  ==========  SETs:
	- pydoc set  ;  syntax:   set1= {"red", "rot", "green"} 
	-!!DIFF:  empty set:  s1=set();  <-->  s1={}  is an empty Dictionary !!
	--- Set Comprehension:
	- set1 = {...} ; eg:  set5 = {x+100 for x in l1 if x%2==0}  ; ##---> {100, 102, 104, 106, 108}
##________________________________________  ___________________________



################### Tuples : #########################################################
#####  ==========  tuples-defining/initializing tuples:
	- pydoc  tuple ; syntax: tup1 =1,2,3  /OR  tup1 = (1,2,3)   ##--!!- more importand ist the ",", not the ()! so tup1=1,2,3 also ok tuple!
	- () are NOT neccessary by defining a tuple! so all ok: tup= 1,2,3 ;  tup= (1,2,3)
	-! Note that it is actually the comma which makes a tuple, not the parentheses. The parentheses are optional, except in the empty tuple case, or when they are needed to avoid syntactic ambiguity.  ... : see docsRF
	- so, type((1))  ist int , but  type ((1,)) is  <class 'tuple'> !!
	- empty tuple tup1=()  ; only-one-element-tuple:  tup1= (1,) (so the comma makes it to tuple !!) :
		>>> t5=1   >>> type(t5)  <class 'int'>   >>> t5=1, >>> type(t5)  <class 'tuple'>
	- onle-element-tuple: just a comma after the elemen:  tup=1,  is.same.as tup=(5,) ; #so: len(tup) is 1
	- unpacking (reverse assignment: tuple to vars):  t=(5,6,7); a,b,c =t ; so eg b is then 6
##________________________________________  ___________________________


#####  ==========  tuples are IMMUTABLE!!:
	- tuples directly are IMmutabale/NOT-changable (but LISTs are mutable/changable)! so: tup=(1,2,3,4,5); tup[2]=5 --> error
	- BUT tuples can have mutable elements. eg: v = ([1, 2, 3], [3, 2, 1]); v[1][2]=5 is ok!
	- So: It is not possible to assign to the individual items of a tuple, however it is possible to create tuples which contain mutable objects, such as lists.
	- see details in: ref.tut--5.3 Tuples and Sequences


################### Iterators :  #####################################################
#####  ==========  DIFF / DEFs:  iterable  <--->  iterator :   difference between an iterable and an iterator? : /python-course.eu/advanced-python/iterable-iterator.php.html :
	--- "iterable"  :
	An object capable of returning its members one at a time ! A list is iterable but a list is not an iterator! 
	! see docsRF_Glossary--iterable : An object capable of returning its members one at a time. Examples of iterables include all sequence types (such as list, str, and tuple) and some non-sequence types like dict, file objects, and objects of any classes you define with an __iter__() method or with a __getitem__() method that implements Sequence semantics. Iterables can be used in a for loop and in many other places where a sequence is needed (zip(), map(), …)
	--- "iterator"  :
	An iterator can be created from an iterable by using the function 'iter'. Iterators are objects with a '__next__' method, which will be used when the function 'next()' is called.  
	! see docsRF_Glossary--iterator :  An object representing a stream of data. Repeated calls to the iterator’s __next__() method (or passing it to the built-in function next()) return successive items in the stream.
	---
	- so, On one hand, they are the same: You can iterate with a for loop over iterators and iterables.
	- Every iterator is also an iterable, but not every iterable is an iterator.
	- "iter(iterable)" built-in function: returns an iterator over the iterable-argument, eg iter(list1)! the argument must supply its own iterator, or be a sequence.
##________________________________________  ___________________________


#####  ==========  your class making iterable:
	- if you want to add an iterator behavior to your class, you have to add the __iter__ and the __next__ method to your class. The __iter__ method returns an iterator object. If the class contains a __next__, it is enough for the __iter__ method to return self, i.e. a reference to itself ! see  /python-course.eu/advanced-python/iterable-iterator.php.html
##________________________________________  ___________________________


#####  ==========  Iterators:
	-!! after ONE using/iterating over an iterator, it is then EMPTY !! (so after one Iterating/list-initiating/iprinting/reading/converting-to-list-or-dict-....)
	 iterators exhaust themselves, if they are used !! see exp: BKlein--Dictionaries: https://www.python-course.eu/python3_dictionaries.php
##________________________________________  ___________________________


#####  ==========  Iterators-funcs/-Libs/...:
    - see pydoc itertools !! + dres1kk ! + !! RefDocs-StdLib--FUNCTIONAL PROGRAMMING MODULES : itertools + functools , ...
##________________________________________  ___________________________

