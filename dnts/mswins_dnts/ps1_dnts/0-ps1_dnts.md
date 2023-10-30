______________________ powershell 5.1 win10 dnts /_200800 :   ____________________________________

    - _RF also : powershell101.pdf , and https://docs.microsoft.com/en-us/powershell/


#####  ==========  pre-start:
	- Update-Help  ##--Downloads and installs the newest help files on your computer/System/OS ! so requires Admin! see:  help  Update-Help
	- if No-Admin, then: Save-Help  dir1  ## saves helps into dir1 ! but Update-Help  saves them into the system, accessible to all ...)
	- get-help -online XX  ##--opens browser and shows online-hlp to XX
##________________________________________  ___________________________


#####  ==========  CTs-powershell :

	ct1808--172-173--RegulaereAusdruecke-in-PowerShell.pdf
	ct1806--168-171--Loslegen-mit-PowerShell-Teil2-Scripting.pdf
	ct1802--166-171--Loslegen-mit-PowerShell-Teil1.pdf
	-! see /up1/w/docs/CTs/CT_Articles_Topics/CT_PowerShells 
##________________________________________  ___________________________


#####  ==========  Allg-nts:

	_______:  PS-Allg:
	- ! TWO variations of PS:  Windows PowerShell (closed-source, is on Windows)vs.  PowerShell Core  (opensource, basis for win-PS!, https://github.com/PowerShell/PowerShell), so like Fedora-Redhat !
	- powershell is full case-INsensitive !
	- alle Cmdlets als Return/Ausgabe eigentlich keinen Text liefern, sondern Objekte !
	- Version??:   $PSVersionTable  ##--it printouts version-infos of your PS !
	
	_______:  CmdLets-Allg:
	-!! Cmdlets return NO-text, but Objects !!
	- !!! Listing/showing all properties/members of returned-object os any CmdLet use Get-Member !! eg:   Get-ChildItem  dir1  | get-member | sort
##________________________________________  ___________________________


#####  ==========  helps:
	https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/get-help
	- Get-Help  == help == man    ##-- help is a function for Get-Help , and man is alias of help !
	- powershell is full case-INsensitive !
	- offline/local helps are NOT there! get them with:  Update-Help   ##--/OR use online-helps:
	- eg-online/browser:   get-help  Get-Alias -online    ##--opens browser to the help-page !
	- Get-Help  *    ##--shows listing of ALL available help-pages !
	- ! return-value of Get-Help is NOT string, BUT Object! so to eg grep its output for certain word, must convert into stream:
	- grep helps returned-object (with Select-String):    Get-Help Add-Member -Full | Out-String -Stream | Select-String -Pattern Clixml
	- man -k (all help-pages containing certain word) : Get-Help -Name  myword1  ##--When you enter a word that doesn't appear in any article title, Get-Help displays a list of articles that include that word.   see https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/get-help	
	- -ShowWindow   ##--show help in the extra window with search/....; eg   get-help  Get-Service  -ShowWindow
	_______:  
	Get-Help -Name Get-Command -Full       ##--eg:   get-help  Get-Service  -Full  ##oder mit -Name ....
	Get-Help -Name Get-Command -Detailed   ##--eg:   get-help  Get-Service  -Detailed
	Get-Help -Name Get-Command -Examples   ##--eg:   get-help  Get-Service  -examples
	Get-Help -Name Get-Command -Online     ##--opens browser and shows online-help to 
	Get-Help -Name Get-Command -ShowWindow ##--use instead :  help Get-Command -Full | Out-GridView
	Get-Help Format-Table -Parameter GroupBy  ##--/OR *

	_______:  "about_*"-files explain the concepts of ...  (see Get-Help page!)
	- Conceptual help articles in PowerShell begin with about_, such as about_Comparison_Operators. To see all about_ articles, type Get-Help about_*. To see a particular article, type Get-Help about_<article-name>, such as Get-Help about_Comparison_Operators.
	- listing of all about-helps:    help about_*
	- eg:   help about_Wildcards

	_______:  * in help xx*yy (placeholders as: * ...)
	help *process*   ##ok but "*" not required.  Get-Help automatically adds the wildcard characters behind the scenes; BUT NOT added if you have a * somewhere !eg: help pro*cess
##________________________________________  ___________________________


#####  ==========  Comparison-Operators (eq , lt, gt, ...):
	help about_Comparison_Operators
##________________________________________  ___________________________


#####  ==========  Arithmetics-OPs-builtin:
	help about_Arithmetic_Operators
##________________________________________  ___________________________


#####  ==========  Variables:
    - listing/show ALL variables (== set):  Get-Variable    ##-without-args ! NOT-env-vars, but vars are printed out! env-vars-listin (== export) with:   ls env:
	- object-var:   $d1 = Get-Date ##--!! return value of ALL Cmdlets are Objects, so NOT-text/numbers/...! so eg:   echo $d1.DayOfWeek   $d1.Year
	- value-var /direct-value-assigment to a var:  $d2 = (Get-Date).Year  ##--so $d2 contains ONLY the property Year of the date-object ! 
##________________________________________  ___________________________


#####  ==========  OPeratos-basics:
	-  ForEach-Object / Alias foreach / Alias "%"  ##--eg:   $v1,  $v2, $v3 | %  { write "____  $_  _____" }
##________________________________________  ___________________________


#####  ==========  OS-Services on PS1:
-!! see  powershell101.pdf--CH03 , eg:
	 Get-Service -Name w32time | Get-Member
	 Get-Service -Name w32time | Get-Member -MemberType Method  ; ##--and then eg stop it:
	 by its method:   (Get-Service -Name w32time).Stop()
	 /OR by cmdlet:    Get-Service -Name w32time | Start-Service -PassThru
	 - running-procs-listing:    Get-Service  | where-object  status -eq running   ##--bzw.-mit-alias:  gsv | ? Status -eq Running
##________________________________________  ___________________________


#####  ==========  Admin-OS-cmds-PS1:
	--- Services/Dienste:
	- Listing ALL services on current PC:   get-service   ##-- help  get-service
	- Restart-Service     Resume-Service     Set-Service     Start-Service     Stop-Service
	- eg:  get-help Get-Service -examples
	- 
##________________________________________  ___________________________


#####  ==========  Aliases:
	 Get-Alias ,  Set-Alias
	 - aliases ONLY to a cmdlet, script, function, or executable file, BUT NOT-with-params! if params, then use a function for that and then alias to that function!!
	 - show all aliasese:     Get-Alias
	 get-alias   ls    ##--shows definition os ls alias
	 get-alias  -definition   Get-ChildItem   ##--shows all aliases of  Get-ChildItem
	 - * also works:
	 Get-Alias   c*           ##--show all aliases stating with c !
	 Get-Alias   -definition   Get-Chil*  ;  Get-Alias   -Definition    get-c*      ##--show all aliases based on get-c* ....
	 full-alias-infos-formatted:    Get-Alias -Name dir | Format-List -Property *   ##--ge-alias retunrs really no text, but an aliasinfo-object !
##________________________________________  ___________________________


#####  ==========  Registry-Handling with PS1 :
	- help registry ;
	- get-psdrive ; 
	- Registry is handeled like Directory-Tree ! ##eg:  cd "HKCU:\Control Panel\Desktop\" ; dir ;  Get-ItemProperty xxx ; Set-ItemProperty  xxx ;
	- list-all-properties/entries of a Reg-key:    Get-ItemProperty     HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem  [ -Name LongPathsEnabled ] 
	- set-an entery/property in REG:   Set-ItemProperty  -Path   HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem  -Name LongPathsEnabled  -Value  $true

##________________________________________  ___________________________


#####  ==========  ENV-vars , vars :
	- ! https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables
	- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_variables
	- !! DIFF:  envVars  <---> Variables !
		-eg: $HOME is NOT an envVar, but just a normal Variable (as default set in win-reg!)
		- listing all envVars:   ls  env:  ##-bzw:  Get-ChildItem  env:
		- listing all Variables of the current shell:  Get-Variable ; eg:  Get-Variable p*   ##-shows all vars starting with p (not-envVars!) !
	- value of a envvar? , simply:  $VAR1  ; eg just: $PSHOME ...
	- ls env:   #-bzw.   dir env:  ##==export ; /OR in win-cmd: SET ; so print ALL envVars ! both ls/dir are aliases of Get-ChildItem
	- ls env:ps*           ##--show all envvar PS*
	- ls $env:ps*          ##--ls of all envVars starting with ps...  (case-INsensitive!)
	- $env:path   ##==echo $PATH
##________________________________________  ___________________________


#####  ==========  IDE/Tools/Utils for PS!:   MS-ISE or MS-Code :

	_______:  IDEs for PS1:
	- MsWIn "Integrated Scripting Environment“ : std in win10 there ! : free
	- MS "Visual Studio Code" mit der dafür verfügbaren PowerShell-Erweiterung : free
	-! DIFF:  MS-"Visual Studio Code" – oder kurz Code – ist nicht zu verwechseln mit Microsofts großer Entwicklungsumgebung Visual Studio: Es ist um Größenordnungen schlanker, schneller installiert und gestartet und steht unter einer OpenSource-Lizenz.
	- COMP:  Code: beeter debugging/watchPoints  ,  ISE: integrated-cmdlets-listing+params !
##________________________________________  ___________________________


#####  ==========  scriptings:

	- ! help  about_Scripts  ## https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_scripts?view=powershell-7.3
	- sourcing / dot-sourcing of scripts with just:  .  sc1.ps1

    _______:  $0 / myname1,mypath1 / myOrgCall/  $x_params:
    - $0_FP /my_FP  :  $MyInvocation.MyCommand.Path
    - $0_DP /my_DP  :   Split-Path $MyInvocation.MyCommand.Path -Parent
    - more attribs/members:   $MyInvocation | select-object * ; $MyInvocation.MyCommand |  Format-List  -Property * ;

##________________________________________  ___________________________


#####  ==========  profiles of PS:

    _______:  !! check-in-PS with:    $PROFILE | select-object *   
    - ! the  "PROFILE"-var (NOT envVar ! so showing with:  Get-Variable  p*  ##NOT-with  ls env:p* !) , see help about_Profiles
	- ! $PROFILE variable stores the path to the "Current User, Current Host" profile. The other profiles are saved in note properties of the $PROFILE variable.
	- ! showing all profiles:   $PROFILE | Select-Object *
	- check if: is  "All Users, All Hosts" profile has been created on the local computer:    Test-Path -Path $PROFILE.AllUsersAllHosts

    _______:  Lv13-WinHome-Profiles :
    $PROFILE | select-object *   ##--:
    AllUsersAllHosts       : C:\Windows\System32\WindowsPowerShell\v1.0\profile.ps1
    AllUsersCurrentHost    : C:\Windows\System32\WindowsPowerShell\v1.0\Microsoft.PowerShell_profile.ps1
    CurrentUserAllHosts    : C:\Users\a1\Documents\WindowsPowerShell\profile.ps1
    CurrentUserCurrentHost : C:\Users\a1\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1
    Test-Path -Path $PROFILE.AllUsersAllHosts   ##---> false

    _______: OL_docs (but NOT-the case on Lv13-Win-Home): 
	- ! help  about_Profiles   ##- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_profiles
	- ! remote sessions:   PowerShell profiles aren't run automatically in remote sessions !!
	- Current User, All Hosts Windows :		$HOME\Documents\PowerShell\Profile.ps1
	- Current user, Current Host Windows :	$HOME\Documents\PowerShell\Microsoft.PowerShell_profile.ps1
	- All Users, All Hosts Windows  : 		$PSHOME\Profile.ps1
	- All Users, Current Host Windows : 	$PSHOME\Microsoft.PowerShell_profile.ps1
##________________________________________  ___________________________

#####  ==========  functions :

	man  about_Functions
	https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_functions?view=powershell-7.3
	- listing all funcs in current scope (using function: drive):   ls function:  ##--bzw.  Get-ChildItem function:
	- display the commands in the Help function that comes with PowerShell, type:  (Get-ChildItem function:help).Definition
	- ! see also:  about_Quoting_Rules
	
	--- params of functiions:
	- ! help about_Functions_Advanced_Parameters
##________________________________________  ___________________________

#####  ==========  CmdLets-/Modules-nts:
	----- Get-ChildItem nts:
	- ! Get-ChildItem does NOT display empty directories.
	- !!! listing of all members (Properties + Methods) of its retuned objects:   Get-ChildItem  myFiles  | get-member | sort
	- !! if using -Name , then it return-object is String (check it with |get-member) ! so, you may sort it with |Sort-Object -Name !! but just with |sort-Object !!
	- its return-object-types depends on the Provider (Filesystem, Registry, ...!?)!
	- in case of normal files its return object ist of: System.IO.FileInfo
	- in case of normal files its return object ist of: System.IO.DirectoryInfo
	- for -filter and -include see also:  https://tfl09.blogspot.com/2012/02/get-childitem-and-theinclude-and-filter.html
	- use -filter  if possible instead -include or pipe to Where-Object (?)  !
 	- -Include switch is only active if you are also using the –Recurse parameter!
	- -filter ist faster than -include ! -filter is provided by the Provider (eg FileSystem-Provider), but -include is done by PS itself !
	- ! -filter *.txt  also means/includes *.txt.and.more  ! so basically as regexp with * !
##________________________________________  ___________________________

#####  ==========  Properties + Methods (Members)-Listings,querys of an object/CmdLet/... :

    --- DIFF : members > properties : 
        - Members include both properties and methods of an object !
        - so to introprospect an obj: 1) xxx | get-member   #-listing-of-all-props+methods   2) Format-List -Wrap ... #-listing of their Names+Values! see below eg !
	--- listing ALL members (properties, methods,...) of an obj/cmdlet/func/... :   help  about_properties :
	- listing ALL Members Names (properties + Methods + ..).. of a CmdLet:   Get-ChildItem  | Get-Member
	- listing ALL properties-Names of a CmdLet:   Get-ChildItem  | Get-Member -MemberType Property
	- listing ALL properties-Names AND their VALUES of an object, eg for prompt-func:  Get-Command   prompt   -CommandType Function  | Format-List  -Property *
##________________________________________  ___________________________

#####  ==========  
##________________________________________  ___________________________

#####  ==========  
##________________________________________  ___________________________



################################### 1coll cmds/cmdlets-onliners,....: ##################################################
- DIR-listing size-sortiert:   dir | sort Length -Descending


