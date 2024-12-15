rem ########################## X13-new-win10-setup : BIOS/mbr parts: more than 4 parts on mbr-/dos-disk, incl. extended-part: ###################
rem /_220918 : worked-OK for X13-frisch-new-install of Win10; before USB-setup x13-Disk partitioned with this script-lines, but manually done commands !
rem  https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/configure-more-than-four-partitions-on-a-biosmbr-based-hard-disk?view=windows-11
rem  USAGE1:  DiskPart  /s  PrepareMyPartitions-x13.txt
rem  assigned drive-letters here :    System--BCD=S, Windows--boot=W, and Recovery--WinRE=R  ; NO MSR-part is required in mbr-/dos-disks !
select disk 0
clean
convert mbr  
rem == 1. System_BCD partition ============================
create partition primary size=4000
format quick fs=fat32 label="Sys_BCD"
assign letter="S"
active
rem == 2. Windows partition =======
create partition primary size=100000
format quick fs=ntfs label="Win_a"
assign letter="W"
rem == 3. Windows-2 partition =======
create partition primary size=110000
format quick fs=ntfs label="Win_b"
rem #############========================================##############
rem == 4. Extended partition ====================
create partition extended
rem == 5. T1FS =====================
create partition logical size=150000
format quick fs=exfat label="T1FS"
assign letter="T"
rem == 6. arx1 +... ================
create partition logical
rem == 7. WinRE, recovery-part ======
shrink minimum=4000
create partition logical
format quick fs=ntfs label="Recovery"
assign letter="R"
set id=27
rem == listing + end : ==============
list volume
exit
