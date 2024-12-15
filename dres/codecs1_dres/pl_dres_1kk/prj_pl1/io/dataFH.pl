#!/usr/bin/perl -W
##--	DATA-filehandle

use warnings;
use strict;

##--use Smart::Comments -ENV;  ##--II-  call it by: perl '-MSmart::Comments=###-d-' tpl2.pl
###-d- =====----- Start:  __PACKAGE__ . " called by " . $0 . " -----====="

########## handling DATA-FH:

#while (<DATA>) {print;}                          ##-- INcluding END-part
#while (<DATA>) {last if /^__END__$/; print;}     ##-- EXcluding END-part

##-- several DATA-files, without using the cpan-packs  Inline::Files:
my $started = 0; while (<main::DATA>) { next if (! $started && ! /^__MyData3__$/); $started=1;  print  ; last if /^__MyData3END__$/; }
##############################


#print "\n-------\n";
###-d- =====----- END:     __PACKAGE__ . " called by " . $0 . " -------====="
1;
######################################################################
__DATA__
dat
dat

__MyData3__
d3
d3aaaa
d3bb b b b 
d3c c cccc 
__MyData3END__

dummy
dummy
dummy
dummy

__MyData4__
d4
d4aaaa
d4bb b b b 
d4c c cccc 
__MyData4END__

__END__
end1
end2
end3
