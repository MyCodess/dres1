#!/usr/bin/perl -w

use warnings;
#use strict;

print "\n" . '-' x 40 . "\n";
our $path1 = "./t1.txt";
#open ($path1, $path1);
open  path1;
while (<path1>) { print "-- ". tell; print; }

#print "\n-------\n";
print "\n" . '=' x 40 . "\n";
