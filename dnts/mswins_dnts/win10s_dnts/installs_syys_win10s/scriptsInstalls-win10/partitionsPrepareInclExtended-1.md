rem  for UEFI/gpt-parts see:  https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/configure-uefigpt-based-hard-drive-partitions?view=windows-11
rem  for BIOS/mbr-parts see:  https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/configure-biosmbr-based-hard-drive-partitions?view=windows-11
rem  for BIOS/mbr-parts + Extended-part :  https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/configure-more-than-four-partitions-on-a-biosmbr-based-hard-disk?view=windows-11
rem  USAGE1:  DiskPart /s F:\CreatePartitions-XXXX.txt
rem  Disk must be dos for BIOS in mswins  AND gpt for UEFI!! so if needed do: select disk x ; convert mbr ; ##-bzw. for UEFI: convert gpt ;
rem  assigned drive-letters here :    System--BCD=S, Windows--boot=W, and Recovery--WinRE=R 
rem  1kk: in mbr-parts try: system_BCD-part as fat32 (then must create extra recovery-part, so not integrated recovery-part into system_BCD-part !)
rem ########################## BIOS/mbr parts: more than 4 parts on mbr-/dos-disk, incl. extended-part: ###################
rem  https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/configure-more-than-four-partitions-on-a-biosmbr-based-hard-disk?view=windows-11
rem  PrepareMyPartitions.txt
rem  assigned drive-letters here :    System--BCD=S, Windows--boot=W, and Recovery--WinRE=R 
rem  parts:   system_BCD=S, two primary data/utilities-parts, extended: Windows=W, and Recovery=R ; NO MSR-part is required in mbr-/dos-disks !
select disk 0
clean
rem 1kk-add:
convert mbr  
rem == 1. System partition ======================
create partition primary size=100
format quick fs=ntfs label="System"
assign letter="S"
active
rem == 2. Utility partition =====================
create partition primary size=100
format quick fs=ntfs label="Utility1"
assign letter="U"
set id=27
rem == 3. Utility partition =====================
create partition primary size=200
format quick fs=ntfs label="Utility2"
assign letter="V"
set id=27
rem == 4. Extended partition ====================
create partition extended
rem == 4a. Windows partition ====================
rem ==    a. Create the Windows partition =======
create partition logical
rem ==    b. Create space for the recovery tools  
rem       ** Update this size to match the size of
rem          the recovery tools (winre.wim)
rem          plus some free space.
shrink minimum=500
rem ==    c. Prepare the Windows partition ====== 
format quick fs=ntfs label="Windows"
assign letter="W"
rem == 4b. Recovery tools partition ==============
create partition logical
format quick fs=ntfs label="Recovery"
assign letter="R"
set id=27
list volume
exit
rem ########################## BIOS/mbr parts:defaullt-wins, three parts: BCD-system, win, recovery ! no-extended: ####################
rem  https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/configure-biosmbr-based-hard-drive-partitions?view=windows-11
rem  USAGE1:   DiskPart /s F:\CreatePartitions-BIOS.txt
rem  parts:   system_BCD=S, Windows=W, and Recovery=R ; NO MSR-part in mbr requred!
rem == CreatePartitions-BIOS.txt ==
rem == These commands are used with DiskPart to
rem    create three partitions
rem    for a BIOS/MBR-based computer.
rem    Adjust the partition sizes to fill the drive
rem    as necessary. ==
select disk 0
clean
rem 1kk-add:
convert mbr  
rem == 1. System partition ======================
create partition primary size=100
format quick fs=ntfs label="System"
assign letter="S"
active
rem == 2. Windows partition =====================
rem ==    a. Create the Windows partition =======
create partition primary
rem ==    b. Create space for the recovery tools  
rem       ** Update this size to match the size of
rem          the recovery tools (winre.wim)
rem          plus some free space.
shrink minimum=650
rem ==    c. Prepare the Windows partition ====== 
format quick fs=ntfs label="Windows"
assign letter="W"
rem == 3. Recovery tools partition ==============
create partition primary
format quick fs=ntfs label="Recovery"
assign letter="R"
set id=27
list volume
exit
rem ########################## UEFI/gpt parts:defaullt-wins, three parts: BCD-system, win, recovery ###################################
rem  https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/configure-uefigpt-based-hard-drive-partitions?view=windows-11
rem  https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/oem-deployment-of-windows-desktop-editions-sample-scripts?preserve-view=true&view=windows-10#-createpartitions-uefitxt
rem  parts:   system_BCD=S, MSR no-letter,  Windows=W, and Recovery=R ;  The MSR partition does not receive a drive letter. in gpt is MSR reuired!
rem  This layout lets you use Windows BitLocker Drive Encryption through both Windows and through the Windows Recovery Environment.
rem  USAGE1:   DiskPart /s F:\CreatePartitions-UEFI.txt
rem == CreatePartitions-UEFI.txt ==
rem == These commands are used with DiskPart to
rem    create four partitions
rem    for a UEFI/GPT-based PC.
rem    Adjust the partition sizes to fill the drive
rem    as necessary. ==
select disk 0
clean
convert gpt
rem == 1. System partition =========================
create partition efi size=100
rem    ** NOTE: For Advanced Format 4Kn drives,
rem               change this value to size = 260 ** 
format quick fs=fat32 label="System"
assign letter="S"
rem == 2. Microsoft Reserved (MSR) partition =======
create partition msr size=16
rem == 3. Windows partition ========================
rem ==    a. Create the Windows partition ==========
create partition primary 
rem ==    b. Create space for the recovery tools ===
rem       ** Update this size to match the size of
rem          the recovery tools (winre.wim)
rem          plus some free space.
shrink minimum=500
rem ==    c. Prepare the Windows partition ========= 
format quick fs=ntfs label="Windows"
assign letter="W"
rem === 4. Recovery partition ======================
create partition primary
format quick fs=ntfs label="Recovery"
assign letter="R"
set id="de94bba4-06d1-4d40-a16a-bfd50179d6ac"
gpt attributes=0x8000000000000001
list volume
exit
