__________________JAVA_ORA_______________________
##________________________________________  ___________________________


#####  ==========  JDBC:
-!! ${ORACLE_HOME}/jdbc/Readme.txt  --> full short listing of all libs,...!
-! ll ${ORACLE_HOME}/jdbc/
-! ll ${ORACLE_HOME}/jdbc/lib
- http://www.oracle.com/java/jdbc

	_______:  jars/libs ora9:
	- JDK.1.1.x: Add [ORACLE_HOME]/jdbc/lib/classes111.zip and [ORACLE_HOME]/jdbc/lib/nls_charset11.zip to your CLASSPATH.
    - JDK.1.2.x & 1.3.x: Add classes12.zip and nls_charset12.zip if JDK 1.2.x or 1.3 is used.
	- JDK.1.4.x: Add ojdbc14.jar and nls_charset12.zip if JDK 1.4 is used.
  - Add [ORACLE_HOME]/jdbc/lib to your LD_LIBRARY_PATH.

	_______:  test-jdbc-conn from server:
	- oemapp jdbctest ; sql> connect dba1/oradba1@DEM01 ; sql> select * from v$instance;
		see: Connecting to "jdbc:oracle:oci8:@DEM01" as "dba1"... done. ...
