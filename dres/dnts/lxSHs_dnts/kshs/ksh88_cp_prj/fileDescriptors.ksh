#!/bin/ksh
# see uxExp-11.13 , Table 11.19.exec ; and Ore-ksh88-ch07 + Table 7.1
# &n : file.descriptor.n , eg. >&4 f.d.4 which is an output f.d.

#================================= OK:
# swaping std-err and out: (UPT-3ed-36.16):
#	grep/cat/...  3>&2 2>&1 1>&3 | mail/tee/.... ; at end close 3>&-  /OR:
exec  3>&2 2>&1 1>&3
...
3>&-

# err to out/pipe, out to file:  eg. $0 | tee out2 (only erreor are in out2) /OR  |mail...
exec 2>&1 1>>out1
cat aaaa_err1
echo out-1 `date`
return

# --- generating a neuw ouput-discriptor:
exec 4>> out2
print "just normal to std-out"
print  "to discriptor-4" >&4
print -u4 "with option -u \tso easier"  # same as above
( date && pwd && hostname ) >&4  # -!-!! without () only hostname is redirected to &4 !!
exec 4>&-   # close output-	f.d.4
return


# --- default-std-err-Redirecting to err1.log ; all errors are appenden/written to err1  (only ">" no appending; ">|"  for noclobber)
exec 2>> err1.log
cat fileNotExist
return

# --- default-std-err-Redirecting to out1.log ; everything is written to out1: (only ">" no appending; ">|" for noclobber)
exec >>out1.log
echo "test1 $( date ) "
return

# --- default-std-in-Redirecting from tt2 ;
exec <tt2
cat
exec <&-  #close std-f.d.input/0
return

# ----- read from tt1 as input-discr.3
exec 3<tt1
#read -u3 d1
#print $d1
cat <&3

# ------------ tech-notes:
-!!-: UPT-3ed-43.3:
	what are file descriptors:
	These file streams may be duplicated; 
	that is, the data stream pointed by the file descriptor on the left,
      will now go to data stream pointed to by the file descriptor on the right.
-!!- the redirection SEQUENCE is absolutely relevant!! ONLY in the tile of redirection is relevant, NOT later:
	eg: 3>&1  1>log : so &3 still points to std-out and NOT to log,...
-!!- Send (Only) Standard Error Down a PIPE (problem: pipes, pipes only std-out): UPT-3ed-43.3
	- ONLY std-err to pipe:
   		me: mycmd 2>&1 1>/dev/null | tee tt1   ; /OR in script: exec 2>&1 ; exec 1>/dev/null ; ...
		UPT:?  (mycmd 3>&1 1>&2 2>&3 3>&-) | ...
	- std-err to pipe, std-out to a file; eg. mailing errors of mycmd, but logging output to a file:
		me: mycmd  2>&1 1>out1 | tee tt1  ; /OR in script: exec 2>&1 ; exec 1>out1 ; ...
		UPT:?  (mycmd 3>&1 > outputfile  2>&3 3>&-) | mail /tee/...  -!!- pipe reads ONLY from std-out, not std-err -!!-
	- easy, redirecting both to a pipe: mycmd  2>&1 | ...
-!!- piping "|" is ONLY relavent for std-out NOT -std-err!!
both std-err und out to a pipe:     command 2>&1 | ...
both std-err und out to a file:     command 2>&1 > logBoth.log
piping ONLY std-err to eg. mail + logfile; but std-err to a file:
    in script: exec > scr.out ....  /OR in subshell online ( ... 1>scr.out....) | tee ... /or | sed ...

# ------------ quickies
exec >&3		: redirect std-out to fd.3 , at least in ksh88; in ksh93 copy std-out ??
exec 2> err.log : redirect std-err &2 to err.log ; /OR >> for append/not overwritung the exeisting file
exec 2>&3		:  redirect std-err &2 to fd.3
exec 3>err.log ; exec 2>&3 	: redirect std-err &2 to err.log (seq. relevant!)
exec 3>&-	# close output-fd.&3
exec 4>out2.log	# create ne output-fd.4 , writing out put to out2.log, e.g print -u4 .., /or echo ...>&4
# - Table 11.19. exec Commands UnixExp-4ed-ch11.13:
exec < filea :		Open filea for reading standard input. read from filea instead &1
exec > filex :		Open filex for writing standard output.: redirect output &2 to filex
exec 2> errors :		Open errors for writing standard error.
exec 2>> errors :		Open errors for writing and appending standard error.
exec 2> /dev/console :		Sends all error messages to the console.
exec 3< datfile :		Open datfile as file descriptor 3 for reading input.: define new fd.3 as input-stream
sort <&3 :				datfile is sorted.
exec 4>newfile :		Open newfile as file descriptor 4 for writing.
ls >&4 :		Output of ls is redirected to newfile.
exec 5<&4 :		Make fd 5 a copy of fd 4. Both descriptors refer to newfile.
exec 3<&- :		Close file descriptor 3, datfile.
# simple basic redirections, Table 11.18. Redirection, UnixExp-4ed-ch11.13:
< file :		Redirect input from file
> file :		Redirect output to file
>> file :		Redirect and append output to file
2> file :		Redirect errors to file
2>> file :		Redirect and append errors to file
1>&2 	:		Redirect output to where error is going
2>&1 	:		Redirect error to where output is going

# -- Table 7.1: I/O Redirectors Redirector Function , Ore-ksh88-ch7.1:
> file 			Direct standard output to file 
< file 			Take standard input from file 
cmd1 | cmd2 	Pipe; take standard output of cmd1 as standard input to cmd2
>> file 		Direct standard output to file; append to file if it already exists
>| file 		Force standard output to file even if noclobber set
<> file 		Use file as both standard input and standard output 
<< label 		Here-document; see text 
n> 				file Direct file descriptor n to file 
n< 				file Set file as file descriptor n 
>&n 			Duplicate standard output to file descriptor n 
<&n 			Duplicate standard input from file descriptor n 
<&- 			Close the standard input 
>&- 			Close the standard output 
|& 				Background process with I/O from parent shell 
>&p 			Direct background process' standard output to the parent shell's standard output
<&p 			Direct parent shell's standard input to background process' standard input

# print & read:
print -uX		 Print to file descriptor X
read  -uX        read from file descriptor X

 
