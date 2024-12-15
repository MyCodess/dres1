#!/usr/bin/perl -W

use warnings;
use strict;

##--use Smart::Comments -ENV;  ##--II-  call it by: perl '-MSmart::Comments=###-d-' tpl2.pl
###-d- =====----- Start:  __PACKAGE__ . " called by " . $0 . " -----====="

########## 
##========== piped open (notice flushing problem):
our $p1="/my/root/test/dir/tt1.txt";
open my $fh1, "|-", "tr '[a-z]' '[A-Z]'"  or die $!;
print $fh1 "$p1 \n";
##--II- to flush pipe.FH.output before next lines, must do "close $fh1" !!  "$|++" does NOT work here, because it is shell.output!!:
#-  close $fh1;
print `basename $p1`;
print "----- pipe-done -------\n";
######
#

##############################
#$\ ="\n--"; print "_____________________"; 
#print "\n-------\n";
###-d- =====----- END:     __PACKAGE__ . " called by " . $0 . " -------====="
1;
######################################################################
__DATA__
__END__

##----------------------- opens:
our $p1=$ARGV[0];

##========== simple open:
use strict; our $p1=$ARGV[0]; open  my $fh1, "<$p1"  or die $!; while (<$fh1>) {print;}
##--OR (also ok with strict): 
use strict; our $p1=$ARGV[0]; open  FH1,     "<$p1"  or die $!;  while (<FH1>) {print;}
##--OR, but no strict (missing my):
no strict 'vars'; our $p1=$ARGV[0]; open  $fh1, "<$p1"  or die $!; while (<$fh1>) {print;}


##========== single.param.open() :
#- in "open FILEHANDLE, EXPR", if EXPR is omitted, the our.scalar.variable.of.same.name as the FILEHANDLE contains the filename (so here "$"."p1"). see perldoc open + perlfaq15: 
#- ONLY works with $p1 as OUR.var, NOT with my.var!!:
our $p1=$ARGV[0]; open p1 or die $!; while (<p1>) {print;}  #filename will be "our $p1" also! see perlfaq5

##========== 
##========== 
##========== 
##========== 
##========== 
##========== 
