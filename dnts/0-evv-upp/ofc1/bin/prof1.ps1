echo "___ prof1__STA1__ ____"
##--I- add this line in Win-PS-Profile:   function sus1() { .    ${env:USERPROFILE}\ofc1\bin\prof1.ps1 }   ##--inq-your-PS-Profiles: $PROFILE bzw.-all:  $PROFILE | select-object *  


#####  ==========  Env-OS/Sys : #######################################################
$myFP11 = $MyInvocation.MyCommand.Path
$myDP11 = Split-Path $myFP11 -Parent
if (!${env:HOME})  { $env:HOME = "${USERPROFILE}" } ; if (${env:HOMESHARE})  { $env:HOME = "${env:HOMESHARE}" }
##--OK1:  if (!${env:HOME})  { $env:HOME = "${env:HOMEDRIVE}${env:HOMEPATH}" } ; if (${env:HOMESHARE})  { $env:HOME = "${env:HOMESHARE}" }
##________________________________________  ___________________________


#####  ==========  Env-evv/upp: #######################################################
##----- ENVs-upp:
$env:q_UPP_DN="up1"
$env:q_UPP_DP="${env:HOME}\${q_UPP_DN}"   ##-- ; $env:q_UPP_DP="${env:HOMESHARE}\up1" ;
$env:TP1DP="T:\t1_RF"
$env:vaarAuDP="${env:TP1DP}\varu\varau"
##________________________________________  ___________________________


cd $myDP11 ; .   .\funcs1.ps1  ; cd ~ ;

$evv_done1 = 1
echo "___ prof1__END1__ ____"

