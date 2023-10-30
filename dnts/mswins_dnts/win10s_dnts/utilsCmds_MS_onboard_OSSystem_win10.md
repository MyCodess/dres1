_______________________________ MsWin10-onboard-org-OS-cmdline-cmds: ________________________________
-!!here onboard-Utils/"*.exe"-cmds which invoke certain OS-GUIs/utils! for pure-cmdlineCms (as robocoy/move/dir/...) see extra-dnts !!
	so basically ".exe"-filename  of OS-GUIs (as system-steuerung, compmgm, power-options, msinfo32, ...)
- so specific areas see their own dnts (as for imaging/boot/ ...., bcdedit, bcdsect, ....)
##________________________________________  ___________________________


#####  ==========  docs:
	-!! RF: https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands
##________________________________________  ___________________________


#####  ==========  listing-eg of onboard-mswin-OS-cmdsUtils:
	msinfo32
	dxdiag
##________________________________________  ___________________________


#####  ==========  wmic  : cmdline FULL-Admin-and-System-Information-tool / Windows Management Instrumentation from cmdline !:
	--- descp:
	-  Windows Management Instrumentation Command line (WMIC) is a software utility that allows users to performs Windows Management Instrumentation (WMI) operations with a command prompt.
	-! wmic is deprecated since Win10-1903, replaced by PowerShell-cmdlets (still not in WinPE), but still can a lot!  -! BUT obsol/replaced by powershell-cmds!:  This utility is superseded by Windows PowerShell for WMI (see Chapter 7—Working with WMI) ! https://docs.microsoft.com/en-us/windows/win32/wmisdk/wmic
		so still ok, since powershell is not accessible in WinPE yet (for Sys-maintenance)! see above link !
	- so Windows Management Instrumentation /WMI   replaced by:  Windows Management Infrastructure (MI) , and wmic replaced by its Powershell-cmdlets !
	--- docs/Refs:
	-! https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc779482(v=ws.10)
	-! https://docs.microsoft.com/en-us/powershell/scripting/learn/ps101/07-working-with-wmi?view=powershell-7.2 
	-  https://docs.microsoft.com/en-us/previous-versions/windows/desktop/wmi_v2/windows-management-infrastructure
	--- HELPs:
	-! help:  wmic /?  ##bzw:   wmic  /?:FULL 
	- list of aliases included with WMIC, type /? at the WMIC command prompt. /OR: wmic /?  ##bzw:   wmic  /?:FULL
	- wmic-cli>  alias_name /?
	--- eg:
	- eg-coll in: https://www.cs.cmu.edu/~tgp/scsadmins/winadmin/WMIC_Queries.txt
	- Disks-listing :    wmic diskdrive list  [brief] #..
	- CPUs-status  : full:  wmic cpu ;#/OR:  wmic cpu get /? ; wmic cpu get xxx      ##-infs about CPUs / as task-manager (spu is an alias! listing all aliases with:  wmic /?  )
	- BIOS-attribs : full:  wmic bios  ; #/OR:  wmic bios  get /? ; eg: mic bios get serialnumber ; 
	- "df" :  wmic logicaldisk get size, freespace, caption  ##-print all partitions, size & free space
	- Display the State of all the Global Switches in Windows :  wmic context 
	- wmic process where ExecutablePath='C:\\windows\\system32\\notepad.exe' get ProcessId
	- wmic process list  ##-all running processes
	- wmic os get version ; wmic os /? ;  wmic os get xxx;
	---
