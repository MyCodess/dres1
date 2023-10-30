____________________ quks, onliners, .... mysql  ________________________________ 
##________________________________________  ___________________________


#####  ==========  count rows of all user-tables:
	-! ist NOT correct, unfortunately, for InnoDB-Engine (dafault):
	SELECT TABLE_NAME, TABLE_ROWS FROM information_schema.tables WHERE table_schema = database(); ##--not updated/correct number in TABLE_ROWS column!!
	so see the two sql-scripts insqls-dir!!
