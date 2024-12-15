________________ REG-entries_1coll-WINs-all : _________________________________


#####  ==========  <TAB>-completion-filenames-in-cmd :
#- complete file and directory name, default TAB, --msREF:  https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands
#- ALL / HKLM :
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Command Processor\CompletionChar
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Command Processor\PathCompletionChar
#- USER /HKCU :
HKEY_CURRENT_USER\SOFTWARE\Microsoft\Command Processor\CompletionChar
HKEY_CURRENT_USER\SOFTWARE\Microsoft\Command Processor\PathCompletionChar
#-- /OR  per cmd-window/-Instance enable/disable  with:  cmd  /F:ON or /F:OFF
##________________________________________  ___________________________


#####  ==========  Time of firmaware/BIOS is UTC (not local as MsWins!):
#-- OK-on-X17:  time of  BIOS/Firmware is  UTC :
    reg add  HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\TimeZoneInformation  /v RealTimeIsUniversal /t REG_QWORD  /d 1
	and disable Zeitgeber /TIme-Dienst:  sc config w32time start=disabled  ##--and also automatische tZeitanpassung, 
#--
#- https://wiki.archlinux.org/title/System_time#UTC_in_Microsoft_Windows
#- disable Zeitgeber /TIme-Dienst:  sc config w32time start=disabled  ##--and also automatische tZeitanpassung, AND:
#- create new QWord (/OR? DWord) key RealTimeIsUniversal = 1 in HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\TimeZoneInformation as:
Windows Registry Editor Version 5.00
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\TimeZoneInformation]
     "RealTimeIsUniversal"=hex(b):01,00,00,00,00,00,00,00
#--bzw: Dword, BUT Dword had got no effect in X13-win10! so use the above QWord / hex !
Windows Registry Editor Version 5.00
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\TimeZoneInformation]
 "RealTimeIsUniversal"=dword:00000001
##________________________________________  ___________________________

