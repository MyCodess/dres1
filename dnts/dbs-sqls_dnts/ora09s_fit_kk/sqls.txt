- sqls + Ora9i
##________________________________________  ___________________________


#####  ==========  SQLs: =================
##________________________________________  ___________________________


#####  ==========  Sessions:
- SELECT sid, serial#, username, status,  LAST_CALL_ET, command, logon_time from v$session where username='FONETSUN' order by status, logon_time, sid;
##________________________________________  ___________________________


#####  ==========  DB-Dictionary: system/user views,tables,infos,...:
-!! USER_OBJECTS , ALL_OBJECTS :views containing all user/available DB-objects (tables,views,indexes,procedures,...)
-! list and description of all Dictionary-entries: select * from DICT; /OR select * from DICTIONARY; and DICT_COLUMNS for columns of DICT ; eg. SELECT column_name, comments FROM dict_columns WHERE table_name = 'USER_SEQUENCES'
-! useful synonyms-list: select * from all_synonyms where synonym_name not like '%\_%' ESCAPE '\' and synonym_name not like '%$%'order by length(synonym_name)  ;
	- eg for USER_xxx : OBJ, SEQ, SYN, COL, CAT (== USER_CATALOG), IND, TABS (== USER_TABLES),
- prefixes: USER_, ALL_, DBA_ , _PRIVS, ...; ALL_ == USER_ (owns) and all others available/granted to the current user;
-! general method for finding relevant DB-objects for eg. ROLEs: select * from all_objects where upper(object_name) like '%ROLE%';
- all user objects (tablrs, seq, ineexes, ...): select object_name, object_type from USER_OBJECTS ; ALL_OBJECTS shows owner too.
- tablespaces: USER_TABLESPACES view: list of tablespaces accessible to the current user;
- default user tablespace,...: USER_USERS view
- tables: select * from USER_TABLES; ALL_TABLES ; USER_TAB_COLUMN ;
- current tables sizes: select * from USER_SEGMENTS;
	 so current user schema size in KB: select sum(bytes)/1024 from user_segments;
- columns of all tablrs/objects: DICT_COLUMNS , USER_TAB_COLUMN ,
- comments of user/system objects:
	- system: ALL_COL_COMMENTS and ALL_TAB_COMMENTS (for columns and tables resp.)
	- user:   USER_COL_COMMENTS and USER_TAB_COMMENTS views
	- in DICT_COLUMNS one finds anyway all columns+comments+....; eg. SELECT column_name, comments FROM dict_columns WHERE table_name = 'USER_OBJECTS' AND column_name IN ('STATUS', 'LAST_DDL_TIME', 'CREATED')
- views: USER_VIEWS , ALL_VIEWS ; key-preserved table/columns of a view:  USER_UPDATABLE_COLUMNS
	- the select statement of view is saved in TEXT column:
	- The TEXT column in the USER_VIEWS data dictionary is of the LONG datatype. By default SQL*Plus does not display more than 80 characters of a LONG. You can increase this length with the SQL*Plus SET LONG command and wrap whole words using the SQL*Plus FORMAT COLUMN command with the WORD_WRAPPED option.
- indexes:  USER_INDEXES and USER_IND_COLUMNS
- sequences: USER_SEQUENCES ,
- constraints: USER_CONSTRAINTS , USER_CONS_COLUMNS , ALL_CONSTRAINTS
	- eg. SELECT constraint_name, table_name, constraint_type FROM user_constraints
	- constraint_type (see Rischert-Table 13.2. Constraint Types)  :The foreign key constraint is listed as constraint type R (Referential Integrity constraint), the NOT NULL and check constraints are shown as constraint type C, and the primary key constraints are displayed as constraint type P. The SECTION table has a unique constraint listed as constraint type U
- synonyms: USER_SYNONYMS (== SYN); ALL_SYNONYMS ;
- objects (also columns,...): USER_OBJECTS (== OBJ), ALL_OBJECTS
- dependencies:  USER_DEPENDENCIES , ALL_DEPENDENCIES
- users: select * from ALL_USERS ;
	- current user: select * from USER_USERS ;
- priviliges (Table 14.4): select object_name from all_objects where object_name like '%_PRIVS'; eg. USER_SYS_PRIVS , DBA_SYS_PRIVS ;
- roles (Table 14.5): select * from all_objects where upper(object_name) like '%ROLE%';
- stored procedures: USER_SOURCE , USER_OBJECTS ;
##________________________________________  ___________________________


#####  ==========  date/time:
- to_date...:
	insert into T4(col1, col2) values ('Str2', to_date('2002-02-05 00:00:00', 'YYYY-MM-DD HH24:MI:SS')); /OR:
	alter session set nls_date_format='YYYY-MM-DD HH24:MI:SS'; insert into T4(col1, col2) values ('Str32', to_date('2002-02-05 00:00:00'));
- DB-server-timezone/functions:
	-! differentiate between (functions for) LOCAL (:client) and SYSTEM (:server) date/time and zones
	- System-Date/Time (server): SELECT DBTIMEZONE, SYSDATE, SYSTIMESTAMP FROM dual ;
	- current date-time:  SELECT TO_CHAR (SYSDATE, 'DD-MM-YYYY HH24:MI:SS')"NOW" FROM DUAL;
	- Client/Session-Date/Time (server):select  CURRENT_DATE, CURRENT_TIMESTAMP, LOCALTIMESTAMP, SESSIONTIMEZONE from dual;
	- changing: ALTER SESSION SET TIME_ZONE = '-8:00'/'America/New_York'/dbtimezone/local/...
- quering DB-system-parameters (as in init.ora, default-dateformat, ...):
	SELECT SYS_CONTEXT ('USERENV', 'NLS_DATE_FORMAT') FROM dual
##________________________________________  ___________________________


#####  ==========  dba, general-DB, basic structure:
##________________________________________  ___________________________


#####  ==========  queries:
- NULL-columns: user NVL(column-name, 0) to get rid of NULL-problems if neccessary, eg: select * from course WHERE NVL(cost,0) < 1595
##________________________________________  ___________________________


#####  ==========  creates:
- table-copying (or partly/short-version) to a test table in one action:
	- eg. create table testsection as select * from section where course_no in (25, 135);
	- or copying only structure eith no data:  create table testsection as select * from section where 1=2;
	- however only data+column-structure will be copied, but not constraints,...
	- Tables created with this construct do not inherit referential integrity, indexes, or any other objects associated with the base table except the not null constraints, which receive a system-generated name starting with the letters SYS_.
- files to tables (see 11.1 Rischert): (eg f1.csv file in /N/0lager/0apps/oracles dir.):
	- as sys do: GRANT CREATE ANY DIRECTORY TO student;
	- student: create directory t1_dir as '/N/0lager/0apps/oracles';
	- CREATE TABLE t1_ext (student_id NUMBER(3), last_name VARCHAR2(25), first_name VARCHAR2(25))
		ORGANIZATION EXTERNAL (TYPE oracle_loader DEFAULT DIRECTORY t1_dir ACCESS PARAMETERS (FIELDS TERMINATED BY ',' (student_id, last_name, first_name)) LOCATION ('f1.csv'));
- copying the data of a table_A to do testing on the table_A and restoring table_A again:
	- copying data to dummy table: create tmp_table as select * from table_A ;
	- after finishing testings: truncate table_A ; insert into table_A select * from table_tmp;
- compound PK: When a primary key on a table consists of more than one column, the constraint must be written as a table-level constraint.
##________________________________________  ___________________________


#####  ==========  ALTER

	_______:  new/enabling/activating constraints:
	- chacking if new PK ok before enabling: SELECT section_id, COUNT(*) FROM section GROUP BY section_id HAVING COUNT(*) > 1
- no ROLLBACK for DDLs as alter,crete,... . And they implicitly/automaticly commit ALL changes up to now without asking!!
- finding violations (Rischert-11.2): Another way to identify constraint violations: Oracle also allows you to record all the rows violating a constraint in a table called EXCEPTIONS with the Oracle script utlexcpt.sql found in the %ORACLE_HOME%\rdbms\admin directory. You can then use the ALTER TABLE tablename ENABLE CONSTRAINT constraint_name EXCEPTIONS INTO exceptions syntax to place the violating rows into the EXCEPTIONS table.
##________________________________________  ___________________________


#####  ==========  pseudo columns:
- ROWID  :the unique physical address of the row; fixed identifier for each row INdependent of select statement (as AAABkGAAGAAAAGlABk); It is the fastest way to access a row.
- ROWNUM :number assigned to the rows of the current select statement (starting from 1 to count(*) )
##________________________________________  ___________________________


#####  ==========  Partitioned Tables:

	_______:  views/tables/infos to parts: (sames for partitioned indexes)
-! 1. USER_PART_TABLES : 	smaller/more.general tab; object-level partitioning information for the partitioned tables (so more general/DB-Level); eg: only count of parts in each tables, so not more details!!
-! 2. USER_TAB_PARTITIONS:	larger/more.detailed tab; partition-level partitioning information ; information to partitions of each table (partition-details/level)
- views:  user_tab_partitions, user_part_tables, user_ind_partitions, user_part_indexes

	_______:  sqls-parts:
- select TABLE_NAME, PARTITION_NAME, logging, TABLESPACE_NAME from user_tab_partitions order by 1,2;
- which tables are partitioned at all?:  select TABLE_NAME, PARTITIONING_TYPE , PARTITION_COUNT from user_part_tables;
- Number of partitions of each partitioned-table: 
	select TABLE_NAME,PARTITION_COUNT from user_part_tables order by PARTITION_COUNT;   -- /OR:
	select count(PARTITION_NAME) No , TABLE_NAME from user_tab_partitions group by TABLE_NAME order by 1,2 ;
- list of partitions of certain table:   select TABLE_NAME, PARTITION_NAME from user_tab_partitions where TABLE_NAME='&1' order by PARTITION_NAME;
- gather-statistics in parts: select TABLE_NAME, PARTITION_NAME, to_char(LAST_ANALYZED,'DD_MM_YYYY HH24:MI:SS') from user_tab_partitions order by 3;
##________________________________________  ___________________________


#####  ==========  Partitioned INDEXES:
- views: user_part_indexes, 
- global OR local?: (LOCALITY column):  select INDEX_NAME, TABLE_NAME , PARTITIONING_TYPE, LOCALITY from user_part_indexes;
- partitioned-indexes:
	- listing of types of part-indexes:
	 select INDEX_NAME, TABLE_NAME, PARTITIONING_TYPE, LOCALITY from dba_part_indexes where owner='WITSB1' order by 1, LOCALITY;
	- infos (joined): select i.INDEX_NAME, i.INDEX_TYPE, i.logging i_log, p.logging p_log, i.degree, p.PARTITION_NAME \
	 from user_indexes i , user_ind_partitions p where i.index_name=p.index_name  AND i.index_name='PK_SERVER_EJ';
- select INDEX_NAME, PARTITION_NAME, STATUS from user_ind_partitions where index_name='PK_BEHAELTER'  order by 1,2
##________________________________________  ___________________________


#####  ==========  indexes:
- DICT indexes:  USER_INDEXES and USER_IND_COLUMNS, user_ind_partitions, user_part_indexes
- usage?: V$OBJECT_USAGE , only if monitored!!: alter index myindex1 monitoring/nomonitoring usage; :start/stop monitoring

	_______:  infos-ind:
	column degree format A5
	column INDEX_TYPE format A10
	- select INDEX_NAME, INDEX_TYPE, TABLE_NAME, TABLESPACE_NAME, LOGGING, DEGREE from user_indexes;
##________________________________________  ___________________________


#####  ==========  misc:
- newline in a select statement: CHR(10)
