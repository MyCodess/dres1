#!/usr/bin/perl -w
##-	just dummy for simple data testies; to play around with vars/arrays/hasges/refs ....

use warnings;
use strict;

print "\n" . '=' x 40 . "dats.1: --\n";

############# vars:
our $pkgname = "Data1";
our $v1 = 11;
our $v2 = 22;
our @a1 = (0..9);
our @a2 = (10..19);
our %h1 = ();
our %h2 = ();
for my $ii (0..9)   { $h1{$ii} = $ii+100;}
for my $ii (10..19) { $h2{$ii} = $ii+100;}

#&printData1();

############# Debugs/Data-printouts:
sub printData1() {
	print "----- $pkgname vars";
	print "\n---$pkgname -- \$v1 : $v1 -- ....  ---\n";
	print "\n---\@a1 : \[ @a1 \] ---\n";
	print "\n---\@a2 : \[ @a2 \] ---\n";
	print "\n--- %h1 : \n"; foreach my $key (sort keys %h1) { print "\t\$h1{$key} => $h1{$key}\n";}
	print "\n--- %h2 : \n"; foreach my $key (sort keys %h2) { print "\t\$h2{$key} => $h2{$key}\n";}
	#print Dumper \%main:: ;
	use Data::Dumper; print Dumper \%Data1::;
	print "----- $pkgname vars-END------------";
	# print Dumper \%h1;
	# print Dumper \%h2;
}
######################
#

#print "\n-------\n";
print "\n" . '=' x 40 . " dats.1-END--\n";
1;
