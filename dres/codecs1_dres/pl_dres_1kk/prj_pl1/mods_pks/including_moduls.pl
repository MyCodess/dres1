#!/usr/bin/perl -w
#BEGIN { $Exporter::Verbose=1 }

use warnings;
#use strict;


print "\n" . '-' x 40 . "\n";

#use M1 qw(su1);
#require M1 ;
do 'M1.pm';
print "\n----M1.IDs:   $M1::myvar1 -- $M1::var1 --\n";
print "\n--noM1.IDs:   $myvar1 -- $var1 --\n";

#eval {our $var1='our1'; my $myvar1='my1';} ;
#print "\n-- $var1 -- $myvar1 --\n";

#print "\n-------\n";
print "\n" . '=' x 40 . "\n";
