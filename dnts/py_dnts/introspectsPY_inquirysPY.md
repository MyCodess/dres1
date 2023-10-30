introspections_py, obj-/class-queryings_py :
=========================================================================================


#####  ==========  __dict__/dir/vars/locals/globals/... introspections-funcs/attribs of classes/modules/... : ==================== 

	_______:  locals() :
    - dict of all local vars + values in the current scope/namespace- !   pydoc locals ;
	- locals() builtin :  Returns a dictionary containing the current scope's local vars+values.
	- for name, value in locals().items(): print  ('{0:20} ==  {1}'.format(name, value)) ;
	- basically  Returns  the __dict__ attribute for a module, class, instance, or any other object with a __dict__ attribute :

	_______:  globals() :
    - dict containing the current scope's global vars+values
	- for name, value in globals().items(): print  ('{0:20} ==  {1}'.format(name, value)) ;

	_______:  __dict__  :
    - dict of  attribs of objects-/modules-querys : 
	- object.__dict__ : object’s (writable) attributes Dictionary.
	- module1.__dict__ ,  module1.__dict__.values() 

	_______:  vars():
    - dict of local vars/attribs    pydoc vars :
	- vars()      ==  locals()               ##-- Without an argument, vars() acts like locals().
	- vars(obj1)  ==  obj1.__dict__

	_______:  dir():
    - List of current-scope-vars-names, except builtins (list! not-dict! no-values) !   
    - see  pydoc dir / builtins  , docsRF--6.3. The dir() Function :
	- dir() : If called without an argument, return a LIST of the names in the current scope (so as vars(), but only names, not their values !).
	- Note that it lists all types of names: variables, modules, functions, etc. except the builtins ! so it does not list the names of built-in functions and variables. 
	- dir(module1) : the module's attributes.  eg: dir(sys) ,so (like __dict__)
	- dir(class1)  : its attributes, and recursively the attributes of its bases.
	- for any other object: its attributes, its class's attributes, and recursively the attributes of its class's base classes.
##________________________________________  ___________________________


#####  ==========  "inspect" StdLib-module:

    _______:  inspect StdLib :
    - pydoc  inspect
	- module-stdlib:   inspect - Get useful information from live Python objects.  ; pydoc  inspect
	- eg:  import inspect ; inspect.isfunction(func1) and inspect.getmodule(func1)
	- eg:  from inspect import getclasstree ;...

    _______:  more-module-query:
    - import module1;  dir(module1)

##________________________________________  ___________________________


#####  ==========  tree-classes / subclasses / class-hierarchy_printout / class-tree / ... :

    - ! see dres:  *tree*.py !!
    - all subclasses of a cls sorted by name:  for ii in sorted(tuple.__subclasses__(), key=lambda x: x.__name__): print (ii)  
##________________________________________  ___________________________

