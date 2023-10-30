___________ setups/installs/... _________________________________
##________________________________________  ___________________________


#####  ==========  docs, see installs in:
	-! ref-manual: Ch.2.2. Installing MySQL from Generic Binaries on Unix/Linux
##________________________________________  ___________________________


#####  ==========  Post.Installation.tasks:
	-!see 2.10. Postinstallation Setup and Testing :
	-  on Unix, you should initialize the data directory and create the MySQL grant tables and
	   all initial accounts in the grant tables have NO passwords. You should assign passwords to prevent unauthorized access.
	-  mysql_install_db for grants/users:  the grant tables are set up by the mysql_install_db program. see man mysql_install_db
	   this wil be run by RPM-installation, but not in generic case!
##________________________________________  ___________________________


#####  ==========  full-manul-installation (generic instattlion): so unpack-tar-and-install:
	-! see ref--ch.2.2. Installing MySQL from Generic Binaries on Unix/Linux ; here short:
	To install and use a MySQL binary distribution, the basic command sequence looks like this [ref.5.5.- p.42]:
	groupadd mysql
	useradd -r -g mysql mysql
	cd /usr/local
	tar zxvf /path/to/mysql-VERSION-OS.tar.gz
	ln -s full-path-to-mysql-VERSION-OS mysql
	cd mysql
	chown -R mysql .
	chgrp -R mysql .
	scripts/mysql_install_db --user=mysql
	chown -R root .
	chown -R mysql data
	command is optional
	cp support-files/my-medium.cnf /etc/my.cnf
	bin/mysqld_safe --user=mysql &
	command is optional
	cp support-files/mysql.server /etc/init.d/mysql.server
##________________________________________  ___________________________


#####  ==========  DIRs-installation on Linux from RPMs:
	-!! best grep of installed system:  u1@vo17:/up1/.cuue/etc/vims $mysqladmin variables | fgrep /
		basedir                                           | /usr                                                                                                                   |
		character_sets_dir                                | /usr/share/mysql/charsets/                                                                                             |
		datadir                                           | /var/lib/mysql/                                                                                                        |
		general_log_file                                  | /var/lib/mysql/vo17.log                                                                                                |
		innodb_log_group_home_dir                         | ./                                                                                                                     |
		lc_messages_dir                                   | /usr/share/mysql/                                                                                                      |
		log_error                                         | /var/log/mysql/mysqld.log                                                                                              |
		pid_file                                          | /var/lib/mysql/vo17.pid                                                                                                |
		plugin_dir                                        | /usr/lib/mysql/plugin/                                                                                                 |
		slave_load_tmpdir                                 | /tmp                                                                                                                   |
		slow_query_log_file                               | /var/lib/mysql/vo17-slow.log                                                                                           |
		socket                                            | /var/run/mysql/mysql.sock                                                                                              |
		tmpdir                                            | /tmp                           
	-! see Table 2.11. MySQL Installation Layout for Linux RPM
	Table 2.11. MySQL Installation Layout for Linux RPM
	Directory				Contents of Directory
	/usr/bin				Client programs and scripts
	/usr/sbin				The mysqld server
	/var/lib/mysql			Log files, databases
	/usr/share/info			Manual in Info format
	/usr/share/man			Unix manual pages
	/usr/include/mysql		Include (header) files
	/usr/lib/mysql			Libraries
	/usr/share/mysql		Miscellaneous support files, including error messages, character set files, sample configuration files, SQL for database installation
	/usr/share/sql-bench	Benchmarks
##________________________________________  ___________________________


#####  ==========  Linux-installion:
	- see ref--ch.2.5
	-! after installation, the mysqld is NOT started! must be started manually!
	- system-user+groups: During RPM installation, a user named mysql and a group named mysql are created on the system. 
##________________________________________  ___________________________


#####  ==========  Redhat/Fedora-installs:
	-!! see ref--2.5.2. Installing MySQL on Linux using Native Package Manager
--############## prev: #######################################
##________________________________________  ___________________________


#####  ==========  setup-nts/installs (see manual!! here just dummy/tr...)
	-!! in suse musste ich: mkdir /var/log/mysql/ ; chown mysql:mysql /var/log/mysql/
	- user+group:   mysql group and the mysql user.
	- datadir creation with : mysql_install_db script creates the server's data directory with mysql as
		mysql_install_db  script used to initialize the mysql database containing the grant tables that store the server access permissions.
		suse: /usr/bin/mysql_install_db  , man mysql_install_db
		- /OR more options eg :  scripts/mysql_install_db --user=mysql --basedir=/opt/mysql/mysql --datadir=/opt/mysql/mysql/data
