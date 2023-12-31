#!/usr/bin/perl -w

use warnings;

print "\n" . '-' x 40 . "\n";
# reading from file
# this is most easily done by having the file itself be
# in the raw data format as shown above.  perl is happy
# to parse complex data structures if declared as data, so
# sometimes it's easiest to do that
# here's a piece by piece build up
$rec = {};
$rec->{series} = "flintstones";
$rec->{nights} = [ find_days() ];
sub find_days() { print "aa"; }
@members = ();
# assume this file in field=value syntax
while (<>) {
	%fields = split /[\s=]+/;
	push @members, { %fields };
}
$rec->{members} = [ @members ];
# now remember the whole thing
$TV{ $rec->{series} } = $rec;
###########################################################
# now, you might want to make interesting extra fields that
# include pointers back into the same data structure so if
# change one piece, it changes everywhere, like for example
# if you wanted a {kids} field that was a reference
# to an array of the kids' records without having duplicate
# records and thus update problems.
###########################################################
foreach $family (keys %TV) {
	$rec = $TV{$family}; # temp pointer
	@kids = ();
	for $person ( @{ $rec->{members} } ) {
		if ($person->{role} =~ /kid|son|daughter/) {
			push @kids, $person;
		}
	}
	# REMEMBER: $rec and $TV{$family} point to same data!!
	$rec->{kids} = [ @kids ];
}
# you copied the array, but the array itself contains pointers
# to uncopied objects. this means that if you make bart get
# older via
$TV{simpsons}{kids}[0]{age}++;
# then this would also change in
print $TV{simpsons}{members}[2]{age};
# because $TV{simpsons}{kids}[0] and $TV{simpsons}{members}[2]
# both point to the same underlying anonymous hash table
# print the whole thing
foreach $family ( keys %TV ) {
	print "the $family";
	print " is on during @{ $TV{$family}{nights} }\n";
	print "its members are:\n";
	for $who ( @{ $TV{$family}{members} } ) {
		print " $who->{name} ($who->{role}), age $who->{age}\n";
	}
	print "it turns out that $TV{$family}{lead} has ";
	print scalar ( @{ $TV{$family}{kids} } ), " kids named ";
	print join (", ", map { $_->{name} } @{ $TV{$family}{kids} } );
	print "\n";
}


#print "\n-------\n";
print "\n" . '=' x 40 . "\n";
