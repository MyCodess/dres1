__________ prel.REFerences/pointers to vars/subs/... ________________________
- see perlref , perlreftut , ..
##________________________________________  ___________________________


#####  ==========  mnemonics/basics:
	-  "+{"  bzw.  "{;"  :The leading +{ and {; always serve to disambiguate the expression to mean either the HASH reference, or the BLOCK. see perlref
##________________________________________  ___________________________


#####  ==========  dereferencing:
	-!! diff: by dereferencing 
		$$hashref{"KEY"}  same-as   ${$hashref}{"KEY"}  same-as   $hashref->{"KEY"}  bzw. $arrayref->[0] ,but
		BUT NOT:   ${$hashref{"KEY"}}  ,and NOT:  ${$hashref->{"KEY"}}
		-!! The dereference of the scalar variable happens BEFORE it does any key lookups in eg $arrayref[0] or $hashref{"KEY"} !! see code-exp in section 2 of perldoc-5.14.0/perlref.html#Using-References
	- two different REFs are pointing to the same location/object/var?:    if ($ref1 == $ref2) { ... } # cheap numeric compare of references 
	- "use strict" and deferencing and ${+...}-syntax,... :see perldoc-5.14.0/perlref.html#Not-so-symbolic-references
	-! hash-keys-based.on-REFs see WARNING in r/perldoc-5.14.0/perlref.html#WARNING
##________________________________________  ___________________________


#####  ==========  subroutines.REFs:
	-! reference to an anonymous subroutine can be created by using sub without a subname:  $coderef = sub { print "Boink!\n" };
	   !! Note the semicolon at the END!!  see perlref
	- dereferencing sub-refs:  &$coderef(1,2,3);  same-as  &{$coderef}(1,2,3);  same-as   $coderef->(1,2,3);  # Subroutine call /dereferencing
	-! calling subs/operations inside a print-statement (with innner interpolation):    see explanation in: perldoc-5.14.0/perlref.html#Using-References
		print "My sub returned @{[mysub(1,2,3)]} that time.\n";
		print "That yields @{[$n + 5]} sum total.\n";
##________________________________________  ___________________________


#####  ==========  closures:
	--! see  
		-perlref  +  perlByExp4ed/ch14lev1sec3.html
		-! OO.closures see /perldoc-5.14.0/perltoot.html#Closures-as-Objects
		-! OO.accessor.closures  see  perldoc-5.14.0/perltooc.html#Locking-the-Door-and-Throwing-Away-the-Key
	-! works ONLY for lexical-vars, so for "my"-vars, AND only in anonymous-subs, but NOT in named-subs !! see perlref
	- DEF: an anonymous function with access to the lexical variables visible when that function was compiled, creates a closure.
		- It retains access to those variables even though it doesn't get run until later.  see perldoc-5.14.0/perlref.html#Function-Templates
		- Anonymous subroutines get to capture each time you execute the sub operator, as they are created on the fly.
		- Glossary: Closure is An anonymous subroutine that, when a reference to it is generated at run time, keeps track of the identities of externally visible lexical variables even after those lexical variables have supposedly gone out of scope.  see perldoc-5.14.0/perlglossary.html
##________________________________________  ___________________________


#####  ==========  symbolic.REFs (* typeglob):   see perlref
	-!! ONLY "our"-vars visible to sym.REFs, NOT "my"-vars!! sym.REFs check symbol-tables of packages for names! :
	  Only package variables (globals, even if localized) are visible to symbolic references.
	  Lexical variables (declared with my()) aren't in a symbol table, and thus are invisible to this mechanism.  see perlref
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  
