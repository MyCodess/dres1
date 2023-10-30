__________ perldata : hashs, arrays, sonstructs,... ___________________
- see  perldata  perldsc perllol , perlref
##________________________________________  ___________________________


#####  ==========  complex.data-access.syntax examples /dsc/AoA/HoH/LoL/..:  array.of.arrays/ hash.of.hashes/ array.of.hashes/ hash.of.arrays/ ....:
	- see perllol , perldsc , perlperf
	- for "Operator Precedence" see also perlop !
	- all exp from  perldsc and perllol
	---!! precedences in syntax:
		- $aref->[2][2]	same.as  $$aref[2][2]  because "$"-prefix binds more then "[]"-postfix:
		  prefix dereferencers ( $ @ * % & ) bind more tightly than the postfix subscripting brackets or braces! :see perldoc-5.14.0/perldsc.html#CAVEAT-ON-PRECEDENCE
		- $$aref[$i] same.as ${$aref}[$i] :first does the dereferencing of $aref, making it take $aref as a reference to an array (say @AoA), and then dereference that, and finally tell you the i'th value of the array pointed to by $AoA.
	--- ALL compare (perldsc):
		- $array[7][12]				# array of arrays
		- $array[7]{string}			# array of hashes
		- $hash{string}[7]			# hash of arrays
		- $hash{string}{'another string'}	# hash of hashes
	--- array.of.arrays syntax: perllol
		- @AoA = ( [ "fred", "barney" ], [ "george", "jane", "elroy" ], [ "homer", "marge", "bart" ],);
		- $ref_to_AoA = [ [ "aaaa", "bbbb" ], [ 1,2,3],];   /OR pointer  $ref_to_AoA = \@AoA   ##--II- watch [..]-syntax and NOT (....) as above!!
		- $AoA[2][2]   short.for    $AoA[2]->[2]
		- $ref_to_AoA->[2][2]  short.for  $ref_to_AoA->[2]->[2]
		  !!BUT:  $ref_to_AoA[2][2]  will be lokking in @ref_to_AoA for [2][2]-element!!
		  !! so DIFF:   $ref_to_AoA->[2][2]   (with.dereferencing)  <-->   $ref_to_AoA[2][2]  (no.dereferencing)  !!
	--- array.of.hashes sytax:
		- hash-element of an array.of.hashes:    $AoH[0]{pet} = "dino";
		-! print.whole.AoH:   for $href ( @AoH ) { for $role ( keys %$href ) { print "$role=$href->{$role} "; } }
	--- hash.of.hashes sytax:
		-! %h3 =(%h1, name => 111, %h2, name2 => 222);  is OK! %h1 and %h2 elements will be COPIED fully into %h3 !!
		-! print.whole.HoH:  foreach $family ( keys %HoH ) { for $role ( keys %{ $HoH{$family} } ) { print "$role=$HoH{$family}{$role} "; } }
	--- hash.of.arrays sytax:
		- $HoA{$who} = [ @fields ];  #hash.element pointing to a copy oa @fields
		- push @{ $HoA{"flintstones"} }, "wilma", "betty";    # append new elements to the array pointed by the hash.element $HoA{"flintstones"}
		- ALL.array.elements in %HoA:   foreach $family ( keys %HoA ) { print "$family:  @{ $HoA{$family} }\n" }
	--- slices syntax:     perldoc-5.14.0/perllol.html#Slices
		- @part = @{ $AoA[4] } [ 7..12 ];
	--- printouts/dumping of complex-data-structures packages...:
		- Dumpvalue - provides screen dump of Perl data
		- Data::Dumper - stringified perl data structures, suitable for both printing and "eval"
		- YAML module (serialization)
		- Dumpvalue - provides screen dump of Perl data.
##________________________________________  ___________________________


#####  ==========  REFs of lists:
	-!! see   perldoc-5.14.0/perlreftut.html#Making-References
	--!!! diff: "(...)"  <-->  "[...]"  <-->  "{...}"  !!!:
		- (...)  : LIST-definition: defines/returns a LIST, so defining Array/Hash, eg:   @a=("a", "d", "f");  %h=("Newton" => "Isaac", "Einstein" => "Albert");
		- [...]  : Array-Ref : defines a new, anonymous array, and returns a reference(scalar) to that array. eg: $aref = [ 1, "foo", undef, 13 ];  # $aref now holds a reference to an array
		- {...}  : Hash-Ref  : defines a new, anonymous hash, and returns a reference to that hash. eg:  $href = { APR => 4, AUG => 8 }; # $href now holds a reference to a has
	--! so:
		[] : you get a new, empty anonymous array.
		{} : you get a new, empty anonymous hash.
		[1, 2, 3] makes an anonymous array containing (1, 2, 3) , and returns you a reference to that array.
		using an array-reference enclosed in {}  is same as using the array-name. so array-/hash-NAME is same as {$reference}, so: 
		@{$aref}  same as:  @array  #vorausgesetzt  $aref  pointer to @array
		$aref = [ 1, 2, 3 ];    same as:   @array = (1, 2, 3); $aref = \@array;
		keys %h	  same as:  keys %{$href}
		$a[3]     same as:  ${$aref}[3]      same as:  $aref->[3]
		$h{'red'} same as:  ${$href}{'red'}  same as:  $href->{red}
		to get the entire array from the REF:  @{$aref} without any index.  "@" tells Perl to get the entire array.
		$u = @h{"first", "second"};  :think of it like this: The type of bracket (square or curly) governs whether it's an array or a hash being looked at. On the other hand, the leading symbol ('$' or '@') on the array or hash indicates whether you are getting back a singular value (a scalar) or a plural one (a list). :see perldoc-5.14.0/perldata.html#List-value-constructors
		var{'a','b'} : A slice of %var; same as ($var{'a'},$var{'b'}).
		-  you can omit the curly brackets whenever the thing inside them is an atomic scalar variable like $aref . For example, @$aref is the same as @{$aref} , and $$aref[1] is the same as ${$aref}[1]
	-- copying lists bzw. lists-REFs:
		- only-REFs-copying:   $aref1 = \@a1  bzw. $aref2 = $aref1;  :not-copying-whole-array, but only its address/pointer
		- physically copying array (independent of each other):  $aref2 = [@{$aref1}];    # [...] builds a NEW anonymous Array, due to @, and returns a pointer to it!
		- physically copying hash  (independent of each other):  $href2 = {%{$href1}};    # {...} builds a NEW anonymous Hash, due to %, and returns a pointer to it!
##________________________________________  ___________________________


#####  ==========  Arrays:
	-!! diff "(...)"   array/list   <-->   "[...]"  array.REF :
		- empty-new-array:         @a1    = ();
		- empty-new-array.REF:     $a1ref = [];   ##- array-constructor / new(array)
		- new-array:               @a1    = ("aaa", 2, "bbb");
		- empty-new-array.REF:     $a1ref = ["aaa", 2, "bbb"];
		- empty-NEW-array.REF:     $a1ref = [@a1];  (@a1 was copied to a NEW memory area and a pointer to it was returned! independent of @a1 !)
		-!! "[]" is the array constructor (new())  ,and  "{}" is the hash constructor: they ALWAYS return absolutely NEW array/hash elements!!
		-! when you assign something in square brackets "[...]", you know for sure it's always a brand NEW reference with a NEW-COPY of the data. perldoc-5.14.0/perldsc.html#COMMON-MISTAKES
	-!! DIFF:   $#a1   <-->    scalar(@a1)  bzw. @a1 in a scalar-context:
	   - $#a1         : last-index of @a1 (one less than its real lenght! a1-index starts by 0)
	   - scalar(@a1)  : real-lenght of @1 (== $#a1 + 1); !prefered/best way for getting @a1-length !!
	   - $a1 in-a-scalar-context  same as scalar(@a1) ,also a1-real-lenght
	   -!! @#a1 shows only the current-last-index of @a1 ,so NOT its lenght!! then @a1-length is @#a1 + 1  (array-index starts by 0)!
	     so it is ALWAYS TRUE:  scalar(@whatever) == $#whatever + 1 ; (in perl-pre-5: $#whatever - $[ + 1;)  :see perldoc-5.14.0/perldata.html#Scalar-values
	-!! copy physically arrays:
		- see sommon.mistakes in  /perldoc-5.14.0/perldsc.html#COMMON-MISTAKES
		- quick.tests ca.:  perl -lwe 'my @a1=(11..15); @a2=@a1; $a1[2]="aa"; print "@a1"; print "@a2";'
		- copy:    @a2 = @a1   bzw.  @a2 = (@a1)  : copies physically, so @a1 and @a2 two different array with similar elements
		- copy:    $v1 = [@a1];   : copies @a1 physically to a NEW anonymous array and returns a pointer to it "[...]". so two independent arrays with similar elements
		- no.copy  @a2 = \@a1  : only pointer, so same arrays
	-!! printout an array with each element in a line: 
		-!!DIFF:   $,  $OUTPUT_FIELD_SEPARATOR    <-->   $\  $OUTPUT_RECORD_SEPARATOR   <-->   $"  $LIST_SEPARATOR   --> see pl_vars.nts
		- $, =  "--";  print "@a1" ;    ##-!! for arrays/lists also works $" the same. but $, works for any kind of fields, including lists.
		- print map { "[$_] , " } @a1; 
		- while (my ($x, $y)= each @a1 ) {print "a[$x] : $y";}
		- use Data::Dumper;  print Dumper \@a1;   /bzw. print Data::Dumper::Dumper \@a1;
		- YAML module (serialization)
	-!! index-of-array-setting bigger>@#a1  bzw. less<@#a1 ?? all inbetween-elements will be automatically hinzugefügt (but undefined) bzw. truncated and no acssess any more possible!!!:
	   !! Assigning to $#days actually changes the length of the array. Shortening an array this way destroys intervening values. Lengthening an array that was previously shortened does not recover values that were in those elements.  :/perldoc-5.14.0/perldata.html#Scalar-values
	-!! unset/null-setting/truncate an array down to nothing by assigning the null list () to it:  @whatever = ();  bzw. is same as:   $#whatever = -1;  :perldoc-5.14.0/perldata.html#Scalar-values
	-! foreach (@array[ 4 .. 10 ])     { s/peter/paul/ }   ;see perldata
	-!! by list-assignments:   perldoc-5.14.0/perldata.html#List-value-constructors  :
	   ONLY The FINAL/LAST element of a list assignment may be an array or a hash:
	   ($a, $b, @rest) = split; /OR   my($a, $b, %rest) = @_;
	   You can actually put an array or hash anywhere in the list, but the first one in the list will soak up all the values, and anything after it will become undefined. This may be useful in a my() or local().
	-  array.pointer.inside.a.hash  :  %h1 :  $h1{a1ref} = [ v1, v2, v3 ]   then  @{$h1->{a1ref}} returns the array
##________________________________________  ___________________________


#####  ==========  Hashes:
	- see LearningPerl_Ore_5ed_0806.pdf--Ch.06
	- DEF:  "=>"  and  ","   (are almost the same):
		"=>"  operator is a synonym for the comma except that it causes its left operand to be interpreted as a string ... #see  perldoc-5.14.0/perlop.html#Comma-Operator
		almost the same:  The => operator is mostly just a more visually distinctive synonym for a comma, but it also arranges for its left-hand operand to be interpreted as a string if it's a bareword that would be a legal simple identifier. => doesn't quote compound identifiers, that contain double colons.  ;see perldoc-5.14.0/perldata.html#List-value-constructors
		so  %map = ('red', 0x00f, 'blue', 0x0f0, 'green', 0xf00);   same.as:  %map = ( red   => 0x00f, blue  => 0x0f0, green => 0xf00,);
	-! DIFF:  (...)  (list.notation)  <-->   {...}  (new.hash.constructor)
		"{}" : is the hash-constructor (new(hash)) and returns always a pointer to a NEW generated hash!! so
		%h1 = (aa=>11, bb=>22, ...)  BUT:   $h1ref = {aa=>11, bb=>22, ...}
	- copy-hash physically:  %h2 = %h1  ca.same.as  %h2 = (%h1) ; (two independent hashes with similar elements) #--II-: much work!! see LearningPerl_Ore_5ed_0806.pdf--Ch.06
	- referencing-hash (new name): my $h1ref= \%h1;  #-derefencing:   print sort keys %$h1ref;  #bzw. print  $$h1ref{9};
	- hash-in-scalar-context: retuns true/false: If you evaluate a hash in scalar context, it returns false if the hash is empty. If there are any key/value pairs, it returns true; more precisely, the value returned is a string consisting of the number of used buckets and the number of allocated buckets, separated by a slash.  :see /perldoc-5.14.0/perldata.html#Scalar-values
	-! pre-allocating/reserving/setting a hash:    keys(%users) = 1000;  # allocate 1024 buckets : You can preallocate space for a hash by assigning to the keys() function. This rounds up the allocated buckets to the next power of two:  :see perldata.html#Scalar-values
	- array-to-hash: %some_hash = ("foo", 35, "bar", "hello", "key3", "value3");
	- hash-to-array back again /unwinding hash: @any_array = %some_hash;  #-II: random order!!
	- hash-as-boolean:
		- if (%hash1) { ..}  : #-true if %hash1 NOT empty!
		- if ($books{$someone}) {print "$someone has at least one book checked out.\n"; }
	- printout the hash:
		- while ( ($key, $value) = each %hash ) {print "$key => $value\n"; }
		- foreach $key (sort keys %hash) { print "$key => $hash{$key}\n"; }
	-!! exists function for hashes:
		key-exist??:  if (exists $books{"dino"}) { ...}
		!!exists returns true even if the hash-element is undefined/never.initialised!!
		!! A hash or array element can be true only if it's defined and defined only if it exists, but the reverse doesn't necessarily hold true. !!  see perldoc -f exists
	- delete $books{$person};  # Revoke the library card for $person
	-! foreach (@hash{qw[key1 key2]})  { s/peter/paul/ }   ;see perldata
##________________________________________  ___________________________


#####  ==========  vars/var-scopes/my,local,our/...:  perldoc-5.14.0/perlsub.html
	-  our : package-scoped global vars
	-  my  : file-scoped lexical vars
	-! local:  see perlsub:
		In general, you wanted "my" /should be using "my" instead of "local". in perl "local" is NOT defining local vars, but only:
		"local" just gives a temporary values to an already defined GLOBAL/package-variable.  It does not create a local/new variable!!
		after leaving the current block (containing local var), the var has got again its original value, before being "local"ized!!
	--- my <--> our <--> local :
	type:	in.sub:		in.eval:		
	my		NO(YES ONLY if both in same scope!!)		YES
	our		YES
	local
	--- my:  perldoc-5.14.0/perlsub.html#Private-Variables-via-my():
		- lexically confined to the enclosing BLOCK bzw. containing FILE-SCOPE!
		- totally hidden from the outside world, including any called subroutines. BUT not if both my AND sub are in the same scope (eg same file-/module-scope) !! ;see refs
		- no-package-assignment!!: Variables declared with my are not part of any package and are therefore never fully qualified with the package name. So:   my $pack::var; # ERROR!  Illegal syntax
		   also a dynamic variable (also known as package or global variables) are still accessible using the fully qualified :: notation even while a lexical of the same name is also visible.
		-! Accessibility of my-variables is based uniquely on the static file scope!! not neccesserily package-scope (except if in the same file, tha packe is enclosed in {...} )   ;see  perldoc-5.14.0/perltooc.html#File-Scoped-Lexicals
		-! You can't use file-scoped lexicals (my-vars) in conjunction with the SelfLoader or the AutoLoader, because they alter the lexical scope in which the module's methods wind up getting compiled.  :see /perldoc-5.14.0/perltooc.html#Translucency-Revisited
	---!! varnames.of.vars-syntax , varnames.bases.on.other.var.values:
		-! see also examples in  perldoc-5.14.0/perlref.html#Using-References  +
			devres/codesColl_devres_kk/perlsColl_devres_kk/prj_pl1/dsc/varnamesVars.pl
		-!!! works ONLY for "our".vars, NOT for my.vars!! because perl looks for the final.varname in package.symbol.table, where my.vars will NOT be found!!
		print ${$animal . "::speak"}; #so if $animal="Horse" , then it prints the value of $Horse::speak
		invoking a sub, based on a var.value:  &{$animal."::speak"}; #will invokes &Horse::speak()
		- varname.based.on.vars:  ${$class . "::var11"}  instead of $MyClass::var1
		- a hash-initiation with the same NAME as its class/package after a class.method.call:
			sub new() { my $self = shift;  %$self = (name => "nn", ....,); ...}
		- 
##________________________________________  ___________________________


#####  ==========  Data-Tranforming, Text-/Strings-Converting/Parsing/Manipulating/readin...; reading csv/tsv/...; Fixed.Width.Data.files, ... :
	---! pack() and unpack():
		- see  perldoc -f pack  + perlpacktut +  perldoc-5.14.0/perlfaq5.html#How-can-I-manipulate-fixed-record-length-files? +
		- transforming data according to a user-defined template; Fixed.Width.Datafiles/.strings-handling,
	- 
##________________________________________  ___________________________


#####  ==========  
