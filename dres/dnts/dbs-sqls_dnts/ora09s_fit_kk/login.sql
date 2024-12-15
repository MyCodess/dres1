-- version withOUT USER-Name , but WITH V$INSTANCE (fixed view)
--    with non-fixed  V_$INSTANCE NO queries possible in mount status; only in open status
--     V$INSTANCE (fixed view) also available in mount status

-- SET SHOWMODE ON
SET LINESIZE  138
-- SET NUMFORMAT $99,999
SET PAGESIZE  300
-- SET PAUSE ON
SET PAUSE '======= Press RETURN to continue ..... ====='
-- set TIME to ON if need Benchmarking for statements:
SET TIME OFF
SET VERIFY ON

-- ______  COLUMN formats:
COLUMN COMMENT  FORMAT  A50
column DEST_NAME format a20
column DESTINATION format a60
column ERROR format a30
COLUMN FILE_NAME FORMAT A60
COLUMN HOST_NAME FORMAT A15
column LOG_USER format A15
COLUMN NAME FORMAT A40
column OBJECT_NAME format a40
column OBJECT_TYPE format a20
COLUMN OWNER FORMAT A15
COLUMN TABLE_NAME FORMAT  A40
COLUMN TABLESPACE_NAME FORMAT A20
-- COLUMN VALUE FORMAT A40
column what format a50
-- _______ like-formats:
COLUMN COMMENTS like COMMENT
COLUMN DESCRIPTION like COMMENT
COLUMN GRANTEE  like OWNER
COLUMN GRANTOR  like OWNER
column MEMBER   like FILE_NAME
-- COLUMN PROPERTY_VALUE like VALUE
column SCHEMA_USER like LOG_USER

-- seting prompt to User/DB:
SET TERMOUT OFF
-- COLUMN  username_c  NEW_VALUE current_username
COLUMN  instance_c  NEW_VALUE current_instance
COLUMN  host_c      NEW_VALUE current_host

-- SELECT  USERNAME username_c FROM USER_USERS;
-- SELECT  INSTANCE_NAME instance_c, HOST_NAME host_c from SYS.V_$INSTANCE;
SELECT  INSTANCE_NAME instance_c, HOST_NAME host_c from V$INSTANCE;
-- SET SQLPROMPT '&&current_host,&&current_instance,&&current_username sql> '
SET SQLPROMPT '&&current_host &&current_instance sql> '
SET TERMOUT ON
-- if prefered, setting prompt only to DB-name:
-- SET SQLPROMPT   '&_CONNECT_IDENTIFIER  SQL> '
-- PROMPT ===== SQLP-Settings-done =====
-- -!-problem with check_space if date format changed:
-- alter session set nls_date_format='YYYY-MM-DD HH24:MI:SS';
-- PROMPT
-- !stty erase ^?  !problems if non-interactive-shell!!
