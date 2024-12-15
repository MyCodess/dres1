#!/usr/bin/perl -W

use warnings;
use strict;
our $verbose; ##-ReDo  0; ##--II-:  0==no.outputs , 2==start-end-minor-printlines , 4==subproccees-data-printouts 
$verbose = 2 unless defined $verbose ;  ##-ReDo  0; ##--II-:  0==no.outputs , 2==start-end-minor-printlines , 4==subproccees-data-printouts 
if ($verbose > 1 ) { print "\n" . '.' x 20 , __PACKAGE__ . " -- called from: $0 ...........\n"; }

########## 
##--I- see perldoc-5.14.0/perlbot.html#INSTANCE-VARIABLES
#---
{
	package Foo;
	sub new {
		my $type = shift;
		my %params = @_;
		my $self = {};
		$self->{'High'} = $params{'High'};
		$self->{'Low'}  = $params{'Low'};
		bless $self, $type;
	}
}
#---
{
	package Bar;
	sub new {
		my $type = shift;
		my %params = @_;
		my $self = [];
		$self->[0] = $params{'Left'};
		$self->[1] = $params{'Right'};
		bless $self, $type;
	}
}
#---
{
	package main;
	$a = Foo->new( 'High' => 42, 'Low' => 11 );
	print "High=$a->{'High'}\n";
	print "Low=$a->{'Low'}\n";
	$b = Bar->new( 'Left' => 78, 'Right' => 40 );
	print "Left=$b->[0]\n";
	print "Right=$b->[1]\n";
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

