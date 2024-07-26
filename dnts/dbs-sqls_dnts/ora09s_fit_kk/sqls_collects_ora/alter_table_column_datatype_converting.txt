--############# sqls -> converting column type / alter table ...: ##############

	_______:  --- http://forums.oracle.com/forums/thread.jspa?threadID=595075 :
Re: how to change the column datatype to number from varchar2 in oracle10g 
Posted: Jan 17, 2008 2:26 AM    in response to: user609736 		 	 	Reply 
Oh that greate solution.
A little shortCut is here.
create table TestTable(ColA varchar2(5));
insert into TestTable values('12345');
alter table TestTable add (ColATemp number(5));
update TestTable set ColATemp = ColA;
alter table TestTable drop column ColA;
alter table TestTable rename column ColATemp to ColA;
##________________________________________  ___________________________


#####  ==========  /OR again:
Re: how to change the column datatype to number from varchar2 in oracle10g 
Posted: Dec 10, 2007 2:52 AM    in response to: user609736 		 	 	Reply 
SQL> create table "USER" (UserId varchar2(5))
Table created.
SQL> insert into "USER" values ('12345')
1 row created.
SQL> alter table "USER" add (UserId_tmp number(5))
Table altered.
SQL> update "USER" set userid_tmp=userid
1 row updated.
SQL> alter table "USER" set unused column userid
Table altered.
SQL> alter table "USER" rename column userid_tmp to userid
Table altered.
SQL> alter table "USER" drop unused columns
Table altered.
SQL> desc "USER"
TABLE USER
 Name                                      Null?    Type                        
 ----------------------------------------- -------- ----------------------------
 USERID                                             NUMBER(5)
##________________________________________  ___________________________


#####  ==========  
Suppose we need to change column data type in Oracle database table. Suppose also that the table has some data. Let's say 1000000 rows. I want to change datatype from NUMBER to VARCHAR2. Lets see. Oracle doesn't allow me to modify column this way when there is data in the table. I can not also rename the column.
Solution:
ALTER TABLE: add new column (temp) with desired datatype.
UPDATE: (copy data to the new column using piecemeal batch size)
ALTER TABLE: drop the original column
ALTER TABLE: add new column with the name of the original and the desired datatype
UPDATE: (copy data to the new column from the temp column using piecemeal batch size)
ALTER TABLE: drop temp column
##________________________________________  ___________________________


#####  ==========  SQL: ALTER TABLE Statement : ==================
http://www.techonthenet.com/sql/tables/alter_table.php :
The ALTER TABLE statement allows you to rename an existing table. It can also be used to add, modify, or drop a column from an existing table.
Renaming a table
The basic syntax for renaming a table is:
ALTER TABLE table_name
 RENAME TO new_table_name;
For example:
ALTER TABLE suppliers
 RENAME TO vendors;
This will rename the suppliers table to vendors.
Adding column(s) to a table
Syntax #1
To add a column to an existing table, the ALTER TABLE syntax is:
ALTER TABLE table_name
 ADD column_name column-definition;
For example:
ALTER TABLE supplier
 ADD supplier_name  varchar2(50);
This will add a column called supplier_name to the supplier table.
Syntax #2
To add multiple columns to an existing table, the ALTER TABLE syntax is:ALTER TABLE table_name
ADD (	column_1	column-definition,
 	column_2	column-definition,
 	...	
 	column_n	column_definition );
For example:ALTER TABLE supplier
ADD (	supplier_name	varchar2(50),
 	city	varchar2(45) );
This will add two columns (supplier_name and city) to the supplier table.
Modifying column(s) in a table
Syntax #1
To modify a column in an existing table, the ALTER TABLE syntax is:
ALTER TABLE table_name
 MODIFY column_name column_type;
For example:
ALTER TABLE supplier
 MODIFY supplier_name   varchar2(100)     not null;
This will modify the column called supplier_name to be a data type of varchar2(100) and force the column to not allow null values.
Syntax #2
To modify multiple columns in an existing table, the ALTER TABLE syntax is:ALTER TABLE table_name
MODIFY (	column_1	column_type,
 	column_2	column_type,
 	...	
 	column_n	column_type );
For example:ALTER TABLE supplier
MODIFY (	supplier_name	varchar2(100)	not null,
	city	varchar2(75)	 	);
This will modify both the supplier_name and city columns.
Drop column(s) in a table
Syntax #1
To drop a column in an existing table, the ALTER TABLE syntax is:
ALTER TABLE table_name
 DROP COLUMN column_name;
For example:
ALTER TABLE supplier
 DROP COLUMN supplier_name;
This will drop the column called supplier_name from the table called supplier.
Rename column(s) in a table
(NEW in Oracle 9i Release 2)
Syntax #1
Starting in Oracle 9i Release 2, you can now rename a column.
To rename a column in an existing table, the ALTER TABLE syntax is:
ALTER TABLE table_name
 RENAME COLUMN old_name to new_name;
For example:
ALTER TABLE supplier
 RENAME COLUMN supplier_name to sname;
This will rename the column called supplier_name to sname.
Acknowledgements: Thanks to Dave M., Craig A., and Susan W. for contributing to this solution!
Practice Exercise #1:
Based on the departments table below, rename the departments table to depts.CREATE TABLE departments
(	department_id	number(10)	not null,
 	department_name	varchar2(50)	not null,
 	CONSTRAINT departments_pk PRIMARY KEY (department_id)
);			
Solution:
The following ALTER TABLE statement would rename the departments table to depts:
ALTER TABLE departments
 RENAME TO depts;
Practice Exercise #2:
Based on the employees table below, add a column called salary that is a number(6) datatype.CREATE TABLE employees
(	employee_number	number(10)	not null,
 	employee_name	varchar2(50)	not null,
 	department_id	number(10),	
 	CONSTRAINT employees_pk PRIMARY KEY (employee_number)
);			
Solution:
The following ALTER TABLE statement would add a salary column to the employees table:
ALTER TABLE employees
 ADD salary number(6);
Practice Exercise #3:
Based on the customers table below, add two columns - one column called contact_name that is a varchar2(50) datatype and one column called last_contacted that is a date datatype.CREATE TABLE customers
(	customer_id	number(10)	not null,
 	customer_name	varchar2(50)	not null,
 	address	varchar2(50),	
 	city	varchar2(50),	
 	state	varchar2(25),	
 	zip_code	varchar2(10),	
 	CONSTRAINT customers_pk PRIMARY KEY (customer_id)
);			
Solution:
The following ALTER TABLE statement would add the contact_name and last_contacted columns to the customers table:ALTER TABLE customers
ADD (	contact_name	varchar2(50),
 	last_contacted	date );
Practice Exercise #4:
Based on the employees table below, change the employee_name column to a varchar2(75) datatype.CREATE TABLE employees
(	employee_number	number(10)	not null,
 	employee_name	varchar2(50)	not null,
 	department_id	number(10),	
 	CONSTRAINT employees_pk PRIMARY KEY (employee_number)
);			
Solution:
The following ALTER TABLE statement would change the datatype for the employee_name column to varchar2(75):
ALTER TABLE employees
 MODIFY employee_name varchar2(75);
Practice Exercise #5:
Based on the customers table below, change the customer_name column to NOT allow null values and change the state column to a varchar2(2) datatype.CREATE TABLE customers
(	customer_id	number(10)	not null,
 	customer_name	varchar2(50),	 
 	address	varchar2(50),	
 	city	varchar2(50),	
 	state	varchar2(25),	
 	zip_code	varchar2(10),	
 	CONSTRAINT customers_pk PRIMARY KEY (customer_id)
);			
Solution:
The following ALTER TABLE statement would modify the customer_name and state columns accordingly in the customers table:ALTER TABLE customers
MODIFY (	customer_name	varchar2(50) not null,
 	state	varchar2(2) );
Practice Exercise #6:
Based on the employees table below, drop the salary column.CREATE TABLE employees
(	employee_number	number(10)	not null,
 	employee_name	varchar2(50)	not null,
 	department_id	number(10),	
 	salary	number(6),	
 	CONSTRAINT employees_pk PRIMARY KEY (employee_number)
);			
Solution:
The following ALTER TABLE statement would drop the salary column from the employees table:
ALTER TABLE employees
 DROP COLUMN salary;
Practice Exercise #7:
Based on the departments table below, rename the department_name column to dept_name.CREATE TABLE departments
(	department_id	number(10)	not null,
 	department_name	varchar2(50)	not null,
 	CONSTRAINT departments_pk PRIMARY KEY (department_id)
);			
Solution:
The following ALTER TABLE statement would rename the department_name column to dept_name in the departments table:
ALTER TABLE departments
 RENAME COLUMN department_name to dept_name;
##________________________________________  ___________________________


#####  ==========  Mini-Tip #18: Changing a Column Data Type : ===========================
LewisC (Database Architect) Posted 1/16/2008
Comments (0) | Trackbacks (0)
http://blogs.ittoolbox.com/oracle/guide/archives/minitip-18-changing-a-column-data-type-21828  :
Another frequent question I get is a lot like an email I received just this morning: 
Hi Lewis, Can you please help me out¿..i want to change the datatype of column. The existing column have datatype as CLOB and I want to change it to NUMBER¿..Is it possible¿Also this column only have null values¿¿. I tried it on 10g but it was giving error SQL> alter table onbs_xml_message modify (cc_message_sysid number); ERROR at line 1: ORA-22859: invalid modification of columns Is there any other way to do so¿¿Mail if it is possible? Thanks a lot Bye¿¿¿
Clobs are a little bit different than other columns so I will leave that to the end. 
This question tells me if the column is empty (which means it is NULLable). That makes this one pretty easy. Since the column is empty, it is easiest to just use: 
ALTER TABLE onbs_xml_message DROP COLUMN cc_message_sysid; ALTER TABLE onbs_xml_message ADD (cc_message_sysid number); 
That would take care of it. If the column had data in it though, it gets a little harder. 
create table test_cols (
  clob_col clob,
  varc_col varchar2(30),
  num_col number);
We'll use this handy little test table. 
BTW, I am running this in 11g (it's all I have available at the moment) but it should work the same as 10g. 
SQL> alter table test_cols modify (clob_col number);
alter table test_cols modify (clob_col number)
                              *
ERROR at line 1:
ORA-22859: invalid modification of columns
SQL> alter table test_cols modify (varc_col number);
Table altered.
The clob change did not work but the varchar2 change did. This would not have worked had the column been populated: 
drop table test_cols;
create table test_cols (
  clob_col clob,
  varc_col varchar2(30),
  num_col number);
insert into test_cols (clob_col, varc_col, num_col)
values ('not empty', 'not empty', 1);
SQL> alter table test_cols modify (varc_col number);
alter table test_cols modify (varc_col number)
                              *
ERROR at line 1:
ORA-01439: column to be modified must be empty to change datatype
What we can do here is rename, recreate and, if the column has data, reassign values. We would end by dropping the old column: 
ALTER TABLE test_cols RENAME COLUMN clob_col TO clob_col_old;
ALTER TABLE test_cols ADD (clob_col number);
UPDATE test_cols
  SET clob_col = clob_col_old;
ALTER TABLE test_cols DROP COLUMN clob_col_old;
That would only work if the data within the old column is type compatible with the data type of the new column. In the case of my record above, the update would fail: 
SQL> UPDATE test_cols
  2    SET clob_col = to_number(clob_col_old);
  SET clob_col = clob_col_old
                 *
ERROR at line 2:
ORA-01722: invalid number
If your starting column is a NOT NULL column, you'll need to define a default value for it. That's not a problem and the default can be dropped after the table is altered. If you are doing this on a large table, the performance impact of the alter can be huge. 
Note that doing alters on your tables may lead to validation issues with any dependent objects. Be especially careful if you use ALTER TABLE RENAME COLUMN. Many dependent objects will continue working (Oracle updates the data dictionary for you). The downside is that if you create a new column with the old name but don't drop the old column, your results may get wacky! Try that when you have a function based index on the old column. Talk about a debugging nightmare. 
If you are manipulating primary and foreign keys, I would recommend dropping your constraints and rebuilding them after. Yes, you can do certain manipulations with everything in place but it is not normally required and is usually more painful than it's worth. These kinds of changes should be rare. I hope that I don't need to say that you should always run these kinds of changes in dev and test BEFORE you run them in production. 
Hope this helps, 
LewisC
Listen to my latest podcast where I discuss RAC and Grid with experts Phillip Newland and Scott Jesse of Oracle - download it here. 
Email me 
My blog represents my thoughts and opinions and not my employers thoughts and opinions. If you want to know what my employers think, it is best to ask them directly. On the other hand, I pretty much say what I am thinking right here.
##________________________________________  ___________________________


#####  ==========  DBMS_REDEFINITION pl/sql : ================================
4. Columns can't be renamed or reorganized
Renaming a table column or changing its data type usually meant creating a new table and copying the old data to it. Columns couldn¿t be renamed at all, and datatypes could be changed only if they had no data (only NULL values).
Oracle 9i has not one but two ways to overcome these limitations. The ALTER TABLE command can now rename columns directly:
ALTER TABLE books RENAME COLUMN tiitle TO title;
Also, a supplied PL/SQL package called DBMS_REDEFINITION enables a DBA to change a table's column structure while the table is online and available to users. It¿s a complex procedure, but in general the steps are as follows:
Use DBMS_REDEFINITION.CAN_REDEF_TABLE to check if the table qualifies for online redefinition, and specify if the redefinition will be by primary key (recommended) or by row IDs.
Create an empty table in the same schema, but with the desired layout. Omit columns you want to drop; include new columns you¿d like to create.
Use DBMS_REDEFINITION.START_REDEF_TABLE to begin the redefinition process. The parameters to this procedure indicate the old table, the new one, and how to map the existing columns to the columns of the new table.
Create any constraints (disabled), triggers, indexes, and grants desired on the new table.
Use DBMS_REDEFINITION.FINISH_REDEF_TABLE to complete the process. The original table is locked for a short time regardless of how large or small it is, while the definitions are swapped between the two tables.
Drop the temporary table used in the redefinition; it is no longer needed.
Of course, redefining a table doesn¿t automatically update any application code that accesses that table. Applications must be changed and tested separately. What DBMS_REDEFINITION does, however, is shorten the time that the table is unavailable to users at cutover time.
##________________________________________  ___________________________


#####  ==========  
