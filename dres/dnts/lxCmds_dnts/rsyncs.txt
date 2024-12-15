_______ rsync devnts + coll + samples .... ________________________
##________________________________________  ___________________________


#####  ==========  syncing two DIR nts:
	---! "/"  trailing slash on the <source> :   eg  rsync -avz foo:src/bar/ /data/tmp  :
		trailing slash on the source to avoid creating an additional directory level at the destination.
		- rsync -r  ./src1    /tmp/target1   ##--> it generates  /tmp/target1/src1/... tree
		- rsync -r  ./src1/   /tmp/target1   ##--> it generates  /tmp/target1/... tree , so putting all files from  ./src1/* into  /tmp/target1/  without generating the subdir src1 !!
		- You can think of a trailing / on a source as meaning “copy the contents of  this directory”  as  opposed to “copy the directory by name”, but in both cases the attributes of the con- taining directory are transferred to the containing directory on the destination.  #-see man
	---!  -no-XXX  :
		- You may turn off one or more implied options by prefixing the option name with “no-”. see: man  /--no-OPTION
		- works with both short+long-option-name, eg  --no-R is the same as --no-relative
		- The  order  of the options is important!
	---! -a :
		-! -a does NOT imply -H (for Hardlinks) !!
		-! -a combined-with  --no-XX  :   want to use -a (--archive) but don’t want -o (--owner),  instead  of  converting -a into -rlptgD, you could specify -a --no-o (or -a --no-owner). The  order  of the options is important!!
	--- permissions/chmod:
		- see man   /--chmod (spec. -D for Dirs and -F for files),  /--perms
##________________________________________  ___________________________


#####  ==========  links/SymLinks/HardLinks-handling:
	-! see man /^SYMBOLIC LINKS
	-! default : symbolic  links  are NOT transferred at all !
	- --links : duplicate symlinks as symlinks!
	-! Hard-Links:  -H : find out the Hardlinks in src and jsut do also a hardlink in target, so do NOT copy the file; without -H a hardlink file is handeled as a normal file and will be tranfered fully.
##________________________________________  ___________________________


#####  ==========  DIRECTIONs:
	--update , -u : keep newer files in target-dir (so in target-dir is more uptodate), so:  rsync -ru ....
	--existing    : skip creating files (including directories) that do not exist yet  on  the destination --> ONLY dest-listing is to be synced (ignore files not existing in DEST, even if they exist in SRC !)
	--ignore-existing  : skip updating files that already exist on the destination (this does not ignore existing directories, or nothing would get done).
	--remove-source-files  : This tells rsync to remove from the sending side the files (meaning non-directories) that are a part of the transfer and have been successfully duplicated on the receiving side.
	--delete  : This  tells  rsync to delete extraneous files from the receiving side (ones that aren’t on the sending side), but only for the directories that are being synchronized.
	   !You must have  asked rsync  to  send  the  whole  directory (e.g. “dir” or “dir/”) without using a wildcard for the directory’s contents (e.g. “dir/*”) since the wildcard is expanded by the shell and rsync thus gets  a request to transfer individual files, not the files’ parent directory.  #see man /--delete
	--delete-before , --delete-during , --delete-delay , --delete-after , --delete-excluded , ... --delete-XXX
##________________________________________  ___________________________


#####  ==========  usefull options more:
	--- dry/verbosity/more-control/listings/progress/logging:
		-n, --dry-run  +  -v , --verbose
		--list-only
		--progress : show progress-line
		--only-write-batch=FILE  ,  --write-batch=FILE  ,  --read-batch=FILE
		--log-file=FILE , --log-file-format=FORMAT
		--stats : statistics printing
	-O, --omit-dir-times  : specially for NFS-/NW-Shares
	-x, --one-file-system
	- MsWin-vfat-problem / --modify-window : if transfering to/from vfat-parts, then probably need to set it to 5 or so..., eg  --modify-window=5  (vfat has a delay of 2 sec.;  modify-window=5 allows times of src-/target-files to differ by up to 5 seconds)
	- additional-DIRs to add to syncs:  --compare-dest=DIR , --copy-dest=DIR, --link-dest=DIR , .... 
	--delay-updates : first transfer files/files-diffs FULLY, and then rename the target-old-files (kind of DB-atomic-transaction)
##________________________________________  ___________________________


#####  ==========  filtering/exclude/include...:
	-! see man : /^FILTER RULES  /^INCLUDE/EXCLUDE PATTERN RULES  ...:
	--max-size=SIZE : skip transfering files > SIZE  ; also see --min-size=SIZE
	-C, --cvs-exclude  : !! is more than just cvsv!! see suffixes there! so alo excludes:  *.old/.orig/.svn/.git/....
	-f, --filter=RULE ; see also FILTER RULES section
	--exclude=PATTERN , --exclude-XXX=PATTERN
	--include=PATTERN , --include-XXX=PATTERN
	--files-from=FILE  : exact file-listing
##________________________________________  ___________________________


#####  ==========  "cp"-replacement, copying instead sync : so using rsync as an advanced "cp ...." (with tree-options):
	- simple copying:   rsync -r  ./d1  /tmp/   ;#OR remote:   rsync -r  ./d1  rdswsd008:/tmp/d08
	  also backup the existing files in target (rename existing target-files int XXX~ ):  rsync -r -b .... #see --backup , --backup-dir=DIR , --suffix=SUFFIX
	---!! path-preserving-copy command (copy.with.path, like cpPathed.sh):   copying files preserving their source-relative-path (implied directories) :
		-! see #see man rsync /--relative  /--no-implied-dirs
		- use  -R, --relative  #eg: rsync -avR /foo/bar/baz.c remote:/tmp/  #see man /--relative
		- eg:  rsync d1/d11/aa.txt /tmp/d1/  results in /tmp/d1/aa.txt  ;BUT  rsync -R  d1/d11/aa.txt /tmp/d1/  results in /tmp/d1/d1/d11/aa.txt
		-! possible to take ony a Part of the relative-path: insert a dot and a slash into the source path
		   eg remote+trick for relative-path:   rsync -avR /foo/./bar/baz.c remote:/tmp/  #--> /tmp/bar/baz.c  #see man   /--relative
		   for older versions, you must use cd :  (cd /foo; rsync -avR bar/baz.c remote:/tmp/)
		- 
##________________________________________  ___________________________


#####  ==========  remotes:
	- copy to remote machine:   rsync -r  ./d1  rdswsd008:/tmp/d08
