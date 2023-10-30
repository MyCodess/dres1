__________________oems.92_____________________________
-! see Alapati.9i-CH.17

	_______:  configs-oem-comm:
	- DIR-structure-oem: see oem-config-guide.App-A
	- $ORACLE_HOME/sysman/...
	- $ORACLE_HOME/sysman/config/...

	_______:  oemapp:
	- starting oem-config based on ManagementServer/oms with em-configuration-Assist.: emca
	- help/list: just oemapp
		Usage: oemapp <application name>
		The installed applications are: txtmgr, worksheet, ocmcli, dbastudio, console, esmsrv, opm, cpta, jdbctest, oemutil, topsess, dataguard, ocm, lmviewer, cp, sdoadvisor, esm, pm	
	- oemapp console oem.loginmode=standalone

	_______:  oemctl start/status/ping/stop/.... oms

	_______:  oemutil: oem-admin-guide.App-C:
	oemapp oemutil <username>/<password>@<oms> <command> <parameters>
	oemapp oemutil -cmdfile <command file name>

	_______:  agent:
	- agentctl stop/stop/status/ping/...
		- DBSNMP-/Entp-/oem-Agent: ${ORACLE_HOME}/bin/agentctl start/stop/status
	- configs-agent:
		- $ORACLE_HOME/network/admin/snmp_ro.ora , snmp_rw.ora, services.ora.
		- $ORACLE_HOME/network/agent/services.ora :When the Intelligent Agent starts, database entries are written to
	- ps:  psg dbs /OR psg snmp
		UID   PID  PPID  CLS PRI    STIME TTY      TIME CMD
		ora92 29957     1   TS   0 18:41:23 pts/2    0:00 /bin/sh /app/oracle92/app/oracle/product/92/bin/dbsnmpwd
		ora92 29961 29957   TS  58 18:41:23 pts/2    0:01 /app/oracle92/app/oracle/product/92/bin/dbsnmp
	- ora817-agent:  lsnrctl dbsnmp_start / dbsnmp_stop / dbsnmp_status

	_______:  oms /Management Server:
	- checking staus WITHOUT gui:  oemctl status oms sysman/oempw1@gatexb1  (!! oms-admin-user+pw NOT DB)
	- starting Management-Server:  oemctl start oms
	- default oem-superadmin-user/pw: SYSMAN + oem_temp ;
	- logs :$ORACLE_HOME/sysman/log/oms.log
	- config: $ORACLE_HOME/sysman/config/omsconfig.properties
	- oemctl start/stop/status/ping oms

	_______:  web-server for oms:
	- configuring with:  oemctl configure rws

	_______:  cmd-tools-misc-oem:
	- esm -cmd help [operation]: Enterprise Security Manager
	-
