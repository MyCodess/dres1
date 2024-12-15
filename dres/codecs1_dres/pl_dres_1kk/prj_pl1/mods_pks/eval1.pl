#!/usr/bin/perl -w

#BEGIN {our $configfile1_FP = '/up1/varu/varau/prjs/prj2/bin/dats.pl' ; do "$configfile1_FP" or die "could not parse the config-file: $configfile1_FP , $@ , $!";}
use warnings;
use strict;

print "\n" . '-' x 40 . "\n";
#print "\n---v3: $v3 --\n";

#################### !!DIFF!! eval-EXPR/".." AND eval-BLOCK/{..} in terms of error/rie ...:
$v1="2/0";
eval  { $v1 ;}; die "==#-eval-block: $@" if $@;  ##-II- no-exception, no-dei
eval  " $v1 ;"; die "==#-eval-EXPR:  $@" if $@;  ##--II- exception! so die!
##--- OR:
eval { our $o1="our1-ev"; my $m1="my1-ev"; };
eval  "our \$o1=111 ; my \$m1=333;" ;
print "\n-- $v1 -- $o1 -- $m1 --\n";



#################### eval + stdin, so a kind of perl-shell:
no strict;
#while (<>) { eval; warn $@ if $@;}
#while (<>) { eval ('$'."$_") unless (/^#/); warn $@ if $@;}
#while (<>) { eval ("\$$_") unless (/^#/); warn $@ if $@;}
#eval `cat /up1/varu/varau/prjs/prj2/bin/dats.pl`;  warn $@ if $@; ##-I- same as do
#print "\n--- $v1 -- $v2 -- @a1 ---- @Data1::a2 --\n";

#################### do:
#do '/up1/varu/varau/prjs/prj2/bin/dats.pl';
#our $configfile1_FP = '/up1/varu/varau/prjs/prj2/bin/dats.pl' ; do "$configfile1_FP" or die "could not parse the config-file: $configfile1_FP , $@ , $!";
#our @appConfigFiles = qw(aaaaaa bbbbb); for my $file (@appConfigFiles) {do "$file" or die " -- Error: could not parse the config file $file \n -- $@ , \n -- $!"}

#print "\n-------\n";
print "\n" . '=' x 40 . "\n";
