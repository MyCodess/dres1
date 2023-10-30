#!/usr/bin/perl -lw
##--II-	varnames.of.vars , varnames.bases.on.other.var.values:
#	see also devres/0devNts/pl/pl_data_dsc.txt
#
#

package VarnamesVar;
use warnings;
use strict;
no strict 'refs';       ##--II- varnames.of.vars needs always this unfortuntealy!! because  "$$ii" is not in package.symbol.table!!

##--II- these vars MUST be our.var, to work with varnames.of.varValues!! does NOT work, if my.var!!
#	see devnts!: because perls looks in package.symbol.table after parsing varnamesVars!! my.vars are NOT in sybol.table!
our @a1=(10..19);
our $a1ref = \@a1;
our %h1;
our $h1ref = \%h1;   ##--II- MUST be our.var !!
##--------
for my $ii (0..9){ $h1{$ii} = $ii+100; };
my $ii;

#-------- array.varnameVar:
print "--- a1:  " . $a1[2];
$ii="a1";
print $$ii[2];  ##--II- does NOT work if "my %h1" !! MUST be "our %h1" !!
print ${$ii}[2];

#-------- arrayRef.varnameVar:
$ii="a1ref";
print "--- a1-Ref:  " . $a1ref->[2];
print $$ii->[2];  ##--II- does NOT work if "my %h1" !! MUST be "our %h1" !!
print ${$ii}->[2];

#-------- hash.varnameVar:
print "--- h1:  " . $h1{2};
$ii="h1";
print $$ii{2};  ##--II- does NOT work if "my %h1" !! MUST be "our %h1" !!
print ${$ii}{2};

#-------- hashRef.varnameVar:
$ii="h1ref";
print "--- h1-Ref:  " . $h1ref->{2};
print $$ii->{2};  ##--II- does NOT work if "my %h1" or my $h1ref !! MUST be "our %h1 AND $h1ref" !!
print ${$ii}->{2};

#-------- packageSymbol.varnameVar:
print "--- packageSymbolTable:  " . $VarnamesVar::a1[2] . " -- " . $VarnamesVar::h1{2};
$ii=__PACKAGE__ ;
print ${$ii . "::a1"}[2];  ##--II- []-notaion specifies an array!  does NOT work if "my %h1" !! MUST be "our %h1" !!
print ${$ii . "::h1"}{2};  ##--II- {}-notaion specifies a   hash!  does NOT work if "my %h1" !! MUST be "our %h1" !!


#-------- packageSymbolRef.varnameVar:
$ii=__PACKAGE__ ;
print "--- packageSymbolTable.REF:  " . $VarnamesVar::a1[2] . " -- " . $VarnamesVar::h1{2};
print ${$ii . "::a1ref"}->[2];  ##--II- []-notaion specifies an array!  does NOT work if "my %h1" !! MUST be "our %h1" !!
print ${$ii . "::h1ref"}->{2};  ##--II- {}-notaion specifies a   hash!  does NOT work if "my %h1" !! MUST be "our %h1" !!

