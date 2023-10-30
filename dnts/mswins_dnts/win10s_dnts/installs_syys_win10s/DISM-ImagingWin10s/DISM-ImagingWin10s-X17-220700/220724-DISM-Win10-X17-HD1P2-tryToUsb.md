tried to restore to USB-Stick , but very "un-organized" so not proper formating, online-image, ... also no scratchDir param, so failed due to capacity,... 
just a fancy try to see ....
##________________________________________  ___________________________


#####  ==========  
REM   220724-Win10-X17-HD1P2.wim  , BUT online dine! so, NOT from WinPE/USB-Stick !! !?
dism  /capture-image /imagefile:U:\Images1\220724-Win10-X17-HD1P2.wim   /captureDir:C:\  /Name:220724-X17
dism  /capture-image /imagefile:G:\Images1\220724-Win10-X17-HD1P2.wim   /captureDir:H:\  /Name:220724-X17

	_______:  --------------------------------------------------------------
- from WInPE done, BUT without SysPrep !! 
G:\Images1>dism  /capture-image /imagefile:G:\Images1\220724-Win10-X17-HD1P2.wim   /captureDir:H:\  /Name:220724-X17
Tool zur Imageverwaltung für die Bereitstellung
Version: 10.0.19041.844
Saving image
[==========================100.0%==========================]
Der Vorgang wurde erfolgreich beendet.
G:\Images1>

	_______:  --------------------------------------------------------------

	_______:  --------------------------------------------------------------
G:\Images1>dism  /apply-image  /imagefile:G:\Images1\220724-Win10-X17-HD1P2.wim  /index:1  /applydir:L:\

	_______:  > aber L: was exfat !?!? geht?? 
  Volume 8     L   WTG1_UB1     exFAT  Wechselmed    52 GB  Fehlerfrei

	_______:  --------------------------------------------------------------
- "df" for wins /cmd :
wmic logicaldisk  get size, freespace, caption
##________________________________________  ___________________________


#####  ==========  FAILED!!! capacity!!  missing /scratchDir !! ---------------
G:\Images1>dism  /apply-image  /imagefile:G:\Images1\220724-Win10-X17-HD1P2.wim  /index:1  /applydir:L:\
Tool zur Imageverwaltung für die Bereitstellung
Version: 10.0.19041.844
Applying image
[===========================55.0%                          ]
Fehler: 112
Es steht nicht genug Speicherplatz auf dem Datenträger zur Verfügung.
Die DISM-Protokolldatei befindet sich unter "X:\windows\Logs\DISM\dism.log".
G:\Images1>
_________________________________________________
G:\Images1>L:\windows\system32\bcdboot.exe  L:\Windows  /s L:
Fehler beim Kopieren der Startdateien.
G:\Images1>H:\windows\system32\bcdboot.exe  H:\Windows  /s L:
Fehler beim Kopieren der Startdateien.
