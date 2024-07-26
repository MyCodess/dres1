##________________________________________  ___________________________


#####  ==========  setup/installs/rdbms-DIR...:
- ?/rdbms/admin/*.sql : ora standard packages
	- /rdbms/admin/catproc.sql  : main one used by creating a database
##________________________________________  ___________________________


#####  ==========  cmdLine-invokes-pls-scripts, ENV-interacts:
	- cmdLine-input-params exp: 92/ctx/sample/script/drjobdml.sql  : ... define idxname = "&1"  ; define interval = "&2" ;
##________________________________________  ___________________________


#####  ==========  SQLs in pls:
	- Data definition language (DDL) is not valid in a simple PL/SQL block (more advanced techniques such as procedures in the DBMS_SQL package will enable you to make use of DDL), yet data manipulation (DML) is easily achieved either by use of variables or by simply putting a DML statement into a PL/SQL block (4.1.1).
##________________________________________  ___________________________


#####  ==========  Source of a Procedure:
	- source of procudeures: select text from user_source where name='STATUSMELDUNG_ALARM';
	- source of eg. FILL_EJ procedure in a sql-script:
		select * from dba_objects where object_name='FILL_EJ';
		spool FILL_EJ_DWITSB02_070214.sql
		select text from dba_source where name='FILL_EJ';
		spool off
