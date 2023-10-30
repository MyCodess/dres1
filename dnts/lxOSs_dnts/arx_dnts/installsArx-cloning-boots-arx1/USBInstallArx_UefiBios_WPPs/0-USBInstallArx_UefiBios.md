_________________ bootable-USB-stick-creation for both EFFI+MBR , and  arx-install on it . ________________________

	_______:  docs:
    - !! https://wiki.archlinux.org/title/Install_Arch_Linux_on_a_removable_medium
    - ! https://wiki.archlinux.org/title/Multiboot_USB_drive#Hybrid_UEFI_GPT_+_BIOS_GPT/MBR_boot  ---> partitioning + formating !
    - ! http://valleycat.org/linux/arch-usb.html
    - for several ISO/OS on one stick to boot alternatively ...: https://wiki.archlinux.org/title/Multiboot_USB_drive
    -- for infos also about system-cloning/migration see:
    - https://wiki.archlinux.org/index.php/Migrate_installation_to_new_hardware
    - https://wiki.archlinux.org/index.php/Migrating_between_architectures
##________________________________________  ___________________________


#####  ==========  partitioning+formating forHybrid UEFI GPT + BIOS GPT/MBR boot :
    -!! see  https://wiki.archlinux.org/title/Multiboot_USB_drive#Hybrid_UEFI_GPT_+_BIOS_GPT/MBR_boot :

    _______:  1--- partitioning:   see the next section below, the gdisk-protocoll !!
    - GPT part-table ! gdisk --> o , ...
    - need at lease 3 partitions, 1kk: 4 parts incl. T1FS (see protocol in above link! ) :
    1- A BIOS boot partition (gdisk type code EF02). This partition must be 1 MiB in size --> NOT-format-it !
    2- An EFI System partition (gdisk type code EF00 with a FAT32 filesystem). This partition can be as small as 40 MiB.
    3- Your OS/arx1 partition (use a filesystem supported by GRUB). This partition can take up the rest of the space of your drive. /ext4 , 8300
    4- your data part: T1FS / exfat , 0700  Microsoft basic data
    --  /:230809  : now ext4/OS etwas kleiner:
    Number  Start (sector)    End (sector)  Size       Code  Name  
    1            2048          206847   100.0 MiB   EF02  BIOS boot partition
    2          206848         6291456   2.9 GiB     EF00  EFI system partition
    3         6293504        83886080   37.0 GiB    8300  Linux filesystem
    4        83888128       244455423   76.6 GiB    0700  Microsoft basic data

    _______:  2--- formating:
    (the steps of valleycat.org a bit diifferent, but probably better!? the mountpoint there is /boot insted /boot/EFI for ESP-part !) :
    - part-1 /BIOS :  NOT-formatting  /dev/sdX1 , 
    - part-2 /EFI  :  mkfs.fat   -F32  -n ESP1 /dev/sdX2      ##--ESP : EFI system partition
    - part-3 /OS   :  mkfs.ext4  -L  2004ARX_P  /dev/sdX3    ##--OS-arx-part + data-up1-ext4
    - part-4 /T1FS :  mkfs.exfat -L  T1FS_P   /dev/sdX4 

    _______:  3--- GRUB-installing (ONLY from INSEIDE-new-System! so, after chroot to it!) for both EFFI+MBR , making bootable-usb-stick:
    - for USB/removable boot-Medias:    https://www.gnu.org/software/grub/manual/grub/grub.html#Installing-GRUB-using-grub_002dinstall  :
	For removable installs you have to use --removable and specify both --boot-directory (kk: for Lagacy-BIOS) and --efi-directory (kk: for UEFI): 
	grub-install --efi-directory=/mnt/usX --boot-directory=/mnt/usX/boot --removable
--
You can now install GRUB to support both EFI + GPT and BIOS + GPT/MBR. The GRUB configuration (--boot-directory) can be kept in the same place.
First, you need to mount the EFI system partition and the data partition of your USB drive.
An example of this would be as follows:
# mount /dev/sdX3 /mnt       ##--new-syssOS-part
# mkdir -p /mnt/boot/EFI     ##--mount-point for EFI-part
# mount /dev/sdX2 /mnt/boot/EFI
##!! the  grub-install cmds MUST be done later after chroot!! here jus as nts from  .../Multiboot_USB_drive :
	grub-install for EFI-part works ONLY from inside of the target system (so after arch-chroot bzw. manualy mount --bind /dev /mnt/dev ,.., and chroot /mnt bash ; ...)
	-! CT: Dazu müssen Sie zuerst ein Rettungs- oder Live-Linux mit UEFI-Mechanismen starten. Mounten Sie damit die Root-Partition des installierten Linux (beispielsweise in /mnt/),um die Pseudo-dateisysteme /dev/, /dev/ptc/ /sys/ und /proc/ per Bind-Mount darunter einzuhängen – etwa mit Befehlen wie mount --bind /dev/ /mnt/dev/. Wechseln Sie anschließendper chroot in die so eingerichtete Dateisystemumgebung des installierten Linux, um dort noch alle in der Fstab definierten Dateisysteme per mount -a zu mounten (auch die ESP-part,which musst be in fstab). ERST dann hängt auch auch die ESP an der vorgesehenen Stelle, womit alles bereit für grub-install ist.
	-Then after chroot to the target system, you can install GRUB for UEFI with:
	-In most cases EFI_MOUNTPOINT will correspond to the /mnt/boot/EFI subdirectory on your mounted USB disk.
# grub-install --target=x86_64-efi --recheck --removable --efi-directory=/EFI_MOUNTPOINT --boot-directory=/DATA_MOUNTPOINT/boot  ##--d.h.:
# grub-install --target=x86_64-efi --recheck --removable --efi-directory=/mnt/boot/EFI/   --boot-directory=/mnt/boot/
	-And for MBR-BIOS with:
# grub-install --target=i386-pc --recheck --boot-directory=/DATA_MOUNTPOINT/boot /dev/sdX    ##--d.h.:
# grub-install --target=i386-pc --recheck --boot-directory=/mnt/boot /dev/sdX    ##--d.h.:
	-As an additional fallback, you can also install GRUB on your MBR-bootable data partition:
# grub-install --target=i386-pc --recheck --boot-directory=/DATA_MOUNTPOINT/boot /dev/sdX3

	_______:  CPU-microcodes (Intel , AMD):
	- see https://wiki.archlinux.org/index.php/Microcode :
	-! For Arch Linux on a removable drive, which could be run on any of these processors, install both packages and add both microcode files as initrd to the boot loader configuration. Their order does not matter as long as they both are specified before the initramfs image.
##________________________________________  ___________________________


#####  ==========  partitioning-/gdisk-protocoll + formatting of  DISK-usb-128GB-tiny-black-hackenForm:
- for BIOS/GPT-combination (as your x13/x17 + GPT-Medias) see:  https://wiki.archlinux.org/index.php/GRUB#GUID_Partition_Table_(GPT)_specific_instructions
root@x13:~# date
Thu Mar 19 14:11:17 CET 2020
root@x13:~# gdisk  -l /dev/sdc
GPT fdisk (gdisk) version 1.0.3
Partition table scan:
  MBR: protective
  BSD: not present
  APM: not present
  GPT: present
Found valid GPT with protective MBR; using GPT.
Disk /dev/sdc: 240353280 sectors, 114.6 GiB
Model: Ultra Fit       
Sector size (logical/physical): 512/512 bytes
Disk identifier (GUID): 4E2AC71A-391A-44B7-ADBB-14BADB4D651F
Partition table holds up to 128 entries
Main partition table begins at sector 2 and ends at sector 33
First usable sector is 34, last usable sector is 240353246
Partitions will be aligned on 2048-sector boundaries
Total free space is 2014 sectors (1007.0 KiB)
Number  Start (sector)    End (sector)  Size       Code  Name
   1            2048          206847   100.0 MiB   EF02  BIOS boot partition
   2          206848         8595455   4.0 GiB     EF00  EFI System
   3         8595456       113453055   50.0 GiB    8300  Linux filesystem
   4       113453056       240353246   60.5 GiB    0700  Microsoft basic data
root@x13:~# mkfs.fat  -F32  -n ESP1 /dev/sdc2
mkfs.fat 4.1 (2017-01-24)
root@x13:~# mkfs.ext4  -L  2004ARX_P  /dev/sdc3
mke2fs 1.44.1 (24-Mar-2018)
Creating filesystem with 13107200 4k blocks and 3276800 inodes
Filesystem UUID: 6e76c744-2da1-49d5-bc9f-9dfc6306d835
Superblock backups stored on blocks: 
	32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208, 
	4096000, 7962624, 11239424
Allocating group tables: done                            
Writing inode tables: done                            
Creating journal (65536 blocks): done
Writing superblocks and filesystem accounting information: done   
root@x13:~# 
root@x13:~# mkfs.vfat -n T1FS_P /dev/sdc4
mkfs.fat 4.1 (2017-01-24)
root@x13:~# 
##________________________________________  ___________________________

