#!/usr/bin/perl -w

#package M1;

#require Exporter;
use strict;
use Exporter;
our @ISA = qw(Exporter);
our @EXPORT = qw(su1);

my $myvar1="myVar1-org-M1";
our $var1="ourVar1-org-M1";
print "--from.M1: $myvar1 --\n";

sub su1(){ print "\n------- M1-sub-1 ---------\n";};
print "======= M1-Module-END ==============";
1;
