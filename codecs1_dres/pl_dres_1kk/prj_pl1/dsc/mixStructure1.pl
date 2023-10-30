#!/usr/bin/perl -w

use warnings;
use strict;

print "\n" . '-' x 40 . "\n";
my $rec = {
    TEXT      => $string,
   SEQUENCE  => [ @old_values ],
   LOOKUP    => { %some_table },
   THATCODE  => \&some_function,
   THISCODE  => sub { $_[0] ** $_[1] },
    HANDLE    => \*STDOUT,
     };


#print "\n-------\n";
print "\n" . '=' x 40 . "\n";
