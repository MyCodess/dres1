#!/usr/bin/perl -w
##--II- perldoc-5.14.0/perltoot.html#Inheritance
#
##--II- see notes in Person.pm
#	call eg, debug all classes:     pldbg=5  Employee.pm   /OR 
#	call eg, debug class Person: :  perl -e '$Person::dbg=1 ; $Employee::dbg=1 ; do "Employee.pm" or die $! , $@;'


package Employee;

use warnings;
use strict;
use Person;
our @ISA = ("Person");
our $dbg=$ENV{"pldbg"} unless defined $dbg ;

sub salary {
	my $self = shift;
	if (@_) { $self->{SALARY} = shift }
	return $self->{SALARY};
}

sub id_number {
	my $self = shift;
	if (@_) { $self->{ID} = shift }
	return $self->{ID};
}

sub start_date {
	my $self = shift;
	if (@_) { $self->{START_DATE} = shift }
	return $self->{START_DATE};
}

############### kk:
if ($dbg) {&test1();}  ##--II- actually should depend on a test.flag, but here just as example for debugging mechanism!
sub test1(){
	my $myclass = __PACKAGE__ ;
	my  $_objname;
	no strict 'refs';
	for (my $ii=1; $ii <6 ; $ii++){
		$_objname= "obj" . $ii;
		${$_objname} = ${myclass}->new();
		$$_objname->name("name$ii"); $$_objname->age($ii +10); $$_objname->peers(qw(p1 p2 p3)); $$_objname->salary($ii * 1000); $$_objname->id_number($ii + 100);
		local $,=" -- "; print  "__ $_objname " , __PACKAGE__ , $$_objname->name , $$_objname->age , $$_objname->peers ,  $$_objname->population , $$_objname->salary , $$_objname->id_number . "\n";
	}
}
1;
