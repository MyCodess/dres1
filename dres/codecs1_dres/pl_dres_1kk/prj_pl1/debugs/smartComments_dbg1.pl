##--II- Usage: 
##--    eg for debug-level = 2 :  perl '-MSmart::Comments "###-dd-" '  dbg1.pl
##--	/OR  without "...":        perl  -MSmart::Comments=###-dd-     dbg1.pl   ##see perlrun

use Smart::Comments  -ENV;   #, qw(###-d); to enable debugging, so you must set in shell:  export Smart_Comments=1

my $call   = "26, 17, 22, hut!";
###-d-   $call

my @play_calls = split /\s*,\s*/, $call;
print $play_calls[1]  == 17 ? "__OK\n" : "__Error\n";
###-d-  @play_calls


my $v1=11;
our @a1=(10..14);
our %h1;
for my $ii (0..9)  { $h1{$ii} = $ii+100; }

###  =========== NO-debug-line!! may NOT be printed by debugging!!

###-d-  ======= a few smart.comments debugging examples ============
###-d-   dbg-1 <here> -- <time> : $v1
###-d-   $play_calls[1] is :   $play_calls[1]
###-dd-   dbg-level-2 : @a1
###-dd-   dbg-level-2 : %h1
###-ddd-  dbg-level-3 : @a1
###-ddd-  dbg-level-3 : %h1
###    :    %h1
#####===================================================
#
###-d-  a few assertions/requirments:
###-d- assert: $play_calls[1] == 17
###-d-     ensure:  $h1{2} == 102
#####===================================================
#
###-d- a few verify/checks:
###-d- verify:  $h1{2} == 103
###-d- check:   $h1{2} == 102
#####===================================================
#
###-d-  a progressing bar in a for-loop:
for my $ii (@a1) {
	###-ddd-  Evaluating...     done
	print "$ii -- ";
}
############### just end of all ! NO debug-line!
print "\n___________ END of ". __PACKAGE__ . "__________\n\n";
