_________________ MsWinsNW_Lx: shares-lx-mswin, samba, NetBios, mounts.ntfs, access-win-shares-from-lx, ... _________________________


#####  ==========  docs:

	_______:  mounting/sharing/accessing/exporting DIRs between Lx-and-MsWins :
    - !!  https://wiki.archlinux.org/title/Samba , da als share-client / -server :
        - ! client-samba, Zugriff als Client auf mswin-shares:  https://wiki.archlinux.org/title/Samba#Client
        - ! server-samba, Shares-Freigabe auf Linux-system für Windows-PCs:  https://wiki.archlinux.org/title/Samba#Server
    - !! File-Sharing-Methods... All alternatives ! https://wiki.archlinux.org/title/Category:File_sharing
    --
    - https://en.wikipedia.org/wiki/Server_Message_Block
    - https://en.wikipedia.org/wiki/NetBIOS
##________________________________________  ___________________________


#####  ==========  mount smb/cifs , mount-MsWins-Freigaben :
    !! Problem/Error:  mswin-user MUST have a PW ! did NOT work with empty-PW !! got error: NT_STATUS_ACCESS_DENIED /OR  NT_STATUS_ACCOUNT_RESTRICTION !! but ehn worked also fine with win-firewall-enabled-in-priv-NW !
    - !! setting files/dir-modes/masks kaum effekt ! see man page! use  rsync -navO --no-perm  –no-owner ... if syncing over cisf !
    to mount a MsWIn-Freigabe / -shared-folder on Lx, just mount.cifs :
    pacman -S cifs-utils ; pacman -S smbclient ;
	mount -t cifs  //<IP>/<share-name>  /mnt/t1  -o  username=a1,iocharset=utf8,uid=u1,gid=gu1   ##--try with IP ! uid and gid corresponds to the local (e.g. client) user/user group !! not the remote/mswin-PC !
    - !! rsync nts: then use rsync -navO --no-perm  –no-owner ... ! to ignore permissions,... if syncing to/from cifs tree !
##________________________________________  ___________________________


#####  ==========  hostnames of mswin-PCs:  --> use zunächst IP to check/test connection !! hostnames then trickly in l1nw due to missing DNS-server !! but here:
	-! with hostname more work/problem! try always first with IP ! or at all with IP !
	-!! DIFF : default-lx-DNS-name-resolution   <-->  MsWIn-PCs-names (NetBios-names)
	-! must use NetBios-hostnames, so :   https://wiki.archlinux.org/title/Samba#NetBIOS/WINS_host_names
	##--?-needed?:  pacman -S samba
	---!   must edit nsswitch and  start winbind.service to provide the NteBios-naming-service! :
	pacman -S   extra/libnss_nis
	pacman -S   extra/nbtscan   ##--Scan networks searching for NetBIOS information ! check its files with pacman -Ql
	so: vi  /etc/nsswitch.conf ##--add wins to the list
	probably the DEactivate win-firewall-on-this-NW if needed!
	systemctl start winbind.service   ##--restart it if new win-Pcs there !
##________________________________________  ___________________________


#####  ==========  setup samba-server + client done on raspi1/smb-server <--> arx1/smbclient /:230803  :

    - !! DIFF:  samba-User  <-->  OS-User are different !! to mount/access a smb-share you need ONLY the  samba-User-credentials, NOT-OS-User !! usu. both have same user-name, but different PW !!
    - ! based-on/ see:  https://wiki.archlinux.org/title/Samba

    _______:  mounting/exploring a MsWin-Share/-Freigabe (for details see the following section for: "cient-setup"):
    -! is much simpler than the rest below (client+server-setups), if you only want to mount/access any mswin-shares/Freigaben, then MsWIn works as the samba-server there !
    - pacman  -S  smbclient  cifs-utils  gvfs-smb ; 
    - mount  -t cifs //192.168.43.113/g11_share   /mnt/t1  -o  username=g11,password=smbpw1,workgroup=L1NW,iocharset=utf8,uid=u1,gid=gu1  ##-see here client-secitoin!
    - FileMgr /thunar :    smb://192.168.43.113/g11_share/   #--requires gvfs-smb package !

    _______:  client-smb-Lx-setup /arx1 :
    https://wiki.archlinux.org/title/Samba#Client
    - for connections you need samba-username+samba-PW ! OS-PW is not relevant there!
    pacman -S  smbclient
    pacman -S  cifs-utils  ##--if-liked--additional to smbclient: provides /usr/bin/mount.cifs ; is a lightweight alternative to smbclient(without support for listing public shares, etc.),...
    pacman -S  gvfs-smb    ##--if-liked--required ONLY for GUI-file-explorers (thunar, ...), otherwise they do not know smb-protocoll! for cmdline-mount/-share not needed ! see:  https://wiki.archlinux.org/title/Samba#File_manager_configuration
    lsmod | grepi cifs ; ##--if not loaded the kernel module cifs, then load it with modprobe /OR reboot ! otherwise mount.cifs will fail !
    /etc/samba/smb.conf  :  if smbd-conf not there, created an empty/dummy (smbclient checks its existance):   sudo mkdir /etc/samba ; touch  /etc/samba/smb.conf  (basically it belongs to the smbd/samba-server-pkg !)
    echo "client min protocol = NT1"  >>  /etc/samba/smb.conf   ##--adds SMB1 features to client queries, required if want hostnames instead IPs (NetBIOS resolution /Samb1)
    - on client eg:  smbclient  -L  192.168.43.113  --user=g11   [ --user=g11%smbpw1 ]  ##-- smb://ip-address/sharing-name/ ...
    - on client-FIleMgr/thunar :  smb://192.168.43.113/g11_share/
    -- mount-manually if liked:
        mount --mkdir -t cifs //SERVER/sharename  /mnt/mountpoint  -o  username=username,password=password,workgroup=workgroup,iocharset=utf8,uid=username,gid=group  ##eg:
        sudo  mount  -t cifs //192.168.43.113/g11_share   /mnt/t1  -o  username=g11,password=smbpw1,workgroup=L1NW,iocharset=utf8,uid=u1,gid=gu1
        fstab  mount-entry if liked (! Spaces in sharename should be replaced by \040 (ASCII code for space in octal) ) :
        //SERVER/sharename  /mnt/mountpoint  cifs  _netdev,nofail,username=smb-user,password=smb-pw  0  0
    -- cmds-eg on client:
        - smbclient  -L  raspi1   --user=g11%smbpw1
        - ! discover any samba-server in your LAN:  map -p 445 "192.168.43.*"  ##--default port of samba 445 !

    _______:  server-smb-Lx-setup /raspi1 :
    https://wiki.archlinux.org/title/Samba#Server  :
    sudo apt-get install  samba    ##--wie:   pacman -S  samba
    useradd -c "anonym1-samba1"  g11    ##--also passwd g11 .... some-complex-PW (smbd will require its own PW later!)
    nts: Although the user name is shared with Linux system, Samba uses a password separate from that of the Linux user accounts. 
    smbpasswd  -a  g11   ##--> some PW for samba-share ! only this PW is needed to access the share !
    checkit and liste samba-users:   pdbedit  -L  -v
    share-dir (eg /share1/):  mkdir /share1/  ; chown -R g11:g11 /share1/ ; ##-if-liked:  chmod 777 /share1/ ;
    - vide-org   /etc/samba/smb.conf  :  ##-->see below for addies!
        - the LATEST setting in smb.conf is taken! so do NOT need to modify any org-settings there! just ADD your own ones at the END in the appropriate [SECTION] and this overwrites the previuos settings !
        - so add-your-share1-to-the-end, see above link ! then testparm it ! testparm - check an smb.conf configuration file for internal correctness
    testparm
    - ?maybe needed?: firewall-stuff, 
    - sudo systemctl enable  smbd ;  sudo systemctl restart smbd ;  ##--better:  systemctl restart  smbd.service  nmbd.service
    - hostnames resolution : check the NetBIOS/nmbd-status (for hostnames instead IP using), must be started:  systemctl status nmbd ; ##--if not, or if pkg-install required, then do it, if want use hostnames instead IPs ! sudo service nmbd restart ;
    - SMB1 : for also using SMB1 (for discoveries, eg in explorer or with smbtree / smbclient): add to server-smb.conf: [global] ... server min protocol = NT1  and for client-conf: client min protocol = NT1
    --- cat  lines-here-below  >>  /etc/samba/smb.conf  on server-site-samba:
    ##---------------------------- evv1-addies :
    [global]
        workgroup = L1NW
        server string = Samba-1 on %h %v
        security = user
        map to guest = bad user
        guest account = g11
        server min protocol = NT1

    [g11_share]
        comment = guest-share-1
        path = /share1/
        public = yes
        only guest = yes
        writable = yes
        printable = no
    ##----------------------------
##________________________________________  ___________________________


#####  ==========  MsWins-Freigaben on Lx mounten/access (so MsWin as SMB-Server and Lx as SMB-client):
    -1 on mswin Explorer:  do Freigabe (for alls)
    -2 on Lx in FileManagers:  smb://192.168.1.1/shared_folder-1  ##--mybe requires pacman -S   gvfs-smb ! see below !
    -2b /OR mount -t cifs  //192.168.1.1/X17--t1_loc  /mnt/t1  -o  username=a1,iocharset=utf8,uid=u1,gid=gu1  
##________________________________________  ___________________________


#####  ==========  lx-filemanagers-access-to-mswin-shares (PCManFM, Thunar, ... acces mswin-Freigaben):
	_______:  lx_filemanages-accesing-mswin-shares (thunar,...):    https://wiki.archlinux.org/title/Samba#File_manager_configuration  :
	pacman -S   gvfs-smb      ##--?-needed? OR is only for the smb-Server !? :  pacman -S samba
	smb://192.168.43.177/X17--t1_loc   (in eg PCManFM/thunar)  ##--!for using hostnames see its section here !  smb://X17/X17--t1_loc   
	smb://192.168.43.7/asus1-t1_loc    (in eg PCManFM)
	--
	In order to access samba shares through GNOME Files, Nemo, Caja, Thunar or PCManFM, install the gvfs-smb package, available in the official repositories.
	smb://servername/share
	The mounted share is likely to be present at /run/user/your_UID/gvfs or ~/.gvfs in the filesystem.
##________________________________________  ___________________________


#####  ==========  troubleshooting/discovery/Tips/scanning/.....
    - !! unbeding1 wollte PW haben der smbclient for coonceting to mswin! NOT-worked with empty-PW or anonymous ! empty-PWs got errors: NT_STATUS_ACCESS_DENIED as tried with:  smbclient -L  192.168.43.15  --user=t1  #-or u1 or ...!!
    -! https://wiki.archlinux.org/title/Samba#Tips_and_tricks
    - pacman -Ss   nmap  smbclient
    - (here eg mswin-PC/server-IP:   192.168.43.7  / ASUS1 ):
    -!! PROBLEM:  if ping mot reaching, then mswin-private-NW is firewalled! so for THAT private-NW (eg A3S-wl1) deactivate its private-firewall !
    - nmap  -Pn -PS445  192.168.43.7  ##--scan your local network to find systems with TCP port 445 open, which is the port used by the SMB protocol.  Note that you may need to use -Pn or set a custom ping scan type (e.g. -PS445) because Windows systems are usually firewalled.
    - hostname (! NetBIOS host ) of the win-server with IP  192.168.43.7 ??:   nmblookup -A 192.168.43.7   ##--! Regardless of the output, look for <20>, which shows the host (! NetBIOS host !) with open services.
    - list which services/shares are shared on the systems (try first with IP instead hostname! hostname requires more work !):
        smbclient -L  192.168.43.113  -U%    ##--take the current-user-credentials and not ask for PW !
        smbclient -L  \\ASUS1  ;    smbclient -L \\X13 ;
##________________________________________  ___________________________


