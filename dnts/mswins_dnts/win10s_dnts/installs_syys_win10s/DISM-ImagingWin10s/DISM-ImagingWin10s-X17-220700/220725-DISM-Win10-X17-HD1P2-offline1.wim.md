##________________________________________  ___________________________


#####  ==========  addies/modifs to the wim and restore it again back to main Win10-D1P2 (formatted), doing from D1P5-win_b :
- 220726 	:  mountpoints-of-parts all deleted from REG ! :
	dism  /Mount-Wim  /WimFile:U:\Images1\220725-Win10-X17-HD1P2-offline1.wim  /Index:1  /MountDir:U:\Unp1\Dir1
	REG:  load  U:\Unp1\Dir1\Windows\system32\config\SYSTEM  to hive Computer\HKEY_LOCAL_MACHINE\Img1 : delete ALL entries, except "default (empty)" of  Computer\HKEY_LOCAL_MACHINE\Img1\MountedDevices
	dism  /apply-image  /imagefile:U:\Images1\220725-Win10-X17-HD1P2-offline1.wim   /applydir:F:\   /index:1  /ScratchDir:U:\Unp1   /LogPath:U:\Images1\220726-D1P2-Win10.log   /English
################################
##________________________________________  ___________________________


#####  ==========  offline capture:
- WinPE start ...
- want to restore to the same PC /X17, so no SysPrep,...
dism  /capture-image  /imagefile:F:\Images1\220725-Win10-X17-HD1P2-offline1.wim   /captureDir:G:\   /Name:220725-Win10-X17-HD1P2-offline1   /ScratchDir:F:\Unp1   /LogPath:F:\Images1\220725-dism.log   /English  
dism  /apply-image  /imagefile:F:\Images1\220725-Win10-X17-HD1P2-offline1.wim   /applydir:E:\   /index:1  /ScratchDir:F:\Unp1   /LogPath:F:\Images1\220725-dism.log   /English
_______________________ Protocoll_1coll : ______________________________________________
DISKPART> list vol
  Volume ###  Bst  Bezeichnung  DS     Typ         Größe    Status     Info
  ----------  ---  -----------  -----  ----------  -------  ---------  --------
  Volume 0     J                       DVD-ROM         0 B  Kein Medi
  Volume 1     C   Boot_P1      NTFS   Partition   4000 MB  Fehlerfre
  Volume 2     G   Win10        NTFS   Partition     97 GB  Fehlerfre
  Volume 3     H   T1FS         exFAT  Partition     78 GB  Fehlerfre
  Volume 4     E   Win10_b-D1P  NTFS   Partition     78 GB  Fehlerfre
  Volume 5     F   D1P7         NTFS   Partition     97 GB  Fehlerfre
  Volume 6     D   win10setup2  NTFS   Wechselmed    28 GB  Fehlerfre
DISKPART>
G:\>dir  /A
G:\>del  /AH  G:\hiberfil.sys
G:\>date
Aktuelles Datum: 24.07.2022
Aktuelle Zeit: 21:38:26,78
G:\>
G:\>dism  /capture-image  /imagefile:F:\Images1\220725-Win10-X17-HD1P2-offline1.wim   /captureDir:G:\   /Name:220725-Win10-X17-HD1P2-offline1   /ScratchDir:F:\Unp1   /LogPath:F:\Images1\220725-dism.log   /English
Deployment Image Servicing and Management tool
Version: 10.0.19041.844
Saving image
[==========================100.0%==========================]
The operation completed successfully.
G:\>time
Aktuelle Zeit: 22:01:47,93

	_______:  ---- restore: -------------------
G:\>time /T
22:10
G:\>dism  /apply-image  /imagefile:F:\Images1\220725-Win10-X17-HD1P2-offline1.wim   /applydir:E:\   /index:1  /ScratchDir:F:\Unp1   /LogPath:F:\Images1\220725-dism.log   /English
Deployment Image Servicing and Management tool
Version: 10.0.19041.844
Applying image
[==========================100.0%==========================]
The operation completed successfully.
G:\>time /T
22:21

	_______:  ------------------------------------

	_______:  --------------------- bcd-add: --------------------
>bcdedit
>bcdedit /copy   {default}  /d "Win10_b"
Der Eintrag wurde erfolgreich in {f6e1ab00-0b96-11ed-b486-e6c08740a2f3} kopiert.
>bcdedit
E:\>bcdedit /set  {f6e1ab00-0b96-11ed-b486-e6c08740a2f3}  device partition=E:
Der Vorgang wurde erfolgreich beendet.
E:\>bcdedit /set  {f6e1ab00-0b96-11ed-b486-e6c08740a2f3}  osdevice partition=E:
Der Vorgang wurde erfolgreich beendet.
