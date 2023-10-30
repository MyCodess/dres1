#!/usr/bin/perl -W

use warnings;
use strict;
our $verbose; ##-ReDo  0; ##--II-:  0==no.outputs , 2==start-end-minor-printlines , 4==subproccees-data-printouts 
$verbose = 2 unless defined $verbose ;  ##-ReDo  0; ##--II-:  0==no.outputs , 2==start-end-minor-printlines , 4==subproccees-data-printouts 
if ($verbose > 1 ) { print "\n" . '.' x 20 , __PACKAGE__ . " -- called from: $0 ...........\n"; }

########## next/last/continue,...in loops:
my $ii=1;
while ($ii < 10) {
	last if $ii > 5;  #--> full-jump-out-of-loop-WITHOUT-continue.block
	next if $ii > 3;  #--> next-loop.iteration+WITH.continue.block
	print "- $ii -";
} continue {          #--> do-before-each-loop.iteration
	print "--cont- $ii -\n";
	$ii++;
}

##############################


########## Tests-Debugs-Verbose: #####################################
#print "\n-------\n";
if ($verbose > 3 ) {
}
if ($verbose > 1 ) { print "\n" . ':' x 20 , __PACKAGE__ . " -- called from: $0 --END::::::\n"; }
1;
__END__
######################################################################

