- validating database/block-corruptions,...:  BACKUP VALIDATE DATABASE ARCHIVELOG ALL; RMAN.UG-9-28 UG

	_______:  deleting expired catalog entries , ( here eg delte all older than 100 days):
	#-- from del_old_cat_entries_DWITSB02_tdp_autoGen_UwFe.rcv : tdp+tape
	connect target system/manager
	connect rcvcat rman/rman@DREC
	allocate channel for maintenance type 'SBT_TAPE' parms
	'ENV=(TDPO_OPTFILE=/opt/tivoli/tsm/client/oracle/bin64/tdpo_DWITSB02.opt)';
	crosscheck backup completed before 'SYSDATE - 100';
	delete noprompt expired backup completed before 'SYSDATE - 100';
	release channel ;
	# -------/OR manually without tdp,...:
	rman target / catalog rman/rman@drec 
	ora8:  allocate channel for maintenance type DISK ;
	ora9:  allocate channel for delete type DISK ;
	crosscheck backup completed before 'SYSDATE - 100';
	delete noprompt expired backup completed before 'SYSDATE - 100';
	release channel ;
--######## shorities: catalog-sql-queries for backups: ################
-! note: for all following sqls: basically all in rman-user-schema in catalog-DB as in : sqlplus rman/rman@DREC
- last_seq_in_rman : SELECT MAX(sequence#) FROM rc_backup_redolog WHERE status='A' AND dbinc_key= (SELECT dbinc_key FROM rc_database_incarnation WHERE upper(name)=upper('DWITSB06')  AND current_incarnation='YES');
