#!/usr/bin/perl -w

use warnings;
use strict;
use Data::Dumper;

print "\n" . '-' x 40 . "\n";

my @a1 = 1..5;
print Dumper \@a1;
print "\n-- $a1[0]-----\n";
#print "\n-------\n";
#
my @a2 ;
print "enter new array elements: ";
while (<>){
	print "\n- $_ -\n";
	push (@a2, [ split ]); 
}
print Dumper \@a2;

print "\n" . '=' x 40 . "\n";
