_________ MySql nts __________________________
-! Ref.Manual.mysql.5.1:  refman-5.1-en.a4.pdf (here all chapters/pages/tables/figs/... refers mainly to this!)
	-!! info mysql #-I manual also as info full online available!!
##________________________________________  ___________________________


#####  ==========  docs.OL.onSystem:
-!! html2text/kk.grep.version: from singleHtmlPage/mysql.info/chaptersHtml/...: 
	mkdir-tree if needed: find . -type d ! -name '[.|..]' -exec mkdir -p ../../0_txt_refmysql51/refman-5.1-en.epub.unp.txt/{} \;
	find . -type f -iname '*.htm*' -exec html2text  -utf8 -width 109  -o ../../0_txt_refmysql51/refman-5.1-en.epub.unp.txt/{}.txt  {}  \;  ##-I- by suse-version were problems due to -nobs
-!! docs/mysql.info : WHOLE-Ref-Manual in info-format!! (in the Binary.tar.file mysql-5.5.15-linux2.6-i686__genericLx32.tar.gz at least is do; can be extracted ang copied/accessible with info ...)
-!! man-dir in binary mysql-5.5.15-linux2.6-i686__genericLx32.tar.gz
-!! many docs online !! as man/info!! also whole manual as info online!!
	- see rpm -ql mysql-xxxxx ...
	- u1@vo17:/usr/share/man $findin . mysql
-!! in mysql.shell is all there!!:  mysql> help contents , ...
--########### files/configs/...  on vo17.suse10.4.mysql.5.1--1108: ##################
-!! cmds-/utils-Listings one-liners: see refmanual: 4.1. Overview of MySQL Programs : for cmds/scripts/daemons/....
##________________________________________  ___________________________


#####  ==========  start/stop of Server/mysqld/Daemon (not DBs but whole daemon/service mysqld)
- see refman:
	4.3. MySQL Server and Server-Startup Programs
	5.1. “The MySQL Server”
- mysqld_safe starts the mysqld and is the recommended way to start a mysqld server on Unix 
- /etc/init.d/mysql  start/stop/status/...    ## in docs: mysql.server scripts
- start-safe    mysql@vo17:~ $ mysqld_safe &  ##-OR- as root: mysqld_safe --user=mysql &
- stop/shutdown:
	/etc/init.d/mysql  start/stop #/OR:
	mysqladmin -u root shutdown
- auto-restart of service:
	 chkconfig --level 345 mysql on #/OR:
	 manualy put "ln -s" of /etc/init.d/mysql in appropriate  /etc/init.d/XXX-DIRs
- suse.114: mysqld         mysqld-debug   mysqld_multi   mysqld_safe    mysqldump      mysqldumpslow ...
- runtime-infos:  ll /var/run/mysql/  ##- current pid,.../in suse; default.refdocs: pid in data-dir
##________________________________________  ___________________________


#####  ==========  config-files/option-files/params/options/...:

	_______:  --  config-files-mysqld-server:
	-!! manref: 4.2.3.3. Using Option Files (bzw. info mysql ...):  
	- Chapter 5. MySQL Server Administration --> ausfuehrlich! params,....
	-! If multiple instances of a given option are found, the last instance takes precedence. 
	-! On Unix platforms, MySQL ignores configuration files that are world-writable. 
	-! option-file-params the same as commandline-params of the util, but without "--"
	-! example-files in /usr/share/mysql/*.cnf (mysql-community-server-5.1.53-4.7.1.i586.rpm)
-- UNIX  --File Name--       --Purpose--  UNIX:
	/etc/my.cnf          Global options
	/etc/mysql/my.cnf    Global options (as of MySQL 5.1.15 and earlier)
	SYSCONFDIR/my.cnf    Global options
	$MYSQL_HOME/my.cnf   Server-specific options
	defaults-extra-file  The file specified with `--defaults-extra-file=PATH, if any
	~/.my.cnf            User-specific options
-- MsWins --File Name--       --Purpose--  MsWins:
	WINDIR\my.ini,       Global options
	WINDIR\my.cnf        
	C:\my.ini,           Global options
	C:\my.cnf            
	INSTALLDIR\my.ini,   Global options
	INSTALLDIR\my.cnf    
	defaults-extra-file  The file specified with `--defaults-extra-file=PATH, if any

	_______:  -- suse.114.species/addies:
	-! see /etc/my.cnf
	-!! datadir bzw. mysql-home:  /var/lib/mysql  ( see /etc/my.cnf : datadir = /var/lib/mysql)
		DBs will be created here!! in datadir !!
	-! /var/log/mysql/mysqld.log  ##-!!- mkdir /var/log/mysql  if not exist, before starting server!!
	- zypper in ... (see coll-file)
	see /etc/my.cnf
	/etc/mysqlaccess.conf
	/etc/mysql
##________________________________________  ___________________________


#####  ==========  Logs/Redo-Logs of Server: 5.2. MySQL Server Logs

	_______:  log-files:
	- By default, all log files are created in the data directory.
	suse: also /var/log/mysql
	- log-files-location?:  mysqladmin variables | grepi log ; also see /etc/my.cnf
	- 

	_______:  log/Redo-types:
	-- Log Type --	:	 -- Information Written to Log --
	Error log 		: Problems encountered starting, running, or stopping mysqld
	General query log 	: (~ ora-redo-logs)Established client connections and statements received from clients
	Binary log 		: All statements that change data (also used for replication)
	Relay log Data 	: changes received from a replication master server
	Slow query log 	: All queries that took more than long_query_time seconds to execute or did not use
##________________________________________  ___________________________


#####  ==========  ! redo.logs / General Query Log (protocol aller sql-stmts,.. for redo/spiegelung/backup):  5.2.3. The General Query Log
	- add to /etc/my.cnf of in cmdline starting ot mysqld with redolog-params:
		--general_log=1    general_log_file=file_name  #!! BOTH MUST be set!
	- As of MySQL 5.1.29, use --general_log[={0|1}] to enable or disable the general query log, and optionally -general_log_file=file_name to specify a log file name. The --log and -l options are deprecated. : see 5.2.3. The General Query Log
	- disabling redologs at runtime: mysql> SET GLOBAL general_log = 'OFF';
	- enabling redolog: SET GLOBAL general_log = 'ON';
##________________________________________  ___________________________


#####  ==========  admins-utils/cmds-db: see s Chapter 5, MySQL Server Administration.

	_______:  see
	-!! see refmanual: 4.1. Overview of MySQL Programs
	-!! see Chapter 5. MySQL Server Administration

	_______:  -- mysqld:
	-!! mysqld --verbose --help
	-!! querying current-config-params:   5.1.3. Server System Variables :
		mysqld --verbose --help	  ##--> will use: values that a server will use based on its compiled-in defaults and any option files that it reads, 
		mysqladmin variables      ##--> is using: what values a running MySQL server is using! /OR:
		SHOW VARIABLES            ##--> is using: current values used by a running server.
		mysqld --no-defaults --verbose --help  ##--> is compiled with: values that a server will use based on its compiled-in defaults, ignoring the settings in any option files
		-- more:
		SHOW [GLOBAL | SESSION] STATUS
	-!! CHECKING the effects of adapting pathes/vars by start: ref--2.12.1.3--155
		To check the effect of specifying path options, invoke mysqld with those options followed by the --verbose and --help op-
		eg:  mysqld --datadir=/data2 --verbose --help
		!! but --verbose and --help must be the last options.

	_______:  -- mysqladmin — Client for Administering a MySQL Server
	mysqladmin is a client for performing administrative operations
	mysqladmin --help
	mysqladmin -u root shutdown
	mysqladmin version
	mysqladmin variables
	mysqladmin ping      -->ora-dbping
	mysqladmin status/shutdown

	_______:  -- mysqlshow — Display Database, Table, and Column Information
	If no database is given, a list of database names is shown.
	mysqlshow  --help
	mysqlshow --user=root  mysql
	mysqlshow -u dbu1 db1   --> tables-list

	_______:  -- mysqlmanager — The MySQL Instance Manager
	can be used in place of the mysqld_safe script to start and stop one or more instances 

	_______:  -- ENVs:
	-!! Table 2.21. MySQL Related Environment Variables
##________________________________________  ___________________________


#####  ==========  mysql.shell-client/terminal (ore-sqlplus) : 

	_______:  see
	- Chapter 3. Tutorial
	-!! 4.5.1. mysql — The MySQL Command-Line Tool : options in 4.5.1.1 , commands on 4.5.1.2. , ...
-!!  mysql> help contents , ... --all helps/sql.syntax/user.mgm/... are there!!

	_______:  logins-mysql.shell:
	mysql -u dbu1 -h localhost --prompt='\U : '  world  ##-I with prompt-setting to user@db ! as sommand: prompt \U : ; OR as option in conf-file prompt=\U :   ##- see  Section 4.5.1.2, “mysql Commands”
	shell> mysql --help  ##-!! If you use a -p or --password option and specify the password value, there must be no space between -p or --password= and the password following it.:
	shell> mysql --host=127.0.0.1 --user=myname --password=mypass mydb  ##-/OR:
	shell> mysql -h 127.0.0.1  -u myname -pmypass mydb  ##-!! for localhost use IP-adresse! see 4.2.2. Connecting to the MySQL Server
	shell> mysql -u root/... -p ...

	_______:  ! help in mysql.shll:
	- see 12.8.3 “HELP Syntax” + 5.1.8. Server-Side Hel
	-!! if helps not there:  shell> mysql -u root mysql < fill_help_tables.sql  ##see 5.1.8. Server-Side Help
	-!! or just view fill_help_tables.sql : whole help-texts are there for mysql.shell (in suse: /usr/share/mysql/fill_help_tables.sql )
	mysql> help contents

	_______:  prompt:  4.5.1.2. mysql Commands , options: 4.5.1.1.
	- in config-file: prompt=... # eg prompt  = '\U \d: '  ## see 4.5.1.2
	- in cmdline: --prompt=.... # eg prompt='\U \d: '
	- in mysql> prompt ... ; eg:prompt \U \d: 
	- or ENV:  export MYSQL_PS1="(\u@\h) [\d]> "

	_______:  queris-db:
	mysql>  select database(), user();
	mysql>  show tables;   ==  $mysqlshow -u dbu1 db1
##________________________________________  ___________________________


#####  ==========  export/import/dump:
mysqldump --> also into sql-/text/csv/xml-files ....
mysqlimport --> also from text-files ...
LOAD DATA INFILE ...
##________________________________________  ___________________________


#####  ==========  setup-nts (see manual!! here just dummy...)
-!! in suse musste ich: mkdir /var/log/mysql/ ; chown mysql:mysql /var/log/mysql/
- user+group:   mysql group and the mysql user.
- datadir creation with : mysql_install_db script creates the server's data directory with mysql as
	mysql_install_db  script used to initialize the mysql database containing the grant tables that store the server access permissions.
	suse: /usr/bin/mysql_install_db  , man mysql_install_db
	- /OR more options eg :  scripts/mysql_install_db --user=mysql --basedir=/opt/mysql/mysql --datadir=/opt/mysql/mysql/data
##________________________________________  ___________________________


#####  ==========  debugs/errors/problems/follow/...:
- perror : ora-oraerr: A utility that displays the meaning of system or MySQL error codes. See Section 4.8.1, “perror — Explain Error Codes”.
- debug-version: mysqld-debug : use it instead mysqld to get more messages..., see Manual
	- eg suse: mysql-community-server-debug : MySQL server with debug options turned on
##________________________________________  ___________________________


#####  ==========  GUIs:
- Download MySQL Workbench : sql.client + Admin + DB-Modelling ...(was also in yast!): http://dev.mysql.com/downloads/
--###############################################
##________________________________________  ___________________________


#####  ==========  done-added in suse11.4-vo17--colls:
- on suse log-dir was missing:  mkdir /var/log/mysql/ ; chown mysql:mysql /var/log/mysql/
- not good?? or ok? (insted useradd mysql2 or so ...; mysql is a SYSTEM-user !!! leave it!):
	vo17:~ # usermod -s /bin/bash mysql # --> home-dir ??
	vo17:~ # passwd mysql
##________________________________________  ___________________________


#####  ==========  perl-mysql:
-! see ref.--2.15 ...

	_______:  -- install perl.modules + mysql-driver!: (on suse per yast! is better!)
shell> perl -MCPAN -e shell
cpan> install DBI
cpan> install DBD::mysql     ##- mysql-driver
##________________________________________  ___________________________


#####  ==========  cmds-mysql-on-suse.114:
u1@vo17:~ $mysqld
mysqld         mysqld-debug   mysqld_multi   mysqld_safe    mysqldump      mysqldumpslow  
u1@vo17:~ $mysql
mysql                       mysql_convert_table_format  mysqlhotcopy                mysqltest
mysqlaccess                 mysqld                      mysqlimport                 mysqltest_embedded
mysqladmin                  mysqld-debug                mysql_install_db            mysql_tzinfo_to_sql
mysqlanalyze                mysqld_multi                mysqlmanager                mysql_upgrade
mysqlbinlog                 mysqld_safe                 mysqloptimize               mysql_waitpid
mysqlbug                    mysqldump                   mysqlrepair                 mysql-workbench
mysqlcheck                  mysqldumpslow               mysql_secure_installation   mysql-workbench-bin
mysql_client_test           mysql_find_rows             mysql_setpermission         mysql_zap
mysql_client_test_embedded  mysql_fix_extensions        mysqlshow                   
mysql_config                mysql_fix_privilege_tables  mysqlslap                   
u1@vo17:~ $uname -a
Linux vo17 2.6.37.6-0.7-default #1 SMP 2011-07-21 02:17:24 +0200 i686 i686 i386 GNU/Linux

	_______:  rpms:
u1@vo17:~ $rpmssg mysql
libdbi-drivers-dbd-mysql-0.8.3-4.7.2.i586
libgda-3_0-mysql-3.1.5-10.4.i586
libgda-4_0-mysql-4.2.2-4.3.i586
libmysqlclient16-5.1.53-4.7.1.i586
libmysqlclient-devel-5.1.53-4.7.1.i586
libmysqlclient_r16-5.1.53-4.7.1.i586
libmysqlclusterclient16-7.1.14-0.3.1.i586
libmysqlclusterclient_r16-7.1.14-0.3.1.i586
libmysqlcppconn1-1.0.5-9.2.i586
libmysqlcppconn-devel-1.0.5-9.2.i586
libmysqld0-5.1.53-4.7.1.i586
libmysqld-devel-5.1.53-4.7.1.i586
libqt4-sql-mysql-4.7.1-7.2.i586
libreoffice-base-drivers-mysql-3.3.1.2-1.2.2.i586
mysql-community-server-5.1.53-4.7.1.i586
mysql-community-server-bench-5.1.53-4.7.1.i586
mysql-community-server-client-5.1.53-4.7.1.i586
mysql-community-server-debug-5.1.53-4.7.1.i586
mysql-community-server-test-5.1.53-4.7.1.i586
mysql-community-server-tools-5.1.53-4.7.1.i586
mysql-connector-java-5.1.6-8.3.noarch
mysql-connector-java-javadoc-5.1.6-8.3.noarch
mysql-connector-java-manual-5.1.6-8.3.noarch
mysql-workbench-5.2.31-3.3.i586
perl-DBD-mysql-4.018-4.2.i586
qt3-mysql-3.3.8b-111.2.i586
u1@vo17:~ $date
Sun Aug 21 15:39:22 CEST 2011
u1@vo17:~ $uname -a
Linux vo17 2.6.37.6-0.7-default #1 SMP 2011-07-21 02:17:24 +0200 i686 i686 i386 GNU/Linux
u1@vo17:~ $

	_______:  
##________________________________________  ___________________________


#####  ==========  
