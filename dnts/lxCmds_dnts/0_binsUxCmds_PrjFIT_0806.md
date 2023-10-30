__________________ ux-cmd-quickies/smallies- so for short notes / copy-paste / parat vorhanden...; mixed: ___________________
_____ so NOT-REF, just shorties; can/must be again repeated in their REF-notes, if needed _____________________
# ========== scp, distribuing specials:
for ii in $sshLoginWitdb ; do scp -p ./check_partitions_witsb.ksh  ${ii}:./pp1/bin/ ; done
# ========== ORAs-cmds , see also binrmt-admsrv for cuut-quickies:
# do sql-src on all servers per SSH:
for srv in $sshLoginAllServers ;  do ssh ${srv}  'export userWorkRoot=${userWorkRoot:-${HOME}/uu1} &&  . ${userWorkRoot}/constants.ksh && .  ${userShellFP} && ${userBinDir}/doSql_AllDBs_here.ksh '; done | tee list.log
# check all oraNet-Connections on the server:
for i1 in $dbNamesListApps ; do sidenv $i1 ; sqlpapp ; done
# - check all alerts for ORA- :
find /data/oraadmin/  -name "alert*" -exec grep -i ORA- {} \;
##________________________________________  ___________________________


#####  ==========  finds,..:
-! find in certain dirs from PREVIOUS find:    find /data/oraadmin -name arch_olds -exec find {} -mtime +0 -ls \;
# ========== find+grep:
grep 'uu1' except comments:     egrep -e '^ *[^#].*uu1.*'  *
# find-grep in notes or prj-dir,...:
cd $prjDir && find . -exec fgrep -il 'V$SESSION' {} /dev/null \;
# =========== loops:
# endless loop for tests..:
(( ii=0 )) ;   while true ; do (( ii+=1 )) ; print - "--- $ii : $( date ) ======="; sleep 3 ; done
# - FOR-loop for running DBs
for ins in $dbNamesList ; do  print  "====name:==$ins-" ; done
# - same with while over DBs:
    echo "$dbNamesListLines" | while read db ; do     print  "====name:==$db" ; done
# add date to all profile files
    for filex in profile.ig* ; do echo 'date' >> $filex ; done
# - renaming all .sh files in surrent Dir to .ksh:
for ii in *.sh ; do mv $ii      $( echo $ii | sed -e 's/\.sh/\.ksh/' ) ; done
#- FOR-loop for running DBs
for ins in $dbNamesList ; do  print  "====name:==$ins-" ; done
# ============ renaming files:
# - renaming all .sh files in surrent Dir to .ksh:
for ii in *.sh ; do mv $ii      $( echo $ii | sed -e 's/\.sh/\.ksh/' ) ; done
# ========= sshs:
# ssh-cmd on all xxx-servers, exp:
for srv in $sshLoginWitdb ; do ssh $srv 'hostname && grep aaa ${HOME}/scripts' ; done 
	/OR:
for srv in $sshLoginWitdb ; do  echo "-----SSHLogin as: $srv" ; ssh ${srv}  'currVerboseLevel=30  . ${HOME}/uu1/constants.ksh &&  . ${userShellFP} &&  initoraCompParam undo_retention' ; done
# --- same with while over DBs:
echo "$dbNamesListLines" | while read db ; do     print  "====name:==$db" ; done
# - converting ssh2-pub-key to openssh-pub-key with authentication: (if wanted, can add comments at the end)
    cd && cd .ssh && cp authorized_keys  authorized_keys.org.1 && ssh-keygen -i -f ./a101s01_ssh2.pub >> authorized_keys
# --- ssh-keys: converting ... :
	- converting ssh2-pub-key to openssh-pub-key with authentication: (if wanted, can add comments at the end)
	cd && cd .ssh && cp authorized_keys  authorized_keys.org.1 && ssh-keygen -i -f ./a101s01_ssh2.pub >> authorized_keys
# ========= solaris-quickies:
# --- kernels, shmmax of system for max avaialable for SGA_MAX_SIZE in ora:
cat /etc/system | sed '/^\*/d;/^ *$/d'  # --> set shmsys:shminfo_shmmax = xxx
grep -i shmmax /etc/system
- ports, which are in use by which app?: e.g  netstat -a | grep -i oracle ; /OR  netstat -an | grep 1521
- IO:  iostat -xtnc 2
# ========= TSMs-quickies:
- removing quickly backuped arch-files eg:
	 for _i in *__2*.arc ; do if dsmc q b $_i >/dev/null ; then echo "____REMOVING______ $_i" ; rm $_i ; else echo "_______NOT_REMOVING________ $_i" ; fi ; done
- dsmc q b -inac -su=y -date=3  -todate=2006-08-01   -optfile=/usr/bin/dsm-tdp-${ORACLE_SID}.opt  -pas=WITDB_TDP  "/${ORACLE_SID}/*"
- dsmc q b -ina "*" -su=y
- dsmc q o ; q se ;
- restore interactive:  dsmc restore "/home/project/*" -pick -inactive
- adm-capcity/occupation-check:  dsmadmc -id=witdb_tdp -pas=XXX  q  occ  witdb_tdp '/DWITSB*'
# ========= ps/ps-listings/... for ora ...:
    - OK: all-Running-Ora-Instance-Names in seperate lines:
    ps -ef | grep -i ora_pmon | grep -v grep| grep -v sed | sed  -e 's/^.*ora_pmon_//'
    - OK:  all-Running-Ora-Instance-Names in one line, seperated with space for eg. a FOR-loop:
    ps -ef | grep -i ora_pmon | egrep  -v 'grep|sed' | sed  -e '{s@^.*ora_pmon_@@;}' | sort | sed -n -e H -e '${x;s/\n/  /g;p;}'
    --old-ps-ora-listing:
    ps -ef | grep -i ora_pmon | grep -v grep| grep -v sed | sed -n -e 's/^.*ora_pmon_//' -e 'H' -e '${x;s/\n/  /g;p;}'
    /OR with egrep:
    ps -ef | grep -i ora_pmon | egrep  -v 'grep|sed' | sed -n -e 's/^.*ora_pmon_//' -e 'H' -e '${x;s/\n/  /g;p;}'
    /OR with shorter sed:
    ps -ef | grep -i ora_pmon | egrep  -v 'grep|sed' | sed -n -e '{s/^.*ora_pmon_//;H;}' -e '${x;s/\n/  /g;p;}'
    ( old: vorbereitung: ps -ef | grep -i ora_pmon | grep -v grep | sed -e 's/^.*ora_pmon_//'| sed -n -e 'H' -e '${x;s/\n/  /g;p;}'  )
# ======== several files replacing, manually / ue1/*.ksh handling e.g.

	_______:  in all uu1/*.ksh replacing manually:
for _i in *.ksh ; do sed -e '1s/^/# keep it compatible to BASH so far feasible, so not /' $_i > ${_i}.1 ; done
for _i in *.ksh ; do diff $_i  ${_i}.1 ; echo "========================================" ; done
for _i in *.ksh ; do mv  $_i ~/tmp/ ; mv  ${_i}.1 $_i ;  done
check them: for _i in *.ksh ; do echo "=========== ${_i} :" ; sed -n -e '1p' ${_i} ; done

	_______:  
##########################################################################################
########### earlier cmd-/sh-script-lines/taken-out/not-needed-now but ok: ##############
# ########### dbNamesLists: dynamic/process-based ones as var/array/lines/... : ###########################
# ----- building DBs-/Instances-Names twith different approaches: processes, oratab,...., also in differnt forms as array, vars,...:
#   - unfortunately in ksh88 array-handling is pretty poor and still not worked out as in ksh93; so not really used here:
#   - xxxList: process-bases ; xxxOratabX : oratab-based ; xxxxUserxxx: only DBs owned by the current user ; xxxLines: just for showing/printouts with lines instead space.
#   - could be added if neede: based on different user as ownr, eg: dbNamesListOra92 , xxxOra817 ; also other arrays; also ora-Home-Arrays from oratab,... .
#   a) oratab-tnries: see oraprof.ksh  (independent from user/sid/oraHome...)
#   b) processes-based-entries, ora_pmon_$SID:
dbNamesListLines=$( ps -ef | fgrep  ora_pmon | egrep  -v 'grep|sed' | sed  -e '{s@^.*ora_pmon_\([^\s$]*\).*@\1@;}' | sort )
dbNamesList=$( echo $dbNamesListLines )  # /OR:  | tr -s '\n' ' '  /OR:  | tr -s  '[:space:]' '[\n*]'
set -A dbNamesListA $dbNamesList  ; export dbNamesListA  # print out tha Array with: print "${dbNamesListA[*]} , ${#dbNamesListA[*]}"
#   - c) current-user-ora-processes-based-entries: ora_pmon owned by the CURRENT-user:
dbNamesListUserLines=$( ps -f -u $LOGNAME | fgrep  ora_pmon | egrep  -v 'grep|sed' | sed  -e '{s@^.*ora_pmon_\([^\s$]*\).*@\1@;}' | sort )
dbNamesListUser=$( echo $dbNamesListUserLines )
set -A dbNamesListUserA $dbNamesListUser ; export dbNamesListUserA  # print out tha Array with: print "${dbNamesListUserA[*]} , ${#dbNamesListUserA[*]}"
#_________ END-building dbNamesLists different variations__________
# ---------- setting ORA-Env for different versions:
# --- 1.each version its own script, based on fit-env/*.sh:
# in userShell.ksh:
ora9EnvFP=${userWorkRoot}/ora9Env.ksh
ora8EnvFP=${userWorkRoot}/ora8Env.ksh
# in profile.ksh:
[[ $oraVerDirSuffix = 8* ]] && . $ora8EnvFP
[[ $oraVerDirSuffix = 9* ]] && . $ora9EnvFP
# --- invoking fit-scripts depends on the version:
oraAppDir=${oraAppDir:=/app/oracle${oraVerDirSuffix}}
SCRIPTS_ENV_FILEPATH=${oraAppDir}/scripts/env/setenv_scripts.sh
SCRIPTS_ORACLE_ENV_FILEPATH=${oraAppDir}/scripts/env/setenv_oracle.sh
. $SCRIPTS_ENV_FILEPATH
. $SCRIPTS_ORACLE_ENV_FILEPATH
# - END old, Envs
# ----------- shifting all cmdLine-params:
set --  /OR:   shift $#   /OR: while (( $# > 0 )) ; do shift ; echo "shift---$#" ;  done
# --- bc variations with scale (ksh88 has no floating calculations):
- with coprocesses:  bc |& ; print -p "scale=2; $1" ; read -p ret ; print "======= $ret --" ;
- only-ksh-builtin (in ksh88, no floating):  { print "$@ == $(( $@ ))" ; } #:(in ksh88 no scale/floating possible; always truncated!!)
# --- reading commanLine params in userShell.ksh: but problems with scripts; so get them by export:
ORACLE_SID=${1:-${ORACLE_SID}}
TERM=${2:-${TERM}}  # !!-CheckIt!!
# --- verbose parameter according to the shell type (before firstline return for non.interactives in userShell.ksh):
#	if you want printouts ANYWAY, even in non-interactive, do: export doVerboseAllways=3  or higher
(( doVerbose=${doVerboseAllways:-3} ))
[[ ! -o interactive && -z $doVerboseAllways ]] && (( doVerbose=0 ))
# --- dbNamesList, running-Ora-list:
# first two USED variations, OK:
dbNamesList="`ps -ef | grep -i ora_pmon | egrep  -v 'grep|sed' | sed  -e '{s@^.*ora_pmon_@@;}' | sort | sed -n -e H -e '${x;s/\n/  /g;p;}' ` "   # ALL Ora-Instances-list
dbNamesListUser="`ps -f -u $LOGNAME | grep -i ora_pmon |  egrep  -v 'grep|sed' | sed  -e '{s@^.*ora_pmon_@@;}' | sort | sed -n -e H -e '${x;s/\n/  /g;p;}' ` " # USER-Ora-Instances-list: only of logged USER, not all
#- new independent of ora_pmon-column-position: (MUST grep -v sed, too, as following)
ps -ef | fgrep  ora_pmon | egrep  -v 'grep|sed' | sed  -e '{s@^.*ora_pmon_\([^\s$]*\).*@\1@;}' | sort
ps -ef | grep -i ora_pmon | egrep  -v 'grep|sed' | sed  -e '{s@^.*ora_pmon_\([^\s$]*\).*@\1@;}' | sort   # independent of position of ora-columns list , seperated yet with \n
#- same with awk:
ps -ef | grep ora_pmon | grep -v grep | awk '{print $NF}' |awk -F"_" '{print $3}'  # same with awk
ps -ef | grep $USER | grep ora_pmon | grep -v grep | awk '{print $NF}' |awk -F"_" '{print $3}'  # same with awk:
# ---
# ----------- old server list:
# uxServersWitdb="witdbb2-eng1.rz.finanzit.sko.de  witdbb3-eng1.rz.finanzit.sko.de  witdbb4-eng1.rz.finanzit.sko.de  witdbp2-eng1.rz.finanzit.sko.de  witdbp3-eng1.rz.finanzit.sko.de  witdbp4-eng1.rz.finanzit.sko.de"
# uxServersWitsb="witsbt2.t-zssb.finanzit.sko.de  witsbt1.t-zssb.finanzit.sko.de  witsbt2.t-zssb.finanzit.sko.de"
# uxServersGatex="gatexb1-eng1.rz.finanzit.sko.de  gatexb2-eng1.rz.finanzit.sko.de  gatexp1-eng1.rz.finanzit.sko.de  gatexp2-eng1.rz.finanzit.sko.de"
# uxServersFonet="fonetb1-eng1.rz.finanzit.sko.de fonetp1-eng1.rz.finanzit.sko.de"
# uxServersDBATests="admsrv1.rz.dvg.sko.de  $uu1RefServer"
# uxServersAll="$uxServersWitdb  $uxServersWitsb  $uxServersGatex  $uxServersFonet "  # not including: $uxServersDBATests"
