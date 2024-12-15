#!/usr/bin/perl -wl
##--II-- : calass data/members   :see perldoc-5.14.0/perltoot.html#Accessing-Class-Data
#	here very simple variation:
#	watch: sound-method is called Horse::sound  :so the first method sound in the object.hierarchie
#	BUT the speak-method is executed in the CONTEX of its OWN class "Animal", and NOT object-class "Horse"
#	so that is why, then  $classvar1 is talken from Animal and not Horse !!
#	!! if instance needs to access class,data ($classvar1), only throuch a access-method, not directly! here is not done yet!


use warnings;
use strict;

###########################
{ package Animal;
	our $classvar1=5;
	##-----------
	sub new{
		my $class = shift;
		my $name = shift;
		bless (\$name, $class);
	}
	##-----------
	sub name {  ##--II- works for both calss- or object-call:
		my $either = shift;
		ref $either ? $$either : "noname $either";
	}
	##-----------
	sub sound { "global-dummy-sound-sub-1" } #-- just dummy func. may not ever be executed!
	##-----------
	sub speak {
		my $self = shift;
		#my $class= ref($self);
		##--II- invoking sound() of the invoking.calls, NOT comlied.class, of the obj/$self !!:
		$self->name . " goes " .  $self->sound . " -classvar1: "  .  ++$classvar1;
	}
	#sub DESTROY{ my $self= shift; print "_____ destroy.it: " . $self->name ; }
}

{ package Horse;
	our $classvar1=23;
	our @ISA = qw(Animal);
	sub sound { "neigh". ++$classvar1 }
}

{ package Sheep;
	our @ISA = qw(Animal);
	sub sound { "baaaah" }
}

######################################
my $horse = Horse->new("horse.no.1");
print $horse->name();
print $horse->speak();
print $horse->speak();

my $horse2 = Horse->new("horse.no.2");
print $horse2->name();
print $horse2->speak();
print $horse2->speak();

