___________ mysql coll _________________
##________________________________________  ___________________________


#####  ==========  quickies-mysql.shell...:

	_______:  logins:
mysql -u dbu1 -h localhost --prompt='\U : '  world
mysql  -u dbu1 -h 127.0.0.1 db1   ##--> client sqlplus-login

	_______:  
mysql> select database(), user(); 
mysql> show tables;   ==  $mysqlshow -u dbu1 db1
mysql> show databases;
mysql> select host, user, max_connections from user;
-- create user:
create user 'dbu5'@127.0.0.1;    ##identifies by '...'
grant all privileges on db1.* to dbu5;

	_______:  creating example-emplyee-DB:
u1@vo17:/up1/varu/varau/packsvar/mysqls/employees_db_full $mysql  -u root -h 127.0.0.1 mysql  < employees.sql

	_______:  creating example-world-DB:
u1@vo17: $ mysql -u root mysql
mysql> drop database world;
Query OK, 0 rows affected (0.00 sec)
mysql> create database world;
Query OK, 1 row affected (0.00 sec)
mysql> grant all privileges on world.* to dbu1;
Query OK, 0 rows affected (0.00 sec)
-
u1@vo17:/up1/varu/varau/prjs/myq1/wks/world_db_wks $mysql -u dbu1 -h 127.0.0.1  world
mysql> USE world;
mysql>  select database(), user();
mysql> SOURCE world.sql;   ##OR engine.file
- check:
mysql> SHOW TABLES;
To see the structure of each table, use SHOW CREATE TABLE. For example: 
mysql> SHOW CREATE TABLE Country;
mysql> SHOW CREATE TABLE City;
mysql> SHOW CREATE TABLE CountryLanguage;

	_______:  
--############### setup-vo17-suse.11.4--110818 ########
##________________________________________  ___________________________


#####  ==========  rpms suse.11.4:
	u1@vo17:~ $rpmssg mysql
	libdbi-drivers-dbd-mysql-0.8.3-4.7.2.i586
	libgda-3_0-mysql-3.1.5-10.4.i586
	libgda-4_0-mysql-4.2.2-4.3.i586
	libmysqlclient16-5.1.53-4.7.1.i586
	libmysqlclient-devel-5.1.53-4.7.1.i586
	libmysqlclient_r16-5.1.53-4.7.1.i586
	libmysqlclusterclient16-7.1.14-0.3.1.i586
	libmysqlclusterclient_r16-7.1.14-0.3.1.i586
	libmysqlcppconn1-1.0.5-9.2.i586
	libmysqlcppconn-devel-1.0.5-9.2.i586
	libmysqld0-5.1.53-4.7.1.i586
	libmysqld-devel-5.1.53-4.7.1.i586
	libqt4-sql-mysql-4.7.1-7.2.i586
	libreoffice-base-drivers-mysql-3.3.1.2-1.2.2.i586
	mysql-community-server-5.1.53-4.7.1.i586
	mysql-community-server-bench-5.1.53-4.7.1.i586
	mysql-community-server-client-5.1.53-4.7.1.i586
	mysql-community-server-debug-5.1.53-4.7.1.i586
	mysql-community-server-test-5.1.53-4.7.1.i586
	mysql-community-server-tools-5.1.53-4.7.1.i586
	mysql-connector-java-5.1.6-8.3.noarch
	mysql-connector-java-javadoc-5.1.6-8.3.noarch
	mysql-connector-java-manual-5.1.6-8.3.noarch
	mysql-workbench-5.2.31-3.3.i586
	perl-DBD-mysql-4.018-4.2.i586
	qt3-mysql-3.3.8b-111.2.i586
	u1@vo17:~ $date
	Sun Aug 21 15:39:22 CEST 2011
	u1@vo17:~ $uname -a
	Linux vo17 2.6.37.6-0.7-default #1 SMP 2011-07-21 02:17:24 +0200 i686 i686 i386 GNU/Linux
	u1@vo17:~ $
##________________________________________  ___________________________


#####  ==========  post-steps- coll:
kk: on suse log-dir was missing:  mkdir /var/log/mysql/ ; chown mysql:mysql /var/log/mysql/

	_______:  
vo17:~ # mysql_install_db --user=mysql  ##-!!- unbedingt mit --user=mysql !! otherwise datafiles,... are owned by system-root, which is wrong!! /OR run it as system-mysql user!!
Installing MySQL system tables...
110818 18:49:40 [Warning] '--skip-locking' is deprecated and will be removed in a future release. Please use '--skip-external-locking' instead.
OK
Filling help tables...
110818 18:49:41 [Warning] '--skip-locking' is deprecated and will be removed in a future release. Please use '--skip-external-locking' instead.
OK
PLEASE REMEMBER TO SET A PASSWORD FOR THE MySQL root USER !
To do so, start the server, then issue the following commands:
/usr/bin/mysqladmin -u root password 'new-password'
/usr/bin/mysqladmin -u root -h vo17.l1nw password 'new-password'
Alternatively you can run:
/usr/bin/mysql_secure_installation
which will also give you the option of removing the test
databases and anonymous user created by default.  This is
strongly recommended for production servers.
See the manual for more instructions.
You can start the MySQL daemon with:
rcmysql start
You can test the MySQL daemon with mysql-test package
Please report any problems with the /usr/bin/mysqlbug script!

	_______:  
mysql@vo17:~ $mysqld_safe &
[1] 17117
mysql@vo17:~ $110818 20:30:19 mysqld_safe Logging to '/var/log/mysql/mysqld.log'.
....

	_______:  
checking connection ..:
mysqladmin version
mysqladmin variables
ll /var/log/mysql/
view /var/log/mysql/mysqld.log 
view /var/lib/mysql/vo17.log
-
mysqlshow
- worke only as db-user root!? :
mysqlshow --user=root  mysql
mysql -e "SELECT Host,Db,User FROM db"  --user=root mysql #worke only as db-user root!?

	_______:  
##________________________________________  ___________________________


#####  ==========  deleting data and runnins script again but as mysql-system-user:

	_______:  
mysql@vo17:~ $mysqladmin -u root shutdown
110818 21:06:26 mysqld_safe mysqld from pid file /var/lib/mysql/vo17.l1nw.pid ended
[1]+  Done                    mysqld_safe
mysql@vo17:~ $mysql_install_db
Installing MySQL system tables...
110818 21:07:00 [Warning] '--skip-locking' is deprecated and will be removed in a future release. Please use '--skip-external-locking' instead.
OK
Filling help tables...
110818 21:07:02 [Warning] '--skip-locking' is deprecated and will be removed in a future release. Please use '--skip-external-locking' instead.
OK
PLEASE REMEMBER TO SET A PASSWORD FOR THE MySQL root USER !
To do so, start the server, then issue the following commands:
/usr/bin/mysqladmin -u root password 'new-password'
/usr/bin/mysqladmin -u root -h vo17.l1nw password 'new-password'
Alternatively you can run:
/usr/bin/mysql_secure_installation
which will also give you the option of removing the test
databases and anonymous user created by default.  This is
strongly recommended for production servers.
See the manual for more instructions.
You can start the MySQL daemon with:
rcmysql start
You can test the MySQL daemon with mysql-test package
Please report any problems with the /usr/bin/mysqlbug script!

	_______:  
##________________________________________  ___________________________


#####  ==========  tests ...:
- many scripts in mysql-test/ and sql-bench/ of tgz-file (or test suite)
--####################### SQLs/mysql-shell: ##############################
##________________________________________  ___________________________


#####  ==========  DB1-setup : dbu1/db1  + ....: (see Ch.3 Tutorial):
as db.root: 
mysql -u root -h localhost
mysql> grant all on db1.* to 'dbu1'@'localhost'; quit;
- db-connecting as dbu1 to db1 at localhost:
$ mysql -u dbu1 -h localhost db1         ##- if needed also -p for PW
mysql> create database db1;  ##-II- Under Unix, database names are case sensitive
mysql> use db1;         ##-I Creating a database does not select it for use; you must do that explicitly. 
mysql>  select database(), user();
	db1        | dbu1@localhost 
mysql> show tables;
mysql> CREATE TABLE pet (name VARCHAR(20), owner VARCHAR(20), species VARCHAR(20), sex CHAR(1), birth DATE, death DATE);
mysql> DESCRIBE pet;
quit  ##- due to problem with load-file, so: login again, with enabled-infile:
$ mysql --local-infile=1  -u dbu1 -h localhost db1
mysql> load data local infile '/up1/varu/varau/wks/mysqlwks/pet.txt' into table pet;
mysql> select * from pet;
##________________________________________  ___________________________


#####  ==========  DB-infos-queries (Ch.-3.4. ...):
mysql> SELECT DATABASE();
mysql> SHOW TABLES;
mysql> DESCRIBE pet;
 mysql>  select database(), user();
...
##________________________________________  ___________________________


#####  ==========  user:
- whoami: select user();
- current DB?:  SELECT DATABASE().
--################ suse11.4-vo17--coll 08.2011: ######################################
##________________________________________  ___________________________


#####  ==========  done-added in suse11.4-vo17--coll:  110800:
	- on suse log-dir was missing:  mkdir /var/log/mysql/ ; chown mysql:mysql /var/log/mysql/
	- not good?? or ok? (insted useradd mysql2 or so ...; mysql is a SYSTEM-user !!! leave it!):
		vo17:~ # usermod -s /bin/bash mysql # --> home-dir ??
		vo17:~ # passwd mysql
##________________________________________  ___________________________


#####  ==========  cmds-mysql-on-suse.114:
u1@vo17:~ $mysqld
mysqld         mysqld-debug   mysqld_multi   mysqld_safe    mysqldump      mysqldumpslow  
u1@vo17:~ $mysql
mysql                       mysql_convert_table_format  mysqlhotcopy                mysqltest
mysqlaccess                 mysqld                      mysqlimport                 mysqltest_embedded
mysqladmin                  mysqld-debug                mysql_install_db            mysql_tzinfo_to_sql
mysqlanalyze                mysqld_multi                mysqlmanager                mysql_upgrade
mysqlbinlog                 mysqld_safe                 mysqloptimize               mysql_waitpid
mysqlbug                    mysqldump                   mysqlrepair                 mysql-workbench
mysqlcheck                  mysqldumpslow               mysql_secure_installation   mysql-workbench-bin
mysql_client_test           mysql_find_rows             mysql_setpermission         mysql_zap
mysql_client_test_embedded  mysql_fix_extensions        mysqlshow                   
mysql_config                mysql_fix_privilege_tables  mysqlslap                   
u1@vo17:~ $uname -a
Linux vo17 2.6.37.6-0.7-default #1 SMP 2011-07-21 02:17:24 +0200 i686 i686 i386 GNU/Linux

	_______:  rpms:
u1@vo17:~ $rpmssg mysql
libdbi-drivers-dbd-mysql-0.8.3-4.7.2.i586
libgda-3_0-mysql-3.1.5-10.4.i586
libgda-4_0-mysql-4.2.2-4.3.i586
libmysqlclient16-5.1.53-4.7.1.i586
libmysqlclient-devel-5.1.53-4.7.1.i586
libmysqlclient_r16-5.1.53-4.7.1.i586
libmysqlclusterclient16-7.1.14-0.3.1.i586
libmysqlclusterclient_r16-7.1.14-0.3.1.i586
libmysqlcppconn1-1.0.5-9.2.i586
libmysqlcppconn-devel-1.0.5-9.2.i586
libmysqld0-5.1.53-4.7.1.i586
libmysqld-devel-5.1.53-4.7.1.i586
libqt4-sql-mysql-4.7.1-7.2.i586
libreoffice-base-drivers-mysql-3.3.1.2-1.2.2.i586
mysql-community-server-5.1.53-4.7.1.i586
mysql-community-server-bench-5.1.53-4.7.1.i586
mysql-community-server-client-5.1.53-4.7.1.i586
mysql-community-server-debug-5.1.53-4.7.1.i586
mysql-community-server-test-5.1.53-4.7.1.i586
mysql-community-server-tools-5.1.53-4.7.1.i586
mysql-connector-java-5.1.6-8.3.noarch
mysql-connector-java-javadoc-5.1.6-8.3.noarch
mysql-connector-java-manual-5.1.6-8.3.noarch
mysql-workbench-5.2.31-3.3.i586
perl-DBD-mysql-4.018-4.2.i586
qt3-mysql-3.3.8b-111.2.i586
u1@vo17:~ $date
Sun Aug 21 15:39:22 CEST 2011
u1@vo17:~ $uname -a
Linux vo17 2.6.37.6-0.7-default #1 SMP 2011-07-21 02:17:24 +0200 i686 i686 i386 GNU/Linux
u1@vo17:~ $

	_______:  
##________________________________________  ___________________________


#####  ==========  
