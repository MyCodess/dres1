_______________ ubuntu-package-mgm APT-tools:   apt/apt-get/dpkg/.... _________________________
-!! see also   apts-dpkgs-gsets-ubts.sh  for uue-cmds_RF in  /up1/.cuue/bin/  and see also uue-aliases !!
##________________________________________  ___________________________


#####  ==========  Allg-nts:
- see man apt ,  apt-get(8), apt-cache(8), aptitude, sources.list(5), apt.conf(5), apt-config(8), The APT User's guide in /usr/share/doc/apt-doc/, apt_preferences(5), the APT Howto. 
- DIFF:   AllPkgs : all-pkgs-in-Repos+Locally   <-->  InstPkgs  :  Only-Locally-Installed-PKGs
-! llinpath apt
- backend-cmd is usu. apt-get !! apt-get is the command-line tool for handling packages, and may be considered the user's "back-end" to other tools using the APT library. Several "front-end" interfaces exist, such as aptitude(9), synaptic(8) and wajig(1).
- see   /usr/share/doc/apt-doc/

	_______:  misc:
-! installed-pkgs-details in?:  /var/lib/dpkg/available   : see man apt-cache  bzw. dpkg-query
-! listing all-availabale/installed packages with apt-show-versions:
	apt-show-versions     ##-(will be listed all installed+available and if uptodate or upgradable!
	apt-show-versions -u  ##-list only upgradable packages!
	see man apt-show-versions
    apt  list  vim*  ##--lists AllPkgs, installed + not-Installed,  vim* pkgs !

	_______:  rpmssg-/yumssg--in-ubt using apt/dpkg/.... :
rpmssg /dpkgssg == dpkg --list | grep -i
rpmslg /dpkgslg == grepi xx /var/lib/dpkg/status   ??

	_______:  -- ubt.cmds.1:
dpkg    : for listing-actions see "dpkg-query actions" in man dpkg  ; eg:   dpkg -l '*vim*' : list all installed vim-packages
aptitude    : The primary and more user-friendly front-end for dpkg is aptitude(1).
apt
apt-get

	_______:  ubt.cmds.2 /more:
dpkg-deb(1) and dpkg-query(1)
##________________________________________  ___________________________


#####  ==========  Status of Packages by pkg --list :  (ii / rc/ ....)
https://linuxprograms.wordpress.com/2010/05/11/status-dpkg-list/
$ dpkg --list   bzw.  dpkg-query -l  
....
rc  dvipdfmx                                        1:20090115-1.2                                  A DVI to PDF translator with CJK support
ii  e2fslibs                                        1.41.11-1ubuntu2                                ext2/ext3/ext4 file system libraries
....
The first column corresponds to the status of a package. How to interpret this status.  Status of every package is represented by three characters xxx
- First character: The possible value for the first character. The first character signifies the desired state, like we (or some user) is marking the package for installation
u: Unknown (an unknown state)
i: Install (marked for installation)
r: Remove (marked for removal)
p: Purge (marked for purging)
h: Hold
-Second Character: The second character signifies the current state, whether it is installed or not. The possible values are
n: Not- The package is not installed
i: Inst – The package is successfully installed
c: Cfg-files – Configuration files are present
u: Unpacked- The package is stilled unpacked
f: Failed-cfg- Failed to remove configuration files
h: Half-inst- The package is only partially installed
W: trig-aWait
t: Trig-pend
- Third Character: This corresponds to the error state. The possible value include
R: Reinst-required The package must be installed.
Now you can easily interpret what ii, pn and rc correspond to. .....
##________________________________________  ___________________________


#####  ==========  aptitude :
- many same cmds as dpkg and apt-get ,...; aptitude provides the functionality of dpkg/dselect and apt-get, as well as many additional features not found in either program.
-! MAIN-docs not in man-pages, but in  /usr/share/doc/aptitude/html/  ; man-page is shortened
- visually in terminal, just call it with no params:  aptitude
- or cmdline with params:  aptitude action [arguments...]
- eg: search all packages whose NAME contains "vim" :  aptitude search "?name(vim)"
##________________________________________  ___________________________


#####  ==========  "what package provides this file! .... : search packages for a certain file :
-!! DIFF : search among install-packages  ( dpkg -S )   <--> or among all ubuntu-pavkages from repositories ( apt-file search ... ) :
- all packages: then check it online:   http://packages.ubuntu.com/ 
- all packages cmdline: "what package provides this file (all-pkgs??)?"  : apt-file update ;   apt-file search [ --regex ] <filename_search_pattern> :
  This command acts like dlocate and dpkg -S, but searches all available packages. It answers the question, "what package provides this file?".
  search Search in which package a file is included. A list of all packages containing the pattern pattern is returned.
-  search among install-packages for a file/pattern:   dpkg -S  <search_pattern> 
##________________________________________  ___________________________


#####  ==========  apt-cache /AllPkgs-inofs :  infos about AllPkgs (installed + in.Repos). Infos are already locally saved in  "package cache" /var/lib/apt/lists/ ... :
- DEF:  "package cache" contains  (locally saved) infos about ALL-packages in all Repos (/etc/apt/sources.list ) ! and of course locally install ones! both! the infos are locally saved in "package cache" in /var/lib/apt/lists/ , ...  ; :kk--I-think-so! :
	see otput of eg (not installed yet):    apt-cache showpkg  axiom-source   ;##/OR   installed one:  apt-cache showpkg  vim-gui-common
-! apt-cache performs a variety of operations on APT's package cache. --> so AllPkgs (installed + uninstalled/in-Repo-only)
- apt-cache  dumpavail bzw. dump --> shows tech-details about ALLpkgs in Repos+locally !
- apt-cache  show  vim-gui-common  axiom-source   ##--shows infos about pkg-param in AllPkgs !
- apt-cache  search  street               ##--search for  *street* in names+description/infos of ALLPkgs
- apt-cache  search --names-only street   ##--search for  *street* in only names  of ALLPkgs
- apt-cache  pkgnames | sort > allPkgs-namesOnly---apt-cache_pkgnames.log  ##--only-names of ALLPkgs
-!! "--installed" param does NOT mean show installed-Pkgs!! but is ONLY about how showing the pkgs-DEPENDENCIES !! : man:  --installed Limit the output of depends and rdepends to packages which are currently installed !
##________________________________________  ___________________________


#####  ==========  "apt" cmdline:  NOT using in in scripts !! use apt-get /apt-cache/.... ; see man apt :
-!! see in man-page the "SCRIPT USAGE":
       The apt(8) commandline is designed as a end-user tool and it may change the output between versions. While it tries to not break
       backward compatibility there is no guarantee for it either. All features of apt(8) are available in apt-cache(8) and apt-get(8)
       via APT options. Please prefer using these commands in your scripts.
-- listing/searching All pckages/repos :
sudo apt list " pdf*    ##--> list all-packages named as pdf* !
sudo apt list "*pdf*"   ##--> list all-packages named as *pdf* ! does NOT work without "..." !!
sudo apt list "*tweak*"       --> listing only package-nams..., No-Description ; for description use "apt show ..."
sudo apt list --installed "dolph*"
sudo apt list --upgradable
-- search:
-- "show" : no-RegExp , ONLY einzelner package name
apt show tweak --> FULL-infos + descp + ... ---> rpm-long-version
-!! shwo descp of ALL pkgs (in REpos):  apt list  | sed  's/\/.*//;s/^Listing..*//' | xargs apt show > apt-show-descp-all-ok.log
##________________________________________  ___________________________


#####  ==========  apt-get  cmdline:
-! is backend for all other APT-cmds !!
apt-get -h
apt-get  --with-new-pkgs  upgrade  #--> install any new dependcies, if needed (but nothing is removed!)
apt-get  --with-new-pkgs  autoremove  upgrade  #--> install any new dependcies, if needed (but nothing is removed!)

	_______:  only one package install/upgrade:
- apt-get install --only-upgrade <packagename>  # This will upgrade only that single package AND ONLY if it is already installed.
- apt-get install  <packagename>    #  install the single package anyway! so install if it doesn't exist, or upgrade it if it does !
##________________________________________  ___________________________


#####  ==========  dpkg cmdline:
-!! internally it calls dpkg-query  OR dpkg-deb for many actions! so basically the same !  see man dpkg !
-!! better listings (with more options) directly with dpkg-query  -l  ... ##--eg with -W -f .... for own output-format !
-!  dpkg --list  (bzw. SAME as : dpkg-query  -l )    -->   list all INSTALLED packages, OK-for-installed-rpms-uue , see dpkg -list--OK.log
-! files-reverse-query, so to which package obelongs this file? :     dpkg  --search  <pattern>   #as in:   dpkg -S /usr/bin/xfview

	_______:  -- etc-/conf-files ...:
-- man dpkg:    --> see examples there !!:
/etc/dpkg/
/etc/dpkg/dpkg.cfg
/var/log/dpkg.log
/var/lib/dpkg/
/var/lib/dpkg/status    : installed pkgs long   --> rpmslg !?
##________________________________________  ___________________________


#####  ==========  dpkg-query : OK long-lisint (but yet no files-listing!)
-!!  Format of listing-output specifying/changing from default: with -f #--so as show ONLY package-names separated with a new line:   dpkg-query   -f '${binary:Package}\n'  -W | sort
-!!  The  output  format  of this option is not configurable, but varies automatically to fit the terminal width. It is intended for human readers, and is not easily machine-readable. See -W (--show) and --showformat for a way to configure the output format. see manpage!!
- own-format of listing:    
  dpkg-query  --showformat='\n=================================================================\n ${binary:Package} --- ${Version} --- ${Architecture} --- ${Status} --- ${Filename} --- ${Package} --- ${Section}\n----------Descp:\n${Description}\n_____________END1________________________________________________\n\n'   -W  '*vim*'
##________________________________________  ___________________________


#####  ==========  release-/distribution-upgrade (eg voll von 16.10 to 17.04 oder so ...):
	-per cmdline:  sudo apt-get install update-manager-core ;   sudo do-release-upgrade  ;
	- /OR  GUI:  update-manager
--############################ Repos-ubt : ##################################################
##________________________________________  ___________________________


#####  ==========  docs/infos Repos:
-- see:
	https://help.ubuntu.com/community/Repositories/Ubuntu
	https://help.ubuntu.com/community/SoftwareManagement
	man add-apt-repository

	_______:  configs/etc:
	/etc/apt/sources.list
	/etc/apt/sources.list.d

	_______:  Universe and Multiverse repositories:  https://help.ubuntu.com/community/Repositories/Ubuntu
	community Repos! so save, but not officially supported! but OK to use:
	not officially supported by Ubuntu, but because they are maintained by the community they generally provide packages which are safe for use with your Ubuntu computer.

	_______:  Repo-Types/-components:
	Ubuntu-Install-CDs contain software from the "Main" and "Restricted" components of the repositories:
	Main - Officially supported software. 
	Restricted - Supported software that is not available under a completely free license. 
	Universe - Community maintained software, i.e. not officially supported software.  (but save more or less to use -kk)
	Multiverse - Software that is not free. not officially supported software.         (but save more or less to use -kk) 

	_______:  URLs ...:
	http://archive.ubuntu.com/ubuntu/dists/"Your-Ubuntu-Release-Code-Name--saucy.name/Your-Repo-Type--repo.component/Your-Hardware-Arch"  as in eg:
	ubuntu-14.10 , release-name/saucy: utopic , repo-component: main, x64-Arch:  http://archive.ubuntu.com/ubuntu/dists/utopic/main/binary-amd64/
	your current releas??:  lsb_release -sc   to find out your release

	_______:  adding Repos:
	- manaully: add to /etc/apt/sources.list
		Remember to retrieve updated package lists by issuing a "sudo apt-get update"  when you're done editing sources.list.
	- cmdline:  add-apt-repository    eg:  If your release is called 'saucy': 
	sudo add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ saucy universe multiverse"
	sudo add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ saucy-updates universe multiverse"
	Don't forget then to retrieve the updated package lists:         sudo apt-get update

	_______:  sources.list :
	deb: These repositories contain binaries or precompiled packages. These repositories are required for most users. 
	deb-src: These repositories contain the source code of the packages. Useful for developers.
##________________________________________  ___________________________


#####  ==========  boot-device to install ubuntu, done for 1504ubt-x13:
	u1@vo17:/up1/t1/nps/2So $  dd if=./kubuntu-14.10-desktop-amd64.iso  of=/dev/sdd  
	2206464+0 records in
	2206464+0 records out
	1129709568 bytes (1.1 GB) copied, 353.777 s, 3.2 MB/s
	u1@vo17:/up1/t1/nps/2So $
	-- or:
	sudo dd if=/path/to/ubuntu.iso of=/dev/sdX bs=4M && sync
##________________________________________  ___________________________

