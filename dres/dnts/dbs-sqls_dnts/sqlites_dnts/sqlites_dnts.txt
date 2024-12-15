_____________________ sqlite-dnts : __________________________________________________
/_230109  :  start-dnts ! based on sqlite3-docs:  file:///usr/share/doc/sqlite/index.html   bzw. same online:   https://sqlite.org/docs.html
##________________________________________  ___________________________


#####  ==========  SQLite on arx ,  core/sqlite 3.40.1-1, /_230109  :

	_______:  setup-arx:
pacman -Ss SQLite              ##--... core/sqlite 3.40.1-1 [installed]
pacman -S  core/sqlite-doc     ##--  /usr/share/doc/sqlite/index.html
pacman -S  community/sqlitebrowser

	_______:  docs:
- server full docs
file:///usr/share/doc/sqlite/index.html   bzw. same online:   https://sqlite.org/docs.html
DB-internal-Schema:  https://www.sqlite.org/schematab.html
- client-shell-docs:
man sqlite3      ##-client-shell ! not server!
client/cli/sqlite-shell  :  sqlite3  ; exit:  .exit bzw. .quit

	_______:  sqlite-client-shell/cli:  sqlite3 :
$ sqlite3 --help  ; man sqlite3
sqlite> .help          ##-II: dot-cmds are db-mgm-shell-cmds, all others are normal SQL-cmds dorwarded to the DB-engine !
sqlite> .help  open    ##--helps to any other dot-cmd for additional params ,...
-! dot-cmds are mgm-admin-cmds, all others are normal SQL-stmts (must terminated with ";") and are forwarded to the db1 engine to be executed !
-! all SQL-stmts must be terminated with ";"  !!  sql-stmt-promt is "...>"
- init-/config-file for sqlite3 : see man sqlite3 ##-- ~/.sqliterc , 

	_______:  create/open/save-db1
sqlite3   <db1-filepath>          ##--opens/creates : if not-existing, it will be generated !
sqlite>  .open ex1.db    ##--if not-existing, it will be generated !
sqlite>  .save ex2.db    ##--!!-if existing, will be OVERWRITEN  WITHOUT asking !
sqlite>  .clone  NEWDB-path    ##--!!-if existing, will be OVERWRITEN  WITHOUT asking !
-check-it:  sqlite> .databases   bzw.  sqlite> .connection
sqlite> .help open/.save/...

	_______:  query-db1-instance / instance-status-infos :
.dbinfo , .databases  , .dbconfig
.show   ##-show current tags-setting
.status

	_______:  query-db1-contents/schema/tables/indexes/...:
- see docs:  6. Querying the database schema
.tables , .indexes , .schema
SELECT name FROM sqlite_schema ;

	_______:  exports/backup/...:   see docs 8.6 ,  8.6. Export to CSV, 8.6.1. Export to Excel, ... , 15. SQLite Archive Support
.excel , .backup  , .clone , .dump , 
sqlite> .mode csv  ; [for-just-one-time:  .once c:/work/dataout.csv ] ; SELECT * FROM tab1; ## vi c:/work/dataout.csv
sqlite> .mode tabs ;  SELECT * FROM tab1; ## vi c:/work/dataout.csv
db1 --> text : docs: 10. Converting An Entire Database To A Text File
	$ sqlite3 ex1 .dump | gzip -c >ex1.dump.gz  ##-restore it to ex2:   $ zcat ex1.dump.gz | sqlite3 ex2
- tar-like-archiving with .archive    docs:  15. SQLite Archive Support

	_______:  imports:   see  docs:  8.5. Importing files as CSV or other formats :
.import ,   #-eg:  .import --csv --skip 1 --schema temp C:/work/somedata.csv tab1
- .read myscript.sql    #docs: 8.2. Reading SQL from a file

	_______:  outputs-helpies/explanationas/descrips/....:
-!  Changing SQL-Output Formats : 
	.mode  <list/table/json/csv/....>   : 14 formats : ascii/csv/json/tabs/html/...:
	see .help  .mode  !!  bzw.  docs "5. Changing Output Formats"
.separator , .width , 
.headers on , 
.log , 
.trace  #Output each SQL statement as it is run
.print some-string  ##- as echo on bash
- comments "#"
- .output  file1  : docs: 8. Redirecting I/O : writing sql-output to file instead terminal ##- or with .once if only this sql-output !

	_______:  VARs definitions/usage:  docs:  16. SQL Parameters :
.parameter     ##--eg:  .parameter set @phoneNumber "'202-456-1111'"

	_______:  OS-cmds/OS-Shell/... :  docs: 21. Using sqlite3 in a shell script
.system CMD   ##- .schema ls /tmp
######################### SQL-stmts-addies/specials for SQLite : #######################
-!! FULL-docs-sqls-Ref:  file:///usr/share/doc/sqlite/lang.html  :  SQL As Understood By SQLite
- PRAGMA Statements : is an SQL extension specific to SQLite and used to modify the operation of the SQLite library or to query the SQLite library for internal (non-table) data.
- enabling/activating support for foreign_keys constraints/check :  sqlite> PRAGMA foreign_keys = ON;
- comments in sql-stmts: either one liner with "-- ..."  /OR multilines with /* ... */
- readin a sql file and gleich creating/overwriting a new DB, from bash-shell:   $ sqlite3   db1  < ./db1-create.sql 
