#!/usr/bin/perl -w

package PL1::Utils1;
use warnings;
use strict;
use Exporter;
our @ISA = qw(Exporter);
our @EXPORT = qw();  ##--II- OK! also ok with: use PL1::Data1 qw($v1);

print "\n" . '=' x 40 . " $0 --\n";


#print "\n-------\n";
print "\n" . '=' x 40 . " $0 -END--\n";
1;
__END__
############# vars:
our $vpkname = "Data1";
our $v1 = 11;
our $v2 = 22;
our @a1 = (0..9);
our @a2 = (10..19);
our %h1 = ();
our %h2 = ();
for my $ii (0..9)   { $h1{$ii} = $ii+100;}
for my $ii (10..19) { $h2{$ii} = $ii+100;}


############# Debugs/Data-printouts:
##--dg-  &printData1();
sub printData1() {
	print "----- Data1-vars";
	print "\n---\@a1 : \[ @a1 \] ---\n";
	print "\n---\@a2 : \[ @a2 \] ---\n";
	print "\n--- %h1 : \n"; foreach my $key (sort keys %h1) { print "\t\$h1{$key} => $h1{$key}\n";}
	print "\n--- %h2 : \n"; foreach my $key (sort keys %h2) { print "\t\$h2{$key} => $h2{$key}\n";}
	use Data::Dumper; print Dumper \%Data1:: ;
	print "----- Data1-vars-END------------";
	# print Dumper \%main:: ;
	# print Dumper \%h1;
	# print Dumper \%h2;
}
######################
#
