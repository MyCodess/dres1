________________ cloning-syys-shorties/qckys/... ; for _RF-protocols see syys-cloning-protocols here !! :_______________________
- here ONLY just 1coll-qckys!! for details and _RF see here cloning-protocols in arxdnts-dir !!
-!! https://wiki.archlinux.org/title/Migrate_installation_to_new_hardware
-!! https://wiki.archlinux.org/title/Rsync#Full_system_backup
##________________________________________  ___________________________


#####  ==========  syys-clones/ OS-syncs/ -qckys __CPs__: ========================================

	_______:  parts/disk:
	#_  sgdisk -o -n 1:0:+100M  -n 2:0:+3G  -n 3:0:+50G  -n 4:0:-0  -t 1:EF02  -t 2:EF00 -t 3:8300 -t 4:0700  /dev/sdb

	_______:  mkfs :
	- mkfs.vfat :
		mkfs.vfat  -v -n ESP1   -i 04B6A1D4  -c  /dev/sdb2    ##-- the param of  -i / UUID/Volume-ID  must be WITHOUT "-", so ONLY hex! so delete it from lsblk1-output !
		fsck.fat  -p  -v -V /dev/sdb2
	- mkfs.ext4:
		date;  mkfs.ext4  -L  2004ARX_P   -v  -c -U dac2d4ce-28e3-4a5c-93de-1f7f227155d9   /dev/sda9 ; date ##--iwith -cc then ca. 5 hours done !
		##--longer, ca. 20 min, if needed:   fsck.ext4  -p -D  -k -f -E optimize_extents  -c  /dev/sdb3
	- mkfs.exfat--cu-version  :
		mkfs.exfat   -L  T1FS_P   /dev/sdb4     ##-has-so-UUID-setting
		then UUID:  tune.exfat   -I  0xEBFE7889  /dev/sdb4   ##--!!-the param to -I MUST: start with 0x (for Hex) AND NO "-" !(otherwise recalculates it as minus and converting to Hex !)
		then:     fsck.exfat -p -v  /dev/sdb4
		- prev-version-of-mkfs.exfat :   mkfs.exfat  -L  T1FS_P  -i  F1B6-F574  /dev/sda10

	_______:  fsck :
	fsck.ext4  -p -D -c -k -f -E optimize_extents  /dev/sdb3

	_______:  grub-inst: Reinstall the boot loader :
	- BIOS:  grub-install  --boot-directory=/mnt/t1/  --efi-directory=/mnt/t1/  --removable --recheck  --target=i386-pc  -v    /dev/sdb    ##--for BIOS-systems or [-v] ? ;
	- UEFI:  grub-install  --boot-directory=/mnt/t1/  --efi-directory=/mnt/t1/  --removable --recheck  -v  /dev/sdb                        ##--for UEFI-systems, [-v] ?
	- vide-org  /mnt/t1/grub/grub.cfg

	_______:  rsync-cloning-syys:
	date;  rsync  -aAXHvx  --delete  /mnt/s1/   /mnt/t1 ; date ;
	-!! if doing src-online-cloning, denke an bind-mounts!! they must be excluded /OR unmounted !! otherwise willbe doubled copied !!
	--- ArxWiki : also check EXTRA nts there:
	ArxWiki--Full-system-backup-rsnyc :  https://wiki.archlinux.org/title/Rsync#Full_system_backup :
	-!! exclude also /home/*/.cache/* /OR /home/ , bind-mounts (online-cloning), /home/*/.gvfs , 
	-! consider using also (ONLY-for-offline-cloning!!):     rsync -S --whole-file --inplace ... !
    ArxWiki--Full-system-backup-rsnyc [-S] :      rsync -aAXHvx --exclude={"/dev/*","/proc/*","/sys/*","/tmp/*","/run/*","/mnt/*","/media/*","/lost+found"}  /src   /path/to/backup
    ArxWiki--Full-system-backup-rsnyc-syys[-S] :  rsync -aAXHvx --exclude={"/dev/*","/proc/*","/sys/*","/tmp/*","/run/*","/mnt/*","/media/*","/lost+found"}  --delete  --exclude={"/VARUfs/*","/UUFS1/*","/boot/*"}  /mnt/s1/  /mnt/t1/ ;
    This approach works well for migrating an existing installation to a new hard drive or SSD.
	- more excludes:
		/home/*/.gvfs (if GVFS installed! otherwise rsync errors!) /OR /home/ fully zunaechst !?
		exclude swap / swap-file , if using!
		/var/lib/dhcpcd/* directory as it mounts several system directories as sub-directories there. (online-cloning)
		/home/ fully, or at least /home/*/.cache/*  /home/*/Trash/* ,  /home/*/.gvfs , /home/*/.thumbnails/* , ... !!
	- excludes are because they are populated on boot, but the directories themselves are NOT created. /lost+found is filesystem-specific.
	!! bind-mounts:  If there are any bind mounts in the system, they should be excluded as well so that the bind mounted contents is copied only once.
	! The command above depends on brace expansion available in both the bash and zsh shells. When using a different shell, --exclude patterns should be repeated manually.
	-1kk:  /OR just exclude the above DIRs fully, and after rsync then mkdir ... in new-syys as root !

	_______:  cmds:
	-! grub.cfg, fstab,  mkinitcpio -P , ...
	vide-org  /mnt/t1/grub/grub.cfg
	vide-org  /mnt/t1/etc/fstab
	mkinitcpio -P  ##-! https://wiki.archlinux.org/title/Mkinitcpio#Image_creation_and_activation
	NWs / wpa : see setup0-nts !
	 --- more...:
	journalctl -k --grep=microcode  ##--check uploading of microcodes
	alsamixer volume  ##-- Reconfigure audio
