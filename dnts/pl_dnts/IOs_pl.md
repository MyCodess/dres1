________ perl-IO , open-files, stdin/out, input-output-filters, redirections/pipes, ARGV-cmdline-parameters,.... __________

	_______:  see:
	- perlopentut
	- perldoc -f open
	- perlop  : O-Operators  (perldoc-5.14.0/perlop.html#I/O-Operators )
	-! perlfaq5 - Files and Formats  :codecs for change/modify/... files, handling FHs,...
	- File::* , IO::* , (PerlIO::*)
##________________________________________  ___________________________


#####  ==========  @ARGV , <STDIN> , <>, <ARGV>, <STDOUT>, :      see perlop  perldoc-5.14.0/perlop.html#I/O-Operators :
	--- <>  : null filehandle :
		- "<>" : read fileNAMES from @ARGV and read.in these files (if @ARGV empty, then read.in from STDIN). so cmdline-params are handeled as filenames to readin!
		- "<>" : Here's how it works: the first time <> is evaluated, the @ARGV array is checked, and if it is empty, $ARGV[0] is set to "-", which when opened gives you standard input. The @ARGV array is then processed as a list of filenames. 
		-  while (<>) { print; ... }  == same.as:    unshift(@ARGV, '-') unless @ARGV; while ($ARGV = shift) { open(ARGV, $ARGV); while (<ARGV>) { ...   # code for each line } }  : so it reads in file from cmdline-params (see perlop : I/O-Operators)
		- so its input comes either from standard input, or from each file listed on the command line.  ;see perldoc-5.14.0/perlop.html#I/O-Operators
	--- <ARGV>-open/read.in :      :see perldoc-5.14.0/perlopentut.html#Filters
		-! When you process the ARGV filehandle using <ARGV> , Perl actually does an implicit open on each file in @ARGV:
		  so by:  myprogram file1 file2 file3  :then "myprogram" can read ALL files in its cmdline-params simply by: while (<>) {...}   #see perlopentut
		  If @ARGV is empty when the loop first begins, Perl pretends you've opened up "-", that is, the standard input <STDIN>.
		  so If @ARGV is empty, then $ARGV, the currently open file during <ARGV> processing, is set to "-" in these circumstances.
		-! you can manually set/manipulate the @ARGV before starting your read-loop. 
	--- <STDIN>-open/read.in :    :see  perlopentut.html#Playing-with-STDIN-and-STDOUT
		- open (my $fd1, "-");   while (<$fd1>) {print ;}    -same.as:
		- while (<>) {print ;}  :when @ARGV is empty! otherwise @ARGV-entries are handeled as fileNAMES to get opened! "<>" is "<STDIN>"
		- do { $line = <STDIN>; ...  } until $line  eq ".\n";
		- redirect:   open(STDIN, "< datafile")  or die $!;
		- When -t STDIN returns true, it generally means that you can interactively ask the user questions. /11.1.plo4
	--- <STDOUT>:
		-! always CLOSE it (also close other FDs)! as:  END { close(STDOUT) || die $!;}
		- redirect:  open(STDOUT, "> output") or die $!;
		- pager of STDOUT:   $pager = $ENV{PAGER} || "(less || more)";  open(STDOUT, "| $pager")  or die $!;  #see perlopentut
##________________________________________  ___________________________


#####  ==========  open/readin/piping files,  ... :
	- file-slurp:   $/ is set to undef (sometimes known as file-slurp mode): reads in the whole file in one line. eg:
	   my @lines = do { local $/; <$in> }; #now the whole file is in @lines  ;see perlfaq5
	   !!-but performance problems: Perl won't give that memory back to the operating system until the process finishes. so avoid it if possible!!
	- file-into-array:  my @a=<>;  /OR my @a=<FD1>;  reads the WHOLE file into @a, with each line assigned to an array-element $a[i], eg:  perl -we 'my @a=<>; print $a[3];' t1.txt 
	- @ARGV/cmdline.params:  while (<>) {...} #see above.nts
	- more-specific-open with  sysopen()  :see perldoc-5.14.0/perlopentut.html#Open-agrave-la-C  +  perlfaq5.html#How-come-when-I-open-a-file-read-write-it-wipes-it-out?
	- is link-valid??: if (-l $file) { unless (defined($whither = readlink($file))) { print "invalid link. $file";} }
	--- open() (to read OR write):       :see perlopentut + open + perlfaq5 :
		-! take 3-param-variation, if <,>,>>,.. needed!! as:   open( INFO, ">", $datafile ) || die $! ;  see perlopentut.html#Simple-Opens
		-! ">" in ANY form ALWAYS truncates the file (delete the file content)!! so also "+>" ,...! if appending/updating wanted, then use ">>", "+<",..
		-! take preferably a var as the first-param/filehandle-name of open() (indirect filehandle name), eg:   open( my $in, $infile )   or die $!; while  ( <$in> ) {...} :
		   indirect filehandle automatically closes when there are no more references to it. Also no multiple opens occurs. And easier to pass filehandles to/from subs!  #see perldoc-5.14.0/perlopentut.html#Indirect-Filehandles
		-! MIXED-read-write on same-file:  "+<" bzw. "+>" , "+>>"   /OR  take: perl -i ...  :see  perldoc-5.14.0/perlopentut.html#Mixing-Reads-and-Writes
		-!! single-argument-open (! works ONLY with our.vars NOT with my.vars $FH1):   our $FH1="/tmp/t1";   open FH1 or die $!  #-is.same.as:   open (FH1, "$FH1" or die $!  #see perldoc-5.14.0/perlopentut.html#Single-Argument-Open
		-! fileName/filePath also as FileHandle.ID, for better error-messages !! eg:  open($path, "< $path");  #see perldoc-5.14.0/perlopentut.html#Paths-as-Opens
		- string.opening /writing-into-string-var:  my $str1="111"; open my $fh1, ">", \$str1 or die $!;   print $fh1 "aa\nbb";   print "___ $str1";
		   /OR: 	open FH, '>', \my $string;  (\my : declare it but return the pointer to it)
	--- open()-both.read+write:
		- see perlfaq5.html#How-come-when-I-open-a-file-read-write-it-wipes-it-out?
		-!! avoid, if possible, simultanous read+writes, specially for textfiles! instead copy file and ....! see perldoc -f open
		-!! Using ">" always clobbers/truncates. Using "<" never does. The "+" doesn't change this. so  (perlfaq5):
		  wrong! truncates the file:     open my $fh, '+>', '/path/name'; # WRONG (almost always)    #-: it truncates/clobber the file!!
		  ok open for update/read+write (not truncate):   open my $fh, '+<', '/path/name';  
		-! NEVER use "+>" ! it truncates the file!  instead use "+<" for read+write for updates/appending!
		-! space and non.utf8.chars in filenames:  Use 3-argument form to open a file with arbitrary weird characters in it!
	--- pipe /shell-piping:
		- see  perldoc -f open +  perldoc-5.14.0/perlopentut.html#Pipe-Opens  +  perldoc-5.14.0/perlipc.html#Named-Pipes
		- pipe.out/to   '|-':   open(FOO, '|-', "tr '[a-z]' '[A-Z]'") or die $!;  /OR  open(FOO, '|-', "tr '[a-z]' '[A-Z]'");
		   open(PRINTER, "| lpr -Plp1") or die $!;  print PRINTER "my.stuff\n";
		- pipe.in/from  '-|':    open(FOO, "cat -n '$file'|")  or die $!;   /OR  open(FOO, '-|', "cat -n '$file'");
		   open (my $fd1, "cat $ARGV[0] |");   while (<$fd1>) {print ;}
		-! ERRORS in shell.cmd  see perldoc-5.14.0/perlopentut.html#Pipe-Opens  +  perldoc-5.14.0/perlfaq8.html#How-can-I-capture-STDERR-from-an-external-command?
		-!! sequence of outputs: eg: piped.out.output of a shell.cmd could be visible after next lines of your code.outputs!! close the piped.filehandle, if you want to wait finishing it or flush its output!
		  !! Closing any piped filehandle causes the parent process to wait for the child to finish, and returns the status value in $?
		- without.shell.invocaton.piping:  see  open '-|' bzw  open '|-' ,and also  system()
		- Named-Pipes : Unix IPC mechanism for processes communicating on the same machine  :see perldoc-5.14.0/perlipc.html#Named-Pipes
	--- TEMP.files:
		- see  perldoc-5.14.0/perlfaq5.html#How-do-I-make-a-temporary-file-name?
		- use open() with undef in place of the file name:   open my $tmp, '+>', undef or die $!;   #perlfaq5
		- use File::Temp qw(tempfile tempdir);
	--- flushing /buffered outputs:
		- see in perlsColl_devres_kk/prj_pl1/io/... + perlfaq5
		- "$|" ($AUTOFLUSH in English) 
		- deactivate buffering, so do flushing the output immediately:  $|++;   #-so just set $| to true! then noting is buffered!
	--- encoding/binary/... IOs:
		- see binmode +  PerlIO , PerlIO::* + PERLIO environment variable in perlrun
##________________________________________  ___________________________


#####  ==========  changing/modifying files:
	-! see perlfaq5
	-! sed.like in-place-substitution by one-liner-perl:  perl -pi -e 's/aa/TT/g  if $. == 5' t1.txt  #see perlfaq5
	   or with backup:  perl -pi.org -e 's/aa/TT/g' t1.txt
	- count.of.lines by one.liner:  perl -lne '} print $.; {'  file   #/OR:  perl -lne 'END { print $. }' file  #see perlfaq5
	- in-place modifying of files in codes as with "perl -i t1.txt":  my $^I = ".org"; ....; #- "perl -i" sets the value of Perl's $^I variable #see perlfaq5
##________________________________________  ___________________________


#####  ==========  <FileHandle/FH>,  <FileDescriptor/FD>:
	-!! DEFs/DIFF  <FileHandles> (perl.world--Strings)   <-->   FileDescriptors  (underlying-OS.world--Numbers) :        perlglossary:
		- <FileDescriptor> /FD:  The little NUMBER the OPERATING SYSTEM uses to keep track of which opened file you're talking about. Perl HIDES the FileDescriptor inside a standard I/O stream and then attaches the stream to a filehandle. (as in shell exec 2>&1  , OR  exec 3>file1 ...)
		- <FileHandle>    /FH:  An String-IDENTIFIER (not necessarily related to the real name of a file) that REPRESENTS a particular instance of opening a file until you close it. If you're going to open and close several different files in SUCCESSION, it's fine to open each of them with the SAME filehandle, so you don't have to write out separate code to process each file.
		-! kk: so: a filehandle points finally to a filedescriptor. Several filehandles can point to the SAME filedescriptor (see duplication filehandles)!
		- converting FileHandle-to-FileDescriptor:    fileno(FH1) : Returns the file descriptor for the filehandle FH1 !
		-! in Perl: also a filename that begins with an ampersand is treated instead as a FileDescriptor if a number, or as a filehandle if a string.
		   That means that if a function is expecting a filename, but you don't want to give it a filename because you already have the file open,
		   you can just pass the filehandle with a leading ampersand. It's best to use a fully qualified handle though, just in case the function happens to be in a different package:  myfunction("&main::LOGFILE");  #see perldoc-5.14.0/perlopentut.html#Re-Opening-Files-(dups)
	--- duplicating of <FileHandles>, reopenning files (ca.same.as in bash):   see perldoc-5.14.0/perlopentut.html#Re-Opening-Files-(dups)
		- in Perl: a filename that begins with an ampersand is treated instead as a FileDescriptor if a number, or as a filehandle if a string.:
			open(FH1DUP, ">&FH1") || die "couldn't dup FileHandle FH1 : $!";
			open(FD4DUP, "<&4")   || die "couldn't dup FileDescriptor FD1 : $!";
		- duplicating/redirecting of STDERR into a logfile:   open my $log, '>>', '/foo/logfile';  open STDERR, '>&LOG';
	--- <DATA> filehandle  bzw.  __DATA__   (bzw. <mypackage::DATA> , <main::DATA>):
		- see perldoc  perldata + SelfLoader + perl-cookbook--Recipe7.12
		-! __END__  is a synonym for  __DATA__ in the main package (but NOT in other modules).
		  so in the  main, <DATA> reads also text of ___END__
		  But Text after  __END__ tokens in other modules is NOT accessible (not even per <Pack1::DATA>).
		-! <DATA> is NOT closed automatically! is programmers task to do it!
		--- eg: 
			- while (<main::DATA>) {print;}
			- excluding __END__ part:    while (<Package1::DATA>) { last if /^__END__$/; print; }
			-! several FileHandles after your code (eg after __DATA__ but only part from __MyData3__  upto  __MyData3END__):
				kk:  my $count = 0; while (<main::DATA>) { next if (! $count && ! /^__MyData3__$/);  ++$count; next if /^#/; print  ; last if /^__MyData3END__$/; }
				use Inline::Files /CPAN  #see cookbook--Recipe 7.13 
			- size of the current scrip?:  print -s DATA;
	-! subs-parameter-passing of filehandles:  just put "&" before the FileHandle by parameter-passing (better also with package name containing it), as:  somefunction("&main::LOGFILE");  #see  perlopentut.html#Re-Opening-Files-(dups)
	-! ?? two handles refer to the same underlying descriptor??:  by fileno(FH1) ,as:  if (fileno(THIS) == fileno(THAT)) { print "THIS and THAT are dups\n"; }
	--- eg FHs:
		- size of the file of FH1?:  print -s FH1; 
##________________________________________  ___________________________


#####  ==========  DIRs:
	- see  perldoc-5.14.0/perlfaq5.html#How-do-I-traverse-a-directory-tree?
	- opendir(),  readdir(DIR),  closedir(DIR); ...
	- RECURSIVELY processing DIRs: use File::Find module. eg, print out all files recursively and adds a slash to directories.  :perlopentut:
	   - File::Find :  full path of current file in $File::Find::name ; just filename in $_ :
	     use File::Find; find( \&wanted, @ARGV ); sub wanted { print "-- $File::Find::name"; }
	     /OR:  @ARGV = qw(.) unless @ARGV;   use File::Find;   find sub { print $File::Find::name, -d && '/', "\n" }, @ARGV;
	-! dead-links finding recursively:   find sub { print "$File::Find::name\n" if -l && !-e }, $dir;
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  
