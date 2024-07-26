=== runinstaller-start:
- start params for runinstaller: Oracle9CD/disk1/install/oraparam.ini
- edit eachtime install/oraparam.ini (no bootstrap, JVM, no distribution,....)
- add fonts to exceed + modify: jvm/lib/font.properties
########## Manually Uninstall 9.2 in Unix: ####
-! first down all oraprocesses:
	psg ora
	agentctl stop ...
	lsnrctl stop
	DBs stop...
	....
- (best as root):
	rm -rf $ORACLE_HOME
	rm -rf /etc/ora*   /OR rm -f /var/app/oracle/oratab
	rm -rf /path/to/your/oraInventory
	- and there are some binaries in /usr/local/bin/ (by default)
	rm -f /usr/local/bin/coraenv
	rm -f /usr/local/bin/oraenv
	rm -f /usr/local/bin/dbhome
-- /OR other way said in FIT:
cd /app/oracle92   #/OR:  cd $ORACLE_BASE
	&& rm -rf all-except-FIT-scripts
	rm /var/app/oracle/oratab
	rm /usr/local/bin/*ora*
	rm /usr/local/bin/dbhome
########## silent/noninteractive: ##############

	_______:  notes/docs:
	- see details in:
		- "non interacitve" in ORA-Refs + ux_install
		- chm: DBA AUtomation QRef
	- use ONLY ABSOLUTE PATHes for response- or record-files
	- logs in : oraInventory/logs : /app/oracle92/oraInventory/logs
	- if the very FIRST-Install (no orabase-DIR,OUI,Inventory yet there): /tmp/ora....log   OR in silent:  /tmp/silentInstall.log

	_______:  params/invokes:
	-record  -destinationFile myFile1_EE.resp
##________________________________________  ___________________________


#####  ==========  
