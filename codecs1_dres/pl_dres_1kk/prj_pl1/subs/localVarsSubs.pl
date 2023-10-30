#!/usr/bin/perl -w

use warnings;
use strict;
#use Data::Dumper;

print "\n" . '-' x 40 . "\n";

our @a1 = (0..4);
our @a2 = (5..9);
my  $vv1 = 1;
our $vv2 = 2;


####################### 
sub s1{
	print "\n=========== s1:\n";
	# print "\n-- @_ --"; $_[1] = 111; $_[7] = 777; $vv2  += 100; print "\n-- @_ --";
	print "\n--vv1: $vv1 --- vv2: $vv2 --";
	print "\n=========== s1-END ==============\n";
}
# &s1(@a1, @a2);   print "\n-- @a1 --- @a2 --\n";


####################### local:
print "\n-----vv2: $vv2 ------ MAIN.pre.s2 --------------\n";
sub s2{
	print "\n=========== s2:\n";
	local $vv2;
	$vv2 += 10; 
	print "\n-----vv2: $vv2 ------ s2-pre-s1 ----------";
	&s1(@a1, @a2);
	print "\n-----vv2: $vv2 ------ s2-END: --------------";
	print "\n=========== s2-END ==============\n";
}
&s2();
print "\n-----vv2: $vv2 ------ MAIN.pos.s2 --------------\n";
################################################################

#print "\n-------\n";
print "\n" . '=' x 40 . "\n";
