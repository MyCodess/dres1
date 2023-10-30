#!/usr/bin/perl -W

package Acc2;

use warnings;
use strict;
our $verbose = 2; ##-ReDo  0; ##--II-:  0==no.outputs , 2==start-end-minor-printlines , 4==subproccees-data-printouts 
our @ISA = qw(Acc);
use Acc;

if ($verbose > 1 ) { print "\n" . '.' x 20 , __PACKAGE__ . " -- called from: $0 ...........\n"; }

sub new() {
	my $class1 = shift;
	print  "\n---- MyClass.: $class1 --";
	Acc->new();
}

#print "\n-------\n";
############# Tests-Debugs-Verbose:

if ($verbose > 3 ) {
	our $acc1 = Acc2->new();
	$acc1->setdata(11, "Joe Julian", 1100);
	$acc1->getdata();
}
if ($verbose > 1 ) { print "\n" . ':' x 20 , __PACKAGE__ . " -- called from: $0 --END::::::\n"; }
1;
