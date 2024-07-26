________________ Imaging / Cloning / Snapshots / VHDs-installs / Wiederherstellung/restore/backup von Win10 ___________________________________
-!! see also  dres/dnts/CT-WImage_cloning_1p_dnts.txt  for CT-nts !
-!! main _RF:  https://docs.microsoft.com/en-us/windows-hardware/manufacture/  == here DW as:  ManufacturingWins--Imaging-Boot-DISM--msDocs.pdf !

#################### DISM / Imagaing/OS-Backups/Restore/...: ###################################################
-! see also syss/stat1-/setup1-files of win10-installs !!
##________________________________________  ___________________________


#####  ==========  imaging-wins:
	-! main/server/professional imaging tools are in Windows Assessment and Deployment Kit (Windows ADK):
	https://learn.microsoft.com/en-us/windows-hardware/get-started/adk-install
	---  Windows System Image Manager Technical Reference :
	https://learn.microsoft.com/en-us/windows-hardware/customize/desktop/wsim/windows-system-image-manager-technical-reference
##________________________________________  ___________________________


#####  ==========  DISM / dism.exe onboard imaging cmd:
	-!! main _RF: ManufacturingWins--Imaging-Boot-DISM--msDocs.pdf--P.853+P.367  bzw.
	  https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/capture-and-apply-an-image?view=windows-11
	  two chapters there!:  Capture, apply, and work with Windows images , P.367  + DISM Command-Line Options , P.853
	https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/capture-and-apply-windows-using-a-single-wim?view=windows-11  ##--> also scripts ...
	https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/what-is-dism
	https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/dism-image-management-command-line-options-s14
	https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/deployment-image-servicing-and-management--dism--command-line-options
	https://docs.microsoft.com/en-us/powershell/module/dism/?view=windowsserver2022-ps  :  DISM cmdlets available in the DISM PowerShell
	---
	-! CTs-WImage-projekt !! see CT-nts !
	- see also CT-nts  in  dres/dnts/CT-WImage_cloning_1p_dnts.txt !
	-! see also scripts of the msRefs-docs of dism in https://go.microsoft.com/fwlink/?linkid=872894 bzw thw whole  ManufacturingWins--Imaging-Boot-DISM--msDocs.pdf !!
	- Systemsteuerung-Onboard-MS-Imaging (Backup/Restore) deprecated/retired ab Win10-1803 !!, aber still there as Win7-imaging in SystemSteuerung and works obv. fine !

	_______:  dism Best Pratices see in ManufacturingWins--Imaging-Boot-DISM--msDocs.pdf:
	-! do OFFLINE (win-source)
    -! remove source swap/suspend/hibernate-file before imaging !
	- SysPrep.exe ?? in %WINDIR%\system32\sysprep\sysprep.exe
	- Disable Antivirus Tools !
	- saving image not to source-HD, lieber ext-USB
	- log-file:  %WINDIR%\Logs\Dism\Dism.log 
	- ... see msRef above !!
	- after imaging:   Dism.exe  /Cleanup-Image /StartComponentCleanup /ResetBase ##--cleanup-updates-store(previous/older-versions)! 
		After cleaning up the component store with the ResetBase option, you will no longer be able to uninstall any of the previously installed updates. The ResetBase option freed up additional 110MB of disk space on the reference update. ##-see-manufacurting-doc !
	-? powercfg /h off : Removes files!  ##/or by offline-imaging remove them: del hib.... swap.. ...
	-! CT:  /checkintegrity /verify %scratchdir%

	_______:  cT-Wimage-dism-param-lines:  see ct-WIMage.x86 file in its zip! :
	- CT.params: dism <capture/append> ...  /name:<dateTIme>-<hostname>-<winEdition>  /description:%...%  /checkintegrity /verify %scratchdir%  #as below:
	%windir%\system32\dism /%action% /imagefile:%workdir%sources\install.wim /capturedir:%sklw%: /name:"%date% %time:~0,5% %computername% %edition%" /description:  %description% /checkintegrity /verify %scratchdir% 
	-! also see/use CT-dism-config-file:  ct-WIMage\ct-WIMage.ini  to exclude hiberfil.sys... and not-compressing aleady compressed file!

	_______:  Image optimization  :see in ManufacturingWins--Imaging-Boot-DISM--msDocs.pdf :
	After applying updates to a Windows image, cleanup the image and then export it to a new file:md c:\mount\Windows
	md C:\mount\temp
	Dism /Mount-Image /ImageFile:"C:\Images\install.wim" /Index:1 /MountDir:C:\mount\Windows
	Dism /Cleanup-Image /Image=C:\mount\Windows /StartComponentCleanup /ResetBase /ScratchDir:C:\mount\temp
	Dism /Unmount-Image /MountDir:C:\mount\Windows /Commit
	Dism /Export-Image /SourceImageFile:C:\Images\install.wim /SourceIndex:1 /DestinationImageFile:C:\Images\install_cleaned.wim
	- see also CT-WImage-config.ini !

	_______:  checking/reducing/verifying if needed:    see manufacturing-doc:  "Repair a Windows Image"
	- Dism /Online /Cleanup-Image  /ScanHealth
	- Dism /Online /Cleanup-Image  /CheckHealth
	- For a quick check of an online image, you may be able to use the command: sfc /scannow to scan and repair.

	_______:  ERRORs, Problems, ...:
	-! to avoid ERRORS due to  un-generalized: do as in manufachtured-pdf--Deployment examples--p.330 : so doing:
		%WINDIR%\system32\sysprep\sysprep.exe  /generalize  /shutdown  +  booting-from-WinPE/USB-Media  +  make-image-of-offline-reference-system !
	---!! 1kk-on-x17-problem:  DRIVE-LETTER ! blank-login-screen!! boot-part(c:\windows) in target-system was E:\ and not C:\ !! (evtl. the the target-part was mounted in source-part as E:\ !?)
		so by imaging: source-part MUST NOT have mounted the fututure target-part !! and better: MUST have as few as possible mounted parts !
		must rename the mount-point/letter offline (or also online, if you get in in safe-mode-with-cmd!?):  https://docs.microsoft.com/en-us/troubleshoot/windows-server/backup-and-storage/restore-system-boot-drive-letter
		Regedit.exe : (load offline-hive of target-par) -> HKEY_LOCAL_MACHINE\SYSTEM\MountedDevices (check key permissions here! Admin FULL!) -> rename the wrong-key/-letter eg: \DosDevices\E: to \DosDevices\C: -> reboot !
		-/OR maybe SysPrep before imaging solves the problem !?!? 2chk !
	-! win10-220725.wim for /apply-image had to do manually on the target-PC (caonaing a fresh minimal WIn10-installation):
	rd "c:\Program Files\WindowsApps" /s  ;   rd c:\ProgramData\Microsoft\Windows\AppRepository" /s 
	-! unp/ScratchD failing:   by dism /apply-image (esp. if to USB) use also the global option /ScratchDir:<HD1-partX\dirX> , otherwise dism unpacks the image into the target-usb-media, and could be capacity paroblem AND is much slower! so set the scratchDir to a local-HD-Dir !

	_______:  restore-into-VHD / Win-Image-restore/Wiederherstellen in VHDs : see below-nts, in VHDs-section !

	_______:  CT.21.11--162-167-WImage-Tipps-Tricks.pdf :
	-!! der trick ist dass: erst ein normales Win-Setup-Stick-mit MCT erstellen, und danach das standard-MS-Setup-image unter source\insall.wim mit unserem erzeugten image überschreiben !
	das Setup-Stick dann wie beim Win-Neu-Installiern starten/booten und Fragen beantworten und auf installieren drucken.
	jetzt zum Installieren der Setup-Stick  automatisch ladet source\install.wim (was jetzt unser erzeugtes Image ist), passt es an, und installiert es auf Ziel-Partition !
##________________________________________  ___________________________


#####  ==========  SysPrep: ===============================================================
	-! CT-22.06--156-159 : SysPrep !! : windows PC für dritte vorbereiten!
	- https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/sysprep--system-preparation--overview?view=windows-11
	- WPs:  https://theitbros.com/sysprep-windows-machine/

	_______:  DEFs:
	- Sysprep (System Preparation) : prepares a Windows client or Windows Server installation for imaging. Sysprep can remove PC-specific information from a Windows installation (generalizing) so it can be installed on different PCs. When you run Sysprep you can configure whether the PC will boot to audit mode or to the Out-of-Box Experience (OOBE).
	- "Audit mode" : allows you to make additional changes to the Windows installation before you send the computer to a customer or capture the image for reuse in your organization.
	- "OOBE mode"  : (Out-Of-Box Experience) is the frisch-win10-setup-running mit den typischen Fragen: lang/KB/... !  OOBE is the default out-of-box experience that allows end users to enter their account information, select language, accept the Microsoft Terms of Service, and set up networking.

	_______:  call/enter/exit into sysprep modes (audit / OOBE):
	- Shift + Ctrl + F3 :  you can boot Windows to Audit Mode or OOBE by pressing Shift + Ctrl + F3 on the OOBE , or the Windows Welcome screen.
	- C:\windows\system32\sysprep\sysprep.exe /? , /OR GUI: just without params !
	- problems?, check log:  %WINDIR%\System32\Sysprep\Panther\setupact.log --> usu.needs then an update (bzw. conclusion of the lates update) !
	- then: The computer will automatically restart and boot to the Audit Mode. Windows automatically boots and logs in with the built-in administrator account when in the Audit Mode. Further, this account will be disabled.
	- despite reboots, still in audit mode, after having started it !!: Windows 11/10 will boot in this mode no matter how many times you reboot your computer until the Sysprep is running.
	--- answer-file after  sysprep.exe /oobe /generalize /shutdown /unattend :
	- see:  https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/windows-setup-automation-overview?view=windows-11#implicit-answer-file-search-order
	- default-search-path-for-answerfile-syspret:  %WINDIR%\System32\Sysprep\Unattend.xml 
	- answer-file and conclusion:  c:\windows\System32\Sysprep\sysprep.exe /oobe  /shutdown /unattend:C:\ps\autounattend.xml ##-With the /generalize option the Sysprep will remove unique computer data. This allows you to safely deploy this reference Windows 10 image on another workstation or laptop. After executing the command, the computer will shut down and next time reboots to OOBE, but with answer-file, so NOT-asking the user for options,... !

	_______:  image-creation steps (eg with dism/...) for generalized new-installs on new PCS, so using sysprep /audit  :
	- steps creating a generalized image:   https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/boot-windows-to-audit-mode-or-oobe?view=windows-11#step-1-transfer-an-image-to-a-different-computer  :
	--> frisch-Reference-PC-installed-newly --> modify/custimization of Ref-PC, add apps/updates/configs/.. to it --> Sysprep /audit /generalize /shutdown   : PC shutdowns in generalized-audit-mode -->
	--> boot-Ref-PC-from-WTG/WinPE/SetupStick/... --> capture-image /dism/... --> goto-new-PC, apply-image into new-PC --> start new-PC --> end the audit mode:   Sysprep /oobe /shutdown --> then it will reboot next time for the customer in OOBE-mode !
	- image-creation must be done on an offline-win-system-generalized(with sysprep) , so Audit-Mode of a PC and shutdowned !! (not-normal-mode/OOBX) ; audit-mode:  call sysprep.exe , option sudit-mode, reboot (CTRL +SHIFT +F3  did not work for me!)
	- see diagram/picture in:  https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/audit-mode-overview?view=windows-11
	- cmdline-options:  ssprep /?  bzw. https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/sysprep-command-line-options?view=windows-11

	_______:  Audit-mode:
	-!! see manufacturing-pdf --Audit Mode --329 :
	- https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/audit-mode-overview?view=windows-11
	- starting audit-mode:  sysprep /audit  /OR   CTRL +SHIFT +F3   bei der ersten fragen beim booten(OOBE)  !
	- ending   audit-mode:  sysprep /oobe  : After you complete your audit mode installations, you must run sysprep /oobe to ensure that the end-user goes through the out-of-box experience and accepts the license terms. 
	-! in audit-mod you get loged in as "Administrator" acc, which is deactivated in normal-win-setup ! (no-login/PW-need,... required) !

	_______:  done-steps:
	-!! _1kk: sysprep bzw. audit-mode,... lohnt sich nut für mehre PCs/NW! und funktioniert richtig NUR wenn:
		1- GLEICH-direkt nach dem Basis-setup0-mit-WinPE, gleich da KEINE weiteren driver/configs/software/... sondern 
		2-dann GLEICH switch to audit mode und erst DA (im audit-mode, NOT-generalize yet! but at the end before switching to /OOBE mode!)
		3- add drivers/softwares/configs/... , und  wenn fully fertig dann
		3b- ALL installed apps/utils MUST be installed for All-USERS and not only cu-user! so NO Apps-from-MsStore (they are installed per user!) !
		4- c:\windows\System32\Sysprep\sysprep.exe /oobe /generalize /shutdown 
		4b- if like with answerfile call above line with: sysprep /oobe /generalize /unattend:C:\MyAnswerFile.xml  #-/OR put-to-dafault-sysprep-search-path: %WINDIR%\System32\Sysprep\Unattend.xml
		5- reboot to WinPE/second-Win10/... make an OFFLINE image of the configured offline Win10 ! 
		-!! ein schon konfiguriertes OS/Win10 geht schlecht mit sysprep/audit ! Fehlermeldungen ...
#################### System-Wiederherstellung-Configs (-punkte): ########################################
	-!! c’t 2021, Heft 10 --S. 012-017
	- see for Imaging,... see extra dnts of CT-WImage ! obv. the win-abbild/imaging MS-app is obsolete !?!? ab win10-1803 !?
	- booten from current-win ins Wiederherstellungmodus: Umschalte-Taste-halten + Restart !
	--- c’t 2021, Heft 10, s. 12-18:
	- default System-Wiederherstellung is deaktiviert seit win10-1709 ! activate it (System ...) ! beim einem halbjährigen "upgrade" wird wieder zurückgesetzt (nicht tägliches "update" )! wieder reaktivieren !
	- Windows speichert die Schatten­ kopien der Wiederherstellungspunkte in dem versteckten System-Ordner „System Volume Information“.
	- Wenn das Booten von Windows dreimal hintereinander misslingt, unternimmt der Bootloader keinen weiteren Versuch, son- dern startet die Wiederherstellungsumge- bung „Windows RE“ (Recovery Environ- ment [1]). Windows RE bietet an, sich an einer automatischen Reparatur zu versu- chen. Klicken Sie stattdessen auf „Erwei- terte Optionen“, dann landen Sie in einem Auswahldialog.
#################### VHDs / install into vhdx : ################################################################
	-! msRefs: ManufacturingWins--Imaging-Boot-DISM--msDocs.pdf --287:  Deploy Windows with a VHDX (Native Boot)
	-! CTs ...!

	_______:  Win-Image-restore/Wiederherstellen in VHDs:
	-! CT:  Windows-VMs in Hyper-V, c’t 20/2020, S. 162 , Axel Vahldiek, VM-Generator, c’t-Skript erstellt
	  : Image restore/Wiederherstellen in einer mit Hyper-V erstellten virtuellen Maschine mithilfe von c’t-Win2Hyper-V 
	-! Image-restore auf einer virtuellen Festplatte mithilfe von ­c’t-Win2VHD : Axel Vahldiek, Versuchslabor, Zweit-Windows per Drag & Drop, c’t 2/2017, S. 88

	_______:  
	-! Windows boot manager can be configured to boot directly into the VHD.
	-! You can use Windows disk-management tools, DiskPart, and the Disk Management Microsoft Management Console (Diskmgmt.msc) to create a VHDX file for Native boot.
	-! with DISM A supported Windows image (.wim) file can be applied to a virtual hard disk !
################################################################################################################
