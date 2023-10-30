export myname11="${BASH_SOURCE[0]##*/}" ;
##--ReDo:  q_pls1  "${myname11}" ;

##-- OS-/syys-Tags for syys-dirs/L1NW-PCs,...  ##--I- diff: syys <--> OS
export  q_osTg=oh1             ##-- ##2310-ofc1-host1--Dev_VDI_1      #- OS-short-abbrev-name : used for q_syysTg...
export  q_osRelTg="$q_osTg"            #- OS-longname: in case of archlinux, due to rolling-system, just your OS-tg, otherwise: distro.ver.arch--at-first-install-time!! not the current-updated/upgraded-one !! ArXis rolling, so NO-release-No, here jsut Kernel-No during install!
export  q_diskTg=             #- OS-short-abbrev-name : used for q_syysTg...; does NOT have to be realy Disk-Part! is just yout TAG !
export  q_syysNoTg=2310               #- MY-assigned-No, just randomly for identifying my system; never changes! usu. the date of very FIRST install YYMM !
export  q_syysCatTg=RF                #- just flag, not used yet. choice: RF, CP, TE (testie), DM (dummy)
export  q_syysTg=${q_syysNoTg}${q_osTg}    #--UNIQUE-ID of a syys !! usu. YYMM<osTg> , as 2209arx
##-echo "   _______  q_syysTg: $q_syysTg"

#####  ==========  ofc1pc1-addies/settings:
: ${USER:="DKX8H1N"}


##__ q_ple1  "${myname11}---${q_syysNoTg}${q_osTg}_${q_Hostname}_${q_diskTg}---${q_osRelTg}"
##--ReDo:  q_ple1  "${myname11}" ;

