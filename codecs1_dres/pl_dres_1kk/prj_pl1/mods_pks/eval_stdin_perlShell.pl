#!/usr/bin/perl -w

use warnings;
#use strict;

print "\n" . '-' x 40 . "\n";

$prompt1 = "perl\> ";

print "$prompt1";        # Print the prompt
while(<STDIN>){
	$result=eval ;  # eval evaluates the expression $_
	if ($@) {warn ($@)} ;  # If an error occurs, it will be assigned to $@
	print "$result\n" if $result;
	print "$prompt1";        # Print the prompt
}

#print "\n-------\n";
print "\n" . '=' x 40 . "\n";
