#!/usr/bin/perl -w

use warnings;
use strict;

print "\n" . '-' x 40 . "\n";

################################## pipe to shell.cmd:
open (F1, "<", "t1.txt");
open F2, "| grep -il 'aa'";
while (<F1>) {
	print "- $. : $_" ;
	print F2;
}
close F1;
close F2;
print "\n-----------------------\n";

################################## pipeed from shell.cmd:
open(NET, "netstat -i -n |")    || die "can't fork netstat: $!";
while (<NET>) {print;}               # do something with input
close(NET); 
print "\n-----------------------\n";

################################## read.and.write FH:
open (F1, "+<", "t1.txt");
#seek (F1,0,0);
my $ii = 0;
while (<F1>) {
#	print "- $. :" ; print ;
	print F1 "-----new $ii\n" if ($ii > 2);
	$ii++;
}
close F1;
print "\n-----------------------\n";

##################################
#print "\n-------\n";
print "\n" . '=' x 40 . "\n";
