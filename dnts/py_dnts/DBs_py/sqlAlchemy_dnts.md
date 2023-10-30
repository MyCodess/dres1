_________________  SQLAlchemy  :  _______________________________________________
- based on:  https://docs.sqlalchemy.org/en/20/tutorial/index.html  , /_230204  ;
##________________________________________  ___________________________


#####  ==========  
pip install SQLAlchemy
##-- user-installed on:   /home/u1/.local/lib/python3.10/site-packages/sqlalchemy/
--
>>> sqlalchemy.__version__
'2.0.1'
##________________________________________  ___________________________


#####  ==========  dnts:
- Core (engine.Connection)  <-->   ORM (engine.Session) !)
- With-Statement for Connection !! :  As the Connection represents an open resource against the database, we want to always limit the scope of our use of this object to a specific context, and the best way to do that is by using Python context manager form, also known as the with statement. ./sqlalchemy_20_dc/tutorial/dbapi_transactions.html

	_______:  commit-styles/-alternatives.
	- "commit as you go":  no-implicit-commmits! the developer must call it explicitely as conn=engine.connect() .... conn.commit()  ...
	- "begin once" : implicit commits! all thing as one transaction-block with:  engine.begin() instead engine.connect() 
	so For this mode of operation, we use the Engine.begin() method to acquire the connection, rather than the Engine.connect() method. see: Py_docsvar/sqlalchemy_20_dc/tutorial/dbapi_transactions.html

	_______:  DB --> Objectsi/App : Reflection ( Table.autoload_with parameter) :!
	- reflection process does it reverse of creating tables from pbjects ! so it reads the DB tables and convert them to py-objects  using the Table.autoload_with parameter !
	some_table = Table("some_table", metadata_obj, autoload_with=engine)
##________________________________________  ___________________________


#####  ==========  addies:
	- Alembic provides for the creation, management, and invocation of change management scripts for a relational database, using SQLAlchemy as the underlying engine.  https://alembic.sqlalchemy.org/
