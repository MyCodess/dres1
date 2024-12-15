#!/usr/bin/perl -w

use warnings;
#use strict;
use Data::Dumper;

print "\n" . '-' x 40 . "\n";

#################### Hash-Slices: Example 5.21.
%officer= ("NAME"=> "Tom.Savage", "SSN" => "510-22-3456", "DOB" => "05/19/66");
print Dumper %officer;
print "\n-------\n";
@info=qw(Marine Captain 50000);
@officer{'BRANCH', 'TITLE', 'SALARY'}=@info;
print Dumper %officer;
print "\n-------\n";
@sliceinfo=@officer{'NAME','BRANCH','TITLE'};
print  @sliceinfo ;
print "\n-------\n";
print Dumper %officer;
print "\n-------\n";

#print "\n-------\n";
print "\n" . '=' x 40 . "\n";
