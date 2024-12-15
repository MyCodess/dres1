#!/usr/bin/perl -wl
##--II-	kk: my very simple exp SingleTon! (can be completed)
#	the manual.code was too much?? in perldoc-5.14.0/perltooc.html#Monadic-Classes !?
#

{
	package Singleton1;
	use strict;
	our %st1=(name=>"n1", birthday=>time(),  stars=>0,);

	sub new(){
		my $self=shift;
		bless \%st1, $self;
	}
}

print our $obj1=Singleton1->new();
print our $obj2=Singleton1->new();
print our $obj3=Singleton1->new();
print "---------------------------------------------------";
foreach my $obj (qw(obj1 obj2 obj3)) {print "--- $obj"; foreach my $key (sort keys %${$obj}) { print "\t $$obj->{$key}";}}
$obj1->{name}="n222";
print "---------------------------------------------------";
foreach my $obj (qw(obj1 obj2 obj3)) {print "--- $obj"; foreach my $key (sort keys %${$obj}) { print "\t $$obj->{$key}";}}
$obj1->{name}="n333";
print "---------------------------------------------------";
foreach my $obj (qw(obj1 obj2 obj3)) {print "--- $obj"; foreach my $key (sort keys %${$obj}) { print "\t $$obj->{$key}";}}

