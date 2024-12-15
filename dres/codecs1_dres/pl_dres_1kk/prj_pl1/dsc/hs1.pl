#!/usr/bin/perl -w

use warnings;
use strict;

print "\n" . '-' x 40 . "\n";

our %HoA = (
	flintstones        => [ "fred", "barney" ],
	jetsons            => [ "george", "jane", "elroy" , "add1",],
	simpsons           => [ "homer", "marge", "bart" ],
);
printhash();
#print "\n-------\n";
# reading from file
# flintstones: fred barney wilma dino
while ( <> ) {
	next unless s/^(.*?):\s*//;
	$HoA{$1} = [ split ];
}
printhash();

print "\n-------\n";
# print the whole thing sorted by number of members
 foreach my $family ( sort { @{$HoA{$b}} <=> @{$HoA{$a}} } keys %HoA ) {
     print "$family: @{ $HoA{$family} }\n"
 }

#print "\n-------\n";
print "\n" . '=' x 40 . "\n";

sub printhash(){
	# print the whole thing
	foreach my $family ( keys %HoA ) {
		print "$family: @{ $HoA{$family} }\n"
	}
}
