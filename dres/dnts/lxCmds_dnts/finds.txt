__________ find-ux __________
##________________________________________  ___________________________


#####  ==========  find:
- size-sum (eg): printout the sum-size of all files newer than fileXX :
	find . -type f -newer fileXX  -printf "%s+"
	then: bc1 'output of previous find'
- delete from this dir downwards everything excep eg zip-files in the current dir:
	find . \(  ! -name "*.zip" ! -name . -prune \)  -exec rm -rf {} \;
- finding files with suid set: find . -perm -4000 -print  (or for setgid -perm -2000)
- use also locate or even lsof sometimes instead find !
- search through a large directory with lots of subdirectories to find all of the .java files that call the method GetRaw( ):
	- ausfhrlich mit line ausgabe: % find . -name \*.java -exec grep -in "GetRaw(" {} \; -print
	- Short: .... grep -l    (jew. mit oder ohne -i)
- Duplicating the directory tree (empty):
	- in GNU (recognizes {} in combinations): find . -type d -exec mkdir /usr/project/{} \;
	- non-GNU ({} alwayas seperated):
		- find . -type d -print | sed 's@^@/usr/project/@' | xargs mkdir  /OR:
		- find . -type d -print | sed 's@^@mkdir @' | (cd /usr/project; sh)
	- in Dos/Win (in "" because of \ ):	find . -type d -exec mkdir "..\t1\{}" ;
- locate/slocate:
	-! wildcard in locate query is like in shell-filnames BUT including "/"; so slash has no special meaning:
		- slocate -d maydb "*/bin"  :find-all dir ending in bin
		- locate '*/bin/*'  :match the files in a directory named bin, but not the directory itself
		- locate '/home/*~'  : anything beginning at /home/ ending in ~ , also in subdirectories
		- -e for exclude directories works only if the path has the exact textual for as the path of -U (or both are absolute path); so very limited
		- also ? and [] ,... as i shell
	- building database (maybe per dir/drive/...):	updatedb --localpaths='root-dir-1  dir2 ...' --output=db1
	- usage:  locate  --database=db1  <pattern> /OR:
	  use my alias locatea /OR ln -s $locateDB  /var/lib/slocate/slocate.db
- Your own locate/db:
	- (cron job?): find <root-dir> -print > <db-name>  ; OR: find <root-dir> -ls > <db-name>
	- later search in it: grep -e <search-pattern> <db-name>
- all text types (e.g. for dos2unix or for sed, ...):
	find  .  \( -name "*.properties" -o -name "*.java"  -o -name "*.sh"  -o -name "*.cmd"  -o -name "*.xml"  -o  -name "*.txt"  -o  -name "*.autoConfig"  -o -name "*.config" -o -name "*.sed" \)  -exec dos2unix -U {}  \;
- traverse the tree except e.g. doc and etc subdirectories:
	- find . \( -name doc -o -name etc \) -prune -o -print
	- find /path -exec test {} = /foo/bar -o {} = /foo/baz \; -prune -o print
- duplicate directory tree (empty):
	- GNU:  % find . -type d -exec mkdir /usr/project/{} \;   otherwise (due to no space before {}):
	- find . -type d -print | sed 's@^@/usr/project/@' | xargs mkdir
	- find . -type d -print | sed 's@^@mkdir @' | (cd /usr/project; sh)
- Absolute /fully qualified path of a dir:  ABSOLUT_PATH=`cd $ANT_HOME && pwd`   #the current PWD will NOT be changed. it happens in a subshell
##________________________________________  ___________________________


#####  ==========  old-find (non-Lx, simple):
- grep-find with filename-printout /old-style :   find . -exec grep -i  myword {} /dev/null \;
