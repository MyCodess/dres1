##_______________________ lx-ps1-equis/similars.... _______________________


#####  ==========  LxCmds-ps1-Similars (Esel-Brücken):

	- ! get-aliases (see below, Listing!)  :  cat, cd, chdir, clear, cp, curl, diff, echo, h, history, kill, lp, ls, man, md, mount, mv, ps, pwd, ren, rmdir, set, sort, tee, type, wget, where, ...
	- ">" / ">>" ==  same  /OR:  Out-File  ,eg: Get-Alias | Out-File -FilePath .\Alias.txt
    - comments-long-multiLines: <# ..... #>
    - afg  (listing of all functions/aliases/cmdlets/..):  Get-Command  -type Function | Alias ... [-ListImported] 
        - ls function: ;  ls function:f* ;
        - ls alias:    ;   ls alias:l*   ;
        - ! Get-Command   -Name *cdll*  -ListImported  -CommandType  Alias,Function  ##--I: -Name accepts globbing/regexp in get-command !!
        - list-only-session-imported-functions+Aliases (egi from user-profile/-script):  Get-Command  -ListImported -type function,Alias
        - user-defined-functions-listing:   Get-Command  -ListImported -type Function
        - Get-Command -Type Cmdlet | Sort-Object -Property Noun | Format-Table -Property Name,Module -Wrap
        - all-props-listed-WRAPED-of a function...:  Get-Command  -ListImported -type function -Name ll | Format-Table  -Wrap -Property *
	- cat  ==  cat alias Get-Content
	- cd : alias -> Set-Location : !works also for Registry/NW/... !
	- du /sizes-of-files/folders :
		- ! sysinternals: du , https://learn.microsoft.com/en-us/sysinternals/downloads/du !
		-  Get-ChildItem  -Recurse | Measure-Object -Property length -Minimum -Maximum -Sum -Average   ##-ouput average/sum/max/min of current-tree !
	- df  ==  Get-PSDrive :
		- it lists NOT-only-filesystems, but also other providers as: Registry/PS/Aliases/ENV/...
		- Get-PSDrive C  #-NOT C: ! see property Name in its output !  bzw.  Get-PSDrive -Name C
		- list ONLY FILESYSTEMS!  :  Get-PSDrive -PSProvider FileSystem
    - export:
        - listing all envVars:   ls env:
        - listing all envVars of H*  :  ls env:H* , ...
		- expg ==  ls env:*xx*  ; /OR longer: ls env:  | Out-String  -Stream |  Select-String  -Pattern  "C:\\Users\\a1"    ##--pattern is regexp ! so not-working with single \ here in eg !! \ mus be escaped 
	- find:
		- find dir1 	=   Get-ChildItem . -Recurse  -Name
		- findin dir1  xxx  =  Get-ChildItem dir1 -Recurse  -filter *xxx* -Name
		- findind dir1 xxx 	=  Get-ChildItem dir1 -Recurse  -filter *test* -Name  -Attributes  Directory
	- grep	==  Select-String  /OR  find.exe + findstr.exe  win-onboard-cmds! :
		--- findstr.exe /? :  ##--find.exe gibt es auch, but older/weak/...
			- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/findstr
			- ! grep -R -i -l -E -v ==  findstr  /S /i /M /R /V ; fgrep == findstr /L  #--Literally
			- ! findstr komischer Syntax/verhalten for its path-param:  findstr /spinM  mypy  * ##--so-OK: * /OR .\* /OR *.*   #-BUT-NOT-OK:  .  /OR .\.  ! Not working !
			- findstr stronger/neuer than find ! win-find-cmds are grep !! and not Lx-finds !! 
 			-  find : !! MUST use """search-string""" to work !! funny!  eg:  C:\WINDOWS\system32\find.exe  /I  """col"""   .\etcau\config\xfce4\teminal_nts.txt
		--- Select-String :
		- eg:  expg ==  ls env:  | Out-String  -Stream |  Select-String  -Pattern  "C:\\Users\\DKX8H1N"    ##--pattern is regexp ! so not-working with single \ here in eg !! \ mus be escaped 
		- Because the Get-Help cmdlet generates a MamlCommandHelpInfo object, not a string, you have to use a cmdlet that transforms the help topic content into a string, such as Out-String or Out-File.
		- eg:  Get-Alias  | Select-String  cd 
		- eg:  Get-Help  Add-Member -Full | Out-String -Stream | Select-String -Pattern Clixml
		- | grepi , so piping to grep (usu. must convert objects into strings):   Get-Alias  | Out-String -Stream |   Select-String  variable
		- grepi -R  bzw. find path1 | grepi str1  ==  Get-ChildItem -Path C:\Windows\System32\*.txt -Recurse | Select-String -Pattern 'str1'
	- less ==  eg:  Get-Help Format-Table | Out-Host -Paging
	- man -k (all help-pages containing certain word)  ==   Get-Help -Name  myword1     ##--When you enter a word that doesn't appear in any article title, Get-Help displays a list of articles that include that word.  
	- mount :
		- listing of mounted parts (lx: mount):  Get-PSDrive
		- new mount-points/parts:    mount -> New-PSDrive
	- prompt  :  is function prompt ; show it:  Get-Content  Function:\prompt ; set-it:  function prompt { (Get-Location).path + ' : '}
	- pushd/popd  :   Push-Location ; then: Get-Location -stack ;  Get-Location -StackName Stack2 ; ...
	- pwd  :
		- Get-Location alias  pwd,  $PWD.path  : ! also for other providers as Registry, NWs, ....:
		- query Reg:   Get-Location -PSDrive HKLM
		- query other pathes:  Get-Location -PSDrive C   ##-! not C: ! get listing of PSdrives with Get-PSDrive
		- Get-Location -PSProvider Registry
	- sort  ==  Sort-Object (Alias: sort)   ##--eg:  dir | sort Length -Descending
	- tree ; tree /f (show also files)
	- type  :
        - type func1 eg:   (Get-Command find1).Definition
		- Get-Command  ,eg: (Get-Command   prompt   -CommandType Function).Definition
		- Get-Content  ; also for other things eg (show prompt function): Get-Content  Function:\prompt
	- wc -l /... :   Get-Content C:\Temp\tmp.txt | Measure-Object -Character -Line -Word
	
	--- Shell-Syntax:
	- if [condition] then something fi  ==	if (condition) { something }
	- test -e file  ==  Test-Path file
	- for ((i=0; i < 10; i++)) ; do echo $i ; done  ==	for ($i=0;$i -lt 10; $i++) { echo $i }	
##________________________________________  ___________________________



#####  ==========  aliases-defaults-MsWin-PS:
Alias           cat -> Get-Content                                                                                     
Alias           cd -> Set-Location                                                                                     
Alias           clear -> Clear-Host                                                                                    
Alias           clhy -> Clear-History                                                                                  
Alias           cls -> Clear-Host                                                                                      
Alias           copy -> Copy-Item                                                                                      
Alias           cp -> Copy-Item                                                                                        
Alias           curl -> Invoke-WebRequest                                                                              
Alias           del -> Remove-Item                                                                                     
Alias           diff -> Compare-Object                                                                                 
Alias           dir -> Get-ChildItem                                                                                   
Alias           echo -> Write-Output                                                                                   
Alias           h -> Get-History                                                                                       
Alias           history -> Get-History                                                                                 
Alias           kill -> Stop-Process                                                                                   
Alias           lp -> Out-Printer                                                                                      
Alias           ls -> Get-ChildItem                                                                                    
Alias           man -> help                                                                                            
Alias           md -> mkdir                                                                                            
Alias           mount -> New-PSDrive                                                                                   
Alias           move -> Move-Item                                                                                      
Alias           mv -> Move-Item                                                                                        
Alias           ps -> Get-Process                                                                                      
Alias           pushd -> Push-Location                                                                                 
Alias           pwd -> Get-Location                                                                                    
Alias           ren -> Rename-Item                                                                                     
Alias           rm -> Remove-Item                                                                                      
Alias           rmdir -> Remove-Item                                                                                   
Alias           sc -> Set-Content                                                                                      
Alias           set -> Set-Variable                                                                                    
Alias           sort -> Sort-Object                                                                                    
Alias           tee -> Tee-Object                                                                                      
Alias           type -> Get-Content                                                                                    
Alias           wget -> Invoke-WebRequest                                                                              
Alias           where -> Where-Object                                                                                  
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


############################# coll equiv-lx-ps : ###############################################################################
========== NWs:
https://www.netscylla.com/blog/2019/11/24/Linux-to-Powershell-CMD-Cheatsheet.html :
-- Bash/Linux	PowerShell
ifconfig	Sort InterfaceIndex | FT InterfaceIndex, InterfaceAlias, AddressFamily, IPAddress, PrefixLength -Autosize
ping	Test-NetConnection
nslookup	Resolve-DnsName  ## Resolve-Dnsname -Name -Type <a/cname/txt/aaaa>
route	Get-NetRoute  ## Get-NetRoute -Protocol Local -DestinationPrefix 192.168*
route add -net	New-Netroute -DestinationPrefix “172.16.8.0/24” -InterfaceIndex 16 -NextHop 192.168.2.2
netstat -an	Get-NetTCPConnection | ? State -eq Listen  ##  Get-NetTCPConnection | ? State -eq Listen | ? LocalAddress -notlike “::*”
traceroute	Test-NetConnection www.microsoft.com –TraceRoute  ## Test-NetConnection outlook.com -TraceRoute | Select -ExpandProperty TraceRoute | % { Resolve-DnsName $_ -type PTR -ErrorAction SilentlyContinue }
netstat
	Get-NetTCPConnection | Group State, RemotePort | Sort Count | FT Count, Name –Autosize
	Get-NetTCPConnection | ? State -eq Established | FT –Autosize
	Get-NetTCPConnection | ? State -eq Established | ? RemoteAddress -notlike 127* | % { $; Resolve-DnsName $.RemoteAddress -type PTR -ErrorAction SilentlyContinue }
who / w	 : ForEach ($log in (get-eventlog system -source Microsoft-Windows-Winlogon -After (Get-Date).AddDays(-7))) {if($log.instanceid -eq 7001) {$type = “Logon”} Elseif ($log.instanceid -eq 7002){$type=”Logoff”} Else {Continue} $res += New-Object PSObject -Property @{Time = $log.TimeWritten; “Event” = $type; User = (New-Object System.Security.Principal.SecurityIdentifier $Log.ReplacementStrings[1]).Translate([System.Security.Principal.NTAccount])}};$res;
