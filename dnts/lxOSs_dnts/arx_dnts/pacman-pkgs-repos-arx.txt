______________________ pacman + Repos in arx : _________________________________
##________________________________________  ___________________________


#####  ==========  misc_1cu:
	-!! GPG-KeyRing-updating :  pacman -Sy archlinux-keyring && pacman -Su ;
	-!! if ERROR-updates, then:   rm -rf /var/lib/pacman/sync ;   ##--if ERROR:  "error: GPGME error: No data ; error: failed to synchronize all databases (invalid or corrupted database (PGP signature))"
##________________________________________  ___________________________


#####  ==========  Vocabs/DIFFs/DEFs-pacman:

	-!! pkgs types/locations DEFs:    installed/All-Repos/Local-packs/System-OS-managed/-packages  bzw. short/in-aliases  {i/a/l/s}pkg == {ins/all/loc/sys}Pkgs :
		- insPkgs  / ipkgs	:  installed-pkgs in the current syss/OS/System/PC , locally usable ;
		- allPkgs  / apkgs 	:  All-Remote-Repos-Pkgs in all sync-Repos , online, ... , all existing possible pkgs in remote Repos ... ;
		--- uue-addies:
		- sysPkgs-DIRs  / spkgs :  from syss/OS/System managed DIRs for Pkgs , as: /var/lib/pacman/ , ....
		+ locPkgs-DIRs  / lpkgs	:  local-packs-DPs as packs/... , or local-mirrors/repos as mirror1/repos1 , .... 
	- "(Package) Databases" of pacman/repos == *.db-files :  as core.db , extra.db , custom1.db ... :
		simple zip/tar files caontainting ONLY text-infos about its packages ! just unpack eg core.db and see containing text-info files of core-Repo
		these DBs are syncable! 
	- "local (package) databases" of pacman/repos :  locally-saved .db-files  in  /var/lib/pacman/sync/core.db  db1.db  extra.db ...    , only-infos/descp-of-pkgs:
		/var/lib/pacman/    : default-location! changable with:   pacman -b, --dbpath <path> #eg for a backuped/rescue syss !
		small-infos-descp-text-/tgz-files locally stored in  /var/lib/pacman/  about all-pkgs of all repos defined in /etc/pacman.conf !
		remote-repos-pkg-infos in  /var/lib/pacman/sync/   , as core.db  db1.db  extra.db ... , just the .db-files are copied there from remote repos; are tgz-files, 
		local-repos-pkg-infos  in  /var/lib/pacman/local/  , one-dir-per-pkg with descp/fileslisting/... as text-files!
		The pacman synced-databases are normally located at /var/lib/pacman/sync . For each repository specified in /etc/pacman.conf there will be a corresponding database file located there. Database files are tar-gzipped archives containing one directory for each package.  https://wiki.archlinux.org/index.php/Pacman
	- "local (package) cache" of pacman/repos :    /var/cache/pacman/pkg/  full-pkgs-copied-from-remoteRepos-here! : 
		Pacman stores its downloaded packages in /var/cache/pacman/pkg/ and does not remove the old or uninstalled versions automatically. 
		A package that has been uninstalled can easily be reinstalled directly from the cache folder, not requiring a new download from the repository.  https://wiki.archlinux.org/index.php/Pacman
		delete cache:  man  paccache
	- pacman sync repositories  :  remote repos of /etc/pacman.conf  which are used by pacman cmdline!
	- pacman sync database  :   list of all possible packages (in Repos, determined by the repositories enabled in /etc/pacman.conf).
	-! DIFF  The local database is the list of all installed packages, the sync database is the list of all possible packages (determined by the repositories enabed in /etc/pacman.conf).
##________________________________________  ___________________________


#####  ==========  docs:

	_______:  Pacmans :
	https://wiki.archlinux.org/index.php/Pacman
	https://wiki.archlinux.org/index.php/Pacman/Tips_and_tricks
	man pacman(8) pacman.conf(5) repo-add(8) libalpm(3)

	_______:  Repos:
	https://wiki.archlinux.org/index.php/Pacman#Repositories_and_mirrors
	https://wiki.archlinux.org/index.php/Official_repositories

	_______:  pkgs:
	https://www.archlinux.org/groups/
	https://wiki.archlinux.org/index.php/Offline_installation_of_packages   #---> also in core.db ....
##________________________________________  ___________________________


#####  ==========  pacman-pathes/files-configs :
-!! see the /etc/pacman.conf comments for listing of all default dirs and changes ... ! /OR
-!!  pacman -v   ##--just-no-params! then lists all cu-DIRs of pacman ! :
	[u1@2004arx 2So]$ pacman -v
	Root      : /
	Conf File : /etc/pacman.conf
	DB Path   : /var/lib/pacman/
	Cache Dirs: /var/cache/pacman/pkg/
	Hook Dirs : /usr/share/libalpm/hooks/  /etc/pacman.d/hooks/
	Lock File : /var/lib/pacman/db.lck
	Log File  : /var/log/pacman.log
	GPG Dir   : /etc/pacman.d/gnupg/
	Targets   : None

	_______:  ! logs:  /var/log/pacman.log

	_______:  conf/runtime:
/etc/pacman.conf     ##/OR  pacman  --config <file>  :Specify an alternate configuration file.
/etc/pacman.d/
/etc/pacman.d/mirrorlist  ---> edit it and put neares as FIRST/oben !

	_______:  DBs locally (sync DBs):   see https://wiki.archlinux.org/index.php/Pacman :
/var/lib/pacman/        :  database location (the default is /var/lib/pacman) , can be changey by param: pacman -b, --dbpath <path>
/var/lib/pacman/sync    :  pacman databases (as core.db , db1.db ...) ; For each repository specified in /etc/pacman.conf there will be a corresponding database file located there. Database files are tar-gzipped archives containing one directory for each package. 
/var/lib/pacman/local/  :  locally-installed-pkgs-infos/DBs (are simple text/zip-files als DBs !)

	_______:  cache locally (of installed pkgs):   see https://wiki.archlinux.org/index.php/Pacman :
/var/cache/pacman/pkg   ##/OR  pacman   --cachedir <dir>  :  Specify an alternative package cache location (the default is /var/cache/pacman/pkg) ....

	_______:  utils/cmds/pkg/...-pacman:
-!! check pkg-search:   https://www.archlinux.org/packages/?q=pacman
pacman -S expac fzf pacutils   pacman-contrib     expac pkgfile
- more :
	pacutils
	pacman-conf   is a utility for parsing the pacman configuration file and returning script-friendly
	pacman-contrib
	paccache , pactree , 
	expac	:	pacman database extraction utility
	pkgfile	:  Description:	a pacman .files metadata explorer ; pkgfile is a tool for searching files from packages in the official repositories.   https://wiki.archlinux.org/index.php/Pkgfile
-!! listing of all /bin/-files of pacman-packages:
	pacman -Ql  pacman  pacman-contrib   |  grep 'bin/'             : see all bin-files in packages of pacman,.. as:  pactree makepkg  vercmp
	The pacman package contains tools such as makepkg and vercmp(8). Other useful tools such as pactree and checkupdates are found in pacman-contrib (formerly part of pacman).
	Run pacman -Ql pacman pacman-contrib | grep -E 'bin/.+' to see the full list.  see:  https://wiki.archlinux.org/index.php/Pacman
##________________________________________  ___________________________


#####  ==========  cache /  clear pac-cache: 
https://wiki.archlinux.org/title/Pacman#Cleaning_the_package_cache

	_______:  clear pac-cache:
	- pacman -Sc    #delete-older-ones  ,so: except currently-installed-pkgs, delete the rest of pac-cache (older/obsol/prev/... pkgs)
	- pacman -Scc   #delete-all, so empty-cache ! /OR  paccache ... !
	- man  paccache  ...
	- /OR  Enable and start paccache.timer / paccache.service  to discard unused packages weekly. https://wiki.archlinux.org/index.php/Pacman#Cleaning_the_package_cache

	_______:  
##________________________________________  ___________________________


#####  ==========  pacman-qckys-params  (see manpage)  :

	_______:  sesrch/query/listing/infos about ppkgs:  pacman -Qxxxx:
-l, --list   List all files owned by a given package.
-g, --groups Display all packages that are members of a named group.
-i, --info   Display information on a given package. The -p option can be used if querying a package file instead of the local database. 
-p, --file   Signifies that the package supplied on the command line is a file and not an entry in the database. The file will be decompressed and queried. This is useful in combination with --info and --list.
-ip, --info  Display information on a package file (locally there) instead of the local database. 
-s, --search <regexp>    Search each locally-installed package for names or descriptions that match regexp.
-Fl, --list   List the files owned by the queried package.

	_______:  install:   pacman -Sxxx  :
-l, --list    List all packages in the specified repositories. Multiple repositories can be specified on the command line.
-w, --downloadonly    Retrieve all packages from the server, but do not install/upgrade anything.

	_______:  Databases, pacman -Dxxx:
k, --check    Check the local package database is internally consistent. This will check all required files are present and that installed packages have the required dependencies ...
##________________________________________  ___________________________


#####  ==========  upgradings/updatings:
-!! Avoid doing partial upgrades. In other words, never run pacman -Sy; instead, always use pacman -Syu  ! https://wiki.archlinux.org/index.php/System_maintenance#Upgrading_the_system
##________________________________________  ___________________________


#####  ==========  mirrors-nts:

	_______:  --!! date-fixing bzw. Downgrading/restore_all_packages_to_a_specific_date and NO-newer-updates for now any more:
	(so NO-updated-pks newer than xx !!/OR even OS1-zurcueck-setzeni/Downgrade auf ein bestimmtes Datum/Stand! eg after a broken/unhappy upgrade!):
	https://wiki.archlinux.org/index.php/Arch_Linux_Archive#How_to_restore_all_packages_to_a_specific_date
	https://wiki.archlinux.org/index.php/downgrading_packages
	-! as Server/mirror-entry works ONLY with archive.archlinux.org !! other mirrors have NO historical archives !!
	mv /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist_1org , and new file: vi /etc/pacman.d/mirrorlist with ONLY one-line:
	Server = https://archive.archlinux.org/repos/2020/02/13/$repo/os/$arch  ##--delete the rest of mirrors
	!! Dates-Listing-URLs:   https://archive.archlinux.org/repos/  ##---> listing of ALL dates! just copy/get the URL from there!!
	-!! Then update the database and force downgrade:     pacman -Syyuu
##________________________________________  ___________________________


#####  ==========  Repos-offline/Locally, Repos-adding  , Custom-Repos :
	-!! your-own-offline-local-collection-of-pkgs-on-HD:   https://wiki.archlinux.org/index.php/Pacman/Tips_and_tricks#Installing_packages_from_a_CD/DVD_or_USB_stick  
	-!! In order to use a repository after adding it, you will need to upgrade the whole system first. : pacman -Syu 
	-! see also   https://wiki.archlinux.org/index.php/Offline_installation_of_packages   for offline core.db ....
	-!! to see sizes /OR gesamt-size: http://ftp.tu-chemnitz.de/pub/linux/archlinux/pool/community/  /OR http://ftp.tu-chemnitz.de/pub/linux/archlinux/pool/
	  by chemnitz the core/extra stuff are ONLY links to .../rchlinux/pool/ ; so the sizes are NOT real !!

	_______:  Network_shared_pacman_cache maybe better than local-repo!?!?:   https://wiki.archlinux.org/index.php/Pacman/Tips_and_tricks#Network_shared_pacman_cache
	reusing/sharing/mounting /var/cache/pacman/pkg between NPs/PCs (NOT-as-link! must be physical-dir! so mount/share it! 
	AND  add this entry in the [options] section of /etc/pacman.conf:   CleanMethod = KeepCurrent
	In order to share packages between multiple computers, simply share /var/cache/pacman/ using any network-based mount protocol.
	Do not make /var/cache/pacman/pkg or any of its ancestors (e.g., /var) a symlink. Pacman expects these to be directories. When pacman re-installs or upgrades itself, it will remove the symlinks and create empty directories instead.
	-! see  sharing/reusing Read-write pacman-cache between PCs instead  local-repo:  https://wiki.archlinux.org/index.php/Pacman/Tips_and_tricks#Network_shared_pacman_cache
	-! also manpage:   --cachedir <dir>  :  Specify an alternative package cache location (the default is /var/cache/pacman/pkg). Multiple cache directories can be specified, and they are tried in the order they are passed to pacman. NOTE: This is an absolute path, and the root path is not automatically prepended.

	_______:  -- USB-/CD-local-Repo:  ------ Installing packages from a CD/DVD or USB stick :
 https://wiki.archlinux.org/index.php/Pacman/Tips_and_tricks#Installing_packages_from_a_CD/DVD_or_USB_stick  :
Notes: Use as an example and avoid duplication (Discuss in Talk:Pacman/Tips and tricks#)
- To download packages, or groups of packages:
# mkdir  ~/Packages ;  cd ~/Packages
# pacman -Syw base base-devel grub-bios xorg gimp .... --cachedir  ~/Packages/ 
# repo-add    ./custom.db.tar.gz    ./*
- Then you can burn the "Packages" folder to a CD/DVD or transfer it to a USB stick, external HDD, etc.
- To install on target PC:
1. Mount the media: # mkdir /mnt/repo # mount /dev/sr0 /mnt/repo    #For a CD/DVD.  # mount /dev/sdxY /mnt/repo   #For a USB stick.
2. Edit pacman.conf and add this repository before the other ones (e.g. extra, core, etc.).
   This is important. Do not just uncomment the one on the bottom. This way it ensures that the files from the CD/DVD/USB take precedence over those in the standard repositories:
	/etc/pacman.conf
	[custom]
	SigLevel = PackageRequired
	Server = file:///mnt/repo/Packages
3. Finally, synchronize the pacman database to be able to use the new repository: # pacman -Syu

	_______:  -- Custom local repository
- Use the repo-add script included with pacman to generate a database for a personal repository. Use repo-add --help for more details on its usage. A package database is a tar file, optionally compressed. Valid extensions are .db or .files followed by an archive extension of .tar, .tar.gz, .tar.bz2, .tar.xz, .tar.zst, or .tar.Z. The file does not need to exist, but all parent directories must exist.
- To add a new package to the database, or to replace the old version of an existing package in the database, run: 
	# repo-add  /path/to/repo.db.tar.gz    /path/to/package-1.0-1-x86_64.pkg.tar.xz
The database and the packages do not need to be in the same directory when using repo-add, but keep in mind that when using pacman with that database, they should be together. Storing all the built packages to be included in the repository in one directory also allows to use shell glob expansion to add or update multiple packages at once:
	# repo-add   /path/to/repo.db.tar.gz    /path/to/*.pkg.tar.xz

	_______:  -- wget-DWs/local-mirroing of repos :
	##---> get/copy them sowehere accessbile during the setup!  eg : USB1_P4/00stg1/mirror1/
	mkdircd   /USB1_P4/00stg1/mirror1/core1 ;
	wget   -e robots=off   -N -nd -np -r  --spider        http://ftp.spline.inf.fu-berlin.de/mirrors/archlinux/core/os/x86_64/   ##--dry
	wget   -e robots=off   -N -nd -np -r  -o  core1.log   http://ftp.spline.inf.fu-berlin.de/mirrors/archlinux/core/os/x86_64/
	mkdircd   /USB1_P4/00stg1/mirror1/extra1 ;
	wget   -e robots=off   -N -nd -np -r  -o  extra1.log  http://ftp.spline.inf.fu-berlin.de/mirrors/archlinux/extra/os/x86_64/
	--- add-nts:
	?? works that to NOT dw cuda* (2 GB)??:  --exclude-directories=*cuda* ?? --> try it
	-!! to see sizes /OR gesamt-size: http://ftp.tu-chemnitz.de/pub/linux/archlinux/pool/community/  /OR http://ftp.tu-chemnitz.de/pub/linux/archlinux/pool/
	  by chemnitz the core/extra stuff are ONLY links to .../rchlinux/pool/ ; so the sizes are NOT real !!
##________________________________________  ___________________________


#####  ==========  
--###################### coll for pkgs/repos/... : ################################################
##________________________________________  ___________________________


#####  ==========  ISO-arx-pkgs-listing (in iso file) /_200300 :
https://git.archlinux.org/archiso.git/tree/configs/releng/packages.x86_64
path: root/configs/releng/packages.x86_64
blob: 46febfd8c3b6d3ae88108bf95604a653c2749f1a (plain)
1  - arch-install-scripts
2  - b43-fwcutter
3  - broadcom-wl
4  - btrfs-progs
5  - clonezilla
6  - crda
7  - darkhttpd
8  - ddrescue
9  - dhclient
10 - dhcpcd
11 - dialog
12 - diffutils
13 - dmraid
14 - dnsmasq
15 - dnsutils
16 - dosfstools
17 - elinks
18 - ethtool
19 - exfat-utils
20 - f2fs-tools
21 - fsarchiver
22 - gnu-netcat
23 - gpm
24 - gptfdisk
25 - grml-zsh-config
26 - grub
27 - hdparm
28 - ipw2100-fw
29 - ipw2200-fw
30 - irssi
31 - iwd
32 - jfsutils
33 - lftp
34 - linux-atm
35 - linux-firmware
36 - lsscsi
37 - lvm2
38 - man-db
39 - man-pages
40 - mc
41 - mdadm
42 - mtools
43 - nano
44 - ndisc6
45 - netctl
46 - nfs-utils
47 - nilfs-utils
48 - nmap
49 - ntfs-3g
50 - ntp
51 - openconnect
52 - openssh
53 - openvpn
54 - partclone
55 - parted
56 - partimage
57 - ppp
58 - pptpclient
59 - refind-efi
60 - reiserfsprogs
61 - rp-pppoe
62 - rsync
63 - sdparm
64 - sg3_utils
65 - smartmontools
66 - sudo
67 - tcpdump
68 - testdisk
69 - usb_modeswitch
70 - usbutils
71 - vi
72 - vim-minimal
73 - vpnc
74 - wget
75 - wireless-regdb
76 - wireless_tools
77 - wpa_supplicant
78 - wvdial
79 - xfsprogs
80 - xl2tpd
##________________________________________  ___________________________


#####  ==========  ================================================================
