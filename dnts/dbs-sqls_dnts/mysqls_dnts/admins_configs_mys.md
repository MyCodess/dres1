___________ admins mysql ____________________________________
##________________________________________  ___________________________


#####  ==========  mysqld :
	--- debugs/problemshooting/...:
		-!! debug-version: mysqld-debug : use it instead mysqld to get more messages..., see Manual
			- eg suse: mysql-community-server-debug : MySQL server with debug options turned on
		- perror : ora-oraerr: A utility that displays the meaning of system or MySQL error codes. See Section 4.8.1, “perror — Explain Error Codes”.
##________________________________________  ___________________________


#####  ==========  confs:
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


#####  ==========  start/stop/status of Server/mysqld/Daemon (not DBs but whole daemon/service mysqld)
	--- see refman:
		- ref--4.3. MySQL Server and Server-Startup Programs
		- ref--5.1 “The MySQL Server”
		- ref--2.10. Postinstallation Setup and Testing  (also for running server as non-ux-user) , esp.  2.10.1.2. Starting and Stopping MySQL Automatically
		- mysqld --verbose --help  and ref-ch.5.1 “The MySQL Server”
		- man mysqld_safe
	--- DIFFs/DEFs:
		-!! DIFF-root-users bzw. DIFF <OS.system.user> ,and  <db.user>:
			DIFF mysql-"root"-user  <-->  unix-"root"-user !!! : 
			"-u root" as params for mysql-tools is always mysql-"root"-user, which in default-setup has NO password !!
			-!! here in all eg "--user=mysql" is meant <OS.system.user> ,and "--user=root" is meant  <db.user> !!
	--- status-check as ux.non.root.user:
		mysqladmin status / ping / version / variables  ##-see man mysaladmin
		mysqlshow  ; mysqlshow mysql ; ....
	--- start/stop-cmds:
		-!! here in all eg "--user=mysql" is meant <OS.system.user> ,and "--user=root" is meant  <db.user> !!
		1- mysqld /mysqld_safe  --user=mysql  start/stop/status/...	##--invoking as ux.root.user usu (except if non-root user has rights. see postinstalltion-tasks...)
			1.b- mysql.server  --user=mysql  start/stop/status/...	##--invoking as ux.root.user usu; it finally calls mysqld_safe ; see nts below.
			usu RPMs copy /usr/share/mysql/mysql.server  to /etc/init.d/mysql (party modified by distro)
		2- mysqladmin  --user=root	    shutdown/status/ping/...   ##--any ux.user who knows mysql-root-pw (dafault; no password! so basically any user in local system)
			!! mysqladmin can NOT start server as non-root, but can shutdown with --user=root !
			!! "start" param is not starting the server, but the replication instance!!
		3- /etc/init.d/mysql start/stop/status   ##--only in System.V (still in suse); it finally calls mysqld_safe with options in /etc/my.cnf
	--- mysqld /mysqld_safe --user=mysql start/stop/... nts:
		- see:  mysqld --verbose --help  and ref-5.1
		-! NEVER start server as unix.root.user!! so do ALWAYS "-u mysql" when invoking as unix.root!! (fot other non-priviliged users see: 5.3.6. How to Run MySQL as a Normal User):
		- init.d-scripts (system-V-scripts) run mysqld_safe anyway as mysql-unix-user as default (see psg mysql; may NOT be root!)
		-!! insted --user=mysql, you can put user option to the [mysqld] group of the /etc/my.cnf option file, so you never forget it !!
		- mysqld_safe / mysqld --user=mysql start &   : Starts the MySQL database server. ALWAYS as non-roor-user do it, so --user=<non-root-unix-user>!
		- mysqld_safe  is the mysqld and is the recommended way to start a mysqld server on Unix 
		- mysqld_safe --user=mysql &  ##- as unix-non.root.user ONLY if the user has access rights to mysql-data-/log-/...-dirs, so if the posinstallation works are so done. otherwise must be invoked as unix-root-user (late the mysqld switches to eg "mysql"-user ....!)
		-! start the server ONLY as non-root-user, as mysql !!! (i shell ok as roo, but with param -u xxx):
		-! ref--ch.2.a0--Postinstallation tasks: It is important that the MySQL server be run using an unprivileged (non-root) login account. To ensure this if you run mysqld_safe as root, include the --user option as shown. Otherwise, you should execute the script while logged in as mysql, in which case you can omit the --user option from the command.
		- debug-version of mysqld:   mysqld-debug
	--- mysql.server nts:
		- manual installtion of mysql.server:   cp mysql.server /etc/init.d/mysql ;  chmod +x /etc/init.d/mysql  ##-see 2.10.1.2. Starting and Stopping MySQL Automatically
		- Before mysql.server starts the server, it changes location to the MySQL installation directory, and then invokes mysqld_safe.
		- RPM package (MySQL-server-VERSION.rpm), or a native Linux package installation, the mysql.server script may be installed in the /etc/init.d directory with the name mysql.
		- also find  mysql.server under support-files/...
	--- auto-restart of service:
		- ##-see 2.10.1.2. Starting and Stopping MySQL Automatically
		 chkconfig --level 345 mysql on    #/OR:
		 manualy put "ln -s" of /etc/init.d/mysql in appropriate  /etc/init.d/XXX-DIRs
		 bzw. to the appropriate places in your /etc/rc* files.
	--- configs/options-files for mysqld (see also the next section here):
		see : mysqld --verbose --help
		Default options are read from the following files in the given order: /etc/my.cnf /etc/mysql/my.cnf /usr/etc/my.cnf ~/.my.cnf
		The following groups are read: [mysqld] [server]  [mysqld-5.5] ; for detailed options 
	--- remote queries for status/admins/...:
		- mysqladmin -h host_name variables  ##but datadir must be accesible as NFS! see 2.10.1.3. Starting and Troubleshooting the MySQL Server
##________________________________________  ___________________________


#####  ==========  option-files/config-files/params/... for server (mysqld, mysqld-safe, ...:
	--- see:
		-! see ref: 4.2.3.3. Using Option Files  (bzw. whole chapter of  4.2.3. Specifying Program Options)
		- Chapter 5. MySQL Server Administration --> ausfuehrlich! params,....
	--- syntax/notes to option-files:
		-!! example-files in /usr/share/mysql/*.cnf (mysql-community-server-5.1.53-4.7.1.i586.rpm)
		-! If multiple instances of a given option are found, the last instance takes precedence. 
		-! On Unix platforms, MySQL ignores configuration files that are world-writable. 
		-! option-file-params the same as commandline-params of the util, but without "--"
	--- [GROUPS] read by server-scripts (eg in /etc/my.cnf , ...):
		Table 2.15. MySQL Startup scripts and supported server option groups
		-Script.name	-Option.Groups:
		mysqld			[mysqld], [server], [mysqld-major_version]
		mysqld_safe		[mysqld], [server], [mysqld_safe]
		mysql.server	[mysqld], [server], [mysql.server] 
		!! --> so, ALL server-scripts read the  [server] group!!
	--- startup option files:  
		- use --help to see:
		  To determine whether a program reads option files, invoke it with the --help option. (For mysqld, use --verbose [436] and --help [406].) If the program reads option files, the help message indicates which files it looks for and which option groups it recognizes. ##see 4.2.3.3. Using Option Files
		--File-Name		--Purpose:
		/etc/my.cnf 		Global options
		/etc/mysql/my.cnf	Global options
		SYSCONFDIR/my.cnf 	Global options
		$MYSQL_HOME/my.cnf 	Server-specific options
		defaults-extra-file	file specified with --defaults-extra-file=path [233], if any
		~/.my.cnf			User-specific options
	--- UNIX-options-files:
		--File Name--       --Purpose--  UNIX:
		/etc/my.cnf          Global options
		/etc/mysql/my.cnf    Global options (as of MySQL 5.1.15 and earlier)
		SYSCONFDIR/my.cnf    Global options
		$MYSQL_HOME/my.cnf   Server-specific options
		defaults-extra-file  The file specified with `--defaults-extra-file=PATH, if any
		~/.my.cnf            User-specific options
	--- MsWins-options.files
		--File Name--       --Purpose--  MsWins:
		WINDIR\my.ini,       Global options
		WINDIR\my.cnf        
		C:\my.ini,           Global options
		C:\my.cnf            
		INSTALLDIR\my.ini,   Global options
		INSTALLDIR\my.cnf    
		defaults-extra-file  The file specified with `--defaults-extra-file=PATH, if any
	--- suse.114.species/addies options-files:
		-! see /etc/my.cnf
		-!! datadir bzw. mysql-home:  /var/lib/mysql  ( see /etc/my.cnf : datadir = /var/lib/mysql)
			DBs will be created here!! in datadir !!
		-! /var/log/mysql/mysqld.log  ##-!!- mkdir /var/log/mysql  if not exist, before starting server!!
		- zypper in ... (see coll-file)
		see /etc/my.cnf
		/etc/mysqlaccess.conf
		/etc/mysql
	----- ENV.vars:
		-!  ref--CH.2.12. Environment Variables : MySQL Related Environment Variables
##________________________________________  ___________________________


#####  ==========  options and server.SYSTEM.VARs for server/mysqld :
	-! see:
		- server-options:      table 5.1.1. Server Option and Variable Reference
		- server-SYSTEM.VARs:  Table 5.2. System Variable Summary  in 5.1.4. Server System Variables   :indicate how server is configured
		- server-STATUS.VARs:  Table 5.4. Status Variable Summary  in 5.1.6. Server Status Variables   :provide information about server operation
	-!! mysqld --verbose --help  ##--II- best as non-root user! sorks ok! even after mysqld is running! the "--help" at the END means: ONLY show the vars!! but --help MUST be the very LAST param!!
	-!! querying current-config-params:   5.1.3. Server System Variables :
		mysqld --verbose --help	  ##--> will use: values that a server will use based on its compiled-in defaults and any option files that it reads, 
		mysqladmin variables      ##--> is using: what values a running MySQL server is using! /OR:
		mysql> SHOW VARIABLES            ##--> is using: current values used by a running server.
	- what are defauls without current option-files??:	mysqld --no-defaults --verbose --help  ##--> are then compiled-default-options with: values that a server will use based on its compiled-in defaults, ignoring the settings in any option files
	- SHOW [GLOBAL | SESSION] STATUS
	-!! CHECKING the effects of adapting pathes/vars by start: ref--2.12.1.3--155
		To check the effect of specifying path options, invoke mysqld with those options followed by the --verbose and --help op-
		eg:  mysqld --datadir=/data2 --verbose --help
		!! but --verbose and --help must be the last options.
##________________________________________  ___________________________


#####  ==========  default.users defined by installation/setup, default/admin-users (root, anonymous, mysql, ...):
	-!! see 2.10.2. Securing the Initial MySQL Accounts
	- root.user.mysql: Some accounts have the user name root. These are superuser accounts that have all privileges and can do anything.
	  The initial root account passwords are empty, so anyone can connect to the MySQL server as root without a password and be granted all privileges.
	  !!DIFF:  it is NOT unix.root.user, but db.root.user !!! as any unix-user can use it with --user=root ....
	- listing users:  mysql -u root ;  mysql> SELECT User, Host, Password FROM mysql.user;
	- "test"-DB : is a default-db and ALL users are allowed to do anything there AND in any DB-name with "test_"!
	--- password-setting (for default/root-users):
		1- with client:
		shell> mysql -u root
		mysql> SET PASSWORD FOR 'root'@'localhost' = PASSWORD('newpwd');
		2- for all root-users with update...:
		mysql> UPDATE mysql.user SET Password = PASSWORD('newpwd') WHERE User = 'root';
		mysql> FLUSH PRIVILEGES;
		FLUSH statement causes the server to reread the grant tables. Without it, the password change remains unnoticed by the server until you restart it.
		3- mysqladmin (does not work for the 'root'@'127.0.0.1' or 'root'@'::1' account! use set password ...):
		shell> mysqladmin -u root password "newpwd"
		shell> mysqladmin -u root -h host_name password "newpwd"
	--- password for default anonymous-user:
		shell> mysql -u root -p
		mysql> SET PASSWORD FOR ''@'localhost' = PASSWORD('newpwd');
		mysql> SET PASSWORD FOR ''@'host_name' = PASSWORD('newpwd');
		/OR:
		mysql> UPDATE mysql.user SET Password = PASSWORD('newpwd') WHERE User = '';
		mysql> FLUSH PRIVILEGES;
	--- anonymous-user drop/delete:
		- shell> mysql -u root -p
		mysql> DROP USER ''@'localhost';
		mysql> DROP USER ''@'host_name';
##________________________________________  ___________________________


#####  ==========  Log-files/problem.shooting
	-!DIFF  logs  <-->  redo.logs
	- see:  ref--ch.5.2. MySQL Server Logs):
	--- log-files / runtime.infos of mysqld:
		-! location:    mysqladmin variables | fgrep "/"
		- By default, all log files are created in the data directory. suse also: /var/log/mysql
		- log-files-location?:  mysqladmin variables | grepi log ; also see /etc/my.cnf
	--- types of log/Redo-files:
		-- Log Type --	:	 -- Information Written to Log --
		Error log 		: Problems encountered starting, running, or stopping mysqld
		General query log 	: (~ ora-redo-logs)Established client connections and statements received from clients
		Binary log 		: All statements that change data (also used for replication)
		Relay log Data 	: changes received from a replication master server
		Slow query log 	: All queries that took more than long_query_time seconds to execute or did not use
	--- troubleshooting throw logfiles:
		- tail host_name.err bzw.  host_name.log
		- runtime-infos:  ll /var/run/mysql/  ##- current pid,.../in suse; default.refdocs: pid in data-dir
		-!! connection-problems/errors??: see whole tips in  ref--ch.6.2.7. Causes of Access-Denied Errors
	---
		-  FLUSH LOGS stmt: to write logs down! /OR by mysqladmin with a flush-logs or refresh argument; or execute mysqldump with a --flush-logs [296] or --master-data [298] option
##________________________________________  ___________________________


#####  ==========  Redo.logs / General Query Log (protocol aller sql-stmts,.. for redo/spiegelung/backup):  5.2.3. The General Query Log
	- add to /etc/my.cnf of in cmdline starting ot mysqld with redolog-params:
		--general_log=1    general_log_file=file_name  #!! BOTH MUST be set!
	- As of MySQL 5.1.29, use --general_log[={0|1}] to enable or disable the general query log, and optionally -general_log_file=file_name to specify a log file name. The --log and -l options are deprecated. : see 5.2.3. The General Query Log
	- disabling redologs at runtime: mysql> SET GLOBAL general_log = 'OFF';
	- enabling redolog: SET GLOBAL general_log = 'ON';
##________________________________________  ___________________________


#####  ==========  admins-Tools , admin-cmds: see s Chapter 5, MySQL Server Administration.
	--- see
		-!! see refmanual: 4.1. Overview of MySQL Programs
		-!! see Chapter 5. MySQL Server Administration
##________________________________________  ___________________________


#####  ==========  mysqladmin — Client for Administering a MySQL Server
	mysqladmin is a client for performing administrative operations
	mysqladmin --help
	mysqladmin -u root shutdown
	mysqladmin version
	mysqladmin variables
	mysqladmin ping      -->ora-dbping
	mysqladmin status/shutdown
##________________________________________  ___________________________


#####  ==========  mysqlshow — Display Database, Table, and Column Information
	If no database is given, a list of database names is shown.
	mysqlshow  --help
	mysqlshow --user=root  mysql
	mysqlshow -u rdb -prdb rdb  --> tables-list
##________________________________________  ___________________________


#####  ==========  mysqlmanager — The MySQL Instance Manager
	can be used in place of the mysqld_safe script to start and stop one or more instances 
##________________________________________  ___________________________


#####  ==========  DB.setup/move/copy-admins as a whole:
	-! see ref--2.11.5. Copying MySQL Databases to Another Machine
	- where location??:  mysqladmin variables | grepi datadir
	- db-files: *.frm  (.MYI, and .MYD files for MyISAM engine)
	--- copy between maschiens/servers/offline.bup/,...:
		-! see ref--2.11.5. Copying MySQL Databases to Another Machine
		-- easiest (although not the fastest) way to move a database between two machines is to run the following commands on the machine on which the database is located:
		shell> mysqladmin -h 'other_hostname' create db_name
		shell> mysqldump db_name | mysql -h 'other_hostname' db_name  ##--or with --compress if network slow!
		-- OR by dupfile-transfer:
		 mysqldump --quick db_name >dump1 #on local machine
		 copy dump1 and goto remote one:
		 shell> mysqladmin create db_name
		 shell> mysql db_name < dump1
##________________________________________  ___________________________


#####  ==========  user-management/create/query/drop/...:
	--- see:
		-! ref--5.5. MySQL User Account Managemen
		-  ref--12.4.1, “Account Management Statements”
	-! initial-/default-mysql.users have no PW (db-users as root, mysql, ...)!!:
	   The accounts that are listed in the MySQL grant tables initially have no passwords. After starting the server, you should set up passwords for them using the instructions in Section 2.10, “Postinstallation Setup and Testing”.
	--- syntax-usernames, specifying users:
		-! see  ref--6.2.3. Specifying Account Names  + !!table in 6.2.4. Access Control, Stage 1: Connection Verification !
		- syntax-username:  'user_name'@'host_name'. if only alphanum, then quotting not needed. user name and host name, if quoted, must be quoted SEPARATELY!
		-! empty-username: a blank value (empty string) as username  matches any user name!
		-! empty-hostname: a blank value (empty string) as hostname is equivalent to 'user_name'@'%'. For example,:'me' is equivalent to 'me'@'%'
		-- wild-cards: “%” and “_” , as in LIKE. but no-wildcards for hostnames-starting-with-digits! (but with IPs ok) [659]
			- ''@'%'  : any user from any host !!
			- 'fred'@'144.155.166.%'   bzw. 'fred'@'144.155.166.0/255.255.255.0'  : fred from any host in the 144.155.166 class C subnet
	--- showing/querying users, stored-locations:
		-!  select User,Host, Password from mysql.user;   #accounts are stored in the "user" table of the "mysql" database.
		-! who-am-i ? with which grants?:  select CURRENT_USER();  show grants;   ##-! if wanted, also select USER(); for DIFFs see section "Anonymous user"
			-!! precedence of identifying:  select host, user from mysql.user order by host desc;
			(due to ambigious names by anonymous users) so more specific hotnames have precedence!! see 6.2.4. Access Control, Stage 1: Connection Verification
		- listing created users:  mysql> select user, host, password,Grant_priv from mysql.user;
		-! usernames without hostname query:  SELECT SUBSTRING_INDEX(CURRENT_USER(),'@',1);
		- hostname only of users:  SELECT SUBSTRING_INDEX(CURRENT_USER(),'@',-1);
	---! Anonymous user and its side effects:
		- An account with a blank user name is an anonymous user.
		-!! a "blank-user-name" matches any user/anonymous-user, so an account of ''@'localhost' enables clients to connect as an anonymous user from the local host with any user name.
		  then if a client connects as user1 from the local host, USER() and CURRENT_USER() return different values!! CURRENT_USER show the final real db-user in effect!
		  see 6.3.11. SQL-Based MySQL Account Activity Auditing
		-! To specify an anonymous user in SQL statements, use a quoted empty user name part, such as ''@'localhost'
		- renaming/deletin anonymous-user:  RENAME USER ''@'localhost' TO 'user1'@'localhost'; 
	--- create-users:
		- eg, create-an-admin-user with privileges on everything AND connected from ANY host:   ref--6.3.2. Adding User Accounts :
		CREATE USER 'monty'@'localhost' IDENTIFIED BY 'some_pass'; GRANT ALL PRIVILEGES ON *.* TO 'monty'@'localhost' WITH GRANT OPTION;
		CREATE USER 'monty'@'%' IDENTIFIED BY 'some_pass';   GRANT ALL PRIVILEGES ON *.* TO 'monty'@'%' WITH GRANT OPTION;
		!! both lines for localhost + "%" are neccessary:
		!! It is necessary to have both accounts for monty to be able to connect from anywhere as monty.  Without the localhost account, the anonymous-user account for localhost that is created by mysql_install_db would take precedence when monty connects from the local host. As a result, monty would be treated as an anonymous user.
	--- deleting/dropping users:
		- drop user ...;
	--- Password-Setting for users:    ref--6.3.5. Assigning Account Passwords :
		- nachtraeglich:  mysql> SET PASSWORD FOR 'jeffrey'@'localhost' = PASSWORD('mypass');
		- by creation:    mysql> CREATE USER 'jeffrey'@'localhost' IDENTIFIED BY 'mypass';
		- cmdline:        shell>  mysqladmin -u user_name -h host_name password "newpwd"
	--- renaming users:
		- RENAME USER ''@'localhost' TO 'user1'@'localhost';
		- RENAME USER 'user2'@'%.example.com' TO 'user2'@'remote.example.com';
	--- alter users:
		- direct modifications of mysql.user table to create/del users: see  ref--12.4.1 ...
##________________________________________  ___________________________


#####  ==========  grants/revokes:
	-!! see  ref--6.2. The MySQL Access Privilege System :
	--- grant-stored in mysql-DB/Schema! Internally, the server stores privilege information in the grant tables of the mysql database
		- account privileges is stored in the user, db, host, tables_priv, columns_priv, and procs_priv tables in the mysql database (see Section 6.2.2, “Privilege System Grant Tables"
		-!! IN-MEMORY : MySQL server reads the contents of these tables INTO the MEMORY when it starts!! (so grant-changes require FLUSH PRIVILEGES; /OR server-restart !!)
		-! see "6.2.2. Privilege System Grant Tables" for details and also direct updating of grant-tables !
		-!! which privileges/grants are possible at all ?? and where saved??:   see Table 6.2. Permissible Privileges for GRANT and REVOKE
	--- grant-showing:
		- show grants;  bzw.:  
		- SHOW GRANTS FOR 'rdb'@'localhost';
		- SHOW GRANTS FOR CURRENT_USER();
		- SHOW GRANTS FOR 'joe'@'office.example.com';
	--- grant-updating without server-restart:
		-! FLUSH: grants are based on the IN-MEMORY copies of the grant tables! so:
		- after grant statements bzw. inserts directely into mysql.user, then:   mysql> FLUSH PRIVILEGES:
	--- grant-rights/privileges/speciefiers,  grant-system/-procedure of privileges:
		-!! see 6.2.1. Privileges Provided by MySQL  + there table 6.2 Permissible Privileges for GRANT and REVOKE
		-!! see "6.2.2. Privilege System Grant Tables" for procedure and rights-system
		- grant ALL / ALL PRIVILEGES : shorthand for “all privileges available at a given privilege level” (except GRANT OPTION ).
		  For example, granting ALL [650] at the global or table level grants all global privileges or all table-level privileges.
	--- eg:
		- MANUALLY grant FILE priv to all rdb users:
		  root.rdb mysql> update  mysql.user set File_priv='Y' where user like 'rdb%';  FLUSH PRIVILEGES; ##-bzw. more comprehensive:
		  root.rdb mysql> select user, File_priv from  mysql.user;  update  mysql.user set File_priv='Y' where user like 'rdb%';  FLUSH PRIVILEGES;  SHOW GRANTS FOR 'rdb'; select user, File_priv from  mysql.user;
		- FILE priv:  GRANT FILE ON *.* TO 'rdb'@'%';  ##-needed for select OUTFILE into ...
		- "create database rbd" who can??:  select user, Create_priv, db from mysql.db;
		- "create database" grant manully:  root> update mysql.user set Create_priv='Y' where user like '%rdb%'; FLUSH PRIVILEGES; #then rdb relogin!
##________________________________________  ___________________________


#####  ==========  DB-Infos / INFORMATION_SCHEMA :
	-!! see Chapter 20. INFORMATION_SCHEMA Tables
	- General-Infos to the Server/DBs/...: show status; show variables; bzw.  tables:  INFORMATION_SCHEMA GLOBAL_STATUS and SESSION_STATUS Tables #-see Ch--20.8
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
