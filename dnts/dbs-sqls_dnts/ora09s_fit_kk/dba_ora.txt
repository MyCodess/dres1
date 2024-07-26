-- basiert auf Ora92
##________________________________________  ___________________________


#####  ==========  ora-FileNames-Abbrev./Variables:
	- for rman-files see!: rman92_ref-CH.2.36 : "BACKUP->Keywords and Parameters"
	- for archive-redologs, DFs: admin92-8.11 + 3.8
##________________________________________  ___________________________


#####  ==========  Startup,...:
	- nomount --> initSID.ora  ; mount -> controlfile ; open --> DBFs, DB-Files,. TS,...
	- startup restrict ; later to open: ALTER SYSTEM DISABLE RESTRICTED SESSION;
##________________________________________  ___________________________


#####  ==========  init-parameters:
	-  select NAME,ISDEFAULT, ISSES_MODIFIABLE from v$parameter order by 1;
##________________________________________  ___________________________


#####  ==========  Processes, OS-system Ora:
- Listener-Procs : psg tnslsnr
- Intelligent Agent-Processes: psg dbsnmp
- Oracle Management Server und Console-Processes: psg oms
##________________________________________  ___________________________


#####  ==========  RedoLogFiles:
- status logfiles active/passive/archives...:  select STATUS, GROUP#, ARCHIVED , THREAD# , SEQUENCE# ,  MEMBERS from v$log;
- relog filenames,path...: column MEMBER format A50 ; select * from v$logfile;

	_______:  resizing online redologs (but better alternative: adding NEW group as tranfer-status...; but hier easier way, however be carefull!!):
	select * from v$logfile;
	select * from v$log;  -- suppose 4 is in the "CURRENT"-status , so drop and resize grop 3 very quickly:
	alter database drop logfile group 3;
		-- ! on SYS/unix:  rm  /data/oradata/DFON209/REDOLOGS/redo31.log /data/oradata/DFON209/REDO_SPIEGEL/redo32.log
	alter database add logfile group 3 ( '/data/oradata/DFON209/REDOLOGS/redo31.log' , '/data/oradata/DFON209/REDO_SPIEGEL/redo32.log' ) size 100M;
	... and the same for all other groups, and inbetween always:
	alter system switch logfile;  select * from v$log; ...
	till are done ....
	after all, 6 times do: alter system switch logfile;  select * from v$log;

	_______:  
##________________________________________  ___________________________


#####  ==========  archive logs:
-- enabling/disabling automatic archiving: 
	- after instance started: ALTER SYSTEM ARCHIVE LOG STOP /START ;
	- by startup in init.ora:  LOG_ARCHIVE_START=FALSE / TRUE;
	- check it: archive log list (--> Automatic archival ...)

	_______:  ---- archivelog_aus.sql:
connect /AS SYSDBA;
alter system switch logfile;
shutdown immediate
startup mount
alter database noarchivelog;
shutdown immediate;
exit;

	_______:  ---- archivelog_an.sql:
connect /AS SYSDBA;
shutdown immediate
startup mount
alter database archivelog;
shutdown immediate;
exit;
##________________________________________  ___________________________


#####  ==========  DBA-Views/Tables-Docs: list of all DBA-Views/Tables with descriptions in:
	- Ora-Docs-DB-Ref: Oracle9i Database Reference , oracle9i-docs-cd\B10501_01\server.920\a96536\toc.htm  /OR in:
	- OraNutSHell_s-CH-06: Data Dictonary (/W/Docs/DBs/Books_DB/Oracles/Oracles_Allg_DBAs_p/OracleNutShell_0212_s/0index.html)
	- Only their listing (without description): Oracle_DBA_SQL_QuickRef_1ed_PTR_0306  : CH-03
##________________________________________  ___________________________


#####  ==========  misc-dba-notes:
- DBA role does not include the SYSDBA or SYSOPER system privileges; but they are NEEDED for BASIC DBA-Operations (Basic== even when the database is not open, so privileges totally outside of the database itself.; so on OS-Level); they can also be thought of as types of connections (for example, you specify: CONNECT AS SYSDBA)
- default schemas for : SYSDBA this schema is SYS; for SYSOPER the schema is PUBLIC. ; SYSDBA or SYSOPER are only System-Privilieges/Connection-Types !
##________________________________________  ___________________________


#####  ==========  controlFiles:
	- (startup mount); alter database backup controlfile to trace as '/tmp/ctlf1.lst' ;
##________________________________________  ___________________________


#####  ==========  misc-dba-sqls:
##________________________________________  ___________________________


#####  ==========  sessions, user-connection:
-- active Sessions:
	column machine format A40
	column schemaname format A15
	column username format a10
	column osuser like username
	select osuser, user#, username,  user#, SID, Serial#,  machine, schemaname, status from V$SESSION;
			or with: ...where username='SYS' ;
	SELECT sid, serial#, username, status,  LAST_CALL_ET, command, logon_time from v$session order by status, logon_time, sid;
	select sid, sum(value) value_sum from v$sesstat  group by sid order by 2;
- disconneting session soft: alter system disconnect session '59,26919' post_transaction; --wait for open transactions
- killing a session eg: alter system kill session '132,60835'; '<SID>,<Serial#>'; the client will notice it by the next query
##________________________________________  ___________________________


#####  ==========  Dictionary:
- select * from dict where TABLE_NAME like '%&name1%'  order by 1;
- rdbms/admin/catalog.sql script contains definitions of the views and public synonyms for the dynamic performance views.
- searching based on column-names:  select TABLE_NAME, COLUMN_NAME, OWNER, DATA_TYPE from DBA_TAB_COLUMNS where COLUMN_NAME='...' order by 1;
- object-infos: select * from dba_objects where object_name='....';
##________________________________________  ___________________________


#####  ==========  DB-/Instance-Infos:
- select * from  V$DATABASE;  -- or  v_$database;  contains:  DBID,...
- select * from v$instance;
##________________________________________  ___________________________


#####  ==========  Ora-OS/System-level:
- 32 or 64 bit sys? : solaris: /opt/ORCLfmap/prot1_32 or 64 ? -> see orahome/root.sh
################# SQL-DBA-collects: ############################
##________________________________________  ___________________________


#####  ==========  Instance/DB-Infos:
- Release/version of the current DB : SELECT * FROM SYS.PRODUCT_COMPONENT_VERSION;
- Instance/DB infos:  SYS.V$INSTANCE , SYS.DATABASE_PROPERTIES
- select * from v$database; : database information from the control file.
- select * from v$version; : version numbers of core library components in the Oracle database server
-  select * from v$instance ; state of the current instance
- select * from v$option ; : options that are installed with the Oracle server.
