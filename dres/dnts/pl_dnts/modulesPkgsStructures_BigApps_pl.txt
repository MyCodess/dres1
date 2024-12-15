_____________ perl-BigApps, Module-/Packages-Structures and integrations in big Apps, Export, _______
-!! see nts for use_require..:   devres/0devNts/pl/pl_mods_use_req_do_eval.txt
##________________________________________  ___________________________


#####  ==========  symbol.table, package.vars and definitions:
	- current package-name:  __PACKAGE__   ;see perlmod
	- Symbol.Table for a package is stored in the hash of that name %<packageName>:: ,eg:  %main:: , or %:: for short.
	  Likewise the symbol table for a nested package  %OUTER::INNER::  bzw.  %MyModPath:: ;see perlmod
##________________________________________  ___________________________


#####  ==========  libs-inclusion by @INC/ENV/PERL5LIB/...:
	- own library precedence over those in listed in the @INC array, put in your prog:  unshift(@INC,".");
	-! new/test libs:  perl -I  at the command line, or set the PERL5LIB 
##________________________________________  ___________________________


#####  ==========  MULTIPLE.packages-in-a.Single.File:  several packages in the SAME file , and problems with loading files by "use" and "parent":
	--- "use":  packages A + B defined in one file as ab.pl, and in package B you have "use A;" :
		- problem: compilation error:   Can't locate A.pm in @INC ...
		- you do NOT need "use there" at all!! just define package A first, and then use package-A-elemnts in package B!:
		  You only need to use "use ..." to LOAD a FILE. It's really only INCIDENTLY that its argument looks like a module name.
		  If you need to interact with a package (and that's all it is: not a module or an object), you just need to have it defined before you want to use it. that is all!!
		- you can put multiple packages in a single file. Since they are already loaded, you do not need to use 'use'.
	--- "parent":  use parent -norequire
		take this, if several classes are defined in the same file and you define a classe hierarchy based on them!
		otherwise compilation errorr:  Can't locate A.pm in @INC ...
	--- scoping in  MULTI.packages-in-a.Single.File:
		- "package" keyword generate also package-scoping, even WITHOUT {...}
		  You also do not need to (but BAD style) create special scoping for the packages, as the package keyword takes care of that.A BUT:
		- my-/our-vars are file-/block-scoped!! so DO enclose each package in its {...}, if several packages in the same file!! so
		package A;  my $myA=11; our $ourA=12  ;  package B; print  $A::myA, " -- " , $A::ourA;		##-->output:  11 -- 12
		{ package A; my $myA=11; our $ourA=12; } { package B; print $myA, " -- " , $ourA; }			##-->output:  compilation errors
		{ package A; my $myA=11; our $ourA=12; } { package B; print $A::myA, " -- " , $A::ourA; }	##-->output:    -- 12 (uninitialized value $A::myA )
	--- back to main package:   .... package main; ....
##________________________________________  ___________________________


#####  ==========  Export-usage:
	-!! more debugs:  BEGIN { $Exporter::Verbose=1 }  #see perldoc-5.14.0/Exporter.html
##________________________________________  ___________________________


#####  ==========  Modules-Handling inside codes:
	- ExtUtils::Installed;  #see perlfaq3 : perldoc-5.14.0/perlfaq3.html#How-do-I-find-which-modules-are-installed-on-my-system?
		eg: use ExtUtils::Installed; my $inst    = ExtUtils::Installed->new(); my @modules = $inst->modules();
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  
