____________ mysql-client-programms in cmdline ___________________________
##________________________________________  ___________________________


#####  ==========  docs-mysql.client, see:
	-!! mysql --help
	- ref--4.5. MySQL Client Programs
	- ref--4.5.1. mysql — The MySQL Command-Line Tool
	- ref--4.5.1.1. mysql Options
	- config-files:  ref--4.2.3.3. Using Option Files +  mysql --help
	-! ref--CH.4.5.1. mysql — The MySQL Command-Line Tool
	- Chapter 3. Tutorial
##________________________________________  ___________________________


#####  ==========  help in mysql> :
	- see 12.8.3 “HELP Syntax” + 5.1.8. Server-Side Hel
	-!! if helps not there:  shell> mysql -u root mysql < fill_help_tables.sql  ##see 5.1.8. Server-Side Help
	-!! or just view fill_help_tables.sql : whole help-texts are there for mysql.shell (in suse: /usr/share/mysql/fill_help_tables.sql )
	-!!  mysql> help contents , ... --all helps/sql.syntax/user.mgm/... are there!!
##________________________________________  ___________________________


#####  ==========  invoking mysql-cmdline, shell-interacts:
	shell> mysql -v -h 127.0.0.1  -u myname -pmypass mydb  ##-!! for localhost use IP-adresse! see 4.2.2. Connecting to the MySQL Server
	-! with  "-v" :  mysql with the --verbose [264] option, which causes each statement to be displayed before the result that it produces.
	- shell-readin-readout: shell> mysql db_name < script.sql > output.tab
	- shell-cmds out of mysql-prompt:   mysql> system pwd;
##________________________________________  ___________________________


#####  ==========  options/configs/vars-mysql-client-tool (shell> mysql): options/params/configs/...:
	-! listion of options for mysql-client:  ref--4.5.1.1. mysql Options
	---!DIFF:   options  <-->  system.VARs  <-->  user.VARs  :
		- options == cmdline.params for client/server startup: are Startup params, which can be on the command line, through configuration files, or both.
		- system.VARs == Server-vars/-params/-options: can be set by SET ; define/indicate the SERVER-configurations. SOME of which can be modified by running server/dynamic; see mysqld --verbose --help for listing !
		- user.VARs (@xx-vars): user.defined.vars (as in pl/sql) to keep query results,...
		-- listings:
		- options-listing with :     shell> mysql -v --help  :options can be set on mysql-client commandline or in option-files!
		- system.VARs-listing with:  mysql> show variables;
		- user.VARs-listing  (@xx vars) as in:   set @v1=11;  select @va;
	--- setting/showing  options for mysql-client:
		- showing:  shell> mysql -v --help
		- setting: either on cmdline as mysql --auto-vertical-output=true  /OR in config-files as in ~/.my.cnf (same names and syntax but just without "--")
			1- shell> mysql --pager=less
			2- in .my.cnf in [mysql] or [client] group:   pager=less  ...
			3- mysql> pager less  ##unsetting with just  mysql> pager  ##-!!- NOT all option can be reset from inside mysql> prompt ! so not all are dynamic!!
	---! option-files for mysql-client:
		-!! see:  mysql --help :   VERY comprehensive listing!:
			Default options are read from the following files in the given order:
			/etc/my.cnf /etc/mysql/my.cnf /usr/local/mysql/etc/my.cnf ~/.my.cnf
			groups for mysql-client: [mysql] and  [client]
		- [client] option group is read by ALL client programs including mysql (but not by server mysqld)!
		- option-names in .my.cnf are the SAME as in mysql --help but just without "--", so eg "--host=xxx" will be "host=xxx"
		-! including your files (uue-configs) in .my.cnf:  !include ~/mysql1.cnf
		-! NOT reading the option file:  mysql --no-defaults ...
		-!! define defaults and include in .my.cnf, and then you, for Abweichungen, use as FIRST argument:
		   mysql --no-defaults/--defaults-file=xxx/--defaults-extra-file=xxx or jsut --print-defaults
		-! printout USER-options-settings:  mysql --print-defaults
	---! usefull options mysql-client:
		-! -v /--verbose :  mysql with the --verbose [264] option, which causes each statement to be displayed before the result that it produces.
		- ctrl-C ignoring:  mysql --sigint-ignore ... ##then use "\c" to ignore the current line!
		- --auto-rehash : TAB-completion of tablenames,..
	--- vertical output:
		- only-this-stmt:   \G : vertical output only this stamt: select * from clearing_house \G;
		- only-this-session:  mysql -E / --vertical
		- globally vertical output as default with option:   auto-vertical-output=true
##________________________________________  ___________________________


#####  ==========  SYSTEM.VARs setting/showing in mysql-client:
	-!DIFF SYSTEM.VARs  <-->  options !! see above DIFF!
	--- show current system.Vars:     see 13.7.5. SHOW Syntax :
		mysql> show variables;   ##- many server-vars, ...
		mysql> show variables like 'auto%';
		mysql> show global variables like  '%inter%';
		SHOW GLOBAL VARIABLES;  ##system-options/configs....
		SHOW [GLOBAL | SESSION] VARIABLES [like_or_where];
	--- setting of SYSTEM.VARs:      see 13.7.4. SET Syntax :
		- SET statement assigns values to the following variables that affect the operation of the server or your client:
		  System variables. See Section 5.1.4, “Server System Variables”
		  User-defined variables. See Section 9.4, “User-Defined Variables”.
		  Stored procedure and function parameters, and stored program local variables. See Section 13.6.4, “Variables in Stored Programs”.
		- eg:  mysql> SET GLOBAL max_allowed_packet=16M;   SET sort_buffer_size=10000;
##________________________________________  ___________________________


#####  ==========  user.VARs-setting/using/showing in mysql-client (@xx vars):
	- setting/showing of user.VARs (@...):   set @v1=11; select @va;
##________________________________________  ___________________________


#####  ==========  errors/debugs/problemshooting:
	- perror : ora-oraerr: A utility that displays the meaning of system or MySQL error codes. See Section 4.8.1, “perror — Explain Error Codes”.
	- mysql> SHOW WARNINGS;
##________________________________________  ___________________________


#####  ==========  prompt:
	-! see
		- ref--4.5.1.2. mysql Commands" for details 
		-! for flags in MYSQL_PS1 bzw. in prompt=xxx  see second table in "4.5.1.2. mysql Commands" [269]
	--- setting prompt in mysql-client:
	1- shell-ENV:  export MYSQL_PS1 ; eg: export MYSQL_PS1="(\u@\h) [\d]> "  #-for: (user@host) [database]>  
	2- cmdline: mysql --prompt="..." 
	3- interactively:  mysql> prompt (\u@\h) [\d]>\_
	4- in .my.cnf :     prompt=....
	- goback to dafult prompt:  mysql> prompt
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
