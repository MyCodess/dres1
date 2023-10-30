______________*ORA-cmdLineTools-bin-executables-Shells-Configs-DIRs-p*_________________________
- see also: LX-ora-install-docs:  post-inst.htm
##________________________________________  ___________________________


#####  ==========  cmds and cmd-tools:
- auto-start/stop: orahomeBin/dbstart and dbshut  --> read all entries from oratab, depending on Y/N   :see install_ux.pdf-4.4
- starting an instance, eg:
	- first with sqlplus-nologin-conn start the instance: SQLPLUS /NOLOG ; CONNECT SYS/PASSWORD AS SYSDBA ; STARTUP ; ...
	- then start listner:  lsnrctl start
	- start isql/ora-apache:  $ORACLE_HOME/Apache/Apache/bin/apachectl stop/start/...
	- test the listener:  lsnrctl stop/start/status
- listener-check:
	- lsnrctl status listener_name/sid-name ,eg: lsnrctl services db1
	- lsnrctl stop/start/status
	- listener starting: /opt/oracle/product/9.2.0/bin/lsnrctl start LIS1
	- log:/opt/oracle/product/9.2.0/network/log/LIS1.log
- apache/isql:
	- $ORACLE_HOME/Apache/Apache/bin/apachectl stop/start/startssl/...  :7777
	- default url: http://23.1.179.11:7777/isqlplus
		http://23.1.179.11:7777/isqlplusdba
	- check if is running: ps -elf | grep httpd
	- conf: $ORACLE_HOME/Apache/Apache/conf/httpd.conf and there see also include... 
- dbhome "$ORACLE_SID"
- sqlplus-login/conn.testing: sqlplus username/password@net_service_name ,eg. sqlplus  scott/tiger@db1
- ENV-stuff: $ORACLE_HOME/bin/oraenv
- Demo-tables (emp,..) manually generation: Lx-AdminRef-ch3_sql.html: Using Demonstration Tables
	- $ sqlplus SCOTT/TIGER  ; SQL> @?/sqlplus/demo/demobld.sql /OR:
	- $ORACLE_HOME/bin/demobld shell script: $ demobld SCOTT TIGER
- oerr  : quering about error messages, eg. oerr ORA 00939
##________________________________________  ___________________________


#####  ==========  gui-tools (mainly in $ORACLE_HOME/bin):
- netmgr	: networkmanager
- dbca : Database Configuration Assistant ,create,delete,... default or cust. instances/DBs.
- netca :network/listener config-manager
- universal-installer:	/cdrom_mount_point_directory/runInstaller
- netmgr	: networkmanager
- dbua :DB-update-assi.
- emca :entp. manager conf. ass.
- esm :entp. security manager: login management,...
- netmgr :net manager: instances,listeners,...
	- service names: enters instance/service-name in tnsnames.ora (so tnsping ==OK)
	- listener: enters the instance name in listener.ora (no tnsping)
##________________________________________  ___________________________


#####  ==========  Java-Ora:
- install Java in Ora: from sqlplus as sysdba:  @?/javavm/install/initjvm.sql
##________________________________________  ___________________________


#####  ==========  dirs/configs/...:
- $ORACLE_HOME/dbs  :default dir for the server init parameter (Win: /database)
- local bin directory == /usr/local/bin
- /etc/oratab	:instaces,startup,..
	*:/opt/oracle/product/9.2.0:N
	db1:/opt/oracle/product/9.2.0:N
	OEMREP:/opt/oracle/product/9.2.0:N
- /usr/local/bin/oraenv :env, switching,...
- http://localhost:7777/isqlplus  /OR isqplusdba if configured http-dba-user.
##________________________________________  ___________________________


#####  ==========  DB-instances, config,templates,create,...
	- init file: $ORACLE_BASE/admin/<sidname>/pfile/init<SID>.ora ; changes need DB-restart
	- init-template for new DBs: $ORACLE_HOME/dbs/init.ora
	- config-files:  $ORACLE_BASE/admin/<db_name>/pfile
	- control/dbf/redoLog-files: $ORACLE_BASE/oradata/<db_name>
##________________________________________  ___________________________


#####  ==========  db1 instance configs (as e.g.):

	_______:  admin,config files:
{ORACLE_BASE}/admin/{DB_NAME}/pfile/init.ora	:initializ-params
{ORACLE_HOME}/dbs/spfile{SID}.ora		:server params file, insteead of init.ora
{ORACLE_BASE}/admin/{DB_NAME}/udump +b/c	:user trace files +bg + coredump

	_______:  runtime/DB files:
- controlfiles:	{ORACLE_BASE}/oradata/{DB_NAME}/
- datafiles:	{ORACLE_BASE}/oradata/{DB_NAME}/example01.dbf
- user+pw: SCOTT + TIGER , system + oracle , sys + manager
- db1 = 	(DESCRIPTION = 		(ADDRESS_LIST = (ADDRESS = (PROTOCOL = TCP)(HOST = in82)(PORT = 1521)) ) 		(CONNECT_DATA = (SERVER = DEDICATED) (SERVICE_NAME = db1) ) 	)
##________________________________________  ___________________________


#####  ==========  install collects:
- OraHome920
- defaults-user+pw: SCOTT + TIGER , system + manager , sys + ...expiresOnLogin
##________________________________________  ___________________________


#####  ==========  docs, protocols, misc-infos,...:
- SQL*Net (Version 7) == Net8 (Version 8) ==Oracle Net (Version 9i) :provides the required communication protocol to the server.
