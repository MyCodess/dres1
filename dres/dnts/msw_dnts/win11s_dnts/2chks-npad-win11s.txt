__________________ 2chk/try/npad/... win11s : _____________________________



#####  ==========  2chks-win11s:

    _______:  Cortana uninstall ??:
    https://pureinfotech.com/uninstall-cortana-windows-11/
    - PS1-admin:  Get-AppxPackage *Microsoft.549981C3F5F10* | Remove-AppxPackage
    - /OR:  winget uninstall --id 9NFFX4SZZ23L
    - To uninstall Cortana from Windows 11, open PowerShell (admin):  “Get-AppxPackage *Microsoft.549981C3F5F10* | Remove-AppxPackage” command.
    - You can also remove Cortana from Command Prompt (admin) :       “winget uninstall –id 9NFFX4SZZ23L” command.

    _______:  Bin disable user:
    https://www.howtogeek.com/826967/how-to-disable-bing-in-the-windows-11-start-menu/
    # if [HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\Explorer] not exit, create the key: 
    on "[HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\]  do: New," then click "Key." Type "Explorer" , then :
    Windows Registry Editor Version 5.00

    [HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\Explorer]
    "DisableSearchBoxSuggestions"=dword:00000001

    _______:  
    _______:  
##________________________________________  ___________________________

