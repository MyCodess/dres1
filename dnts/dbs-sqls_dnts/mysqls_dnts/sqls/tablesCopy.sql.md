-- ---------------------------------------------------------------------------
--  copy.table:
    - ONLY structure (no data):  CREATE TABLE copy LIKE original; INSERT INTO copy SELECT * FROM original;
       /OR with more specifications:  CREATE TABLE student2 (id INT(3) auto_increment primary key) SELECT student.name,student.class, student.mark fr>
    - ONLY data copy:  insert into t2 select * from t1; ##-must have same structures! otherwise specify columns ...
    - structurei + data :  CREATE TABLE copy LIKE original; INSERT INTO copy SELECT * FROM original;
          /OR in one step:  create table copy1 select * from org1;
          /OR:  CREATE TABLE IF NOT EXISTS copy1 SELECT * FROM org1 WHERE class='Four'
    - with where:   create table copy1 select * from org1 where col1>1;
    - insert into table2 ( col1 , col2 , col3 ) select field3 , ( field7 + field8 ) * 9.37 , 0 from table1
-- ---------------------------------------------------------------------------
