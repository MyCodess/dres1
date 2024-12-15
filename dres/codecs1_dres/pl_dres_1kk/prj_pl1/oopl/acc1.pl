#!/usr/bin/perl -w

use warnings;
use strict;
use Acc;

print "\n" . '-' x 40 . "\n";

our $acc1 = Acc->new();
$acc1->setdata(11, "Joe Julian", 1100);
$acc1->getdata();


our $acc2 = Acc->new();
$acc2->setdata(22, "Frank Hatle", 2200);
$acc2->getdata();

our $acc3 = Acc->new2(33,, "3nn 3ff", 3300);
$acc3->getdata();


print "\n-- final instaces Data: -----\n";
$acc1->getdata();
$acc2->getdata();
$acc3->getdata();

#$acc1->printhash();
#print "\n-------\n";
print "\n" . '=' x 40 . "\n";
