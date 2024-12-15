#!/usr/bin/perl -wl
#BEGIN { $Exporter::Verbose=1 }

use warnings;
#use strict;


print "\n" . '-' x 40 . "\n";

our $v1 = "localtime()";   #"`ls`";
#system("sdaf") or die  "==###Fatal-Err: $@ -- $! -- $?" ;
#print "\n---- $@ -- $? ---\n";  

print eval "$v1";

#eval {while (<>) {print "\n___ $_\n" ; system("$_") || die  $@ if $@;}} ; #warn $@ if $@;

#eval { our $o1="our1-ev"; my $m1="my1-ev"; };
eval  "our \$o1=111 ; my \$m1=333;" ;
print "\n-- $v1 -- $o1 -- $m1 --\n";


#$v1=<>; chomp ($v1);
#eval ($v1);  die  "==###Fatal-Err: $@ -- $! -- $?" ;

#print eval "$v1"; ;
$v1="2/0";
eval  { $v1 ;}; die "==#-eval-block: $@" if $@;
eval  " $v1 ;"; die "==#-eval-EXPR:  $@" if $@;
#eval {$v1=2/0 ;}; die "==###Fatal-Err: $@ -- $! -- $?"   if $@;
#eval {system(aaaa) ;}; die "==###Fatal-Err: $@ -- $! -- $?"   if ($@ or $!);
print  "== $@ -- $! -- $?" ;

#print "\n-------\n";
print "\n" . '=' x 40 . "\n";
