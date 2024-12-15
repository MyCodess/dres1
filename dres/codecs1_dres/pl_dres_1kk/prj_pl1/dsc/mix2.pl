#!/usr/bin/perl -w

use warnings;
#use strict;

print "\n" . '-' x 40 . "\n";
$rec = {
    TEXT      => $string,
   SEQUENCE  => [ @old_values ],
   LOOKUP    => { %some_table },
   THATCODE  => \&some_function,
   THISCODE  => sub { $_[0] ** $_[1] },
    HANDLE    => \*STDOUT,
     };

     use FileHandle;
     $rec->{HANDLE}->autoflush(1);
     $rec->{HANDLE}->print(" a string\n");
#print "\n-------\n";
print "\n" . '=' x 40 . "\n";
