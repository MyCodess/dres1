__________ renaming files/trees, with sed,.... __________
##________________________________________  ___________________________


#####  ==========  Files and Dir names: Renameing/Moving/changing/.... collectively processing:
- first try it with echo instead of command (e.g. mv)
- change all suffixes: (eg. all .tar to .tbz): for i in *.tar; do mv -iv $i `basename "$i" .tar`.tbz ;done

	_______:  upper-to-lower with "tr" for files/dir-names in the current dir (surronded by " due to spaces or spec.chars):
	- for i in *; do mv -v "$i"  "`echo $i | tr [A-Z] [a-z]`"         ; done  /OR:
	- for i in *; do mv -v "$i"  "`echo $i | tr [:upper:] [:lower:]`" ; done
-- replacing certain chars with "tr" (eg. eliminating "&" in: mv "Pop & Wave 6 - 2 (99)"  "Pop n Wave 6 - 2 (99)" ):
	- for i in *\&* ; do mv "$i" "`echo $i | tr \& n`" ; done
	- e.g. replacing all sspaces in filenames:  for i in *\ *; do mv -iv "$i" "`echo $i | sed -e 's/ /_/g' `"; done
	- in tr space is \
	- to delete chars use -d e.g. to delete this special chars use:   tr -d ",.\!?;:\"\'`"
- "sed" command variation, e.g.: changing all *xxx* files to *yyy*  file names (for including subdirectories, use find or ls -R, ...):
	- for i in *xxx*; do mv -v "$i"  "`echo "$i" | sed -e 's/xxx/yyy/g'`"  ;done    (" is to avoid  space/leerraum problem ; or use instead " then xargs -O as further below), e.g:
		for i in *.html; do mv -iv "$i" `echo "$i" | sed -e 's/^[0-9]*-//'`;  done;
	------- [UPT3 -10.9] Renaming, Copying, or Comparing a Set of Files (Using sh -v Section 27.15) will show the commands as the shell executes them):
	$ ls -d *.new | sed "s/\(.*\)\.new$/mv '&' '\1.old'/" | sh            (or c-shell: % ls -d *.new | sed 's/\(.*\)\.new$/mv "&" "\1.old"/' | sh)
	Following method works for ANY Unix command that takes a pair of filenames. For instance, to compare a set of files in the current directory with the original files in the /usr/local/src directory, use diff:
	% ls -d *.c *.h | sed 's@.*@diff -c & /usr/local/src/&@' | sh
	Note that diff -r does let you compare entire directories, but you need a trick like this to only compare some of the files.
	- Note: if from the command line --> all sed -e ... must be in '....'
- sed+xargs variation:
	----- [UPT3 -9.17]: The GNU version does expand {} in the middle of a string. So this works fine for GNU-find:
	% find . -type d -exec mkdir /usr/project/{} \;
	On versions that don't, though, the trick is to pass the directory names to sed  , which substitutes in the leading pathname:
	% find . -type d -print | sed 's@^@/usr/project/@' | xargs mkdir
	% find . -type d -print | sed 's@^@mkdir @' | (cd /usr/project; sh)
	------ SPACES:
	- xargs may have problems with filenames that contain embedded spaces. (Versions of xargs that support the -0  option can avoid this problem
	- find ... -print0 does also the same, so: prints the full file name on the standard output,  followed by  a  null character instead of newline.
