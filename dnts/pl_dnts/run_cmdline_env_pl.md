__________ perlrun, perl.cmdline.call, perl <params>, ... _____________________
##________________________________________  ___________________________


#####  ==========  run perl cmdline:
    -! perl.shell.simulation /quick-interactive-trying of onliners...:   perl -de 42  -->then just enter any perl stuff and try quick onliners...
        -! also TAB works there!! so in debug-prompt, eg:  DB<XX> print %main::<TAB>  ---> shows symbol.table.keys
	--- perl -n / -p:
		-!! after-loop-codes (closing the "-n"-loop, eg for codes after the loop), eg:  count the lines in a file:  perl -lne '} print $.; {'  t1.txt
		  because -n is basically: "while (<>) { <your-cmdline-codes> }" , so that is why thy fancy brakets in the tip above,to close the loop!
		-! put changes to @ARGV in a BEGIN{} block, If you're using the -n or -p command-line options
##________________________________________  ___________________________


#####  ==========  System-Env for perl: Modules installed, @INC-status,..
	--- Modules.on.System / @INC:
		-!! cpan -l  :  listing of all modules already installed on my system
		- printout INC-entries (see quickies.nts):   alias plincprint='perl -le "print for @INC ;" '
##________________________________________  ___________________________


#####  ==========  pre.settings by invoking scripts:
	- pre.setting of some vars, beofor the real execution:      perl -e 'BEGIN {$PL1::Utils1::verbose=5;} ; do "t1.pl" or die $! , $@;'
	- pre.using of some modules (not coded in your t1.pl) with    pre.settings:    perl -e 'BEGIN {$PL1::Utils1::verbose=5;} ; use PL1::Utils1; do "t1.pl" or die $! , $@;'
	- pre.using of some modules (not coded in your t1.pl) without pre.settings:    perl -MPL1::Utils1  t1.pl
##________________________________________  ___________________________


#####  ==========  Diagnostics, Error.Messages, ...:
	- see perlfaq3
	- splain:  myapp.pl 2> diag.out ;   splain [-v] [-p] diag.out ...  #see man splain
	- perldoc  perldiag
	- use diagnostics;
