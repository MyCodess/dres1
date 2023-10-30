______________ sed _____________________________________________
-!! main-quickRef-doc: SedAwk_PocketRef_Ore_2ed_0207.pdf  --> so the notes from there mainly are NOT repeated hee again!
##________________________________________  ___________________________


#####  ==========  Abbrevs:	
PS	Pattern Space
HS	Hold Space
AP	Adress Pattern
SP	Search Pattern
RP	Replace Pattern
NF	Normal Flow : after reading a new line go back to the "FIRST line of the sed-script"  bzw. "FIRST sed-cmd" (see nts-section "Flow of Control" here below)
CF	changed-Flow-Control (so NOT-normal-flow):   NOT applying all cmds to ALL new lines, as in case of n/N or b/t (see nts-section "Flow of Control" here below)
--############################# 2013-added-nts: #####################################################

	_______:  ! generate a dummy-text-tesf-file for following exp:
	for (( ii=100 ; ii<1000 ; ii+=100 )); do echo $ii --- $ii --- $(( ii +10 )) ; done >| t1.txt

	_______:  ! DIFFs: grouping cmds together with {} and differens effects/constalations:
	- sed -n -e '/xxx/{s/0/1/g;p}' t1.txt  : substitute-and-print-ONLY lines containg xxxx
	- sed -n -e '/xxx/s/0/1/g;p' t1.txt    : substitute in lines containg xxxx, but print ALL lines!

	_______:  DEFis:
	-- pattern space  <-->  hold space : buffers to play with...:
	pattern space:	sed copies each line of input first into the pattern space. 
	hold space:		a special temporary buffer.

	_______:  ! Flow-of-Control:  Normal Flow (NF)   <-->   Changed-Flow-Control (CF) :
	--- Normal--Flow-Control (NF) : after reading a new line go back to the "FIRST line of the sed-script"  bzw. "FIRST sed-cmd", so that ALL cmds are always appllied to ALL lines, from the beginning!
	--- Changed-Flow-Control (CF) : cmd-control JUMPS to some other point, so NOT-normal-flow with cmd-execs in sequence:   NOT applying all cmds to ALL new lines, as in case of n/N or b/t :
		so eg: "n": Control passes to the command following "n" instead of resuming at the top of the script. --> see notes for "n" below!
		so after reading a new line it does NOT go the FIRST "cmd" bzw. "line of the sed-script", BUT continues with the NEW line with the cmd AFTER "n" !!
		/OR "b" which branches to label bzw. start of the script if no label, so the rest of the cmds are ignored! so NOT NF !
	---! commands that change flow control, so NOT-normal-flow: d, n, b (bzw. D,N,t):
		n/N : CONTINUE from current cmd-position after n/N for the NEW line! does NOT go back to the first cmd after reading a NEW line, but continues from cmd after n/N
		d/D : JUMP to the first cmd after deleting. the rest of cmds after d/D are NOT applied any more to the PS, because it is deleted
		b/t : JUMP to the LABEL or to First-line if no label.. so NOT all cmds are applied to all PS.
	--- verhalten of CF-cmds and relevant points: 
		1- what is the next command which will be executed? fo back the the first cmd OR continue from current cmd-position??
		2- will the current PS will be printed/cleared, before their action (eg before deleting d/D , or before reading the next line n/n, ...)??
		- cmds of CF and their verhalten:
		- Do.Ouput.PS, Clear.PS, Readin.next.line,  go.Back.to.first.cmd/to.first.line.of.Script:
		-------------------------------------------------------------------------------------
		/d	-	Y	Y	Y	
		/D	-	Y-\n	If.PS==empty	Y	
		/n	Y	Y	Y	N	next.cmd.after.n
		/N	N	N+append	Y+\n	next.cmd.after.N

	_______:  hold + pattern-space/-buffers handling (yank+put):
	h	: Copy into hold space; overwrite the hold space:  Copy the pattern space into the hold space, a special temporary buffer. The previous contents of the hold space are obliterated. You can use h to save a line before editing it.
	H	: Copy into hold space; append to what's there.:   Append a newline and then the contents of the pattern space to the contents of the hold space. Even if the hold space is empty, H still appends a newline. H is like an incremental copy.
	g	: get/Paste the contents of the hold space back into the pattern space, overwrite the previous contents of the pattern space.
	G	: get/Paste+append: Same as g, except that a newline and the hold space are pasted to the end of the pattern space instead of overwriting it.
	x	: Exchange contents of the hold and pattern spaces.

	_______:  next-line:
	--- COntrol-Flow for n/N :
	"n" / "N" : -->  Not-Normal-Flow (CF) : after reading a line continues with the NEXT cmd after n/N !
	outputs the contents of the pattern space and then reads the next line of input WITHOUT returning to the top of the script. 
	Control passes to the sed-cmd following "n" instead of resuming at the top of the script. --> see notes for "n" below!
	so after reading a new line it does NOT go to the FIRST "cmd" bzw. "line of the sed-script", BUT continues with the NEW line with the cmd AFTER "n" !!
	--- "n" / next line command:

	_______:  addressing,...:
	-! startLineNo"~"incremental.step  (firstline is 0 ; only gnu.sed) #eg: every third line starting with line.No.2:  2~3 ; #eg: only odd-lines: 1~2 #eg: every fifth lines 0~5
	- only lines between first line containg "300" up to line containg 500, do transating 0 to 2 and 3 to 9:  sed -e "/300/,/500/y/03/29/" t1.txt
	- from line containing "300" print out 2 lines (and no other lines):  sed -n -e "/300/,+2{p}" t1.txt  #bzw. same.as:  sed -n -e "/300/{N;N;p}" t1.txt
	- NOT containg xxx lines:  '/xxx/!' ;eg print all lines NOT ending with "EEE":  sed -ne '/EEE$/!p' t1.txt

	_______:  append/insert:
	- append a new line "bbb" after ALL lines containing 300:  sed -e "/300/a bbb" t1.txt
	- append before  after ALL lines containing 300: sed -e "/300/i bbb" t1.txt

	_______:  replacing/substitution/search.replace
	- "oder" == "\|" (gnu-sed) : eg replace all "2" OR "4" with "x" : sed -e 's/2\|4/x/g' t1.txt   ##-so NOT just "|" but "\|"
	- addressing: replace in all lines NOT containg xx , a with b :   sed -e '/xx/!s/a/b/g'  t1.txt
	- from line containing "300" + 2 lines, replace these lines with the text " aaa\nbbb":  sed -e "/300/,+2c aaa\nbbb" t1.txt
	- numbered.based.actions: replacce "- "+3.chars after it with xx: sed -e "s/- .\{3\}/xx/"  t1.txt

	_______:  deleting:
	- from line containing "300" + 2 lines, delete these lines:  sed -e "/300/,+2d" t1.txt

	_______:  
	- jede zweite Zeile print (nur gerade-line-numbers):  sed -n "n;p" t1.txt
	- reverse line-orders printout:  sed -n -e '1{h;n};x;H;${g;p}' t1.txt  ##-emulates "tac" cmd
	- whole-file as one line/string without linebreaks;   sed -n -e 'H;${g;s/\n//g;p;q}' t1.txt
	- whole-file as one line/string without linebreaks in reverse line-order; sed -n -e 'x;H;${g;s/\n//g;p;q}' t1.txt

	_______:  countings:
	- \{n,m\} (so WITH "\" )  :#eg:  .\{81\} genau 81 chars;  
--############################# 2007.pre-nts: #################################################
##________________________________________  ___________________________


#####  ==========  sed:
- see:
	-!! check gnu additional params!! man sed , info sed !!
	-! shell.by.exp.4ed: Table 5.1. sed Commands
	- pement online script examples
	- here  0devNts/ux/seds.xls
	- Ore: pocketRef + sed-awk-book
	- man pages, gnu-docs

	_______:  !!!:  (notes, tricks, common mistakes,...):
	- in cmds '...{...;}' do NOT forget the last ';' before '}' ,it is always a MUST, otherwise grabbled commands message!!
	- {...} in cmdLines:  sed -n -e "1{p;d;}" f1.txt  : all lines  <-> but  sed -n -e "1p;d" f1.tx  : print only the first line!
	- Dos-cmdLine: in dos must use " instead of ' in -e ...

	_______:  addressing:
	- /north/,$p	:print from line containing "north" to EOF
	- /north/,/south/p	:print from line containing "north" to the line containing "south"
	- sed -n '5,/^northeast/p' datafile		:Prints the lines from line 5 through the first line that begins with northeast.
	- sed '1,3d' myfile		:delete lines 1-3
	- sed -n '/^bb/,/^ww/p' f1.txt	: print out from line starting with bb to line startintg with ww
	- sed '/west/,/east/s/$/**VACA**/' datafile		:For lines in the range between the patterns east and west, the end-of-line ($) is replaced with the string **VACA**. The newline is moved over to the end of the new string.

	_______:  exps,colls,usages,commands,options, ... :
	-! sed '/eastern/{ n; s/AM/Archie/; }' datafile   :
	-! several inline-commandsd: sed -e '/WE/{h; d; }' -e '/CT/{G; }' datafile   :NOTE: watch space in {...; }
	-! sed '/east/,/west/s/North/South/' filex   :For any lines falling in the range from east to west, substitutes North with South.
	- reading a file into the curr-file:  sed '/Suan/r newfile' datafile :
		The contents of newfile are read into the input file datafile, after the line where the pattern Suan is matched.
	- sed 's/....//' filex  :Deletes the first four characters of each line.
	- sed 's/...$//' filex  :Deletes the last three characters of each line.
	- writing into a file: sed -n '/north/w newfile' datafile  :All lines containing the pattern north are written to a file called newfile
	- sed  '/^bb/a test-text' f1.txt	: append to lines starting with "bb"
	- sed  '/^bb/d' f1.txt	: delete lines starting with "bb"
	- sed '3d' datafile	:delete 3rd line
	- sed '3,$d' datafile	: third line through the last line are deleted
	- sed '$d' datafile	: delete last line
	- sed '/Tom/!d' file : delete lines NOT containing Tom
	- wc -l ::  sed -n '$=' f1.txt

	_______:  using loop-veriables for addressing in cmdLine, eg reading file names from a file for mv command:
	- just test the output (see echo part!): for i in  1 2 3  ; do  sed -n -e `echo $i`p  filenamesFile ; done
	- using a addressing-variable/j and looping over all files in the current dir:  let j=1 ; for i in *; do echo $i -- `sed -n -e $(($j))p list1` ; let j+=1 ;done

	_______:  Env-vars in shells and sed:
	- eg in sh:  sed -e '/'"$env_var"'/p'

	_______:  commands:
	-!! control flow:
		1- goes back ot the beginning of script:  d,
		2- continues from the current position:   the rest (n,...)
	-! d  :does NOT touch the holdspace; after d holdspace is still unchanged; do goes back to the scriptStart; so:
		"d" :deletes line(s) from pattern space. Thus, the line is not passed to standard output (even without -n ). A new line of input is read and editing resumes with first command in script. so:
		"d" :delete patternSpace + no output + readin newline + goto-scriptStart; the holdspace remains unchanged for the next loop !!

	_______:  cmdLine invok:
 	- multi-sed-comands eg: no-range: sed -e 'x;G;p' file ;with-range:  sed -e '/regex/{x;p;x;}'  file
	-e- setting label (a) and jumping to it eg: sed -e :a -e 's/^.\{1,78\}$/ &/;ta'  (align all text flush right on a 79-column width)
- hex/oct (only gsed >3.02.80): \xhex \ooct eg. \x0D == \o015 == <CR> (std-sed knows no hex/ascii code); more eg. see sed-pement/dos-convertions

	_______:  Comments-deleting in a source code: hier eg. xml-file with <!-- ... --> as comment-signs; otherwise replace them with appropriate:
	- sed   -e 's/<!--.*-->//g'  -e '/^[[:blank:]]*<!--/,/-->/d' -e '/^[[:blank:]]*$/d' server.xml >| nocomments.multilines.server.xml
			-->so no comments, but still multiline tags; hier putting allt tags in one line:
	- sed -n  -e '/>/{H;s/.*//;x;s/\n/ /g;p;d;}' -e '/>/!H'  nocomments.multilines.server.xml >| nocomments.server.xml
	-- discussion:
		-! first delete always one-line-comments seperately as the very first command, otherwise you'll loose code-lines!!
			so WRONG: sed  -e '/<!--/,/-->/d' ... deletes in case of one-line-comments, several line up to the end of the next comment line!!!
		-! mixed lines (code + coments), do:
			-! consider mixed-lines: code+comments, that's why first substitute onliners!!

	_______:  DOS Text Conversion And Substitution: see pement converting masters for diferent shells/envs !
 --- exp-sed:
	- change/modify all html-files in current directory:   for i in *.htm*; do sed -e 's@xxx/@yyy@g' $i > _tmp ; mv _tmp $i; done
	- % somecommand  | sed 's/old/new/' |  othercommand
	- % sed -e 's/old/new/' -e '/bad/d' myfile
	- % sed 's/old/new/; /bad/d' myfile  : Or you can use semicolons (;), which are a sed command separator
	- % sed -f scriptfile myfile
	- Compare/Check differences before changing:  sed -f sedscr.txt  myfile | diff myfile  -
	- deletes from the first line up to the first blank line:    sed  1,/^$/d  file.txt
	- delete all except line 3-8: sed 3,8/!d  file.txt
