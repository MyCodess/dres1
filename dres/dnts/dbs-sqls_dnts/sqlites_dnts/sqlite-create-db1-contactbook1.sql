-- simple-examples-db1 _1kk for AdressBook / contactbook /telefonbuch :

-- enabling/activating support for foreign_keys constraints/check :
PRAGMA foreign_keys = ON;

-- people-name-tel-table with AUTOINCREMENT id1 (set it to NULL for inserts) :
create table peop1 (id INTEGER PRIMARY KEY, name varchar(100), tel int, email varchar(50) UNIQUE, birth datetime ) ;
-- Adresse-table
create table adr1 (id INTEGER PRIMARY KEY, street varchar(100), plz int, city varchar(50), updated datetime, FOREIGN KEY(id) REFERENCES peop1(id) ) ;

insert into peop1 values (NULL, "aaa", 1111, "aaa@aaa", 2001-01-01) ;
insert into peop1 values (NULL, "bbb", 2222, "bbb@bbb", 2002-02-02) ;
insert into peop1 values (NULL, "ccc", 3333, "ccc@ccc", 2003-03-03) ;


insert into adr1 values (1, "str1-no1", 1000, "aaa@aaa", 2011-10-11) ;
insert into adr1 values (2, "str2-no2", 2000, "bbb@bbb", 2012-11-12) ;
insert into adr1 values (3, "str3-no3", 3000, "ccc@ccc", 2013-12-13) ;


