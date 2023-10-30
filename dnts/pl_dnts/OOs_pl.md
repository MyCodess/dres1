___________ OO-perl _______________________________

	_______:  - see:
	perlboot, perltoot. perltooc
	perlobj,  perlref,  perlmod, perltie
	parent , base , 
##________________________________________  ___________________________


#####  ==========  FAZIT.OO "use ..." :
	-!! Fazit:  best if possible:    "use parent" > [ "use base" ] > "@ISA=..."
		- base is obsolete bzw. replaced by parent!     :see  perldoc  parent , base :  
		- OO-hierarchy can be defined by:  parent  /OR  use base  /OR  @ISA
		- parent: when several classes in the same file: use parent -norequire  #see perldoc parent
		- @ISA is done at runtime, so is errorprone! base/parent at compile-time!
	-!! In Perl, METHODS execute in the context of the class they were DEFINED in, NOT that of the OBJECT that triggered them.   : perldoc-5.14.0/perltoot.html#Accessing-Class-Data
		kk: what it means?: assume class A-is.oarent.of-B , class.global.OUR.var-$v1 is defined in both A+B with different values,
		an Instance ob B "b" calls nethod m1:  b->m1 , and m1 is defined in A
		---> m1 takes the $v1 defined in A, where the method is defined, and NOT which type the object "b" is (which is B)
		!! BUT if the method m1 itself is also defined in both classes A+B, then b->m1 will call B::m1 !!
		!! also: die Methode selber, wird die erste Object-methode in er Hirarchie ausgeführt,
		aber dann die Ausführung dieser Methode dann geschieht im Context der Klasse der Methode, und nicht Klasse des Objekts!!
		:see  devres/codesColl_devres_kk/perlsColl_devres_kk/prj_pl1/oopl/classMembers.pl
##________________________________________  ___________________________


#####  ==========  DEFs-OO.perl:   see perlobj:
	- Object:	An object is simply a reference that happens to know which class it belongs to.
	- Class:	A class is simply a package that happens to provide methods to deal with object references.
	- Method:	A method is simply a subroutine that expects an object reference (or a package name, for class methods) as the first argument.
	- Constructor:  A constructor is merely a subroutine that returns a reference to something "blessed" into a class, generally the class that the subroutine is defined in.
	- Blessing:	 bless(refX, classX) takes the reference refX and tells it (modifies it), that it is a TYPE/Object of the classX (so adds its class-membership to the object refX), and then returns the reference refX. so the referenced object refX knows that it has been blessed.
	-- more DEFs.nts:
		- Perl objects are just references to a special type of object that happens to know which package it's associated with.
		  Constructors are just special subroutines that know how to create that association. see perlref
		- Within the class package, the methods will typically deal with the reference as an ordinary reference.
		  Outside the class package, the reference is generally treated as an opaque value that may be accessed only through the class's methods.  :perlobj
	---! DIFF:  REFs  <-->  Objects/Instaces (blessed REFs):	
		- Perl objects are blessed. References are not.
		- Objects know which package they belong to. References do not.
##________________________________________  ___________________________


#####  ==========  parent bzw. base xxx: 
	- see perldoc base , perldoc  parent , intermediateperl-CHP-11-SECT-5.html (obviously pre-"parent"-pragma):
	- take "use parent bzw. base" instead  @ISA=...  (intermediateperl-CHP-11-SECT-5.html), so:
		--instead ISA for subclassing: 
			package Cow;
			use Animal;
			use vars qw(@ISA);
			@ISA = qw(Animal);  bzw.  push @ISA  qw(Animal);
		--take parent bzw. base:
			package Cow;
			use parent qw(Animal);  bzw.  use base qw(Animal);
	- "use base 'Foo';" is pretty compact. Furthermore, use base has the advantage that it's performed at compile time, eliminating a few potential errors from setting @ISA at runtime, like some of the other solutions.
	--- parent  :
		- "use parent 'Foo';"  was forked from base to remove the cruft (==mess /Over-Coding) that had accumulated in it. : perldoc  parent
		- parent: when several classes in the same file:  "use parent -norequire, qw(Foo Bar);"   ;see perldoc parent
##________________________________________  ___________________________


#####  ==========  @ISA /inheritance / ... :
	---! DEF: @ISA is a special array within each package, which says where else to look for a method if you can't find it in the current package. This is how Perl implements inheritance.
	          Each element of the @ISA array is just the name of another package that happens to be a class package.
			  The classes are searched for missing methods in depth-first, left-to-right order by default (see "perldoc mro" for alternative search order and other in-depth information).
			  The classes accessible through @ISA are known as base classes of the current class. i   ;see perlobj
    - @ISA-Tree-search is recursive, depth-first, left-to-right in each @ISA by default (see mro for alternatives).  see perldoc-5.14.0/perlboot.html
	--- SUPER :
		-!! "SUPER" refers to the superclass of the CURRENT PACKAGE, not to the superclass of the object (referenced by $self /$obj/...) !  :see  perldoc-5.14.0/perlobj.html#Method-Invocation
		-!  superclass-constructor will NOT be called automatically in the subclass-constructor!
		-!!  "SUPER" can only currently be used as a modifier to a method name, but not in any of the other ways that class names are normally used!  perlobj
		      so, ok:  $self->SUPER::method(...);    -BUT Wrong:   SUPER::method(...);  /OR   SUPER->method(...);   #see perlobj
		-! method-calls: parents-class-method "m1" will NOT be called automatically from the derived-class-method "m1"!!  see below!
	--- UNIVERSAL    :see perlobj , perldoc-5.14.0/perlobj.html#Default-UNIVERSAL-methods
		- UNIVERSAL - base class for ALL classes (blessed references)   :see perldoc UNIVERSAL  bzw.  perldoc-5.14.0/perltoot.html#UNIVERSAL
		  so all objects hava:  $self->isa(class) ,  $self->can(METHOD) ,  $self->VERSION( [NEED] ); ...  ;see perldoc  UNIVERSAL
		- UNIVERSAL::AUTOLOAD method to trap unresolved method calls to any kind of object.  :see /perldoc-5.14.0/perltoot.html#AUTOLOAD:-Proxy-Methods
		  to  stop the AUTOLOAD inheritance simply do:  sub AUTOLOAD;   #see perlobj
		  DESTROY is subject to AUTOLOAD lookup. So if your class has an AUTOLOAD method, but does not need any DESTROY actions, just do make an empty DESTROY function!  :see perldoc-5.14.0/perlobj.html#Destructors
##________________________________________  ___________________________


#####  ==========  constructors/new().method:
	---!! DIFFs:  C++.OO.constructors <--> perl.OO.constructors : perldoc-5.14.0/perlobj.html#An-Object-is-Simply-a-Reference :
		- perl.constructors can be named anything. so they do NOT have to be named "new()" (or as in java "<classname>")
		- perl.constructors have to allocate their own memory (eg by $self={}  /OR $self=[] , ...).
		- perl.constructors do NOT automatically call overridden-base-class constructors
		- Perl classes do method inheritance ONLY, but NOT class-Data inheritance!! Data inheritance is left up to the class itself.  ;see perldoc-5.14.0/perlobj.html#A-Class-is-Simply-a-Package
	---! INHERITED-constructor /Inheritance.of.new.method:
		- class of derived obj:  A parent of B , and new() defined in A (not in B), then the class of $b=B->new() is still always B (and not A)!!
		  perl -lwe '{ package A; sub new{bless {}, shift;} }  ; { package B; our @ISA=qw(A); } ; { print ref (my $b = B->new()); }'  ##-> prints: B
		  see perldoc-5.14.0/perlbot.html#INHERITING-A-CONSTRUCTOR
		-!! ALWAYS use the two-arg-style of bless:   bless ($self, $class); !!
		-!! An inheritable constructor MUST use the two-parameter-form of bless() which allows blessing directly into a specified/origin-class of the Instance!!.
		-!! Inheritance: superclass-constructor will NOT be called automatically in the subclass-constructor!! must be called manually, if needed!!  see eg perldoc-5.14.0/perlbot.html#INSTANCE-VARIABLE-INHERITANCE
	        this is the same also for other methods!! see perldoc-5.14.0/perlbot.html#OBJECT-RELATIONSHIPS
			a constructor does NOT automatically call its overriden base-class-constructors!!  :see perldoc-5.14.0/perlobj.html#An-Object-is-Simply-a-Reference
	--- Blessing:
		-!! bless() operates on the final object and not on the reference to it!! so the FINAL-object knows its class-belonging, as in:
		   perl -lwe  '$a = {}; $b = $a; bless $a, BLAH; print ref($b);'  ##--> prints: BLAH  (not HASH) !! ;without blessing, it will print "HASH" !
	---! short/compact constructors:
		sub new { bless [  ], shift }   #/OR   sub new { bless { }, shift }
		sub new { my ($class, %args) = @_;  bless \%args, $class; }  #-with a full hash as arg for the new
	-! using Array instead Hash in "new" for instance.data:   my($NAME, $AGE, $PEERS) = ( 0 .. 2 );    sub new { my $self = []; $self->[$NAME] = undef; ...}  # see perldoc-5.14.0/perltoot.html#Arrays-as-Objects
	-! closures in OO.constructors see /perldoc-5.14.0/perltoot.html#Closures-as-Objects
	-! constructor can be called as Class+Object-method:   sub new { my $self= shift; my $class= ref($self) || $self;  my $self= {}; ...; bless($self, $class);}
	- sub-REF instead of obj-REF of a constructor/new.method:  see Example 14.16.   perlByExp4ed/ch14lev1sec3.htm
##________________________________________  ___________________________


#####  ==========  destructors:
	-! see perlobj  bzw.  perltoot /Class Destructors  ,  perlmod
	-!! DIFF:
		- "DESTROY" method: is the OBJECT destructor, which handles the death of each distinct object.  ;see  perlobj , /perldoc-5.14.0/perlobj.html#Destructors  
		- "END" method: is the CLASS destructor, which is executed when the package/class is unloaded bzw. the program exits.  ;see perltoot /Class Destructors  bzw. perlmod
	--- "DESTROY" method (Instance-Level-Destructor-Method):           perlobj:
		- When the last reference to an object goes away, the object is automatically destroyed.
		- "DESTROY" method is to capture control just before the object is free, to do any extra cleanup:
		- MUST be called "DESTROY" and ist called automatically+randomly by perl-garbage-collector (GC) ! see /perldoc-5.14.0/perltoot.html#Destructors
		-!! Perl passes a REF to the object under destruction as the first (and only) argument.
		    THis REF ist readonly, BUT not its underlying hash/array/object/scalar:
		    this passed reference is a read-only value, and cannot be modified by manipulating $_[0] within the destructor!
			BUT The object itself (i.e. the thingy the reference points to, namely ${$_[0]} , @{$_[0]} , %{$_[0]} etc.) is not readonly, so is not similarly constrained as its REF!!
	--- "END" method (Class-/Package-Level-Destructor-Method):     perltoot , perlmod :
		- it gets called whenever your program exits (bzw. package is unloaded), unless it execs or dies of an uncaught signal.
		- manual destructor-jobs for the WHOLE class/... (deleting files, DB.connections,...), by:    sub END {...} :
		  When the program exits, all the class destructors (END functions) are be called in the opposite order that they were loaded in (LIFO order).   :see  /perldoc-5.14.0/perltoot.html#Class-Destructors
##________________________________________  ___________________________


#####  ==========  methods , method.calls:
	---! DIFF  class.methods  <-->  instance.methods :    see perldoc-5.14.0/perlboot.html#Accessing-the-instance-data  :
		- class.methods:     first.param is the CLASS.name, so  Animal->speak   same.as  Animal::speak("Animal")  bzw.  Animal::speak($class)
		- instance.methods:  first.param is the INSTANCE.self, so  $horse1->name("p1", "p2")  same.as   Horse::name($horse1, "p1", "p2")
		- so: Whatever is on the left side of the arrow, whether a reference or a class name, is passed to the method subroutine as its first argument.
		-! in both cases, the implicit.first.param.additions occurs ONLY by using  "->"  (methed.call) , noth the "::"-package.sub.call !! see the next diff.nts!
		-! so, It's traditional to shift the first parameter into a variable named $self for instance methods and into a variable named $class for class methods.
		- covering BOTH-instance-OR-class-methods in a method:   see perldoc-5.14.0/perlboot.html#Making-a-method-work-with-either-classes-or-instances :
		    sub name { my $either = shift; ref $either ? ....instance-kramm... :  ...class-kramm...; }
	---! DIFF:    "->"  method.call   <-->   "::"  function.call     ;eg:  Animal->speak   <-->   Animal::speak()  :
		--!! perldoc-5.14.0/perltoot.html#Inheritance :
			-1 method calls get implicitly/automatically an extra argument by perl (Class.REF OR Instance.REF). But functions NOT ! so:  Person->new()   same.as  Person::new("Person")
			-2 function calls do NOT do inheritance. BUT methods do !  so:  Employee->new()  same.as  Person::new("Employee")   , if class Employee is a subclass of Person
			- So do NOT use function calls "::"  when you mean to call a method.
		--!! CLASS-param: only by method.call.syntax "->" is the first parameter of the sub, its classname, otherwise NOT!!, so:
		   Animal->speak   same.as   Animal::speak("Animal")  bzw.  Animal::speak($class), see perldoc-5.14.0/perlboot.html#Overriding-the-methods
		   so  Class->method(@args);  constructs an argument list of:   ("Class", @args)  and attempts to invoke:  Class::method("Class", @args);
		--!! method look up mechanism (in the heritance-hirarchy) works ONLY with  "->"  (methed.call) !! so not by "::"-call  :see  perldoc-5.14.0/perlboot.html#Starting-the-search-from-a-different-place
		  so Animal->speak  /OR even  $myclass->Animal::speak  /OR  $myclass->SUPER::speak  wille be looking for the speak() upwards in the class.inheritance.tree, BUT
		  BUT Animal::speak  will be looking for speak() ONLY in the package Animal and NOT int the tree!!
	--- lookup of the method.call:
		- normal.method.lookup:  just $self->method1();  (lookup in the $self-class and then upwards in @ISA-entiries ..)
		- forcing a specific method-call of the object (not bases on inheritance-search):  eg  $foo->Bar::display(23, 34);  #see perldoc-5.14.0/perlobj.html#Method-Invocation
		- parents-/inheritance-lookup:   Start looking for the method in the packages named in the current class's @ISA list: eg  $self->SUPER::display("Name", @args);
		  SUPER::speak   means: look in the current package's @ISA for a class that implements speak , and invoke the first one found.
		   !! BUT  $class->SUPER::method;  :does NOT look in the @ISA of $class unless $class happens to be the current package! see perlboot.html
	-! inheritance and method-calls: parents-class-method "m1" will NOT be called automatically from the derived-class-method "m1"!!
		so: {package A; sub m1{...}} and {package B; use parent "A"; sub m1{...}}  --> then B->m1  will NOT call A-m1 !!
		if you want it, then do in m1 of B:  {$self=shift; if ($self->can("SUPER::m1")) { $self->SUPER::m1; ...} }  #see perldoc-5.14.0/perltooc.html#More-Inheritance-Concerns
		see also:  perldoc-5.14.0/perlbot.html#OBJECT-RELATIONSHIPS
	-! ?is this method called by an instance or as ckass.metho??:  use "ref(shift)" :this  returns a string (the classname) when used on a blessed reference (on an instance), and an empty string when used on a string (like a classname).  :see perlboot
	   ref EXPR  :Returns a non-empty string if EXPR is a reference (obj/instance, the empty string otherwise (class/package).
	-! class.name no matter if called as instance- or calss-method:    sub s1{ my $obclass = shift;	my $class   = ref($obclass) || $obclass;  ...; }
	-!! debugging whole.class OR each.instance  :see perldoc-5.14.0/perltoot.html#Debugging-Methods
	- mro - Method Resolution Order  ;see perldoc mro
##________________________________________  ___________________________


#####  ==========  class-variables/-data/-members/-attributes (not instance.data/.attributes):
	- DEF:  package's eponymous hash  ==  a Hash of the package with the SAME-NAME as the package/class itself! used very ofen, see perltooc , perldoc-5.14.0/perltooc.html#The-Eponymous-Meta-Object
	-! see perltooc  +  perltoot  :
		WHOLE chapter perltooc - Tom's OO Tutorial for Class Data in Perl  : /perldoc-5.14.0/perltooc.html
		perldoc-5.14.0/perltoot.html#Accessing-Class-Data
		- accessing (private) class.data from the instance see eg  perldoc-5.14.0/perltoot.html#Autoloaded-Data-Methods  (by accessing %fields in the new() and AUTOLOAD methods )
		- for including/encapsulating of class.data into the instance/object see eg in  perldoc-5.14.0/perltoot.html#Accessing-Class-Data
	-!! DEF/DIFF:  compiling.package (non.relative.package) <-->  invoking.package (relative.package) :     see perldoc-5.14.0/perltooc.html#Inheritance-Concerns  :
		suppose:  B is subclass of A  ,with A{...; our $classVarA=...; sub m1() ...;} ;  and  $obj1 = B->new;
		then $classvarA is defined/compiled in A  and invoked/instantiated by an instance of B !
		- invoking.package/.class   for obj1->m1()  :class the object belongs to, was instantiated in, so "B" !
		- compiling.package/.class  for obj1->m1()  :class the method m1() was originally defined  in, so "A" !
		-!! the class.data $classVarA and classMethodA are always executed/evaluated in the context of "A"/compiled.package and NOT "B"/invoking.package)!!
		-!!  __PACKAGE__  always refers to the compilied.package (non.relative)!! so the package/class where __PACKAGE__ is about to be set!
		-!! ref(obj1)  returns always obj1's invoking final package/class! see code on perltooc
		-!! see code in  perldoc-5.14.0/perltooc.html#The-Eponymous-Meta-Object
	-! ??was I invoked by an instance/obj or as class.method??:     $self=shift; ref($self) ? <obj...> : <class....>;
	-!! ??by inheritance, class.data/.methods are executed in the context of the base or derived class or the instance??:
		class attributes are stored in the package into which those methods were COMPILED (so of BASE class)!!
		class methods are executing in the context of their BASE class, not in that of their derived class!
		so to access them by package-notation, do: eg  $baseClass::data1  (and NOT $derivedClass::data1)  see: perldoc-5.14.0/perltooc.html#Inheritance-Concerns
	-! accessing-class.data/package.vars by variable.based.varnames, then must temporarily disable the strict references: no strict "refs";
	-! accessing-class.data through the instance (recommended method to access class.data)  :see perldoc-5.14.0/perlbot.html#CLASS-CONTEXT-AND-THE-OBJECT
	   eg: %classdata1={aa => 11, bb => 22}; ...; sub new{ my $class=shift; my $self={}; $self->{"classdata1"}= \%classdata; ...}
	   because you are accessing/manipulating the package's symbol-table !! eg: {no strict "refs"; my $varname = $class . "::CData1"; $$varname = ... ;}
	-!! private.data.enforcing: { my $CData1; sub m1 { >...handling $CData1...>, return $CData1;}  #see perldoc-5.14.0/perltooc.html#Locking-the-Door-and-Throwing-Away-the-Key
	   /bzw. using closure (my-vars with anonymous-sub)
	- version-checking needed for your class?? then add (eg in Person):  our $VERSION = '1.1';
	  then version-checking happens by perl, if in subclass:  use Person 1.1;   #see perldoc-5.14.0/perltoot.html#UNIVERSAL:-The-Root-of-All-Objects
##________________________________________  ___________________________


#####  ==========  instance-variables/-data/-members/-attributes (not class-data/-attributes):
	- see perldoc-5.14.0/perlbot.html#INSTANCE-VARIABLES
	- usually defined in the class.constructor/new.method, as an anonymous Hash-element, eg:
	  sub new { my $class = shift; my $self  = {}; $self->{NAME} = undef; $self->{AGE} = undef; ...;  bless ($self, $class); }
	- An anonymous array or anonymous hash (inside the scope of new()/constructor) can be used to hold instance variables. 
	-! accessing class.data from the instance: using pointer/ref to the class.data inside the constructor as an Hash-element 
	   eg: class A{ my $Census="classdata1";  sub new {... $self->{"_CENSUS"} = \$Census;} ... }   :see perldoc-5.14.0/perltoot.html#Accessing-Class-Data
	- 
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  
--########### codecs-snippets-OO: ####################################

	_______:  adding new attributes/instance-data in the subclass/to derived instances: 13.5. Additional Instance Variables in Subclasses : intermediateperl-CHP-13-SECT-5.html
	{ package RaceHorse;
	  our @ISA = qw(Horse);
	  ## extend parent constructor:
	  sub named {
		my $self = shift->SUPER::named(@_);
		$self->{$_} = 0 for qw(wins places shows losses);
		$self;
	  }     ## additional instance-methods:
	  sub won { shift->{wins}++; }
	  sub placed { shift->{places}++; }
	  sub showed { shift->{shows}++; }
	  sub lost { shift->{losses}++; }
	}
	-!! BUT not absolutely perfekt/encapsulated solution!! see intermediateperl-CHP-13-SECT-5.html
	----------

	_______:  very short OO-methods without my $ref=shift ...: /intermediateperl-CHP-13-SECT-2.html
	{ package Barn;
	  sub new { bless [  ], shift }  #/OR with a full hash as arg for the new:
	  sub new { my ($class, %args) = @_; bless \%args, $class; }
	  sub add { push @{+shift}, shift }
	  sub contents { @{+shift} }
	}
	- {+XX} means XX is a funcion to be executed/replaced, not a bareword/...
	----------

	_______:  methods/subs with NAMED-params: /perlByExp4ed/ch14lev1sec2.html : Example 14.8. + .9 :  Passing parameters as a hash:
	$employee = Employee->new( "Name"=>$name, "Address"=>$address, "Extension"=>$extension, "PayCheck"=>$basepay,);
	----------
##________________________________________  ___________________________


#####  ==========  managing.instances /instance.Registries:

	_______:  Register all instances/objects centrally (as a DB) and keep a ref to them: intermediateperl-CHP-13-SECT-6.html
	our %REGISTRY;
	sub named {
	  my $class = shift;
	  my $name = shift;
	  my $self = { Name => $name, Color => $class->default_color };
	  bless $self, $class;
	  $REGISTRY{$self} = $self;  # also returns $self
	}
	-! but problems with destroying! so see chapter.13.7
	----------
##________________________________________  ___________________________


#####  ==========  instance-OR/AND-class-handling-methods:

	_______:  ??what is the class (invoking.class) of the current object, which invoked this method (class- bzw. instance-method??:
	sub xx{  my $self  = shift;  my $class = ref($self) || $self; ...}

	_______:  either-instance-OR-class-methods exclusively: /intermediateperl-CHP-12-SECT-14.html
	-- a method which expects ONLY an instance as its first parameter:
	use Carp qw(croak);
	sub instance_only {
	  ref(my $self = shift) or croak "instance variable needed";
	  ... use $self as the instance ...
	}
	-- a method which expects ONLY a CLASS as its first parameter:
	sub class_only {
	  ref(my $class = shift) and croak "class name needed";
	  ... use $class as the class ...
	}
	----------

	_______:  BOTH-instance-And-class-handling-method:   see perldoc-5.14.0/perlboot.html#Making-a-method-work-with-either-classes-or-instances :
	   sub classAndInstanceMethod {
        my $either = shift;
        ref $either ? <instance.stuff...> : <class.stuff...>;
    }
	--- more detailed  /intermediateperl-CHP-12-SECT-6.html :
	sub name {
	  my $either = shift;
	  ref $either ? $$either;     # it's an instance, return name : "an unnamed $either";   # it's a class, return generic
	}
	-- if blessed-data was a hash:  intermediateperl-CHP-12-SECT-8.html
	sub name {
	  my $either = shift;
	  ref $either ? $either->{Name} : "an unnamed $either";
	}
	----------

	_______:  ! invoker.class.name no matter if called as instance- or calss-method:
    sub s1{
	my $obclass = shift;	
	my $class   = ref($obclass) || $obclass;  ...;
	}

	_______:  ! tri-natured: function, class method, and object method  :see perldoc-5.14.0/perltooc.html#The-Eponymous-Meta-Object  :
    sub _classobj {
		my $obclass = shift || __PACKAGE__;
		my $class   = ref($obclass) || $obclass;
		no strict "refs";   # to convert sym ref to real one
		return \%$class;
    } 
##________________________________________  ___________________________


#####  ==========  class.data:
	-!! see whole manual:  perldoc-5.14.0/perltooc.html

	_______:  ! relative-/non-relative-package  (compiling-/invoking-package):    see  perldoc-5.14.0/perltooc.html#The-Eponymous-Meta-Object  :
	package Some_Class;
    use strict;
    # create class meta-object using that most perfect of names
    our %Some_Class = (   	# our() is new to perl5.6
		CData1 => "",
		CData2 => "",
    );
    ##------- this accessor is calling-package-relative:
    sub CData1 {
		my $obclass = shift;	
		my $class   = ref($obclass) || $obclass;
		no strict "refs"; 	# to access eponymous meta-object
		$class->{CData1} = shift if @_;
		return $class->{CData1};
    }
    ##------- but this accessor is not:
    sub CData2 {
		shift;			# XXX: ignore calling class/object
		no strict "refs"; 	# to access eponymous meta-object
		__PACKAGE__ -> {CData2} = shift if @_;
		return __PACKAGE__ -> {CData2};
    }
    ##------- bzw. same:
	sub CData2 {
		shift;			# XXX: ignore calling class/object
		no strict "refs"; 	# to access eponymous meta-object
		my $class = __PACKAGE__;
		$class->{CData2} = shift if @_;
		return $class->{CData2};
    }
##________________________________________  ___________________________


#####  ==========  getter+setter-methods creation variations:
-  Class::MethodMaker can be a bit much. We can also check out the lighter Class::Accessor.  : IntermediatePerl_Ore/intermediateperl-CHP-14-SECT-5.html
- dynamically (a bit nasty): AUTOLOAD : IntermediatePerl_Ore/intermediateperl-CHP-14-SECT-4.html
	to  stop the AUTOLOAD inheritance simply do:  sub AUTOLOAD;   #see perlobj

	_______:  auto.generated-setter.getter.methods:
	-- auto.generated.accessors, which can be called as function, class method, or object method:
		-!see final code.exp in:   perldoc-5.14.0/perltooc.html#The-Eponymous-Meta-Object
	--!?!? auto.generated-setter.getter.methods (by AUTOLOAD):   see exp in perldoc-5.14.0/perltoot.html#Autoloaded-Data-Methods
		kk: looks a bit buggy! does not works for non.scalaras (@peers in %fields)
		and also DESTORY and other auto-called methods must be also added to %fields!
		!! this approach was modified in perldoc-5.16 (no setter anymore + added DESTROY + and abraten!)
	--  auto.generated-setter.getter.methods-with-closures and enforced private.class.data:
		see: perldoc-5.14.0/perltooc.html#Locking-the-Door-and-Throwing-Away-the-Key :
		package Some_Class;
		{  # scope for ultra-private meta-object for class attributes
			my %ClassData = ( CData1 => "", CData2 => "",);
			for my $datum (keys %ClassData ) { 
				no strict "refs";    
				*$datum = sub {
					use strict "refs";    
					my ($self, $newvalue) = @_;
					$ClassData{$datum} = $newvalue if @_ > 1;
					return $ClassData{$datum};
		} } }

	_______:  getter-setter shorter: intermediateperl-CHP-12-SECT-12.html
	sub set_color { $_[0]->{Color} = $_[1] }

	_______:  getter-setter-BOTH-same-method: /intermediateperl-CHP-12-SECT-13.html
	 simplerer BUT really more ERROR-prone!! so NOT so recommeded!?:  see /intermediateperl-CHP-12-SECT-13.html
	- This strategy is attractive because of its simplicity, but it also has disadvantages. It complicates the actions of the getter, which is called frequently. It also makes it difficult to search through our code to find the setters of a particular parameter, which are often more important than the getters. We've been burned in the past when a setter became a getter because another function returned more parameters than expected after an upgrade.
	sub name {
        my $self = shift;
        if (@_) { $self->{NAME} = shift }
        return $self->{NAME};
    }  #see perldoc-5.14.0/perltoot.html#Constructors-and-Instance-Methods
##________________________________________  ___________________________


#####  ==========  
