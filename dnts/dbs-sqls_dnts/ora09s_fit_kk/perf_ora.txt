___________ performance-ora: ____________________
--################ static-params:
lock_sga = true
java_pool and log_buffer (rest of SGA is dyn.)
--################ dyn-params:
alter system set db_cache_advice=ON;
--################ Memories/Bufers/Caches/...: ###########################
=== SGA-Allg:
	- v$sysstat , v$sgastat , 
	- V$SGA V$SGA_CURRENT_RESIZE_OPS V$SGA_RESIZE_OPS V$SGA_DYNAMIC_COMPONENTS V$SGA_DYNAMIC_FREE_MEMORY V$SGASTAT 
	- select name, value/1024/1024 MB from v$sga;
	- sga-curr-status/verbrauch:	select * from  v$sgastat;
	- before any tests flush SGA: alter system flush shared_pool;
=== DB_Buffer/Cache:
	- V$DB_CACHE_ADVICE , V$BUFFER_POOL , V$BUFFER_POOL_STATISTICS
	- with  db_cache_advice=ON for days:  V$DB_CACHE_ADVICE :  --> values for: DB_CACHE_SIZE  : 
		select SIZE_FOR_ESTIMATE, ESTD_PHYSICAL_READS, ESTD_PHYSICAL_READ_FACTOR from v$db_cache_advice;
	- physical/logical reads RATIO: parameter must be on, otherwise values only historically: db_cache_advice		
		- querying basic values:
			select name,value from v$sysstat   where name in ('physical reads','db block gets', 'consistent gets', 'physical reads direct');
		- calculating tha Ratio of physical/logical-reads (logicals- and consinten gets are from Buffers; physical reads are IO;  'physical reads direct' are from PGA):
			Buffer cache hit ratio=1-(physical reads - physical_reads_direct) /(db block gets + consistent gets _ physical_reads_direct)
		-! NOT always 99% is good, esp. in DWarehousing is usu. not. see TIP-CH19.6-Alapati
=== Shared_Pool (see also extra parts for lib-cache,...): lib_cache + DIct_Cache
	- V$SHARED_POOL_ADVICE  -> adaptions/evaluations
	- current size?: show parameter /OR: select to_number(value)/1024/1024 MB_shared_pool_size from v$parameter where name='shared_pool_size';
	-! Advice/tunning-sharedPool:   select * from v$shared_pool_advice;
	--- Sizing/evaluating the Shared Pool: ch19.4 : not too low AND not too much?:
		 - too low?: wee saw (see lib-cache,..): if hit-ratio > .99 for lib-cache and > 90 for dict-cache --> is okay. is NOT low.
		 - too much?  select bytes/1024/1024 MB from v$sgastat where pool='shared pool'and name = 'free memory'; 
		 	--> sometimes is okay if high. but consistently high is too much.; if less than 5 MB free, then ist too low!
	--- Determining the Correct Shared Pool Size /Listing 19-4: ??? check 250 ??? (extreme large results for gx??)
	 select to_number (value) shared_pool_size, sum_obj_size, sum_sql_size,
	  sum_user_size, (sum_obj_size + sum_sql_size + sum_user_size) * 1.2 min_shared_pool 
	  from (select sum(sharable_mem) sum_obj_size from v$db_object_cache), (select sum(sharable_mem) sum_sql_size from v$sqlarea), 
	  (select sum(250 * users_opening) sum_user_size from v$sqlarea), v$parameter where name='shared_pool_size';
	-- Determining the Objects to Be Pinned in the Shared Pool /Listing 19-5:
 	select type, count(*) objects, sum(decode(kept, 'YES', 1, 0)) kept, sum(loads) - count(*) reloads from v$db_object_cache group by type order by objects desc; 
=== Library_Cache:
	-  v$librarycache , V$DB_OBJECT_CACHE , 
	- checking if sql-stmts are reused or not: see CH19.2.Alapati.9: 
		alter session set sql_trace=true; alter system flush shared_pool; ....; evaluating with: TKPROF !!
	- V$DB_OBJECT_CACHE view has information on all objects that are presently cached in the library cache
	- indicator of the library cache hit ratio: 
		SQL> Select sum(pinhits)/sum(pins)  Library_cache_hit_ratio From v$librarycache;
		: should be about 1. OK, but STILL sonsider waits seperately!! ch19.1-Alapati-Ora9
	- Determining the Efficiency of the Library Cache : ch19.2
	  SELECT namespace,pins,pinhits,reloads  From v$librarycache order by reloads;
	 - current status of lib-cache:
	   select * from V$LIBRARY_CACHE_MEMORY ;
	--- Optimzing parameters for lib-cache (except resizing it):
		- Cursor_Sharing = force
		Cursor_space_for_time=true
		Session_Cached_Cursors = true : if many users send ca. same sqls (as by forms/guis/...)
=== Dictionary Cache:
	- V$ROWCACHE :	displays statistics for data dictionary activity. Each row contains statistics for one data dictionary cache.
	- much much smaller than lib-cache.
	- status/efficiency: select (sum(gets - getmisses - fixed)) / sum(gets) "data dictionary hit ratio" from v$rowcache;
		:shióuld be > 95%
=== PGA:
	-! V$PGA_TARGET_ADVICE and V$PGA_TARGET_ADVICE_HISTOGRAM , V$PROCESS; V$PGASTAT
	-! curr used PGA by each process in : V$PROCESS
	-! V$PGASTAT see: Listing 5-9: Using the V$PGASTAT View /Alapati.9
	- pga_aggregate_target :sets maximum limit on the total memory allocated to the PGA.
	- for memory-intensive tasks such as group by, order by, rollup, and hash joins
	- Sizing-Tip for pga_aggregate_target,  Oracle-Guielines:
		- OLTP database: the target should be 16 to 20 percent of the total memory allocated to Oracle.
		- DSS database: the target should be 40 to 70 percent of the total memory allocated to Oracle.
=== UGA (users globa ares), session-memoryx-usages...:
	- lists all current sessions, per Oracle user and currentUGA (user global area) memory use for each session (ora.docs):
	 select sess.sid, sess.serial# ,  USERNAME, VALUE/1024/1024 UGA_Usage_MB  FROM V$SESSION sess, V$SESSTAT stat, V$STATNAME name WHERE  sess.SID = stat.SID AND stat.STATISTIC# = name.STATISTIC# AND name.NAME = 'session uga memory'order by value;
=== Large-Pool: an optional component of the SGA, for providing memory for backup and restores, and shared server processes.
--#################### WAITS/EVENTS : ##############################
	- V$SYSTEM_EVENT, V$SESSION_EVENT, and V$SESSION_WAIT , v$event_name
	-! ONLY okay if: timed_statistics parameter is set to true!!!
	-!! V$SESSION_WAIT   :lists the resources or events for which ACTIVE SESSIONS are waiting.
		The real-time information in this view provides you tremendous insight into what is holding up things in the database RIGHT NOW.
	- V$SYSTEM_EVENT   :lists total waits for an event since the Instance-Startup/System-wide /high-level view of waits 
	- V$SESSION_EVENT  :lists waits for an event by a SESSION
	- Deadlock-Events are rare and are usually a result of coding design issues and not high load! However, database performance is often highly dependent on the way in which applications are built. 
	---! starting wait-analysis:
		-- querying the V$SYSTEM_EVENT view to see if there are any significant wait events currently occurring in the database,
		- col event for a40 ; select event, TIME_WAITED/100, AVERAGE_WAIT/100 from v$system_event order by 3,2 ;
		Listing 19-25: Using the V$SYSTEM_EVENT View to View Wait Events:
		- unfiltered/grob:  select event, time_waited, average_wait from v$system_event group by event, time_waited, average_wait order by time_waited desc;
		-! filtered/relevants: (does not work eith spaces and %, so ignore SQL*Net-events ...):
			select event, total_waits,time_waited from V$system_event where event NOT IN 
			('pmon timer', 'smon timer', 'rdbms ipc reply', 'parallel deque wait', 'virtual circuit', '%SQL*Net%', 'client message', 'NULL event') order by time_waited desc;
			-- or the same as LIKE-statement (works with %):
			select event, total_waits,time_waited, AVERAGE_WAIT/100 from V$system_event where event NOT IN ('pmon timer', 'smon timer', 
			'rdbms ipc reply', 'parallel deque wait', 'virtual circuit', 'client message', 'NULL event' ) AND event not like '%SQL*Net%' order by  time_waited desc;
		- idle events (not signifikant):
		SELECT name FROM v$event_name WHERE name LIKE '%null%' OR name LIKE '%timer%' OR name LIKE '%SQL*Net%' OR name LIKE '%rdbms ipc%' OR name LIKE '%ispatcher%' OR name LIKE '%virtual circuit%' OR name LIKE '%PX%' OR name LIKE '%pipe%' OR name LIKE '%message%' OR name LIKE 'jobq%';
--###################### Statistics / Statspack/perfstat (see also sit-notes) : ###########
	--- analyse/tables statistcs online: (do compute , not estimate):
		- analyze table tab1 compute statistics;		
--###################### perf-diagnostics: ############################
=== Tracing/diagnose:
	- tracing queries: alter session set sql_trace=true; then query....; check udump/xxx.trc
	intrace file: PARSE #1:c=20000,e=3022,p=0,cr=0,cu=0,mis=1,r=0,dep=0,og=0,tim=4131708539275
	... mis=1 indicates a hard parse because this SQL isn't present in the library cache.
	  mis=0 indicating there wasn't a hard parse but merely a soft parse, which is a lot cheaper
	- trace-output evaluating/formating: tkprof <trace-file-name> ....
--################ packages/plsqls/...-perf:
=== statistics/gathers:
	- login as app-user and: execute DBMS_STATS.GATHER_SCHEMA_STATS (ownname => NULL, estimate_percent => NULL,  options => 'GATHER');
		set estimate to NULL to use "compute" (so no estimate)!
		check: select table_name, LAST_ANALYZED from user_tables order by 2;
--################ notes:
- you can dynamically change the settings of all the SGA components except the redo log buffer and the Java pool
- shared_pool: library cache and the data dictionary cache
--################# npad: #####################################
