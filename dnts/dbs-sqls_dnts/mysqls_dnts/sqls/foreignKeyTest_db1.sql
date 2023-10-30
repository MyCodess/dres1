/*------ testing foreign-keys dependencies with "ON DELETE CASCADE" ------ */

/* as -u root , create db1 and dbu1 on localhost :
mysql -u root -e "create user  'dbu1'@'localhost' ";
mysql -u root -e "DROP DATABASE IF EXISTS db1;  create database  db1;  grant ALL on db1.* to  dbu1;"
# then as dbu1:
mysql  --user='dbu1' db1
mysql> source  ./foreignKeyTest_db1.sql
*/


/* -------- create tables: ------ */
show tables;
DROP table IF EXISTS  child2_nocascade, child1, parent2, parent1 CASCADE;
show tables;

CREATE TABLE parent1 (
    id int unsigned not null primary key,
    pname varchar(255) default null
);

CREATE TABLE parent2 (
    id int unsigned not null primary key,
    pname varchar(255) default null
);

CREATE TABLE child1 (
    col1_id int unsigned not null,
    col2_id int unsigned not null,
    PRIMARY KEY (col1_id, col2_id),
    KEY pkey (col2_id),
    CONSTRAINT child1_parent1_id_fk FOREIGN KEY (col1_id) REFERENCES parent1 (id)  ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT child1_parent2_id_fk FOREIGN KEY (col2_id) REFERENCES parent2 (id)      ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE child2_nocascade (
    col1_id int unsigned not null,
    col2_id int unsigned not null,
    PRIMARY KEY (col1_id, col2_id),
    KEY pkey (col2_id),
    CONSTRAINT child2_parent1_id_fk FOREIGN KEY (col1_id) REFERENCES parent1 (id),
    CONSTRAINT child2_parent2_id_fk FOREIGN KEY (col2_id) REFERENCES parent2 (id)
);

/* --------- data: --------------  */
insert into parent1 values   (1, 'p1-1'),  (2, 'p1-2');
insert into parent2 values   (1, 'p2-1'),  (2, 'p2.2');
insert into child1 values            (1, 1), (1, 2), (2, 1), (2, 2);
insert into child2_nocascade values  (1, 1), (1, 2), (2, 1), (2, 2);

/* --------- selects/show : --------------  */
select * from parent1;
select * from parent2;
select * from child1;
select * from child2_nocascade;
show tables;

/* ---- testing for foreign keys: -------- 
try these, it should work:

-- tests1:
source ./foreignKeyTest_db1.sql
DELETE FROM parent1 WHERE id = 2;   ##-can not!
drop table child2_nocascade;
DELETE FROM parent1 WHERE id = 2;  ##-should work!
select * from child1;

-- tests2
source ./foreignKeyTest_db1.sql
alter table child2_nocascade drop  FOREIGN KEY child2_nocascade_ibfk_1;
alter table child2_nocascade add   FOREIGN KEY child2_nocascade_ibfk_2  (col1_id) REFERENCES parent1 (id) ON DELETE CASCADE ON UPDATE CASCADE;
DELETE FROM parent1 WHERE id = 2;  ##- should work!

-- test3:
source ./foreignKeyTest_db1.sql
SET foreign_key_checks = 0;
DELETE FROM parent1 WHERE id = 2;  ##-works, but then db is not consistent any more! user is resposbile to make it consistent!!
SET foreign_key_checks = 1;

--! test4 : transaction=0:
SET foreign_key_checks = 0;
select * from parent1;
delete from parent1 where id=1;   -- now NON-consistent db due to child1 constraint violation!!
SET foreign_key_checks = 1;
select * from parent1;
select * from child1;
select * from child1 left join parent1 on (parent1.id = child1.col1_id);  -- !! see now the NULL entries there !! NON-consistent rows!!
-- !! finding ONLY NON-consistent rows:
select * from child1 left join parent1 on (parent1.id = child1.col1_id) where child1.col1_id  IS NOT NULL AND parent1.id  IS NULL;
*/


