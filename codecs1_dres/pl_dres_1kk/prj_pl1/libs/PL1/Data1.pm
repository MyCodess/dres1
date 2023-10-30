#!/usr/bin/perl -w

package PL1::Data1; ##--II- can be commented out, so that data belongs to the caller, if done with do/eval ! eg :
# USAGE1:  BEGIN { $PL1::Data1::verbose=6 ;}   #/OR also for debugging:  BEGIN {$Exporter::Verbose=1 }
#          use  PL1::Data1;   /OR  use  PL1::Data1 qw(/[ahp].*/ );  /OR  require "PL1/Data1.pm";  /OR 
#          not recommend: do "PL1/Data1.pm";   /OR   eval `cat /up1/varu/varau/prjs/pl1/libs/PL1/Data1.pm` or die "====##Fatal.Error-Eval.Problem:" . $@;
use warnings;
use strict;
use Exporter qw( import );    #/OR with ISA-inheritance:  use Exporter;our @ISA = qw(Exporter);
our @EXPORT    = qw();
our @EXPORT_OK = qw(printData1 @a1 @a2 @a3 %h1 %h2 %h3);
our $verbose;
$verbose = 2 unless defined $verbose ;  ##-ReDo  0; ##--II-:  0==no.outputs , 2==start-end-minor-printlines , 4==subproccees-data-printouts 
if ($verbose > 1 ) { print "\n" . '.' x 20 , __PACKAGE__ . " -- called from: $0 ...........\n"; }

############# vars:
our $vpkname = "Data1";
our $v1 = 11;
our $v2 = 22;
our @a1 = (0..9);
our @a2 = (10..19);
our @a3 = map {chr($_ + 65)x4} @a1;
our %h1 = ();
our %h2 = ();
our %h3 = ();
for my $ii (0..9)  { $h1{$ii} = $ii+100; }  ##--OR:   $h{$_} = $_ +100 for (0..9) ;
for my $ii (0..9)  { $h2{$ii} = $ii+110; }  ##--OR:   $h{$_} = $_ +110 for (0..9) ;
for my $ii (0..9)  { $h3{$ii} = chr($ii + 65) x 5; }  ##--OR:   $h{$_} = $_ +110 for (0..9) ;


############# Debugs/Data-printouts:
sub printData1() {
	print "----- Data1-vars";
	print "\n---\@a1 : \[ @a1 \] ---\n";
	print "\n---\@a2 : \[ @a2 \] ---\n";
	print "\n---\@a3 : \[ @a3 \] ---\n";
	print "\n--- %h1 : \n"; foreach my $key (sort keys %h1) { print "\t\$h1{$key} => $h1{$key}\n";}
	print "\n--- %h2 : \n"; foreach my $key (sort keys %h2) { print "\t\$h2{$key} => $h2{$key}\n";}
	print "\n--- %h3 : \n"; foreach my $key (sort keys %h3) { print "\t\$h3{$key} => $h3{$key}\n";}
	print "----- Data1-vars-END------------";
	# use Data::Dumper;
	# print Dumper \%main:: ;
	# print Dumper \%h1;
	# print Dumper \%h2;
}
######################
#

#print "\n-------\n";
############# Tests-Debugs-Verbose:
if ($verbose > 3 ) {
	&printData1();
}
if ($verbose > 1 ) { print "\n" . ':' x 20 , __PACKAGE__ . " -- called from: $0 --END::::::\n"; }
1;
