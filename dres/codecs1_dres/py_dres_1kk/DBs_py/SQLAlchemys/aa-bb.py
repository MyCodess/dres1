##-------- MetaDat/Table/Column/...-objects with SQLAlchemy : so ORMapping !
##-- based on:  docsvar/Py_docsvar/sqlalchemy_20_dc/tutorial/metadata.html

##-- create basic engine:
from  sqlalchemy import create_engine
from sqlalchemy import text
##--either in memory DB (non-persistent))
##__ engine =  create_engine("sqlite+pysqlite:///:memory:", echo=True)
##--OR with file/persistent:
engine = create_engine("sqlite+pysqlite:///db1-sqlal.sqlite", echo=True)

##-- so MetaData  <---> DB-MasterSchema / dbschema
from sqlalchemy import MetaData
metadata_obj = MetaData()

##--I-ORMapping:  With the above example, when we wish to write code that refers to the user_account table in the database, we will use the user_table Python variable to refer to it.
#- so: user_account table in the database  <--->   user_table Python variable/Obj :
from sqlalchemy import Table, Column, Integer, String
user_table = Table(
    "user_account",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("fullname", String),
)

##-- ForeigKey relations:
from sqlalchemy import ForeignKey
address_table = Table(
    "address",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("user_account.id"), nullable=False),
    Column("email_address", String, nullable=False),
)

##-- print DDLs + create tables/objects + commit :
metadata_obj.drop_all(engine)  ##--if-wanted: to drop all and re-create each time calling this script! and so also generating the full  DDLs later with metadata_obj.create_all( ,....
metadata_obj.create_all(engine)

##-------------------- Reflection : ---------------------------------
print("\n","="*80)
print("----- Reflection /other-way-round: from DB-tables into App-Objects mapping : ------------")
##-- in DB the table user_account must already exist! was created with the previous py-script! :
##-- for eg do in DB:  insert into "main"."user_account" values (2, "u2", "User2");
user_account_obj = Table("user_account", metadata_obj, autoload_with=engine)
user_account_obj.insert().values({"id": 3, "name": "u3", "fullname": "User3-from-App"})  #--??did NOT work yet this insert !!??
conn = engine.connect()
conn.execute(text("INSERT INTO user_account VALUES (2, 'u2', 'User2')"))
conn.commit()

