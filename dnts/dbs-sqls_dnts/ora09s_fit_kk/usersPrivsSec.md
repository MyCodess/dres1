______________ ORA-users/privs/roles/sec/...:
##________________________________________  ___________________________


#####  ==========  Roles/Privs: (Curr == current USER)
- Roles-Curr-Listing:	what are MY curr active roles in my cur seesion?:  select * from session_roles;
- Roles-All-Existing-Listing:	Listing all existing Roles?:  select * from dba_roles order by role;
- Roles-All-Assigned-to-Users (Roles<->Users , who/what?):  select * from dba_role_privs order by 1;
- Privs-All(-Granted-anytime to anybody):	select * from dba_sys_privs order by privilege, grantee;
- Privs-Curr to me (NOT detailed; also containg Roles):  select * from user_sys_privs;
- Privs-Curr-Listing-Details: select * from session_privs ; (/OR manually:  select rsp.privilege  from role_sys_privs rsp , user_role_privs urp where urp.GRANTED_ROLE=rsp.role;)
- Privs-Role-X:		listing all prives in a Role: select * from ROLE_SYS_PRIVS where ROLE='DBA';

	_______:  views for roles/privs:
- select * from dict where table_name like '%ROLE%';
- select * from dict where table_name like '%PRIV%'; 
- ora-roles are creted by ./rdbms/admin/sql.bsq , catexp.sql , catalog.sql ,.... 
##________________________________________  ___________________________


#####  ==========  Users:
- users attr.: col EXTERNAL_NAME for a15 ; select USERNAME, USER_ID, DEFAULT_TABLESPACE, TEMPORARY_TABLESPACE, EXTERNAL_NAME from dba_users;
##________________________________________  ___________________________


#####  ==========  PW-mgm:

	_______:  changing user-PW to login as the user and setting it back to the original one:
	- select password from dba_users where username='U1';  -->  3A2F0F2C4AC6DEBC
	.... alter user U1 identified by 'test1'; conn U1/test1 ; ... do stuff;
	- changing back: alter user U1 identified by values '3A2F0F2C4AC6DEBC'; <--- old PW from
--############################## collects: ###############################
-===== User-Mgm, Roles, Privliges,...:
select * from DBA_USERS;
select * from sys.dba_roles;
select * from sys.DBA_ROLE_PRIVS where grantee='DBA';
select * from dba_sys_privs  where grantee='RESOURCE';

	_______:  -

	_______:  -----
