#!/usr/bin/perl -wl
##--II--  see code.exp.2 in:  perldoc-5.14.0/perltooc.html#Indirect-References-to-Class-Data
#	accesssing class.data BUT with values defined in derived.class (even if the methods/... all defined in the base.class!)
#	so class.data BUT in the context of derived.class!!
#	methods are executed in the context ot the class/package, where they are defined (so compiled.class), and not context of the object/invoked.calss.
#	but here each derived class must define alse a var named as %Some_Class::<my.derived.class.name> , and then it is taken
#	see example with   %Some_Class::Derived1 = ...
#
{
package Some_Class;

use strict;
no strict 'refs';
our %Some_Class = ( CData1 => "C11", CData2 => "C12",);  ##-- CData==Class.Data as opposite to ObData==Object.Data

##----------- obj.invoking.class (original.final.class, not this compiled.class!):
sub _classobj {
	my $self  = shift;
	my $class = ref($self) || $self;
	no strict "refs";
	# get (hard) ref to eponymous meta-object
	return \%$class;
} 
##-----------
sub new {
	my $obclass  = shift;
	my $classobj = $obclass->_classobj();
	bless my $self = {   ##-- CData==Class.Data as opposite to ObData==Object.Data
		ObData1 => "Ob11",
		ObData2 => "Ob22",
		CData1  => \$classobj->{CData1},
		CData2  => \$classobj->{CData2},
	} => (ref $obclass || $obclass);
	return $self;
} 
##-----------
sub ObData1 {
	my $self = shift;
	$self->{ObData1} = shift if @_;
	return $self->{ObData1};
} 
##-----------
sub ObData2 {
	my $self = shift;
	$self->{ObData2} = shift if @_;
	return $self->{ObData2};
} 
##-----------
sub CData1 {
	my $self = shift;
	$self = $self->_classobj() unless ref $self;
	my $dataref = $self->{CData1};
	$$dataref = shift if @_;
	return $$dataref;
} 
##-----------
sub CData2 {
	my $self = shift;
	$self = $self->_classobj() unless ref $self;
	my $dataref = $self->{CData2};
	$$dataref = shift if @_;
	return $$dataref;
}
}
#################################################################
#
#######################
{
	package Derived1;
	use strict;
	use base qw(Some_Class);
	##-- class.data taken by objects os derived.class, even if the accessor.methods for these vars are defined in the parent.class:
	%Some_Class::Derived1 = ( CData1 => "Derived1.CD1", CData2 => "Derived1.CD2",);  

}
########### kk:
my $obj1=Some_Class->new();
print $obj1->ObData1;
print $obj1->ObData1("11");
print $obj1->ObData2;
print $obj1->ObData2("12");
print $obj1->CData1;
print $obj1->CData1("21");
print $obj1->CData2;
print $obj1->CData2("22");
####
print "----- derived.obj: --------";
my $obj2=Derived1->new();
print $obj2->ObData1;
print $obj2->ObData1("11");
print $obj2->ObData2;
print $obj2->ObData2("12");
print $obj2->CData1;
print $obj2->CData1("21");
print $obj2->CData2;
print $obj2->CData2("22");
####

__END__
print Some_Class->ObData1;
print Some_Class->ObData1("11");
print Some_Class->ObData2;
print Some_Class->ObData2("12");
print Some_Class->CData1;
print Some_Class->CData1("21");
print Some_Class->CData2;
print Some_Class->CData2("22");
####
