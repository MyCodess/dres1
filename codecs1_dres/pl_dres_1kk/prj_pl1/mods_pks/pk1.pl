#!/usr/bin/perl -w

use warnings;
#use strict;
#use Data::Dumper;

print "\n" . '-' x 40 . "\n";

my $v1="main-v1";
print "\n--main.1- $v1 --\n";

###############
package pb;{
our $v2="pb-v2";
print "\n--pb- $v1 --\n";
print "\n--pb-2- $v2 --\n";
}
###############
our $v3;
{
	$v3=3;
}
package main;
print "\n--main.2- $v1 --\n";
#print "\n--main-2- $main::v2 --\n";
print "\n--main-2-v3- $v3 --\n";

###########################################
print "\n---new1 ----\n";
   # Context
@now = localtime;  # List context
print "@now\n";   # Scalar context

$now = localtime;
print "$now\n";

print localtime, "\n"; # prints in list context
print scalar localtime,"\n"; # Forced to scalar context

print "\n" . '=' x 40 . "\n";
