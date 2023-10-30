#!/usr/bin/perl -wl
##--II-	Singleton-/Monadic-Classes  in:  perldoc-5.14.0/perltooc.html#Monadic-Classes
#	
#
{
	package Cosmos;
	use strict;
	no strict 'refs';
	our %Cosmos = ();

##-------- accessor method for "name" attribute
	sub name {
		my $self = shift;
		$self->{name} = shift if @_;
		return $self->{name};
	}

##-------- read-only accessor method for "birthday" attribute
	sub birthday {
		my $self = shift;
		die "can't reset birthday" if @_;  # XXX: croak() is better
		return $self->{birthday};
	}

##-------- accessor method for "stars" attribute
	sub stars {
		my $self = shift;
		$self->{stars} = shift if @_;
		return $self->{stars};
	}

##-------- oh my - one of our stars just went out!
	sub supernova {
		my $self = shift;
		my $count = $self->stars();
		$self->stars($count - 1) if $count > 0;
	}

##--------- constructor/initializer method - fix by reboot
	sub bigbang { 
		my $self = shift;
		%$self = (
			name  	 => "the world according to tchrist",
			birthday 	 => time(),
			stars 	 => 0,
		);
		return $self;	    # yes, it's probably a class.  SURPRISE!
	}

# After the class is compiled, but before any use or require 
# returns, we start off the universe with a bang.  
	__PACKAGE__ -> bigbang();

	1;
}

################## test:
print Cosmos->name("nn22");
print Cosmos->birthday();
Cosmos -> bigbang();
print Cosmos->name();
