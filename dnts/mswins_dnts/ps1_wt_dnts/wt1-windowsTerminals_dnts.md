_____________________ wt.exe / WindowsTerminal.exe dnts : __________________________________
- !! see REF:  https://learn.microsoft.com/en-us/windows/terminal/command-line-arguments?tabs=powershell  :

--- nts-Allg-wt1 :
    - !! esacping chars in wt1 with ` (backtick) !! (so as "\"in bash!) ; eg. opening two-tabs-wt from PS-Terminal:   wt `; `;
	- so: PowerShell uses a semicolon ; to delimit statements. To interpret a semicolon ; as a command delimiter for wt command-line arguments, you need to escape semicolon charactersusing backticks. PowerShell also has the stop parsing operator (--%), which instructs it to stop interpreting anything after it and just pass it on verbatim.
	- !! obv. wt1-cmdline-params are doch case-sensitive, as -p <profile-name>  and NOT -P !?

--- portable-setup:
	- https://learn.microsoft.com/en-gb/windows/terminal/distributions#windows-terminal-portable :
	- !! unzip + cd <unzipped-wt> ; touch .portable ;
	- Portable mode needs to be enabled manually. After unzipping the Windows Terminal download, create a file named .portable next to WindowsTerminal.exe.
	- settings in ptb-wt:  Windows Terminal will automatically create a directory named settings in which it will store both settings and runtime state such as window layouts.
	- Disabling Portable mode : You can restore Portable mode unpackaged installation to its original configuration, where settings are stored in %LOCALAPPDATA%\Microsoft\Windows Terminal, by removing the .portable marker file from the directory containing WindowsTerminal.exe.
	- Upgrading a Portable mode Install : 	You can upgrade a portable mode installation of Windows Terminal by moving the .portable marker file and the settings directory to a newly-extracted unpackaged version of Windows Terminal.
	- If you wish to reenable portable mode, you can create a new .portable marker file next to WindowsTerminal.exe.

--- start multiple tabs from powershell (see REF above!):
    PowerShell > wt `; `;   ##--two-tabs-wt
    PS>  wt nt -p "winps" -d "${env:USERPROFILE}\ofc1"  `;  nt -p "winps" -d "${env:USERPROFILE}\ofc1\etc" `;
    PS>  wt nt -p "winps" -d "$HOME\ofc1"  `;  nt -p "winps" -d "$HOME\ofc1"

--- inputrc (ctrl-a, ctrl-e, ...):
	- for inputrc/ctrl-a,ctrl-e,... see entries in  ofc1\bin\prof1.ps1   ##--:  Import-Module PSReadLine ; Set-PSReadlineOption -EditMode Emacs
	- https://learn.microsoft.com/en-us/powershell/module/psreadline/about/about_psreadline?view=powershell-7.3
	- keyboard-shortcuts-seetings see wt-json-file settings.json bzw. ctrl-, bzw. "Actions" in settings !

################################# 1coll-wt1 : ###############################################
C:\Progs2\0ptb\wt\WindowsTerminal.exe  new-tab  -d <path1>
C:\Progs2\0ptb\wt\WindowsTerminal.exe  new-tab  -d <path1>  -p "gitbash"

