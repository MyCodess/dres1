#!/usr/bin/perl -w

##--	USAGE: see DebugComments1.pm : debug-statements as comments
#
#
use strict;
use warnings;

##--II- do this, if want your own debug-comment-symbols:    BEGIN { $DebugComments1::ds = "##-d";}
#
#
##- use DebugComments1 "##-d";  ##--II-  comment out this line to DEactivate debugging-outputs  /OR instead use-stmt just activate it on cmdline by : perl -MDebugComments1  filter1.pl

print "\n===== debugging-comments-exp: ======\n";
my $v1="101";
my @a1 = (10..14);

##__ " simple debugging text" , 1234
##__ "-v1-value: " , $v1
##__ "-v1-value: " , $v1 , " ---a1-values: ", "@a1"
##__ "@a1"
## normal no-debugging-comment
##-d "you could set your own debugging-symbol by defining  DebugComments1::ds variable."
#==================================
#
print "\n---------END------\n";


