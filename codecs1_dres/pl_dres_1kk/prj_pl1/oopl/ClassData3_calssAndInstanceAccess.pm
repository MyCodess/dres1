#!/usr/bin/perl -lw
##--II- see: perldoc-5.14.0/perltooc.html#Indirect-References-to-Class-Data
#	class.data-handling.by.BOTH.instance.and.class, with+without package.global.vars ( {ObData1} / $CData1)
#	is more comprehensive/complex exp, with new details
#	for a simpler variation, see perltoot
#
#
package Some_Class;
use strict;
no strict 'refs';           ##- kk: due to $self-hashes
our($CData1, $CData2);      # our() is new to perl5.6

#------------------
sub new {
	my $obclass = shift;    ##- could be class OR obj.REF
	return bless my $self = {      ##-- CData==Class.Data as opposite to ObData==Object.Data
		ObData1 => "",
		ObData2 => "",
		CData1  => \$CData1,
		CData2  => \$CData2,
	} , (ref $obclass || $obclass);        ##--II- org wag "=>" instead "," between two params of bless !?!? but it worked also !!
} 

#------------------
sub ObData1 {
	my $self = shift;       ##- could be class OR obj.REF
	$self->{ObData1} = shift if @_;
	return $self->{ObData1};
} 

#------------------
sub ObData2 {
	my $self = shift;
	$self->{ObData2} = shift if @_;
	return $self->{ObData2};
} 

#------------------
sub CData1 {
	my $self = shift;
	my $dataref = ref $self ? $self->{CData1} : \$CData1;
	$$dataref = shift if @_;
	return $$dataref;
	} 

#------------------
sub CData2 {
	my $self = shift;
	my $dataref = ref $self ? $self->{CData2} : \$CData2;
	$$dataref = shift if @_;
	return $$dataref;
}

########### kk:
print Some_Class->ObData1("11");
print Some_Class->ObData1;
print Some_Class->ObData2("12");
print Some_Class->ObData2;
print Some_Class->CData1("21");
print Some_Class->CData1;
print Some_Class->CData2("22");
print Some_Class->CData2;
####
my $obj1=Some_Class->new();
print $obj1->ObData1("11");
print $obj1->ObData1;
print $obj1->ObData2("12");
print $obj1->ObData2;
print $obj1->CData1("21");
print $obj1->CData1;
print $obj1->CData2("22");
print $obj1->CData2;
####

