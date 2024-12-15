__________ Perl-testings : ______________________
##________________________________________  ___________________________


#####  ==========  see /docs:
	--- see perldocs/cpan:
		- qa.perl.org/
		- perldoc  Test::Tutorial - A tutorial about writing really basic tests  /CPAN
		- perldoc  Test::xxx , esp.  Test , TAP::Harness , Test::Simple , Test::More , ....
		- perldoc  TAP::*  : TAP, the Test Anything Protocol, is a simple text-based interface between testing modules in a test harness.  #see:  http://testanything.org/
		- perldoc  prove
	--- see BKs:
		-! Perl_Testing__A_Developers_Notebook_Ore_0507.chm
		- IntermediatePerl_Ore : Chapter.17+18 ...
		- Perl Hacks : Hack 53. Debug with Test Cases
##________________________________________  ___________________________


#####  ==========  Utils-testing.pl:
		--- prove:   Run tests through a TAP harness. 
			-!! prove basicallay just evaluates the OUTPUT of the script!! see exp Perl_Testing__A_Developers_Notebook_Ore_0507.chm--CH.1.3--Interpreting-test-results
			- run one test from compiled stuff:  perl -Mblib t/assert.t    #/OR  prove -v t/assert.t
			  !see  perldoc blib
			- see man prove + /perldoc-5.14.0/index-utilities.html 
			- perldoc  App::Prove  :Implements the "prove" command.
##________________________________________  ___________________________


#####  ==========  Modules/Packages/Libs-Testings & QAs:
	--- see
		- TAP::* (the Test Anything Protocol)
		- Test::Builder , Test::*  (common Test libraries)
		- Bundle::Test and also   perldoc-modules of "Test::*"
		(Michael Schwern earned the title of "Perl Test Master" for getting the Perl core completely tested)
	-! Bundle::Test  /CPAN (its modules-listing!): A set of modules for software and hardware testing using Perl
	- Test::Class - a simple way of creating classes and objects to test your code in an xUnit/JUnit style
	- Devel::Cover /CPAN.
	- Test::Inline - Embed your tests in your code, next to what is being tested
##________________________________________  ___________________________


#####  ==========  modules.testings.tips:
	- finally/at end of testing do all tests also in taint-mode , so by perl -Tw  bzw.  #!/usr/bin/perl -Tw 
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
