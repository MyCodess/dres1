#!/usr/bin/perl -wl
##--I- see perldoc perlmod

#package p1;
use warnings;
use strict;

CHECK { print "_____  ${^GLOBAL_PHASE} -- CHECK ______ $main::b1 " ;};
INIT { print "_____  ${^GLOBAL_PHASE} -- INIT ______ $main::b1 " ;};
UNITCHECK { print "_____  ${^GLOBAL_PHASE} -- UNITCHECK ______ $main::b1 " ;};
END { print "_____  ${^GLOBAL_PHASE} --END.1 ______ $main::b1 " ;};

######## main:
print "\n" . '-' x 40 ;
#die "==###### crashed.1 =============";
BEGIN { print "_____  ${^GLOBAL_PHASE} -- BEGIN.1 ______"; $main::b1=5 ;};
END { print "_____  ${^GLOBAL_PHASE} --END.2 ______ $main::b1 " ;};
print "\n--- main-running -------- $main::b1 ----";
print "\n" . '=' x 40 ;
########

BEGIN { print "_____  ${^GLOBAL_PHASE} -- BEGIN.2 ______"; $main::b1=5 ;};


__END__
########## output: #################################
u1@vo17:/up1/varu/varau/prjs/pl1/bin/mods_pks $begin_end.pl 
_____  START -- BEGIN.1 ______
_____  START -- BEGIN.2 ______
_____  START -- UNITCHECK ______ 5 
_____  CHECK -- CHECK ______ 5 
_____  INIT -- INIT ______ 5 

----------------------------------------

--- main-running -------- 5 ----

========================================
_____  END --END.2 ______ 5 
_____  END --END.1 ______ 5 

u1@vo17:/up1/varu/varau/prjs/pl1/bin/mods_pks $

####################################################

