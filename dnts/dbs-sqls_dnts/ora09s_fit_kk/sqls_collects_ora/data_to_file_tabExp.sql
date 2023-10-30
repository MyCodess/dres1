REM   This SQL script is to be run from SQL*Plus with the following syntax:
REM
REM     @"tabexp.sql" <schema owner> <table name> <ASCII Character Code delimiter>
REM
REM   And an output file will be created in the '<Oracle Home>\Bin' folder
REM   with the name:
REM
REM     <SCHEMA>.<TABLE NAME>.LST
REM
REM   For example, issuing the following call from SQL*Plus
REM
REM     @"D:\Oracle\Ora81\Scripts\tabexp.sql" SCOTT EMP 44
REM
REM     (NOTE: The ASCII Character Code 44 = ',')
REM
REM   returns a comma delimited text file of all the data in the EMP table of
REM   SCOTT's schema.
REM
REM   Caveats:
REM   (1) System defaults apply.  DATE datatypes are formatted based on the
REM       value of your NLS_DATE_FORMAT parameter.
REM   (2) The width of each row of delimited data that will be written to the
REM       output file has been set to 100 characters by default.  If your rows
REM       of data will be longer, please increase this value appropriately.
REM   (3) No National Language Support (NLS) datatype translation is performed.
REM   (4) LONG, LONG RAW, CLOB, BLOB, and BFILE datatypes are not translated
REM       since errors may occur.
REM   (5) Delimiter characters that are found in text fields being translated
REM       will be converted to the tilde (~) character.
REM
REM
--------------------------

  set echo off
  set feedback off
  set pages 0

REM  Increase the following value to the number of characters a row
REM  of delimited data in the table will require for export.

  set lines 100

  set verify off

prompt
prompt Creating command file for...
prompt
prompt schema owner = &1
prompt table name   = &2
prompt delimited by = ASCII(&3)
prompt

  set termout off
  spool cmd.sql

REM  Start writing the SQL statement to a temporary file, 'cmd.sql',
REM  in the <Oracle Home>\Bin folder.

  select 'Select rtrim(' from dual;

REM  We're converting everything to the CHAR datatype.
REM  Watch for extra spaces at the end of CHAR columns.
REM  Convert any embedded delimiter characters to tildes (~).
REM  Do not convert the following datatypes: LONG, LONG RAW,
REM  CLOB, BLOB, and BFILE

  select decode(data_type ,'NUMBER',   'to_char('
                          ,'DATE',   'to_char('
                          ,'CHAR',   'rtrim(translate('
                          ,'VARCHAR2', 'rtrim(translate('
                          ,NULL) ||
         column_name ||
         decode(data_type ,'NUMBER', ') || chr(&3) || '
                          ,'DATE', ') || chr(&3) || '
                          ,'CHAR'  , ',chr(&3),chr(126) )) || chr(&3) || '
                          ,'VARCHAR2', ',chr(&3),chr(126) )) || chr(&3) || '
                          ,' || chr(&3) || ')
  from all_tab_columns
  where   table_name = upper('&2')
    and   owner      = upper('&1')
    and   data_type not in ('LONG','LONG RAW','CLOB','BLOB','BFILE');

REMREMember that we concatenated an extra "||" on the end
REM  of the last column.  We can't leave it hanging, so put a
REM  space on the end of the row to maintain proper syntax.

  select 'chr(32))' from dual;

REM  Now, tack on the FROM clause...

  select 'from &1' || '.' || '&2;' from dual;
  spool off

REM  Done creating extract statement.  Wanna see it?

  set termout on
  get cmd.sql

prompt
prompt Hit any key to start the export, or press <ctrl>-c to cancel
  accept keypress
prompt
prompt Now exporting the delimited table...
prompt
prompt schema owner = &1
prompt table name   = &2
prompt delimited by = ASCII(&3)
prompt

REM  Uncomment the following line to suppress screen output of the results

REM  set termout off

REM  Let's export some Data!!

  spool &1..&2..LST
  @cmd.sql
  spool off

REMREMove the temporary spool file.

  host erase cmd.sql
  set termout on

prompt Export Completed.
prompt
prompt Spooled to file '&1..&2..LST' in <Oracle Home>\Bin.
prompt

REM  End of file.

