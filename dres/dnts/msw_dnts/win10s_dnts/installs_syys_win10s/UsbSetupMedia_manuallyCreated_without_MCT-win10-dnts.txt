____________________ generating a Win10-Install-Media without using MS-MediaCreationTool) : ____________________
!! MANUALLY creating (so WITHOUT using MS-MCT) a win10-Setup/-Installation-Media on a USB-Stick, just instead of DVD-setup-media, so to install OS on a NB! (instead of on DVD/CD, as earlier)!
!! so NOT-Win10-ToGo / Not-OS-FULL-running-Win10-from-USB!! , so NOT-"Windows-To-Go, WtG",  so NOT-USB-Test-System! so 
	for installing Full-Win10-OS-on-USB as frull-running-system (so Windows-ToGo / WtG  as your test/portable-OS) see the RUFUS-approach in : ct.19.11--148-153   :  Windows 10 auf USB-Laufwerk installieren !!
##________________________________________  ___________________________


#####  ==========  Manually create USB-Setup-Media:
	-! Manufacture.pdf--Install Windows from a USB Flash Drive--266 ! is basically nur usb-formatting+copying-iso-tree :
	Format the USB with FAT32 (eg in compmgmt or diskpart)  --> but max-filesize < 4GB !
	Mark Partition as Active (diskpart)
	if source/*.wim > 4GB : Dism /Split-Image /ImageFile:D:\sources\install.wim /SWMFile:E:\sources\install.swm /FileSize:3800 (and then remove org-install.wim): Windows Setup automatically installs from this file, so long as you name it install.swm !
	Use File Explorer to copy and paste the entire contents of the Windows product DVD or ISO to the USB flash drive
##________________________________________  ___________________________


#####  ==========  
echo   creating USB-Boot-Installation-Media (as replacement for DVD/CD-Install-Media, and NOT using MCT) for Win10 from the downloaded ISO-File:
	 This topic covers how to create a bootable Windows installation USB drive from a Windows 10 install-iso or -DVD:

	_______:  
so: DW first the : ISO-Datei ohne Media Creation Tool (MCT)
https://www.microsoft.com/de-de/software-download/windows10ISO
or CT:   https://www.heise.de/select/ct/2019/26/softlinks/yfvy   :   Windows 10: ISO-Datei ohne Media Creation Tool

	_______:  
C:\up1\t1\nps\2So>dir
30.03.2018  14:56     4.710.961.152    Win10_1709_German_x64.iso

	_______:  - creating USB-boot-Media-FOR-Installation (!!NOT-USB-Test-System! so NOT-running-FULL_WIn10_OS-from-USB!! ) from Win10.iso (other alternative: directly from internet into USB-Stick by Media-Creation-Tool):
https://answers.microsoft.com/de-de/windows/forum/windows_7-windows_install/problem-bei-der-erstellung-eines-bootf%c3%a4higen/74b69da3-c6ff-40b1-a226-f079f418446e
-!! partiotioning/Formattting/activation MUST be dene ONLY by diskpart, due to make it bootable (bootsect.exe)!!
    (OR directly creating the USB-boot-media by MCT), so:
	diskpart
	select disk X        (X = Nr. USB Drive)
	clean                   (Stick wird gelöscht)  ##-> clean is important! resets all MBR/boorsector on the media!
	create partition primary
	select partition 1
	active
	format fs=fat32 label="WIN10DE" quick
	assign
	Diskpart beenden.
- copy/extract the contens of the ISO-file just simply to the usb-Media (e.g. with 7zip or explorer,...)
  OR with   xcopy X:\*.* /s/e/f Y:\  ;OR with robocopy ...

	_______:  done !
- is problems setting it active, see also below nts of axv:
##________________________________________  ___________________________


#####  ==========  https://www.heise.de/ct/artikel/Partition-aktivieren-unter-Windows-10-4798946.html   :
Um einen neu partitionierten und formatierten USB-Stick unter Windows 10 bootfähig zu machen, wollte ich die erste primäre Partition auf dem Stick aktiv setzen. Das funktioniert allerdings nicht.
-Frage:   Ich habe einen USB-Stick unter Windows 10 in der Datenträgerverwaltung neu partitioniert und formatiert. Damit er bootfähig ist, wollte ich die erste primäre Partition auf dem Stick aktiv setzen. Doch der Eintrag in ihrem Kontextmenü ist ­ausgegraut.
- AW:  Das passiert, wenn der Stick als Partitionsschema nicht MBR, sondern GPT trägt – GPT kennt keine aktiven Partitionen. Das Problem kann aber auch bei MBR-partitionierten Sticks auftreten, was wir für einen Windows-Bug halten. Es passiert nämlich nach unseren Beobachtungen nur, wenn das gerade laufende Windows per UEFI bootete statt klassisch (Legacy BIOS). Dann will die Datenträgerverwaltung auf keinem Laufwerk eine Partition aktiv setzen, obwohl das wie bei Ihrem Stick erforderlich sein kann.
Immerhin gibt es mit dem Kommandozeilenprogramm Diskpart.exe ein weiteres Bordmittel zum Partitionieren, und das leidet nicht unter dem Bug. Eine ausführliche Einführung in Diskpart finden Sie in c’t 3/2018. Hier die Befehle in Kurzform: Drücken Sie Windows+R und tippen Sie diskpart ein. Verschaffen Sie sich mit list disk einen Überblick über die Laufwerke. Ihren Stick erkennen Sie meist an der Größe. Wenn er beispielsweise die Datenträgernummer 5 abbekommen hat, wählen Sie ihn mit select disk 5 aus. Mit detail disk bekommen Sie die Volumes auf dem Stick zu sehen, inklusive Laufwerksbuchstaben und -namen. Haben Sie den richtigen Datenträger erwischt, lassen Sie sich mit list partition die Partitionen darauf anzeigen. Suchen Sie die Partitionsnummer heraus und tippen dann select partition 1 ein (Nummer anpassen). Zum Schluss setzt der Befehl active die Partition aktiv. (axv)
##________________________________________  ___________________________


#####  ==========  see Anleitung/descp:
https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/install-windows-from-a-usb-flash-drive  :

	_______:  -- Install Windows from a USB Flash Drive : 01/31/2018
You can install Windows on a device without a DVD drive by using a USB flash drive.
Note: If you're looking for a tool that downloads Windows 10 and creates a bootable USB Windows installation drive, see Download Windows 10.
This topic covers how to create a bootable Windows installation USB drive from a Windows 10 install .iso or DVD.
- What you need:
	- Windows 10 install .iso or DVD
	- USB flash drive with at least 5GB free space. This drive will be formatted, so make sure it doesn't have any important files on it.
	- Technician PC (1kk: Source-PC to prepare the boot-Media/Stick) - Windows PC that you'll use to format the USB flash drive
	- Destination PC - A PC that you'll install Windows on
- Step 1 - Format the drive and set the primary partition as active :
    Connect the USB flash drive to your technician PC.
    Open Disk Management: Right-click on Start and choose Disk management.
    Format the partition: Right-click the USB drive partition and choose Format. Select the FAT32 file system to be able to boot either BIOS-based or UEFI-based PCs.
    Set the partition as active: Right-click the USB drive partition and click Mark Partition as Active.
    Note :
    If Mark Partition as Active isn't available, you can instead use diskpart to select the partition and mark it active.
- Step 2 - Copy Windows Setup to the USB flash drive
    Use File Explorer to copy and paste the entire contents of the Windows product DVD or ISO to the USB flash drive.
    Optional: add an unattend file to automate the installation process. For more information, see Automate Windows Setup.
- Step 3 - Install Windows to the new PC
    Connect the USB flash drive to a new PC.
    Turn on the PC and press the key that opens the boot-device selection menu for the computer, such as the Esc/F10/F12 keys. Select the option that boots the PC from the USB flash drive.
    Windows Setup starts. Follow the instructions to install Windows.
    Remove the USB flash drive.

	_______:  -------- Troubleshooting: 
- file copy fails
	This can happen when the Windows image file is over the FAT32 file size limit of 4GB. When this happens:
	Copy everything except the Windows image file (sources\install.wim) to the USB drive (either drag and drop, or use this command, where D: is the mounted ISO and E: is the USB flash drive.)
	robocopy D: E: /s /max:3800000000
	Split the Windows image file into smaller files, and put the smaller files onto the USB drive:
	Dism /Split-Image /ImageFile:D:\sources\install.wim /SWMFile:E:\sources\install.swm /FileSize:3800
	Note, Windows Setup automatically installs from this file, so long as you name it install.swm.
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  also for the tool to create a copy of an ISO onto a USB or DVD (under Win7/8 ..) see/dw:
https://www.microsoft.com/en-us/download/details.aspx?id=56485
##________________________________________  ___________________________


#####  ==========  
