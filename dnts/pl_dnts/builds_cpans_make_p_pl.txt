__________ cpan.stuff, Make+Build modules, ...  _________________________________________

	_______:  see:
	-!! comprehensive simple intro on Wins+Lx of cpan/make/build/... : Perl_Testing__A_Developers_Notebook_Ore_0507.chm--Ch.01
	- man cpan  + cpan.org--help
	- perlmodlib  --> "Guidelines for Module Creation"
##________________________________________  ___________________________


#####  ==========  modules-building-and-implementing allg and for CPAN-Contributions:
	- see  perlmodlib  --> "Guidelines for Module Creation"
	- modules-check-script: inside : http://www.cpan.org/authors/id/P/PH/PHOENIX/ :
		/usr/lib/perl5/5.8.8/
		/usr/lib/perl5/vendor_perl/5.8.8
	- modules-implementing/writing:  man perlmodinstall  perlmodlib
##________________________________________  ___________________________


#####  ==========  Manually Make+Build+Install modules:
	-! see Perl_Testing__A_Developers_Notebook_Ore_0507.chm--Ch.01
	--- make+build-stuff. the modules either use
		- ExtUtils::MakeMaker,  so:   perl Makefile.PL;  make;  make test;  make install  #/OR:
		- Module::Build      ,  so:   perl Build.PL;    ./Build;   ./Build test;  ./Build install   #-bzw. je perl ./Build ...
	--- non-root-modules-building:
		- perl Makefile.PL PREFIX=~/perl5/lib    #-if ExtUtils::MakeMaker used.  /bzw:
		- perl Build.PL --installbase=~/perl     #-if Module::Build used
	--- testing compiled stuff:
		- perl -Mblib=dir script [args...]  ,eg: perl -Mblib t/assert.t
		  -Mblib same as "use blib;"  #see  perldoc blib
##________________________________________  ___________________________


#####  ==========  CPAN.pm usages, cpan-invokation:
	- /usr/bin/cpan basically   same.as:  perl -MCPAN -e shell   #see perlutil
	- 
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
