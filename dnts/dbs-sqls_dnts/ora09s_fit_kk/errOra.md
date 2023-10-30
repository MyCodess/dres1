ORA-00600	low level problems; generic code for internal errors, HW-problems, File corruption, 
##________________________________________  ___________________________


#####  ==========  ORA-01555:
show parameter UNDO
alter system set undo_retention = 10800;

	_______:  calculating undo_retention: (admin.pdf_13-11)
- info for UNDo-Statistics: v$undostat
- problem cases:  select * from v$undostat where ( SSOLDERRCNT > 0 OR NOSPACEERRCNT > 0 );
    SSOLDERRCNT == # ORA-01555 was happened!
-UndoSpace required in UNDO-TableSpace = UR * UPS + overhead = Undo_Retention_seconds * UPS_TransactionsPerSecond + overhead:
    UPS=Number of TransactionsPerSecond :
    select BEGIN_TIME, END_TIME, UNDOTSN, UNDOBLKS , TXNCOUNT from v$undostat order by TXNCOUNT;
    UPS= TXNCOUNT / (END_TIME - BEGIN_TIME in seconds)
