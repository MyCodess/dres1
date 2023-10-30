##________________________________________  ___________________________


#####  ==========  Bea-Documents/Files:
	- deciding which oracle driver for you: jdbc-doc file:///W/Docs_J/Bea/wls81/Htmls/jdbc/intro.html
	-! jdbc_drivers.pdf: WebLogic Type 4 JDBC Drivers: the BEA WebLogic Type 4 JDBC drivers with WebLogic Server; file:///W:/Docs_J/Bea/WLS81/Htmls/jdbc_drivers/oracle.html
	- oracle.pdf: WebLogic jDriver for Oracle /type2: install and develop applications using WebLogic jDriver for Oracle, BEA’s type-2 Java Database Connectivity (JDBC) driver for the Oracle Database management system, for local and distributed transactions.
	- jdbc.pdf: Programming WebLogic JDBC / API/ 3.party Drivers: JDBC with WebLogic Server (jdbc-API Programming)
	- Config file/Info for all BEA-Jdbc-Drives (listed in console): C:\bea\weblogic81\server\lib\jdbcdrivers.xml
	- Client-libs: WL_HOME\server\lib\wlbase.jar and wlutil.jar: (jdbc_drivers.pdf)To use the driver with a WebLogic client, you must copy the following files to the client and add	them to the classpath on the client:
##________________________________________  ___________________________


#####  ==========  BEA-Ora-typ4  (WL_HOME\server\lib\wloracle.jar)
	- Driver-XA:		weblogic.jdbcx.oracle.OracleDataSource
	- Driver-Non-XA:	weblogic.jdbc.oracle.OracleDriver
	- URL: jdbc:bea:oracle://dbserver:port   ; URL="jdbc:bea:oracle://localhost:1521"
	- OK: <JDBCConnectionPool DriverName="weblogic.jdbcx.oracle.OracleDataSource" Name="beaOra4x" Password="{3DES}kgLQd/HYKAM=" Properties="user=u1;portNumber=1521;SID=db1;serverName=localhost" Targets="exps" TestConnectionsOnReserve="true" TestTableName="SQL SELECT 1 FROM DUAL" URL="jdbc:bea:oracle://localhost:1521"/>
	- OK: <JDBCConnectionPool DriverName="weblogic.jdbc.oracle.OracleDriver" Name="beaOra4_NoX" Password="{3DES}kgLQd/HYKAM=" Properties="user=u1;portNumber=1521;SID=db1;serverName=localhost" Targets="exps" TestConnectionsOnReserve="true" TestTableName="SQL SELECT 1 FROM DUAL" URL="jdbc:bea:oracle://localhost:1521"/>
	- error outputs like: [BEA][WebLogic Type 4 JDBC driver name]......
	- supports Oracle 8i R3 (8.1.7) and Oracle 9i running on Windows and UNIX.
	- Properties,...: file:///W:/Docs_J/Bea/WLS81/Htmls/jdbc_drivers/oracle.html
##________________________________________  ___________________________


#####  ==========  Oracle-typ4 (in  ojdbc14.jar from Oracle, but also in BEA-Install)
	- DriverName-XA:		oracle.jdbc.xa.client.OracleXADataSource
	- DriverName-Non-XA:	oracle.jdbc.driver.OracleDriver
	- URL="jdbc:oracle:thin:@localhost:1521:db1"  
	- OK: <JDBCConnectionPool DriverName="oracle.jdbc.xa.client.OracleXADataSource" Name="ora4x" Password="{3DES}GBdEdKrnhDg=" Properties="user=scott" Targets="ws1" TestConnectionsOnReserve="true" TestTableName="SQL SELECT 1 FROM DUAL" URL="jdbc:oracle:thin:@localhost:1521:db1"/>
##________________________________________  ___________________________


#####  ==========  BEA-JDrive/Ora-typ2:
	-- Non-XA mode:
	* Driver class: weblogic.jdbc.oci.Driver
    * URL: jdbc:weblogic:oracle
    -- XA mode:
    * Driver class: weblogic.jdbc.oci.xa.XADataSource
    * URL: none required
##________________________________________  ___________________________


#####  ==========  Oracle-Type2:
	- %ORACLE_HOME%\jdbc\lib\classes12.zip
############## from jdbcdrivers.xml (C:\bea\weblogic81\server\lib\jdbcdrivers.xml): ######
<Driver 
    Database="Oracle" 
    Vendor="WebLogic" 
    Type="Type 2" 
    DatabaseVersion="8.1.7,9.0.1,9.2.0" 
    ForXA="true"
    Cert="true"
    ClassName="weblogic.jdbc.oci.xa.XADataSource"
    URLHelperClassname="weblogic.jdbc.utils.WebLogicOracleJDBCDriverURLHelper"
    TestSql="SELECT 1 FROM DUAL">
	<!-- to make this SHOW up in the UI, note it will be stuffed in the Properties object -->
        <Attribute Name="DbmsName" Required="true" InURL="false"/>
	<!-- to make this NOT show up in the UI -->
        <Attribute Name="DbmsHost" Required="false"/>
	<!-- to make this NOT show up in the UI -->
        <Attribute Name="DbmsPort" Required="false"/>
        <Attribute Name="DbmsUsername" Required="true" InURL="false"/>
        <Attribute Name="DbmsPassword" Required="true" InURL="false"/>
    </Driver>
  <Driver 
    Database="Oracle" 
    Vendor="WebLogic" 
    Type="Type 2" 
    DatabaseVersion="8.1.7,9.0.1,9.2.0" 
    ForXA="false"
    Cert="true"
    ClassName="weblogic.jdbc.oci.Driver"
    URLHelperClassname="weblogic.jdbc.utils.WebLogicOracleJDBCDriverURLHelper"
    TestSql="SELECT 1 FROM DUAL">
        <Attribute Name="DbmsName" Required="true" InURL="false"/>
	<!-- to make this NOT show up in the UI -->
        <Attribute Name="DbmsHost" Required="false"/>
	<!-- to make this NOT show up in the UI -->
        <Attribute Name="DbmsPort" Required="false"/>
        <Attribute Name="DbmsUsername" Required="true" InURL="false"/>
        <Attribute Name="DbmsPassword" Required="true" InURL="false"/>
  </Driver>
  <Driver 
    Database="Oracle" 
    Vendor="BEA" 
    Type="Type 4"
    Cert="true"
    DatabaseVersion="8.1.7,9.0.1,9.2.0"
    ForXA="false"
    ClassName="weblogic.jdbc.oracle.OracleDriver"
    URLHelperClassname="weblogic.jdbc.utils.WLOracleJDBC4DriverURLHelper"
    TestSql="SELECT 1 FROM DUAL">
        <Attribute Name="DbmsName" Required="true" InURL="false"/>
        <Attribute Name="DbmsHost" Required="true" InURL="true"/>
        <Attribute Name="DbmsPort" Required="true" InURL="true" DefaultValue="1521"/>
        <Attribute Name="DbmsUsername" Required="true" InURL="false"/>
        <Attribute Name="DbmsPassword" Required="true" InURL="false"/>
  </Driver>
  <Driver 
    Database="Oracle" 
    Vendor="BEA" 
    Type="Type 4"
    Cert="true"
    DatabaseVersion="8.1.7,9.0.1,9.2.0"
    ForXA="true"
    ClassName="weblogic.jdbcx.oracle.OracleDataSource"
    URLHelperClassname="weblogic.jdbc.utils.WLOracleJDBC4DriverURLHelper"
    TestSql="SELECT 1 FROM DUAL">
        <Attribute Name="DbmsName" Required="true" InURL="false"/>
        <Attribute Name="DbmsHost" Required="true" InURL="true"/>
        <Attribute Name="DbmsPort" Required="true" InURL="true" DefaultValue="1521"/>
        <Attribute Name="DbmsUsername" Required="true" InURL="false"/>
        <Attribute Name="DbmsPassword" Required="true" InURL="false"/>
  </Driver>
  <Driver 
    Database="Oracle" 
    Vendor="DataDirect" 
    Type="Type 4"
    DatabaseVersion="8.1.7,9.0.1,9.2.0"
    ForXA="false"
    ClassName="com.ddtek.jdbc.oracle.OracleDriver"
    URLHelperClassname="weblogic.jdbc.utils.DDOracleJDBC4DriverURLHelper"
    TestSql="SELECT 1 FROM DUAL">
        <Attribute Name="DbmsName" Required="true" InURL="false"/>
        <Attribute Name="DbmsHost" Required="true" InURL="true"/>
        <Attribute Name="DbmsPort" Required="true" InURL="true" DefaultValue="1521"/>
        <Attribute Name="DbmsUsername" Required="true" InURL="false"/>
        <Attribute Name="DbmsPassword" Required="true" InURL="false"/>
  </Driver>
  <Driver 
    Database="Oracle" 
    Vendor="DataDirect" 
    Type="Type 4"
    DatabaseVersion="8.1.7,9.0.1,9.2.0"
    ForXA="true"
    ClassName="com.ddtek.jdbcx.oracle.OracleDataSource"
    URLHelperClassname="weblogic.jdbc.utils.DDOracleJDBC4DriverURLHelper"
    TestSql="SELECT 1 FROM DUAL">
        <Attribute Name="DbmsName" Required="true" InURL="false"/>
        <Attribute Name="DbmsHost" Required="true" InURL="true"/>
        <Attribute Name="DbmsPort" Required="true" InURL="true" DefaultValue="1521"/>
        <Attribute Name="DbmsUsername" Required="true" InURL="false"/>
        <Attribute Name="DbmsPassword" Required="true" InURL="false"/>
  </Driver>
  <Driver 
    Database="Oracle" 
    Vendor="Oracle" 
    Type="Thin" 
    DatabaseVersion="8.1.7,9.0.1,9.2.0" 
    ForXA="false"
    Cert="true"
    ClassName="oracle.jdbc.driver.OracleDriver"
    URLHelperClassname="weblogic.jdbc.utils.OracleJDBC4DriverURLHelper"
    DbmsPortRequired="true"  
    DefaultDbmsPort="1521"
    DbmsHostRequired="true" 
    UserNameRequiredInURL="false"
    PasswordRequiredInURL="false"
    TestSql="SELECT 1 FROM DUAL">
        <Attribute Name="DbmsName" Required="true" InURL="true"/>
        <Attribute Name="DbmsHost" Required="true" InURL="true"/>
        <Attribute Name="DbmsPort" Required="true" InURL="true" DefaultValue="1521"/>
        <Attribute Name="DbmsUsername" Required="true" InURL="false"/>
        <Attribute Name="DbmsPassword" Required="true" InURL="false"/>
  </Driver>
  <Driver 
    Database="Oracle" 
    Vendor="Oracle" 
    Type="Thin" 
    DatabaseVersion="8.1.7,9.0.1,9.2.0" 
    ForXA="true"
    Cert="true"
    ClassName="oracle.jdbc.xa.client.OracleXADataSource"
    URLHelperClassname="weblogic.jdbc.utils.OracleJDBC4DriverURLHelper"
    TestSql="SELECT 1 FROM DUAL">
        <Attribute Name="DbmsName" Required="true" InURL="true"/>
        <Attribute Name="DbmsHost" Required="true" InURL="true"/>
        <Attribute Name="DbmsPort" Required="true" InURL="true" DefaultValue="1521"/>
        <Attribute Name="DbmsUsername" Required="true" InURL="false"/>
        <Attribute Name="DbmsPassword" Required="true" InURL="false"/>
  </Driver>
  <Driver 
    Database="Oracle" 
    Vendor="Oracle" 
    Type="OCI" 
    DatabaseVersion="8.1.7,9.0.1,9.2.0" 
    ForXA="false"
    ClassName="oracle.jdbc.driver.OracleDriver"
    URLHelperClassname="weblogic.jdbc.utils.OracleJDBCDriverURLHelper"
    TestSql="SELECT 1 FROM DUAL">
        <Attribute Name="DbmsName" Required="true" InURL="true"/>
        <Attribute Name="DbmsHost" Required="false" InURL="false"/>
        <Attribute Name="DbmsPort" Required="false" InURL="false"/>
        <Attribute Name="DbmsUsername" Required="true" InURL="false"/>
        <Attribute Name="DbmsPassword" Required="true" InURL="false"/>
  </Driver>
  <Driver 
    Database="Oracle" 
    Vendor="Oracle" 
    Type="OCI" 
    DatabaseVersion="8.1.7,9.0.1,9.2.0" 
    ForXA="true"
    ClassName="oracle.jdbc.xa.client.OracleXADataSource"
    URLHelperClassname="weblogic.jdbc.utils.OracleJDBCDriverURLHelper"
    TestSql="SELECT 1 FROM DUAL">
        <Attribute Name="DbmsName" Required="true" InURL="true"/>
        <Attribute Name="DbmsHost" Required="false" InURL="false"/>
        <Attribute Name="DbmsPort" Required="false" InURL="false"/>
        <Attribute Name="DbmsUsername" Required="true" InURL="false"/>
        <Attribute Name="DbmsPassword" Required="true" InURL="false"/>
  </Driver>
##############  OLD : #################
##________________________________________  ___________________________


#####  ==========  OK: Worked even with creation of table on in82 + Ora92 BUT not with transactions (also just mit direct client, but not with MDBs):
<JDBCConnectionPool DriverName="oracle.jdbc.driver.OracleDriver" InitialCapacity="0" MaxCapacity="1" Name="cdmv_tm_pool" Password="{3DES}8+dQ+04UMjs=" Properties="user=u1" Targets="s1" TestConnectionsOnCreate="true" TestConnectionsOnRelease="true" TestConnectionsOnReserve="true" TestTableName="dual" URL="jdbc:oracle:thin:@localhost:1521:sid6"/>
##________________________________________  ___________________________


#####  ==========  Oracle-JDBC-Driver (thin driver, ..):
- Hos_config: <JDBCConnectionPool DriverName="oracle.jdbc.driver.OracleDriver" Name="CDMV_POOL" Password="{3DES}zkizKDKXWuY=" Properties="user=CDMVSPL1_DATA_AG3D" Targets="myserver" TestTableName="SQL SELECT 1 FROM DUAL" URL="jdbc:oracle:thin:@localhost:1521:UPS"/>
- OK url: jdbc:oracle:thin:@evo4:1521:cdmvdev ; Driver: oracle.jdbc.driver.OracleDriver
- OK-in82-Ora-Pool: <JDBCConnectionPool DriverName="oracle.jdbc.driver.OracleDriver" InitialCapacity="0" MaxCapacity="1" Name="cmdv_pool" Password="{3DES}Qdo388UdKBk=" Properties="user=u1" Targets="s1" TestConnectionsOnCreate="true" TestConnectionsOnRelease="true" TestConnectionsOnReserve="true" TestTableName="dual" URL="jdbc:oracle:thin:@evo4:1521:cdmvdev"/>
##________________________________________  ___________________________


#####  ==========  WL-Ora-Drivers: BEA WebLogic Type 4 JDBC Oracle driver are:
The driver classes for the BEA WebLogic Type 4 JDBC Oracle driver are:
	XA: weblogic.jdbcx.oracle.OracleDataSource
	Non-XA: weblogic.jdbc.oracle.OracleDriver
Use these driver classes when configuring a JDBC connection pool in your WebLogic Serverdomain.

	_______:  URL: To connect to an Oracle database, use the following URL format:  jdbc:bea:oracle://dbserver:port 
e.g.:  	jdbc:bea:oracle://evo4:1521  
	user=u1
	portNumber=1521
	SID=cdmvdev
	serverName=evo4
##________________________________________  ___________________________


#####  ==========  WL: ORACLE_THIN

	_______:  Test in82:   java utils.dbping ORACLE_THIN  u1   AG   localhost:1521:sid6
	**** Success!!! ****
	You can connect to the database in your app using:
  java.util.Properties props = new java.util.Properties();
  props.put("user", "u1");
  props.put("password", "AG");
  props.put("dll", "ocijdbc9");
  props.put("protocol", "thin");
  java.sql.Driver d =    Class.forName("oracle.jdbc.driver.OracleDriver").newInstance();
  java.sql.Connection conn =    Driver.connect("jdbc:oracle:thin:@localhost:1521:sid6", props);

	_______:  - or TEST:  java utils.dbping ORACLE_THIN  u1   AG  evo4:1521:cdmvdev
Test-Output:
	W:\Tests\eclipseW\TransMgm\config>java utils.dbping ORACLE_THIN  u1   AG   evo4:1521:cdmvdev	
	**** Success!!! ****	
	You can connect to the database in your app using:	
	  java.util.Properties props = new java.util.Properties();
	  props.put("user", "u1");
	  props.put("password", "AG");
	  props.put("dll", "ocijdbc9");
	  props.put("protocol", "thin");
	  java.sql.Driver d =	    Class.forName("oracle.jdbc.driver.OracleDriver").newInstance();
	  java.sql.Connection conn =    Driver.connect("jdbc:oracle:thin:@evo4:1521:cdmvdev", props);
##________________________________________  ___________________________


#####  ==========  WL-Ora-Driver:
- java utils.dbping ORACLE user password server   ; e.g.: java utils.dbping ORACLE u1 AG cdmvdev
	 output of that for cdmvdev:	 
	 **** Success!!! ****	 
	 You can connect to the database in your app using:	 
	   java.util.Properties props = new java.util.Properties();
	   props.put("user", "u1");
	   props.put("password", "AG");
	   java.sql.Driver d =	     Class.forName("weblogic.jdbc.oci.Driver").newInstance();
	   java.sql.Connection conn =     Driver.connect("jdbc:weblogic:oracle:cdmvdev", props);
- The driver classes for the BEA WebLogic Type 4 JDBC Oracle driver are:
	XA: weblogic.jdbcx.oracle.OracleDataSource
	Non-XA: weblogic.jdbc.oracle.OracleDriver
- To connect to an Oracle database, use the following URL format:  jdbc:bea:oracle://dbserver:port
- OK-Ora-cmdv-evo4: <JDBCConnectionPool DriverName="weblogic.jdbc.oci.Driver" InitialCapacity="0" MaxCapacity="10" Name="cmdv_pool1" Password="{3DES}Qdo388UdKBk=" Properties="user=u1" Targets="s1" TestConnectionsOnCreate="true" TestConnectionsOnRelease="true" TestConnectionsOnReserve="true" TestTableName="DUAL" URL="jdbc:weblogic:oracle:cdmvdev"/>
 misc: ?
- ConnectionPool: URL== jdbc:weblogic:oracle:cdmvdev ; Driver == weblogic.jdbc.oci.Driver
- OraConPool_IN82 	jdbc:oracle:thin:@in82:1521:sid6 	oracle.jdbc.xa.client.OracleXADataSource 	
