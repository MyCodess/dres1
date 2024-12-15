#!/usr/bin/perl -W

use warnings;
use strict;
our $verbose; ##-ReDo  0; ##--II-:  0==no.outputs , 2==start-end-minor-printlines , 4==subproccees-data-printouts 
$verbose = 2 unless defined $verbose ;  ##-ReDo  0; ##--II-:  0==no.outputs , 2==start-end-minor-printlines , 4==subproccees-data-printouts 
if ($verbose > 1 ) { print "\n" . '.' x 20 , __PACKAGE__ . " -- called from: $0 ...........\n"; }

########## 
##--I- see perldoc-5.14.0/perlbot.html#CLASS-CONTEXT-AND-THE-OBJECT
#	notice here also the subclassing!
#---
{
	package Bar;
	our %fizzle = ( 'Password' => 'XYZZY' );
	sub new {
		my $type = shift;
		my $self = {};
		$self->{'fizzle'} = \%fizzle;
		bless $self, $type;
	}
	sub enter {
		my $self = shift;
		# Don't try to guess if we should use %Bar::fizzle
		# or %Foo::fizzle.  The object already knows which
		# we should use, so just ask it.
		#
		my $fizzle = $self->{'fizzle'};
		print "The word is ", $fizzle->{'Password'}, "\n";
	}
}
#---
{
	package Foo;
	our @ISA = qw( Bar );
	our %fizzle = ( 'Password' => 'Rumple' );
	sub new {
		my $type = shift;
		my $self = Bar->new;
		$self->{'fizzle'} = \%fizzle;  ##-- here reset it to new subclass-data!
		bless $self, $type;
	}
}
#---
{
	package main;
	my $a = Bar->new;
	my $b = Foo->new;
	$a->enter;
	$b->enter;
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

