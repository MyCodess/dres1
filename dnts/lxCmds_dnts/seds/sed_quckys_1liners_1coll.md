_____________ sed one-liners quickies, short scripts,... _____________
-!! here only most favorite... one-liners/short-scripts/....
	- for more see:
	- pement_exp_sed.txt  in   w/docs/Unix/SEDs/pement_exp_sed.txt
	- pement/sedfaq4.html  in  w/docs/Unix/SEDs/Pement_Seds/faq_sed_SF_pement/sedfaq4.html
	- /sed_manual_Ref.html#Examples    in  w/docs/Unix/SEDs/sed_manual_Ref.html#Examples
	- devres/codesColl_devres.. (not much there yet, but comes...)

	_______:  put ALL line between two tags (here eg "itemX") together: (good eg for structured texts, as xml-files,...):
sed -ne '$ba;/^itemX/!{H;d};:a;x;s/\n/ :: /g;p;' t1.txt
/bzw. with the branch-label  "a"  ausgeschrieben as  "lastline" :
sed -ne '$blastline;/^itemX/!{H;d};:lastline;x;s/\n/ :: /g;p;' t1.txt

	_______:  numbering file lines in one line and aligned right  (like cat -n)
- not aligned, but then for files of all sizes:
sed -e "v;="  t1.txt | sed 'N;s/\n/:  /;'
- aligned with "0" up to four-digit of linenumbers (for longer files, more than 4 digit for line numbers, just put more dots in  \(....\) ):
sed -e "v;="  t1.txt | sed 's/^/000000000/;s/.*\(....\)/\1/;N;s/\n/:  /;'
- aligned with space up to four-digit of linenumbers
sed -e "v;="  t1.txt | sed 's/^/       /;s/.*\(....\)/\1/; N;s/\n/:  /;'

	_______:  newlines-replacement/deleting :
- replace all \n in the whole file with space:  sed ':a;N;$!ba;s/\n/ /g' file
	explanation:
	:a create a label 'a'
	N append the next line to the pattern space
	$! if not the last line, ba branch (go to) label 'a'
	s substitute, /\n/ regex for new line, / / by a space, /g global match (as many times as it can)
	sed will loop through step 1 to 3 until it reach the last line, getting all lines fit in the pattern space where sed will substitute all \n characters
