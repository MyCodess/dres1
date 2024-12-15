#!/usr/bin/perl -w

use warnings;
use strict;

############# Example 12.9. 
use English1;    # Use English words to replace special Perl variables
print "The pid is $PROCESS_ID.\n";
print "The pid is $PID.\n";
print "The real uid $REAL_USER_ID.\n";
print "This version of perl is $PERL_VERSION.\n";


#print "\n-------\n";
print "\n" . '=' x 40 . "\n";
