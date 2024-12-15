#!/usr/bin/perl -w

package Acc;

use warnings;
use strict;
# use PL1::Utils1 qw(printhash); #-: was ok, but for practicality now outcommented.

print "\n" . '-' x 40 . "\n";

#&printhash(\%accdata);

sub new() {
	my $class1 = shift;
	my $accdata = {accno => 0 , accname => "nnnn" , accbal => 0};
	print  "\n-- MyClass.: $class1 --";
	return bless ($accdata, $class1);
}

sub new2($$$) {
	my $class1 = shift;
	my $accdata = {accno => $_[0] , accname => $_[2], accbal => $_[2]};
	print  "\n-- MyClass:: $class1 --";
	return bless ($accdata, $class1);
}

sub getdata(){
	&printhash(shift);
}

sub setdata($$$){
	my $self1 = shift;
	$self1->{accno} = $_[0];
	$self1->{accname} = $_[1];
	$self1->{accbal} = $_[2];
}

#print "\n-------\n";
print "\n" . '=' x 40 . "\n";

##################### privates: #############
######## printout hashes: from PL1/Utils1.pm , worked also ok, but now here just for practicality:
# params: $_0 == ref.to.hash
sub printhash($){
	my $h1ref = shift;
	print "\n--- Hash-Values:  \n";
	foreach my $key (sort keys %{$h1ref}) { print "\t$key => $h1ref->{$key}\n";}
	print "------------------------\n";
}
########

#############################################
1;
