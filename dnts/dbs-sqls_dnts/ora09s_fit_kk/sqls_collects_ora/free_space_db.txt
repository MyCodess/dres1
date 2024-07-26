##________________________________________  ___________________________


#####  ==========  Freespace-Check (elm-ol.Guent.-0607-0ra9i):
SELECT a.name, b.tablespace_name, substr('Free : '||round(sum(b.bytes)/1024/1024,2),1,30) as SIZE_in_MegaBytes
FROM dba_free_space b, v$database a
GROUP BY b.tablespace_name, a.name
UNION
SELECT a.name, b.tablespace_name, substr('Total: '||round(sum(b.bytes)/1024/1024,2),1,30)
FROM dba_data_files b, v$database a
GROUP BY b.tablespace_name, a.name
ORDER BY 1,2,3;
NAME      TABLESPACE_NAME                SIZE_IN_MEGABYTES

	_______:  ------ ------------------------------ ------------------------------
DWITSB01  DRSYS                          Free : 85.72
DWITSB01  DRSYS                          Total: 100

	_______:  ------ ------------------------------ ------------------------------
.....
##________________________________________  ___________________________


#####  ==========  
