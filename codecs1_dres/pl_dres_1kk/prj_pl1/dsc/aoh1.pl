#!/usr/bin/perl -w

use warnings;
use strict;

print "\n" . '-' x 40 . "\n";
our @AoH = (
	{
		Lead     => "fred",
		Friend   => "barney",
	},
	{
		Lead     => "george",
		Wife     => "jane",
		Son      => "elroy",
	},
	{
		Lead     => "homer",
		Wife     => "marge",
		Son      => "bart",
	}
);

printaoh();

#print "\n-------\n";
print "\n" . '=' x 40 . "\n";

# print the whole thing with refs
sub printaoh(){
	for my $href ( @AoH ) {
		print "{ ";
		for my $role ( keys %$href ) {
			print "$role=$href->{$role} ";
		}
		print "}\n";
	}
}

######
# reading from file
# format: LEAD=fred FRIEND=barney
sub readFromFile(){
	while ( <> ) {
		my $rec = {};
		for my $field ( split ) {
			my ($key, $value) = split /=/, $field;
			$rec->{$key} = $value;
		}
		push @AoH, $rec;
	}
	print "\n-------\n";
}

# print the whole thing with indices
for my  $i ( 0 .. $#AoH ) {
	print "$i is { ";
	for my $role ( keys %{ $AoH[$i] } ) {
		print "$role=$AoH[$i]{$role} ";
	}
	print "}\n";
}
print "\n-------\n";

