##_______________ evv-PS1: funcs/cmdlets/.... __________________________

##############################  Lx-cmds-PS1 : ################################
##--!! check also the defaul-ps-aliases for many Lx-cmds !

##----- afg, ... :
function afg ([parameter(mandatory, HelpMessage="name-of-Alias/Func-to-search")]  [string]$p1 )  { Get-Command  -Name "*${p1}*"  -ListImported  -CommandType  Alias,Function   | Sort-Object -Property Name |  Format-Table -Property Name,Parameters,Definition  -Wrap }

##----- ENVs, exports-funcs,...
function expg  ([parameter(mandatory, HelpMessage="ENV-search-pattern")]  [string]$p1 )  { Get-ChildItem  "env:*$p1*" }

##----- ls/ll :
function  ll   ([string]$path1 = ".")  { Get-ChildItem  $path1 | Sort-Object -Property Name }
function  lla  ([string]$path1 = ".")  { Get-ChildItem  $path1 -Force | Sort-Object -Property Name }

##----- cd:
function cdll   ([string]$path1 = "$HOME")  { Set-Location "$path1" ; ll }
function cdlla  ([string]$path1 = "$HOME")  { Set-Location "$path1" ; lla  }

##------- finds: 
function  find1     ([parameter(mandatory, HelpMessage="Start-Dir")]  [string]$path1 = ".")  { Get-ChildItem  -Path $path1 -Recurse  -Name | Sort-Object }
function  findls1   ([parameter(mandatory, HelpMessage="Start-Dir")]  [string]$path1 = ".")  { Get-ChildItem  -Path $path1 -Recurse | Sort-Object -Property Name | select @{Name="KB Size";Expression={ "{0:N1}" -f ($_.Length / 1KB) }}, FullName, LastWriteTime; }
function  findin1   ([parameter(mandatory, HelpMessage="Start-Dir")]  [string]$path1, [parameter(mandatory)]  [string]$pattern1)  { Get-ChildItem  -Path $path1 -Recurse  -Name -filter *${pattern1}* | Sort-Object }
function  findind1  ([parameter(mandatory, HelpMessage="Start-Dir")]  [string]$path1, [parameter(mandatory)]  [string]$pattern1)  { Get-ChildItem  -Path $path1 -Recurse  -Name -filter *${pattern1}* -Attributes  Directory | Sort-Object }
##--ok1: function  findls1   ([parameter(mandatory, HelpMessage="Start-Dir")]  [string]$path1 = ".")  { Get-ChildItem  $path1 -Recurse  -Name -Length | Sort-Object -Property Name }

##------- greps-finds:
function  grepi-r  ([parameter(mandatory, HelpMessage="Start-Dir")]  [string]$path1, [parameter(mandatory)]  [string]$pattern1)  { Get-ChildItem  -Path $path1 -Recurse  | Sort-Object | Select-String -Pattern "$pattern1" }

##------- miscs-basics:
#-setting the prompt to open new tabs in the same DIR as prev-tab:
##__  ##-- https://learn.microsoft.com/en-us/windows/terminal/tutorials/new-tab-same-directory  :  Opening a tab or pane in the same directory in Windows Terminal :
##__  function prompt {
##__  	$loc = $executionContext.SessionState.Path.CurrentLocation;
##__  	$out = ""
##__  	if ($loc.Provider.Name -eq "FileSystem") {
##__  		$out += "$([char]27)]9;9;`"$($loc.ProviderPath)`"$([char]27)\"
##__  	}
##__  	$out += "PS $loc$('>' * ($nestedPromptLevel + 1)) ";
##__  	return $out
##__  }
##__  ##-----------------------------------------------------------------------
##--evv1-OK1:  function prompt { (Get-Location).ProviderPath + ' : '}
#-ok1:  function prompt { (Get-Location).path + ' : '}
#-ok1:  function prompt { 'ev1: ' + (Get-Location) + ' : '}

##------- ps :
function ps-cpu { get-process |Sort-Object -Property CPU | Format-Table }  ##--: ps sorted by CPU-usage

##------- pythons/devels:
#--env-py:
$env:pyvar_DP="${env:vaarAuDP}\py1var"
$env:PYTHONPYCACHEPREFIX="${env:pyvar_DP}\pycache1"
#--funcs-py:
function  pydoc1  ([parameter(mandatory, HelpMessage="Py-Module-Name")]  [string]$module1 )  { python -m pydoc $module1 }


############################## funcs3: longer, more ################################


##----- funcs-upp:
function cdupp { cdlla "$env:q_UPP_DP" }


#################################################################################################
echo "___ funcs1__END1__ ____"
