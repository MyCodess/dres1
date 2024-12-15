rem https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/capture-and-apply-windows-using-a-single-wim?view=windows-11
rem Capture and apply a Windows image using a single .WIM file
rem Sample script :
rem Below is an simple sample script that applies an image to a disk that's been partitioned using one of the hard disk partitioning scripts from step 2.

rem Part-Letters:  In these DiskPart examples, the partitions are assigned the letters: System=S, Windows=W, and Recovery=R because these are the letters assigned by CreatePartitions-UEFI.txt and CreatePartitios-BIOS.txt.
rem
rem =================== == capture image:  ==========================
rem Dism /Capture-Image /ImageFile:"D:\Images\Fabrikam.wim" /CaptureDir:C:\ /Name:Fabrikam

rem =================== go to the new/target-PC and boot with WInPE/WinToGo to appy image offline!: ============
rem === partition the new disk:    diskpart /s CreatePartitions-UEFI.txt  bzw. diskpart /s CreatePartitions-BIOS.txt  ##-see the scripty there  ##-see the scripty there!!

rem =================== == ApplyImage.bat == ==========================
rem == These commands deploy a specified Windows image file to the Windows partition, and configure the system partition.
rem Usage: ApplyImage WimFileName
rem Example: ApplyImage E:\Images\ThinImage.wim ==

rem == Set high-performance power scheme to speed deployment ==
call powercfg /s 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c
rem == Apply the image to the Windows partition ==
dism /Apply-Image /ImageFile:%1 /Index:1 /ApplyDir:W:\
rem == Copy boot files to the System partition ==
W:\Windows\System32\bcdboot W:\Windows /s S:
:rem == Copy the Windows RE image to the
:rem Windows RE Tools partition ==
md R:\Recovery\WindowsRE
xcopy /h W:\Windows\System32\Recovery\Winre.wim R:\Recovery\WindowsRE\
:rem == Register the location of the recovery tools ==
W:\Windows\System32\Reagentc /Setreimage /Path R:\Recovery\WindowsRE /Target W:\Windows
:rem == Verify the configuration status of the images. ==
W:\Windows\System32\Reagentc /Info /Target W:\Windows
rem ====================== _END_ ==========================================

