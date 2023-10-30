##________________________________________  ___________________________


#####  ==========  sqlplus==============
--!! see
	- short-good-quick:  Rischert-WB-App.C
	- quick-ref: Ora9i-Docs-quickRef
	- Ora9i-Docs: ugRef + gs + quickRef
	- Oreilly-QRef

	_______:  OutPut-Settings: (with their default values):
- set autotrace on	:print execution statistics
- SET DEFINE  x	:instead & use x for substitution variables (cannot be alphanumeric or white space)
- set echo off	:lists each command in a script as the command is executed
- set feedback on	:Displays the number of records returned by a script
- set Heading on	:printing of column headings in reports
- set headsep on	:Defines the character used as the heading separator character
- set linesize 80
- set long 80	:blob/clob length
- SET NUM[WIDTH] {10|n}	:Sets the default width for displaying numbers
- SET PAGES[IZE] {24|n}	:Sets the number of lines in each page.
- SET PAU[SE] {ON|OFF|text}	:control scrolling of your terminal
- SET SERVEROUT[PUT] {ON|OFF} [SIZE n] [FOR[MAT] {WRA[PPED]|WOR[D_WRAPPED]|TRU[NCATED]}]	:DBMS_OUTPUT.PUT_LINE-lines
		Controls whether to display output (that is, DBMS_OUTPUT.PUT_LINE) of stored procedures
- SET SHOW[MODE] {ON|OFF}	:old-new  :lists the old and new settings
- SET TERM[OUT] ON	:script-outputs (not interactive statements)
- SET VER[IFY] {ON|OFF}	:sql-script-lines : Controls whether to list the text of a SQL (including old-new) --> OFF: show ONLY DBMS_OUTPUT-lines
- SET WRA[P] {ON|OFF}	:Controls whether to truncate the display of a selected row if it is too long for the current line width

	_______:  call:
	- sqlplus -Help
	- sqlplus  k152/k152@skdb     :eg-cmd:   title SQLPlus && cmd  /E:ON  /F:ON /T:4f  /K  sqlplus  k152/k152@skdb @%~dp0..\etc\dbs\t1.sql
	- {username[/password][@connect_identifier]|/} [AS {SYSOPER|SYSDBA}]  | /NOLOG
	- nologin-conn: SQLPLUS /NOLOG ; CONNECT SYS/PASSWORD AS SYSDBA ; STARTUP ; ...
	- with running a script:  sqlplus k152/k152@skdb @C:\Ablage\workspace\bkda\doc\dbs\t1.sql
	- /OR - sqlplusw  : win-version (cmd-version is better, due to command history)

	_______:  configs-starts (Site+User Profiles):
	- sql-prompt:
		COLUMN  instance_c  NEW_VALUE current_instance
		COLUMN  host_c      NEW_VALUE current_host		
		SELECT  INSTANCE_NAME instance_c, HOST_NAME host_c from V$INSTANCE ; -- /OR: SYS.V_$INSTANCE
		SET SQLPROMPT '&&current_instance &&current_host sql> '
	- site profile file is $ORACLE_HOME/sqlplus/admin/glogin.sql
	- usu. is named login.sql  in your current directory, and then the directories you specify with the SQLPATH environment variable
-! help:
	- installing help (us-EN): cd $oracle_home/sqlplus/admin/  ; SQLPLUS SYSTEM/manager (NOT in SYS-schema !!) ; @?/sqlplus/admin/help/hlpbld.sql helpus.sql
	- help index   :list of all commands  ; eg.  help column/.../
	- sqlplus -Help
- invoking/cmdLine:
	- executing scripts:	 @{ url | file_name[.ext] } [arg ...]  ; @filename == start filename ;
	- cmdline without going into the prompt, executing sqls, eg:
ora92@u015ada6:/export/home/ora92#   sqlplus -S "/ as sysdba" <<EEE
> shutdown immediate
> EEE
- edit/get/run @t1.sql
- setting the editor:		define  _editor = uedit32.exe
-  clear screen

	_______:  Setting/Unsetting:
	--- sqlp-Env/Config-attribs:
		- set + show ; eg. set  trimout  off ; show trimout
	--- User-Variables (user-/config-/env-varialbles):
		-! assigning a column-value to a the bind-variable aa1 :
			column INSTANCE_NAME new_value aa; 
			select INSTANCE_NAME from v$instance;  ---> now &&aa has the value of INSTANCE_NAME
			prompt &&aa;
		- showing(echo): 	define varName /OR define :shows all user variables
		- unsetting: undefine varName
		- setting (like set in cmd):	 define bb1 = ddd   ; DEF[INE] [variable]|[variable = text]
		- setting from cmdline: accept var1 ....(reads on line from cmdLine)
		- referencing a variable with:		&var1
		- using & as a normal char:  set define off  /OR set define <another-char>  ; SET DEF[INE] {&|c|ON|OFF}
		- Saving current setting of all system variables into a file:  STORE SET file_name ; restoring the saved configs: START   file_name
- connect skowner/skowner@skdb  ; disconnect
- DESCRIBE :command describes the structure of a table or view, detailing its columns and their datatypes and lengths
- edit  <filename>
- HOST command executes an operating system command without exiting SQL*Plus
- list :current sql buffer content
- set:
	- serveroutput on [size xxxx] :print server outputs (as from procedures/functions/plsql/..., or  DBMS_OUTPUT.PUT_LINE lines)
	- verify on : show old/new values of substitution variables (as &var1)
	- feedback 1        :show always #selected rows

	_______:  displaying/showing columns,...:
	- set wrap off/on (cutting of result lines ==off)
	- set linesize  130  (length of display-line)
	- column c1  format  A20  /OR for numbers $99.99
- Html-exporting-eg: SET MARKUP HTML ON SPOOL ON ; spo file1.html ; select * from T1 ; spo out ;
- writing/piping the output to a file:
	- starting writing: spo file1.txt  -> stopping/flushing writing: spo out ; alles zwischen "spo file1.txt  " und "spo out " wird NACH "spo out" in file1.tx reungeschrieben.

	_______:  Isqlplus:  (see: - quick-ref: Ora9i-Docs-quickRef)
	- http://machine_name.domain:port/isqlplus[?UserOpts]
	- http://machine_name.domain/isqlplusdba[?DBAOpts]
