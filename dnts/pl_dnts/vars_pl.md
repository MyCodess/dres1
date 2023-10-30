______ perl.vars,.... __________
- see perlvar
##________________________________________  ___________________________


#####  ==========  SIGs, signal-handling,...
	- printout all SIGs:  %SIG    ;so eg:
		- foreach my $key (sort keys %SIG) { print $key, "\t ==>\t ", (defined $SIG{$key} ? $SIG{$key} : "not-defined"); }
		- use Data::Dumper; print  Data::Dumper::Dumper \%SIG;
##________________________________________  ___________________________


#####  ==========  LISTs.vars:
	-!! DIFF:   $,  $OUTPUT_FIELD_SEPARATOR    <-->   $\  $OUTPUT_RECORD_SEPARATOR   <-->   $"  $LIST_SEPARATOR :
		$,  $OUTPUT_FIELD_SEPARATOR    : eg. between EACH array element by eg print @a1 (so usu. space)  : is printed BETWEEN each of print's arguments. Default is "undef".
		$\  $OUTPUT_RECORD_SEPARATOR   : eg. at the END of whole print of  eg print "@a1"  (so usu. \n)  : is printed after the LAST of print's arguments. Default is "undef".
		$"  $LIST_SEPARATOR            : similar to $, but, so between EACH array element, but stringified, so enclosed in ".." as in  print "array-elements: @a1"  :  When an array is interpolated into a double-quoted string, its elements are separated by this value. Default is a space.
		-!	$,= "--";  print @a1; #-OK    , BUT   print "@a1"; NOT.OK
			$"= "--";  print "@a1"; #-OK  , BUT   print  @a1;  NOT.OK
			beetween RECORds eg:  $\= "\n------\n";  print "@a1";  print "@a1";
