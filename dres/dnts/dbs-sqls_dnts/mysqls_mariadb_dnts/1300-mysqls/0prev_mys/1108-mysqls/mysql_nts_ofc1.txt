__________ mysql2 + prj.mysql  ____________________________________

	_______:  cmdline1:
	- export MYSQL_PS1="\d.\u \h:\p mysql> "
	- export  MYSQL_HOST=$(hostname -s)  MYSQL_PORT=10400  MYSQL_USER=rdb  MYSQL_PW=rdb  DBNAME=rdb  
	- export  MYSQL_HOST=127.0.0.1       MYSQL_PORT=10400  MYSQL_USER=rdb  MYSQL_PW=rdb  DBNAME=rdb
	- mysql -h ${MYSQL_HOST} -P ${MYSQL_PORT} -u ${MYSQL_USER} -p${MYSQL_PW} -D ${DBNAME}
	  addies:  --tee=tables1.log
	-- tr/manually/...:
	  	mysql -h ${MYSQL_HOST} -P ${MYSQL_PORT} -u ${MYSQL_USER} -p${MYSQL_PW} -D ${DBNAME}  --prompt="[ ${MYSQL_HOST}:${MYSQL_PORT}--${DBNAME}.${MYSQL_USER} ]\nmysql:${MYSQL_PORT}> " 
		mysql -h -h 127.0.0.1 -P 10100 -u rdb -prdb -D rdb 
--############ prj.mysql / gtsenv.mysql / loc.lx-mysql / ...: ######################################################
##________________________________________  ___________________________


#####  ==========  prj.mysql in gtsenv-ENV:
	--- DIRs-prj.mysql/configs.prj:
		-! see vars in 001: /opt/gts/bin/*db* : cleanupdb.sh  install_db_data.sh  install_db_schema.sh  install_db.sh  m3db  manage_db.sh  uninstall_db.sh  :
			SQL_SCRIPT_ROOT=/opt/gts/bin
			SQL_ROOT=/opt/gts/usr/share/sql
			DB_ETC=/opt/gts/etc/dataaccess/databases/${DBNAME}
			LOG_FILE="/opt/gts/var/log/DBs_operations.log"
	--- schema-rdb-drop/setup:
		[kampkur@rdswsd008:E001 ~]$ uninstall_db.sh rdb
		Removing rdb database and  its user and grants.
		[kampkur@lx4325:E004 gts]  /opt/gts/bin/install_db.sh $MYSQL_HOST  $MYSQL_PORT $DBNAME $DBNAME /schema   ##OR: full with data:
		[kampkur@rdswsd008:E001 ~]$ install_db.sh rdb
		Creating rdb database and assigning its user and grants.
		Installing rdb schema from /opt/gts/usr/share/sql/rdb/1_rdb.sql
		Installing rdb schema from /opt/gts/usr/share/sql/rdb/2_rdb.sql
	--- admin/connect/dump/connects/system/.... prj.db:
		- nc -v $MYSQL_HOST $MYSQL_PORT -w 1 2> /dev/null  ##- is any tcp.ip-listener there??
		- connect:  [kampkur@rdswsd008:E001 gts]  mysql -h 127.0.0.1 -P 10100 -u rdb -p -D rdb  ##-OR -prdb for PW.in.cmdline
		- dump:
			with "-B bzw. --databases ${DBNAME}" to also generate the database/schema statements!! ( CREATE DATABASE IF NOT EXISTS `rdb` ; USE `rdb`; ... the rest of create+inserts) !!
			mysqldump -v -h ${MYSQL_HOST} -P ${MYSQL_PORT} -u ${MYSQL_USER} -p${MYSQL_PW}  -B ${DBNAME} > ${DBNAME}.dump.sql    ##--I- without -B does not add the above "create database ..." stmts!
			mysqldump -v -h 127.0.0.1 -P 10100 -u rdb -prdb rdb > rdb-dump.sql
		- mysql-root/admin-pw-setting in gtsenv: [kampkur@rdswsd008:E001 gts]$
		- pw.admin/roo-setting:  /opt/gts/3pp/mysql/bin/mysqladmin -h 127.0.0.1 -P 10100  -u root password "mypw"
		--  see vars in 001: /opt/gts/bin/*db* :
			MYSQL_USER='gtsdbadmin'
			MYSQL_PW=`sudo -u xman get_admin_passwd.sh`
	--- mysqladmin :
		- mysqladmin  -h 127.0.0.1 -P 10100 -u rdb -prdb  version  ##-I- or just -p instead -prdb for no.PW in cmdline!
		bzw.  mysqladmin  $myqconn
		-!! mysqladmin  -h 127.0.0.1 -P 10100 -u rdb -prdb  variables  ##--> all configs/datadir/logs/... :
		start/inits : /opt/gts/etc
		conf	: /opt/gts/var/lib/mysql/gts-my.cnf
		datadir : /opt/gts/var/lib/mysql/
		basedir : /opt/gts/3pp/mysql
		pidfile	: /opt/gts/var/run/mysql/my.pid
	--- mysqlshow :
		-  mysqlshow $myqconn
		-! mysqlshow $myqconn rdb ##-OR test ... any DB/Schema
		-! mysqlshow $myqconn rdb institution
	--- mysql client/queries:   (after tables listing with:  mysqlshow $myqconn rdb ):
		-  mysql $myqconn -e "SELECT name, symbol, description from rdb.institution"  ##bzw:
		-  mysql $myqconn rdb  -e "SELECT name, symbol, description from institution"
	--- gtsenv-stuff (!! but from rdswsd008:E001 env !):
		- scripts.db.gtsenv: /opt/gts/bin/cleanupdb.sh , install_db_data.sh , install_db_schema.sh , install_db.sh , manage_db.sh ,  .....
		-! configs (port,host,...) in:  /opt/gts/etc/dataaccess/mysql/mysql.conf  ##-see  /opt/gts/etc/initscripts.d/mysqld_service_fixauto
			MYSQL_IPADDR="127.0.0.1" MYSQL_PORT="10100" SQL_SCRIPT_ROOT=/opt/gts/bin SQL_ROOT=/opt/gts/usr/share/sql
		- see details in gts.mysql.start-script:  /opt/gts/etc/initscripts.d/mysqld_service_fixauto  :
		  /opt/gts/etc/initscripts.d/mysqld status , ...
	--- rdb DB:
		-! setup-rdb-DB for btsenv.00X:   /opt/gts/bin/install_db*.sh
		-! create.schema.rdb-sql.script:  /opt/gts/usr/share/sql/rdb/1_rdb.sql  and 2_rdb.sql
		- confs:  /opt/gts/etc/initscripts.d/ ,  /opt/gts/etc/dataaccess/mysql/ , ...
		- refdata.sample.default:  /opt/gts/usr/share/doc/sample-refdata/refdata-load-dump.sql
	--- tools-loc-lx (admin, client, gui,...):
		- gui-adin in loc.lx: /opt/mysql-gui-tools-5.0/mysql-administrator
		- gui-query: /opt/mysql-gui-tools-5.0/mysql-query-browser
--############ installs/setups/configs/tools/server/generals/ ...: ##############################################
##________________________________________  ___________________________


#####  ==========  Installs,...:
	-! manual install see: 2.2. Installing MySQL from Generic Binaries on Unix/Linux
##________________________________________  ___________________________


#####  ==========  confs:
	- /etc/my.cnf  on loc.lx
	- /etc/rc.d/init.d/mysqld
	--- startup option files:  
		- use --help to see:
		  To determine whether a program reads option files, invoke it with the --help option. (For mysqld, use --verbose [436] and --help [406].) If the program reads option files, the help message indicates which files it looks for and which option groups it recognizes. ##see 4.2.3.3. Using Option Files
		-! see ref--4.2.3.3. Using Option Files  :
		File-Name	Purpose:
		/etc/my.cnf 		Global options
		/etc/mysql/my.cnf	Global options
		SYSCONFDIR/my.cnf 	Global options
		$MYSQL_HOME/my.cnf 	Server-specific options
		defaults-extra-file	file specified with --defaults-extra-file=path [233], if any
		~/.my.cnf			User-specific options
##________________________________________  ___________________________


#####  ==========  pathes:
	- ref--ch.2.5.1:
	Directory Contents of Directory
	/usr/bin	 	Client programs and scripts
	/usr/sbin 		The mysqld server
	/var/lib/mysql 		Log files, databases
	/usr/share/info 	Manual in Info format
	/usr/share/man 		Unix manual pages
	/usr/include/mysql 	Include (header) files
	/usr/lib/mysql 		Libraries
	/usr/share/mysql 	Miscellaneous support files, including error messages, character set files, sample configuration files, SQL for database installation
	/usr/share/sql-bench 	Benchmarks
	- find /usr/bin -iname "*mysql*"
##________________________________________  ___________________________


#####  ==========  sample-db:
	- /OR use:  mysql> source myfile,sql  /OR manually:
	connect test;
	CREATE TABLE pet (name VARCHAR(20), owner VARCHAR(20), species VARCHAR(20), sex CHAR(1), birth DATE, death DATE);
	load data local infile '/home/kampkur/prj1/tests/mysql1t/pet_table.txt' into table pet;
	CREATE TABLE event (name VARCHAR(20), date DATE, type VARCHAR(15), remark VARCHAR(255));
	load data local infile '/home/kampkur/prj1/tests/mysql1t/event_table.txt' into table event;
##________________________________________  ___________________________


#####  ==========  prompt:
	- best, export MYSQL_PS1 in shell (bzw. setting in my.cfg): it is dynamic-prompt and changes if eg switching schema/user/...,
		see ref.manual:  Section 4.5.1.2, “mysql Commands”
		for options/abbrevs in MYSQL_PS1 see "4.5.1.2. mysql Commands" table for options [269]
	- best, shell-var, as:   export MYSQL_PS1="(\u@\h) [\d]> "  #-for: (user@host) [database]>  
	- or on cmdline (not dynamic):  mysql -h ${MYSQL_HOST} -P ${MYSQL_PORT} -u ${MYSQL_USER} -p${MYSQL_PW} -D ${DBNAME}  --prompt="[ ${MYSQL_HOST}:${MYSQL_PORT}--${DBNAME}.${MYSQL_USER} ]\nmysql:${MYSQL_PORT}> " 
	- or interactively:  mysql> prompt (\u@\h) [\d]>\_
	- or in .my.cnf : prompt=....
	- goback to dafult prompt:  mysql> prompt
##________________________________________  ___________________________


#####  ==========  mysql-client-cmdline (shell> mysql) options/params/configs/...:
	- see:
		-!! mysql --help
		- ref--4.5. MySQL Client Programs
		- ref--4.5.1. mysql — The MySQL Command-Line Tool
		- ref--4.5.1.1. mysql Options
		- config-files:  ref--4.2.3.3. Using Option Files +  mysql --help
	---! config-files see output of :  mysql --help :
		Default options are read from the following files in the given order:
		/etc/my.cnf /etc/mysql/my.cnf /usr/local/mysql/etc/my.cnf ~/.my.cnf
		- The following groups are read: [mysql] and  [client]
		- The [client] option group is read by all client programs (but not by mysqld), including mysql !
		- including other files in .my.cnf:  !include /home/mydir/myopt.cnf
	-! -v :  mysql with the --verbose [264] option, which causes each statement to be displayed before the result that it produces.
	- ignore ctrl-C:  mysql --sigint-ignore ... ##then use "\c" to ignore the current line!
	- shell-readin-readout: shell> mysql db_name < script.sql > output.tab
	-!! NOT reading the option file:  mysql --no-defaults ...
	-! printout user-options-settings:  mysql --print-defaults
	- setting/showing options:
		- show CURRENT optins:  mysql --help
		- setting optins: either on cmdline as mysql --auto-vertical-output=true  /OR in config-files as in ~/.my.cnf
		1- shell> mysql --max_allowed_packet=16M
		2- in .my.cnf:  [mysql] max_allowed_packet=16M ...
		3- mysql> SET GLOBAL max_allowed_packet=16M; ##- but obviously not ALL options can be resetted so (after mysql is started)!
	--- vertical output:
		-! \G : vertical output only this stamt: select * from clearing_house \G;
		- global vertical output with option: auto-vertical-output=TRUE  in optionfile OR on cmdline!
	- shell-cmds from mysql with "system":   mysql> system pwd;
##________________________________________  ___________________________


#####  ==========  server-stuff:
	- see:
		mysql> help contents
--############ sql-stuffs in mysql : cretes.schemas.tables/show/...: ################################################
##________________________________________  ___________________________


#####  ==========  show/geneal.schema+db.queries/...:
	-! DIFF show <--> select cases!! see below for eg!
	-! help show
	- show databases;
	- select database();  /* current databse */
	- connect test;
	- show tables;
	-! sql-stmt-queries for schema:
		SHOW CREATE TABLE account;  ##sql-stmt-for-account!!
		show create database rdb;
		SHOW CREATE VIEW view_name		
		! SHOW TABLE STATUS from rdb;
	- which database is currently selected/using?:  SELECT DATABASE();
	SELECT VERSION(), CURRENT_DATE, now(), user();
##________________________________________  ___________________________


#####  ==========  set/show vars, options, system-vars,...:
	- user-vars (@...): 	set @v1=11; select @va;
	- options/system-variables/configs setting:
		shell> mysql --max_allowed_packet=16M
		mysql> SET GLOBAL max_allowed_packet=16M;
	-- show options/system-vars:
		SHOW [GLOBAL | SESSION] VARIABLES [like_or_where];
		SHOW GLOBAL VARIABLES;  ##system-options/configs....
		show global variables like  '%inter%';
##________________________________________  ___________________________


#####  ==========  output-piping/saving/paging/ to file,....
	1- shell-piping:   shell> mysql db_name < script.sql > output.tab  ##see man mysql
		OR 1.b-  mysql -e "SELECT ..." > file_name to generate the file on the client host.
	2- tee-option in mysql: --tee=out.log  cmdline-option bzw.  mysql>tee out.log (disableing in mysql with "notee" bzw. "\t" after statement):   mysql  --tee=tables1.log ...
	  or just \T as in mysql> \Tout1.log #and then notee if needed ... #and then notee if needed ...
	3- pager-mysql:  mysql> pager cat > /tmp/log.txt  /OR  mysql> pager less -n -i -S  (disabling just with "pager")#- see ref--4.5.1.2 ... mysql — The MySQL Command-Line Tool
	4- SELECT ... INTO OUTFILE / DUMPFILE 'file_name' :  To write data from a table to a file!  ref--CH.13.2.9.1. SELECT ... INTO Syntax
		quickly dump a table to a text file on the SERVER-machine (locally or mounted! due to path!)
		if remotely / client maschine, then use method.1 , as : mysql -e "SELECT ..." > file_name 
##________________________________________  ___________________________


#####  ==========  input-loading/readin data from files, cmdline-sqls...:
	-! see
		- man mysql  bzw. mysql --help
		- ref--ch.3.3.3
		- ref--ch.4.5.1.5. Executing SQL Statements from a Text File
	--- sql.input.files (not only data as csv-files!):
		- shell-piping:   shell> mysql db_name < script.sql > output.tab  ##see man mysql
		- source:   mysql>  source  <filepath>   ##bzw.  mysql> \. file_name
		- cmd-param for exec:  shell>  mysql ... -e "SELECT VERSION(), CURRENT_DATE, now(), user();"
		- mysqlimport : a command-line interface to the LOAD DATA INFILE SQL statement.  ##see 4.5.5. mysqlimport — A Data Import Program
	--- text-data-input-files / LOAD DATA (no sqls, just eg csv-data,...) :
		- see mysql.ref--CH.3.3.3. Loading Data into a Table , and ref--CH.13.2.6. LOAD DATA INFILE Syntax :
		- see also here nts for mysqlimport (which is an interface to LOAD DATA INFILE)!!
		-! mysql> help load data
		- LOAD DATA INFILE statement reads rows from a text file into a table at a very high speed
		- To load the text file pet.txt into the pet table, use this statement:
		mysql> LOAD DATA LOCAL INFILE '/path/pet.txt' INTO TABLE pet;
		for windows (for windows.files add: LINES TERMINATED BY '\r\n'; ):
		mysql> LOAD DATA LOCAL INFILE '/path/pet.txt' INTO TABLE pet LINES TERMINATED BY '\r\n';
##________________________________________  ___________________________


#####  ==========  export/import:
	-!! params-order IS important! the LAST param is most in effect!! so options are processed first to last.
	--- export/dump:  mysqldump — A Database Backup Program   : see 4.5.4
		- mysqldump  --help
		- mysqldump -v -h ${MYSQL_HOST} -P ${MYSQL_PORT} -u ${MYSQL_USER} -p${MYSQL_PW}  -B ${DBNAME} > ${DBNAME}.dump.sql
		- table dump:   mysqldump rdb account > account.dump.sql
		- readin the dump file:   shell> mysql < dumpfile
		-! config/options.file:  [mysqldump] and [client] groups of an option file, eg ~/.my.cnf
		-! use/see --opt (is default) for a collection of best params!! 
		-! current options-values?? :  mysqldump  --help
		-! locking!:  --single-transaction option and the --lock-tables [297] option are mutually exclusive because LOCK TABLES causes any pending transactions to be committed implicitly.
		---!! usefull param (except --opt which is a group of useful params and is default):  see Table 4.5. mysqldump Options :
			--opt (is default): Shorthand for --add-drop-table --add-locks --create-options --disable-keys --extended- insert --lock-tables --quick --set-charset.
			--compact (good short lesbar!): enables the --skip-add-drop-table -- skip-add-locks --skip-comments  --skip-disable-keys -- skip-set-charset options.
			--complete-insert , -c  : include column names by insert-statement
			--dump-date  (with --comments , then timestamp will be added to the dump)
			-! ONLY structure (create db / table ! no data! NO insert stmts!): --no-create-info , -t 
			-! ONLY data (no create db/table...! ONLY insert-stmts...): --no-create-db , -n  bzw.  --no-create-info , -t
			--replace  : Write REPLACE statements rather than INSERT statements.
			--result-file=file_name , -r  : instead piping
			-! TAB.seperated-output files /.tsv: --tab=path , -T path : Produce tab-separated text-format data files. For each dumped table, mysqldump creates a tbl_name.sql file
			   that contains the CREATE TABLE statement that creates the table, and the server writes a tbl_name.txt file that contains its data.
			   ! The option value is the directory in which to write the files.
			   ! should be used only when mysqldump is run on the same machine as the mysqld server.
			- XML-output:  --xml , -X  :Write dump output as well-formed XML.
			-v verbose
		---! use-cases /common use of mysqldump: see [304]:
			shell> mysqldump db_name > backup-file.sql
			You can load the dump file back into the server like this:
			shell> mysql db_name < backup-file.sql
			Or like this:
			shell> mysql -e "source /path-to-backup/backup-file.sql" db_name
			mysqldump is also very useful for populating databases by copying data from one MySQL server to another:
			shell> mysqldump --opt db_name | mysql --host=remote_host -C db_name
			It is possible to dump several databases with one command:
			shell> mysqldump --databases db_name1 [db_name2 ...] > my_databases.sql
			To dump all databases, use the --all-databases [294] option:
			shell> mysqldump --all-databases > all_databases.sql
			For InnoDB tables, mysqldump provides a way of making an online backup:
			shell> mysqldump --all-databases --single-transaction > all_databases.sql
!	--- import:   mysqlimport — A Data Import Program  : see 4.5.5. : basically an interface to "load data infile"
		- mysqlimport  --help
		- mysqlimport provides a command-line interface to the LOAD DATA INFILE SQL statement!
		-! config/options.file:  [mysqlimport] and [client] groups of an option file, eg ~/.my.cnf
		- readin the dump file:   shell> mysql < dumpfile
		---! usefull params: 
			-! --delete [307] delete [307] Empty the table before importing the text file
			-! --columns=column_list [307], -c column_list This option takes a comma-separated list of column names as its value. The order of the column names indicates how to match data file columns with table columns.
			-! --fields-terminated-by=... [307], --fields-enclosed-by=... [307]
			--lock-tables [297], -l
			--replace : new rows replace existing rows that have the same unique key value.
##________________________________________  ___________________________


#####  ==========  Transactions/commits/rollbacks/...:
	-! mysql> help START TRANSACTION ; help ISOLATION ; /OR category to see all items: help transactions;
	- START TRANSACTION; ...;  COMMIT;/ROLLBACK;
	-! default is autocommit by mysql!! otherwise:  SET autocommit=0; .... ; commit/rollback;
##________________________________________  ___________________________


#####  ==========  Foreign.Keys/Constrains/inter-relationships/dependencies/....:
	- SET foreign_key_checks = 0;
##________________________________________  ___________________________


#####  ==========  dates/times: see mysql.ref--tut--ch.3.3.4
	- current-date/-year:  select  curdate() as CurrDate, year(curdate()) CurrYear, month(curdate()) CurrMonth;
	- SELECT name, birth, death, (YEAR(death)-YEAR(birth)) - (RIGHT(death,5)<RIGHT(birth,5)) AS age;
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  TEST.stuff: T1 table,..., quickies:
	- create table T1 (C1 INT(12), C2 VARCHAR(50));
--##################### coll, ... ######################################################
