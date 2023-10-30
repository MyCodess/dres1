_________ docs mysql ______________________________________________
##________________________________________  ___________________________


#####  ==========  links (see opera BMs):
	 http://dev.mysql.com/downloads/
##________________________________________  ___________________________


#####  ==========  mysql.help.online.on.system in mysql-client:
	- filling mysql-help-system if not done:  mysql -u mysql < fill_help_tables.sql  ##(eg suse in /usr/share/mysql/)
	-! in mysql.shell is all there!!:  mysql> help contents , ...
	-!  mysql>  help contents
	- show tables from mysql like '%help%'  ##- check if they are there and are full!?
	  otherwise fill them with download of fill_help_tables-5.5.sql  and: shell> mysql -u root  mysql <  ./fill_help_tables-5.5.sql
	- search in online-help also by vi fill_help_tables-5.5.sql  ; BUT with  "mysql> help ..." is just more beatufied.
##________________________________________  ___________________________


#####  ==========  docs.online.on.System /live-helps:
	-!! docs/mysql.info : WHOLE-Ref-Manual in info-format!! (in the Binary.tar.file mysql-5.5.15-linux2.6-i686__genericLx32.tar.gz at least is do; can be extracted ang copied/accessible with info ...)
	-!! man-dir in binary mysql-5.5.15-linux2.6-i686__genericLx32.tar.gz
	-!! many docs online.on.system !! as man/info!! also whole manual as info online!!
		- see rpm -ql mysql-xxxxx ...
		- u1@vo17:/usr/share/man $findin . mysql
##________________________________________  ___________________________


#####  ==========  help/docs/...:
	-!! html2text/kk.grep.version: from single.HtmlPage/mysql.info/chapters.Html/epub/...: 
		mkdir-tree if needed: find . -type d ! -name '[.|..]' -exec mkdir -p ../../0_txt_refmysql51/refman-5.1-en.html.txt/{} \;
		find . -type f -iname '*.htm*' -exec html2text  -utf8 -width 109  -o ../../0_txt_refmysql51/refman-5.1-en.html.txt/{}.txt  {}  \;  ##-I- by suse-version were problems due to -nobs
##________________________________________  ___________________________


#####  ==========  listings/...:
	-!! utils-/cmds-mysql-Listings: see refmanual: 4.1. Overview of MySQL Programs : for cmds/scripts/daemons/....
