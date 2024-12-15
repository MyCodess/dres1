#!/usr/bin/perl -W

use warnings;
use strict;
our $verbose; ##-ReDo  0; ##--II-:  0==no.outputs , 2==start-end-minor-printlines , 4==subproccees-data-printouts 
$verbose = 2 unless defined $verbose ;  ##-ReDo  0; ##--II-:  0==no.outputs , 2==start-end-minor-printlines , 4==subproccees-data-printouts 
if ($verbose > 1 ) { print "\n" . '.' x 20 , __PACKAGE__ . " -- called from: $0 ...........\n"; }

########## 
###--I-	see  perldoc-5.14.0/perlbot.html#INSTANCE-VARIABLE-INHERITANCE
#---
{
	package Bar;
	sub new {
		my $type = shift;
		my $self = {};
		$self->{'buz'} = 42;
		bless $self, $type;
	}
}
#---
{
	package Foo;
	@ISA = qw( Bar );
	sub new {
		my $type = shift;
		my $self = Bar->new;
		$self->{'biz'} = 11;
		bless $self, $type;
	}
}
#---
{
	package main;
	$a = Foo->new;
	print "buz = ", $a->{'buz'}, "\n";
	print "biz = ", $a->{'biz'}, "\n";
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

