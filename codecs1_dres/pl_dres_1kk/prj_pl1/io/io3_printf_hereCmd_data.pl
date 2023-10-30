#!/usr/bin/perl -w

use warnings;
use strict;
print "\n" . '-' x 40 . "\n";

############# printf:
print "\n" . '=' x 60 . "\n";
printf ("%-15s | %-20s\n", "Jack", "Sprat");
printf ("%-15s | %-20s\n", "Jack adfsd", "Sprat sadfdsa");
printf ("%-15s | %-20s\n", "Jack sdfasddd", "Sprat");
printf "The formatted floating point number is |%8.2f|\n", 123456789.5678;
print "" . '=' x 60 . "\n";

############# <<x :
print "\n---x.4 : ----\n";
print << x 4;
test1

####
############# <<EEE :
my $v1=<<EEE;
value.line.1 aaa bb
value.line.1 cc dd
value.line.2  xxx23 34
EEE
print "\n---v1 : ----\n";
print $v1;

############# cmd-return-values:
my $v2 = `ls`;
my @a2 = `ls`;
print "\n---v2:\n $v2 --------\n";
print "\n---a2:\n @a2 --------\n";

print "-- ", localtime();  #- 5027118711112191

############# DATA filehandle :
print "\n--- DATA-section: --------\n";
print <main::DATA>;  ##--also ok:  print <DATA>;

print "\n" . '=' x 40 . "\n";

__END__
dummmy text,... not on DATA
abab ababbab

__DATA__
11111
2222
33333
444444
EEEEEEE
_____________

