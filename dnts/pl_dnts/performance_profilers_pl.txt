_________ performance-checking, bottelnecks, profilers, ... ________________

	_______:  see:
	- perlfaq3:  Programming Perl--chapter20  +  Mastering Perl--chapter5  in: perldoc-5.14.0/perlfaq3.html#How-do-I-profile-my-Perl-programs?

	_______:  2check:
	perl -d:DProf program.pl
	dprofpp - display perl profile data
	Devel::DProf
	Devel::NYTProf

	_______:  regexp-performance-hints:
	-!! $`, $&, and $´ are tempting, but dangerous. Their very presence anywhere in a program slows down every pattern match because the engine must populate these variables for every match. This is true even if you use one of these variables only once, or, for that matter, if you never use them at all, only mention them. Using $& is no longer so expensive as the other two.  :perl-cookbook.chm--ch.6
	    instead use the variables @- and @+ for matched substrings ... !
