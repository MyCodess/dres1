##--!!-Check your PS-Profile-Path with:  $PROFILE bzw. all-profiles-pathes-with:  $PROFILE  | Select-Object * #-and put this file there !
##-- https://learn.microsoft.com/en-us/windows/terminal/tutorials/new-tab-same-directory  :  Opening a tab or pane in the same directory in Windows Terminal :
function prompt {
    $loc = $executionContext.SessionState.Path.CurrentLocation;
    $out = ""
    if ($loc.Provider.Name -eq "FileSystem") {
        $out += "$([char]27)]9;9;`"$($loc.ProviderPath)`"$([char]27)\"
    }
    $out += "PS $loc$('>' * ($nestedPromptLevel + 1)) ";
    return $out
}
##-----------------------------------------------------------------------

################### evv-call/alias PS1 : #########################################
##--OK1:   .    ${env:USERPROFILE}\ofc1\bin\prof1.ps1
##--OK2:  function sus1() { .  ${env:USERPROFILE}\ofc1\bin\prof1.ps1 }     ##--!!-MUST call as sourced, so:  .  sus1
##--OK:   
Set-Alias sus1  ${env:USERPROFILE}\ofc1\bin\prof1.ps1  ##--!!-MUST call as sourced, so:  .  sus1
##--  .  sus1
###################################################################################
