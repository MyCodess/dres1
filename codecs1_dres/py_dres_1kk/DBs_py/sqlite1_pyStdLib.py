##--see7based on:  https://docs.python.org/3.10/library/sqlite3.html#sqlite3-tutorial  ##online-doc! not the PDF-one ! are different !

import sqlite3

##--I-RAM-db : Pass ":memory:" to open a connection to a database that is in RAM instead of on disk! see pydoc sqlite3.connect
##--OR-in memory/RAM-db (non-persistent):   db_filepath=":memory:"
db_filepath="/tmp/db1.sqlite"
con = sqlite3.connect(db_filepath)

cur = con.cursor()
##-- check if the table movie is there? if not, create it:
res = cur.execute("SELECT name FROM sqlite_master where name='movie'")
##__  print (res.fetchall())
if res.fetchone()  is not None:
    cur.execute("drop table 'movie'")
cur.execute("CREATE TABLE movie(title, year, score)")
res = cur.execute("SELECT name FROM sqlite_master")
print("-- table-names in sqlite_master table  :  ", res.fetchone())

res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'") ##--NON-existing-table! must return none !
print("-- non-existing-table  :  ",res.fetchone() is None)

##-- insert new values:
cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")
con.commit()

##-- query:
res = cur.execute("SELECT score FROM movie")
print("-- scores: ", res.fetchall())

##-- Now, insert three more rows by calling cur.executemany(...):
data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]
cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
con.commit()  # Remember to commit the transaction after executing INSERT.

##-- verfiy the inserts:
for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
    print(row)

##-- closing DB:
con.close()

##-- ening a new one, creating a new cursor, then querying the database to verify it:
new_con = sqlite3.connect(db_filepath)
new_cur = new_con.cursor()
res = new_cur.execute("SELECT title, year FROM movie ORDER BY score DESC")
title, year = res.fetchone()
print(f'The highest scoring Monty Python movie is {title!r}, released in {year}')

