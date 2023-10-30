##--based on file:///up1/t1/t1var/docsvar/Py_docsvar/0-RefDocsVar_py/docs-html/library/sqlite3.html#sqlite3-tutorial
from  sqlalchemy import create_engine
from sqlalchemy import text
engine =  create_engine("sqlite+pysqlite:///:memory:", echo=True)   ##--OR with file/persistent:  create_engine("sqlite+pysqlite:///db1-sqlal.sqlite", echo=True)

########## 1- Core pkg /Connection : ################### 
from sqlalchemy import text
with engine.connect() as conn:
	result = conn.execute(text("select 'hello world'"))
	print(result.all())

##--Core-pkg/Connection with  "commit as you go" method of Connection /: must invoke commit()/rollback() explicitely! :
with engine.connect() as conn:
    conn.execute(text("CREATE TABLE some_table (x int, y int)"))
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
    )
    conn.commit()

##--Core-pkg/Connection with  "begin once" method of Connection: as Transaction, and implicit/including commit():
# "begin once"
with engine.begin() as conn:
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 6, "y": 8}, {"x": 9, "y": 10}],
    )

########## 2- ORM pkg (Session): the same as above ###################
##--I-Session is auto-commit as default!
from sqlalchemy.orm import Session
stmt = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y")
with Session(engine) as session:
    result = session.execute(stmt, {"y": 6})
    for row in result:
        print(f"x: {row.x}  y: {row.y}")

