##________________________________________  ___________________________


#####  ==========  Ora 9.2 install on SuSe.9.3 , 0510: ========================

	_______:  pre install steps:
	groupadd -g 300 -v dba
	useradd -c "oracle DBA and SW-Owner" -g dba -G users -m -u 1300 ora92
	passwd ora92   ---> ora92
	ORACLE_ROOT_DIR=/opt/ora   # just for my convienience; NO oracle req.
	ORACLE_BASE=${ORACLE_ROOT_DIR}/oracle
	ORACLE_HOME=${ORACLE_BASE}/product/ora92
	ORACLE_DOC=${ORACLE_ROOT_DIR}/oradoc/ora92
	ORACLE_DATA=${ORACLE_ROOT_DIR}/oradata
	ORACLE_SID=db1
	LD_ASSUME_KERNEL=2.4.21; export LD_ASSUME_KERNEL
	# is included in orarun....rpm package of suse; installer needs it:
	LD_PRELOAD=/usr/lib/libInternalSymbols.so ; export LD_PRELOAD
	mkdir -p $ORACLE_HOME  $ORACLE_DOC  $ORACLE_DATA
	chown -R ora92:dba $ORACLE_ROOT_DIR
	ll -R $ORACLE_ROOT_DIR
##________________________________________  ___________________________


#####  ==========  jdbc-ora
- thin driver: jdbc:oracle:thin:@<server>[:<1521>]:<database_name>
	eg. for Squirell-Sql: 
##________________________________________  ___________________________


#####  ==========  install-LAGER/quicky notes: try-1, Ora92-Suse93:

	_______:  --- logs:
ls   -lt /opt/ora/oracle/oraInventory/logs
tail -f /opt/ora/oracle/oraInventory/logs/installActions

	_______:  --- JRE-changes in /opt/ora/Disks_Ora9204/Disk1> ll install/linux/oraparam.ini :
JRE_LOCATION=../../stage/Components/oracle.swd.jre/1.3.1.0.0/1/DataFiles/Expanded/jre/linux
#JRE_LOCATION=/usr/lib/jvm/java-1.4.2-sun-1.4.2.06/
#JRE_LOCATION=/usr/lib/jvm/java-1.4.2-sun-1.4.2.06/jre

	_______:  -- apache, isqlplus install:
Launched configuration tool Starting HTTP Server
Command which is being spawned is /opt/ora/oracle/product/ora92/Apache/Apache/bin/apachectl  start
Configuration tool Starting HTTP Server succeeded
The following information is available in:
/opt/ora/oracle/product/ora92/Apache/Apache/setupinfo.txt
The HTTP Server can be accessed using the following URLs:
Non SSL Mode (executed at install time):
user-login:	http://in82:7776/isqlplus ,  http://127.0.0.1:7776/isqlplus   ( Apache: http://in82:7776 )
DBA-Login:	http://in82:7776/isqlplusdba  : BUT an additional apache-user must be configured by apache-server.
	has nothing to do with Oracle-User! see docs: http://127.0.0.1:7776/iplus/help/us/ui.htm#1031151
SSL mode (not started as default):
http://in82:7777
https://in82:null

	_______:  -- Manual CHanges in system from orarun-suse:
1001     cdl /opt/ora/lager_ora/orarun_sles/orarun-1.8-109.15.i586.unp/usr/lib
1003    cp  libInternalSymbols.a   libInternalSymbols.so.1  /usr/lib/
1012    cd /usr/lib/
1013	ln  -s libInternalSymbols.so.1  libInternalSymbols.so

	_______:  -- 
##________________________________________  ___________________________


#####  ==========  Lager-SQL:
- new user 
	create user adm2 identified by ora92 default tablespace users;
	grant sysdba, dba, connect, resource to adm2;
