#!/usr/bin/perl -w
##-I_ from:  perldoc perlmod

# begincheck
print         "10.prin Ordinary code runs at runtime.\n";
END { print   "16.END    So this is the end of the tale.\n" }
INIT { print  " 7.INIT INIT blocks run FIFO just before runtime.\n" }
UNITCHECK { print " 4.UNIT   And therefore before any CHECK blocks.\n" }
CHECK { print " 6.CHEC   So this is the sixth line.\n" }
print         "11.prin   It runs in order, of course.\n";
BEGIN { print " 1.BEGI BEGIN blocks run FIFO during compilation.\n" }
END { print   "15.END    Read perlmod for the rest of the story.\n" }
CHECK { print " 5.CHEC CHECK blocks run LIFO after all compilation.\n" }
INIT { print  " 8.INIT   Run this again, using Perl's -c switch.\n" }
print         "12.prin   This is anti-obfuscated code.\n";
END { print   "14.END  END blocks run LIFO at quitting time.\n" }
BEGIN { print " 2.BEGI   So this line comes out second.\n" }
UNITCHECK { print " 3.UNIT UNITCHECK blocks run LIFO after each file is compiled.\n" }
INIT { print  " 9.INIT   You'll see the difference right away.\n" }
print         "13.prin   It merely _looks_ like it should be confusing.\n";
__END__
