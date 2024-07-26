___________________ gunu-tar-nts_RF __________________________________________________
- see also ch-38+39--UPT3

	_______:  --  kk-testing-trying of "--exclude-xxx" option of tar : checked by kk /150300/gnu-tar/ubuntu-14.10 :
  /home/i1/te1/  dir containts the uue-exclude-tag-file  "NoBup1_flg.txt " :
-OK2-default-kk:  tar-ed also xxx-dir/NoBup1_flg.txt but nothing more there!  :
	tar --one-file-syste   --exclude-caches  --exclude-tag="${uueNoBupFlagFN}"  --show-omitted-dirs  -cpzvf  i1-excl-test-$($cudts).tgz   $@   ##--I-take out --exclude-caches if want onlly uue-excludes!
- tar-excludes-try-check-test--infos:
-OK2-better: tared also home/i1/te1/NoBup1_flg.txt : tar --one-file-syste   --exclude-caches  --exclude-tag="${uueNoBupFlagFN}"  --show-omitted-dirs  -cpzvf  i1-excl-test-$($cudts).tgz   $@
-OK1b- no dir /home/i1/te1/ at all! :  tar --one-file-syste   --exclude-caches  --exclude-tag-all="${uueNoBupFlagFN}"  --show-omitted-dirs  -cpzvf  i1-excl-test-$($cudts).tgz   $@
-OK1a- nothing under home/i1/te1/ :  tar --one-file-syste   --exclude-caches  --exclude-tag-under="${uueNoBupFlagFN}"  --show-omitted-dirs  -cpzvf  i1-excl-test-$($cudts).tgz   $@
-OK0-putNoBupFlag.sh-resurvicely:    find /home/  -type d  \( -iname "*trash*" -o -iname "tmp" -o -iname "*thumbnails*" -o -iname "*cach*" -o -iname .chmsee -o -iname .beagle -o -iname .adobe -o -iname .macromedia \) -exec putNoBupFlag.sh {}  \;

	_______:  -- mainly from  ch-38+39--UPT3 :
-! also see/use perl-utils:   ptardiff , ptargrep , ptar
- tar all files newer than xxx-date (!! not -N but --newer-mtime ; N considers any actions,, not only changed/modified; older/not-gnu variant with find see next points):
	- tar  -cvf t1.tar --newer-mtime=20040925  ./tmp  (for date format see gnu-manual. is not in man-page!!) /OR: better if date starts with . or / , it is considered as the timestamp of the file
	- tar  -cvf t1.tar --newer-mtime=./last-backup-timestamp-file.txt  ./tmp
- find+tar for certain files/pre-selection (problem with filenames containing space,specialChar; so must be print0 + xargs), eg:  find ./myDir -print0 | xargs -0 tar -zcvf myDir.tar.gz
- use -k by extarcting: keep existing files; do not overwrite them from archive
- never create an archive of a directory that starts with slash (/) or tilde (~), due to reconstruction problems. Avoid using absolute paths when you create an archive.GNU tar. It strips the leading / by default when creating archives.
- wildcards & tar (see UPT3 38.10):  GNU tar understands wildcards in the names of files within an archive
	- non-gnu-tar: extracting some files/path with wildcards: tar -xvf tarfile.tar `tar -tvf arfile.tar  |  egrep  'lib/(foo|bar)'` ;replace  'lib/(foo|bar)' with your <searchword-filaneme>
- If you want to archive several directories without starting "/", you can use several -C options:% tar c -C /home/mike ./docs  -C /home/susan ./test
- permissions by extracting: tar -x ... places all the original files into it, with the same permissions as found on the original system. The new files will be owned by the user running tar xvf (you) unless you are running as root, in which case the original owner is generally preserved. Some versions require the o option to set ownership.
- recursively extract/unzip all the files and the files contained within them (is for zip-files! adapt it for tgz files): while [ "`find . -type f -name '*.zip' | wc -l`" -gt 0 ]; do find -type f -name "*.zip" -exec unzip -- '{}' \; -exec rm -- '{}' \;; done
