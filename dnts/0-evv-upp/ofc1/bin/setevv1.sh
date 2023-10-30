#!----/bin/bash

##-------- append follwoing lines unCommented in cyg to your .bashrc , eg in:   [/cygwin]/home/a1
################# 1evv-addies in  cyg/mswins : ####################################
##__UnComment:   source  "${USERPROFILE}/ofc1/bin/setevv1.sh"
###### __1END__ # 1evv-addies in  cyg/mswins : ####################################


############################# 1evv-addies : ####################################
shopt  -s  nocaseglob     ##--case-INsensitve path handling on mswins!
shopt  -s  nocasematch
##__?? error!?!?!:  declare -xi  q_profsDebug11=20 ; export   q_profsDebug11=20
##-- export  q_Host1full=$(hostname)
export  USER=${USERNAME:="userXX"}
export  HOME=${USERPROFILE}     ##--OK1:  export HOME="${HOMEDRIVE}/${HOMEPATH}"
export  q_Host1full=2310oh1  ##2310-ofc1-host1--Dev_VDI_1
source  "${HOME}"/up1/.ev13/etc/profile.sh    ##--did-not-work:  "C:\Users\DKX8H1N\up1\.ev13\etc\profile.sh"

