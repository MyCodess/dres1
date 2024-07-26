______________ SQL.Compound.Statements: Procedures, Functions, Routines, Cursors, prepared.stmt, ... (like plsql in Ora): __________
##________________________________________  ___________________________


#####  ==========  Routines.Builtin: builtin-Functions+Procedures+Operators:  (-DIFF with user-defined-funcs !!)
    -!! see.
        - ref--Chapter 12. Functions and Operators
        - ref-- Function IndexSection
        -!  help contents --> help Functions --> eg: help Date and Time Functions  -->  help TIMESTAMP FUNCTION
    --- Date/Time:
        -!! see ref--12.7. Date and Time Functions  + for format-tables see the second table there!!
        - select CURRENT_TIMESTAMP(), CURDATE(), CURTIME();
        - select DATE_FORMAT( CURRENT_TIMESTAMP(),  "%Y-%m-%d");   ##--> 2013-01-05
        - select DATE_FORMAT( CURRENT_TIMESTAMP(),  "%Y-%m-%d --- %H-%i-%s ---Day.of.Year: %j");  ##-see:  help DATE_FORMAT
        -
    --- Operators (as AND, OR, <,<,=, IS NULL, REGEXP, ....)
        -!! see table in ref--12.3. Operators
    --- CASE / IF/ LOOPs /IFNULL/... in SQL-Stmts:   Control Flow Function (buildin):
        -!!DIFF:  CASE/IF in sql-stmts  syntax  <-->   CASE/IF in Stored.Procedures syntax !!:
        	- for  IF/CASE/.... in SQL-Stmts (select,...) see: ref--12.4. Control Flow Functions
			- for IF/CASE/.... in PROCEDURES/Stored.Routines/User.Function-Constructs see "ref--13.6.5. Flow Control Statements":
		-!! LOOPS are only in User.Routines (FUNCTIONS/PROCEDURES/TRIGGERS/..., so in  Compound-Statements; see nts in next section)
		      so there are more LOOPs/WHile/....... constructs, but only in Compound-Statements (enclosed in begin-end, eg in user-procedures !!
		--- IF-in-SQLs:
			- SELECT IF(1>2, 2, 3);  ##--> 3
			- SELECT IF(STRCMP('test','test1'),'no','yes');  ##--> no
			- select IF ((select count(*) from registered_participant) = 98, "OK", "Not-OK") as registered_participant-counts-check,
    --- REGEXP:
        -!! see ref--12.5.2. Regular Expressions
        -! help regexp ; ...
##________________________________________  ___________________________


#####  ==========  Routines.User.defined: User.defined-Functions(UDF) + Procedures(UDP) + Operators/Triggers/...: (-DIFF with Buildin-funcs !!)
    -!! see:
		- description:  ref--Chapter 19. Stored Programs and Views
		- syntax:       ref--Chapter 13. SQL Statement Syntaxref  --> -! 13.1.15. CREATE PROCEDURE and CREATE FUNCTION Syntax  + Section 13.6, “MySQL Compound-Statement Syntax”. + 13.7.3. Plugin and User-Defined Function Statements
		- Forum: http://forums.mysql.com/list.php?98.
	---
	- dictionaries in:  mysql.proc + INFORMATION_SCHEMA ROUTINES Table”
	-!! DELIMITER // <my routine ....>  DELIMITER ;  ##--II- otherwise get	error, because mysql considers the first ";" as end-of-stmt and executes it immediately !!
	--- PROCEDURE / FUNCTION:
		-!! NEVER use the same name for parameters as the column names!! make problems!!
		--- show:
		- SHOW CREATE PROCEDURE routine1;  SHOW CREATE FUNCTION routine1;
		- show procedure status [like 'proc1%'];
		- show function  status [like 'proc1%'];
		- listing all stored procedures and stored functions in a given database (faq-B.4.6):
		  SELECT ROUTINE_TYPE, ROUTINE_NAME FROM INFORMATION_SCHEMA.ROUTINES WHERE ROUTINE_SCHEMA='dbname';
		--- using/invoking procs/funcs:
			- procedures-using with "CALL":  CALL proc1("xxx"); ##-as in:   proc1(out pam1 varchar(30)) ...; --> then: set @aa=0; call proc1(@aa);  select @aa;
			- funcs-using:
				- select hello1("aaa");  ##-- with eg: CREATE FUNCTION hello(s CHAR(20)) RETURNS CHAR(50) RETURN CONCAT('Hello, ',s,'!');
				- /OR intoa var:  set @v1=hello("me1");  select @v1;
		- drop function hello1;
	--- LOOPs, WHILE, UNTIL, ITERATE, REPEAT .... :  " Flow Control Statements"
		- ref-13.6.5. Flow Control Statements
		-! FOR : mysql has NOT for-loops!
	--- Triggers:
		- INFORMATION_SCHEMA TRIGGERS Table
		- SHOW TRIGGERS [FROM db_name] [like_or_where]
##________________________________________  ___________________________


#####  ==========  Cursors:
	- see:
		http://en.wikipedia.org/wiki/Cursor_%28databases%29
		SQL_CompleteReference_McGrawHill__Y1999.pdf--p.376-Multi-Row Queries
	--- Using of cursors:  http://en.wikipedia.org/wiki/Cursor_%28databases%29 
		To use cursors in SQL procedures, you need to do the following:
		Declare a cursor that defines a result set.
		Open the cursor to establish the result set.
		Fetch the data into local variables as needed from the cursor, one row at a time.
		Close the cursor when done.
		-- eg mysql:
		DECLARE table_names CURSOR for SELECT table_name FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = DATABASE();
		OPEN table_names;
		WHILE done = 0 ; DOFETCH NEXT FROM table_names INTO TNAME; ....;  END WHILE;
		CLOSE table_names;
	---
##________________________________________  ___________________________


#####  ==========  
