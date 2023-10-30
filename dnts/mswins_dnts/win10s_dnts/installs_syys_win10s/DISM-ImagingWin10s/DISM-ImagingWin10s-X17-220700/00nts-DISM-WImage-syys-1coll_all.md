############################################################################## 26.07.2022 :

#####  ==========  image-with-SysPrep in Audit mode :
c:\windows\system32\Sysprep\sysprep.exe /audit --> reboot
#go into audit-PC ohne PW...
cd c:\windows\system32\Sysprep
c:\windows\system32\Sysprep\sysprep.exe  /?
c:\windows\system32\Sysprep\sysprep.exe  /OOBE /shutdown /generalize /unattend:U:\Images1\audit1.xml.txt 
############################################################################## 26.07.2022 :
##________________________________________  ___________________________


#####  ==========  customizing manually (Regedit : volume letter changing): 26.07.2022
U:\Images1>dism  /Mount-Wim  /WimFile:U:\Images1\220725-Win10-X17-HD1P2-offline1.wim  /Index:1  /MountDir:U:\Unp1\Dir1
--> Regedit -> load-hive U:\Unp1\Dir1\Windows\System32\config\system -> mounteddrives : removed all the rest abd renamed E:\ to C:\ (maybe could work also removing All !?)
dism   /Unmount-Wim   /MountDir:U:\Unp1\Dir1  /commit

	_______:  re-imaging
U:\>dism  /apply-image  /imagefile:U:\Images1\220725-Win10-X17-HD1P2-offline1.wim   /applydir:L:\   /index:1  /ScratchDir:U:\Unp1   /LogPath:U:\Images1\220726-dism-usb128-after-std-setup.log   /English
Deployment Image Servicing and Management tool
Version: 10.0.19041.844
Applying image
[==========================100.0%==========================]
The operation completed successfully.
U:\>

	_______:  ----------
Reg: deleted all "mountedDevices"-entries in HKLM-System-file ! even C:\,... , mal sehen ..!
##load-hive:  L:\windows\system32\config\SYSTEM
############################################################################## 220725 :
##________________________________________  ___________________________


#####  ==========  D1-P5-again incl. OS-install ============
- 220725, 21:15 : D1P5 reformated, started from WInPE-Install-Stick, installed a new frish Win there, booted, all fine, and now again the same image-apply:
dism  /apply-image  /imagefile:U:\Images1\220725-Win10-X17-HD1P2-offline1.wim   /applydir:S:\   /index:1  /ScratchDir:U:\Unp1   /LogPath:U:\Images1\220725-dism-D1P2.log   /English

	_______:  ERROR, then (second try, bootet from WinPE-Stick):
- MANUALLY had to delete on the target-part of apply-image:
F:\>rd /s "E:\Program Files\WindowsApps"
Möchten Sie "E:\Program Files\WindowsApps" löschen (J/N)? j
F:\>rd /s "E:\ProgramData\Microsoft\Windows\AppRepository"
Möchten Sie "E:\ProgramData\Microsoft\Windows\AppRepository" löschen (J/N)? j
dism  /apply-image  /imagefile:F:\Images1\220725-Win10-X17-HD1P2-offline1.wim   /applydir:E:\   /index:1  /ScratchDir:F:\Unp1   /LogPath:F:\Images1\220725-dism-D1P2-from_WInPE.log   /English
############################################################################## 25.07.2022
##________________________________________  ___________________________


#####  ==========  WIn-D1_P2-restore-fully with image, which D1_P5 has problems! ============
X:\Sources>date /t
25.07.2022
X:\Sources>time /t
13:53

	_______:  --------------------
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

	_______:  -------------------------------

	_______:  formatting:
DISKPART> detail part
Partition 2
Typ      : 07
Versteckt: Nein
Aktiv    : Nein
Offset in Byte: 4195352576
  Volume ###  Bst  Bezeichnung  DS     Typ         Größe    Status     Info
  ----------  ---  -----------  -----  ----------  -------  ---------  --------
* Volume 2     G   Win10        NTFS   Partition     97 GB  Fehlerfre
--
DISKPART> FORMAT FS=NTFS LABEL=Win10-D1-P2-a   QUICK
  100 Prozent bearbeitet
DiskPart hat das Volume erfolgreich formatiert.

	_______:  -------------------------------
F:\Images1>dism   /Get-ImageInfo  /imagefile:F:\Images1\220725-Win10-X17-HD1P2-offline1.wim
Tool zur Imageverwaltung für die Bereitstellung
Version: 10.0.19041.844
Details for image : F:\Images1\220725-Win10-X17-HD1P2-offline1.wim
Index : 1
Name : 220725-Win10-X17-HD1P2-offline1
Description : <undefined>
Size : 23.507.962.407 bytes
Der Vorgang wurde erfolgreich beendet.

	_______:  ---------------------------------
X:\Sources>dir F:\Images1\220725-Win10-X17-HD1P2-offline1.wim
 Datenträger in Laufwerk F: ist D1P7
 Volumeseriennummer: FA7A-B391
 Verzeichnis von F:\Images1
24.07.2022  21:58     7.903.022.657 220725-Win10-X17-HD1P2-offline1.wim
               1 Datei(en),  7.903.022.657 Bytes
               0 Verzeichnis(se), 64.536.174.592 Bytes frei
X:\Sources>time /t
14:16
X:\Sources>dism  /apply-image  /imagefile:F:\Images1\220725-Win10-X17-HD1P2-offline1.wim   /applydir:G:\   /index:1  /ScratchDir:F:\Unp1   /LogPath:F:\Images1\220725-dism-D1P2.log   /English
Deployment Image Servicing and Management tool
Version: 10.0.19041.746
Applying image
[==========================100.0%==========================]
The operation completed successfully.
X:\Sources>time /t
14:29
X:\Sources>

	_______:  ---------------------------------
###########################################################################
