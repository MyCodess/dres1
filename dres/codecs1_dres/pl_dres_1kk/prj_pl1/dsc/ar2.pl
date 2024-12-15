#!/usr/bin/perl

use warnings;
use strict;

print "\n" . '-' x 40 . "\n";
my @a1=0..9;
print "\t --a1:  @a1[2..4]--\n";
my @AoA = (
	[ "fred", "barney" ],
	[ "george", "jane", "elroy" ],
	[ "homer", "marge", "bart" ],
);

# print the whole thing with refs
for my $aref ( @AoA ) {
	print "\t --aref: @$aref --\n";
}

###########
our @a2 = @a1;
#our (@a2) = @a1;
$a2[1] = 111;
print "\n-- @a1 -- @a2 --\n";
###########

print "\n-- [ @a1 ] -- [ @{$AoA[1]} ] --\n";
#print "\n-------\n";
print "\n" . '=' x 40 . "\n";
