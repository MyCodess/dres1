__________ StyleGuide-nts: Coding-Styles, Programming-Tips, Namings, ...: _________________________--
- see:  perlstyle , perlmodlib:"Guidelines for Module Creation"
##________________________________________  ___________________________


#####  ==========  Utils, Modules, ..:
	-!! perltidy (add to your system!): http://perltidy.sourceforge.net
##________________________________________  ___________________________


#####  ==========  styling.rules:
	-! start every program like this:  (perldoc-5.14.0/perldsc.html):
		#!/usr/bin/perl -w
		use strict;
	-! insert a line like this, at the start of your script:  $|=1;  #-flush right away and after every write or print  :perldoc-5.14.0/perldebtut.html : OUTPUT TIPS
		- Various useful techniques for the redirection of STDOUT and STDERR filehandles are explained in perlopentut and perlfaq8.
	-! UPPERCASE.function.names : automatically invoked by perl!! :
	   Perl on occasion uses purely UPPERCASE function names as a convention to indicate that the function will be automatically called by Perl in some way, eg "DESTROY".
	   Others that are called implicitly include BEGIN, END, AUTOLOAD, plus all methods used by tied objects, described in perltie.
	   see: /perldoc-5.14.0/perltoot.html#Destructors
##________________________________________  ___________________________


#####  ==========  addies,...
	--- OOs.styling:
		- class-attribs-  <-->  instance-attribs-naming diffs, eg: capital for class attributes  <--> small for instance attributes :
			our %Vermin = ( PopCount => 0,		# capital for class attributes
			color    => "beige",    # small for instance attributes	);   #see /perldoc-5.14.0/perltooc.html#Translucency-Revisited
