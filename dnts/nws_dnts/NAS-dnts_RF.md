_______________ NAS-devnts: ssh, NFS, mount, smb, .... NAS-Lx-System ___________________
-!! use "Test Connection" under "Info-->Service" Menupoint to check/test them !!
##________________________________________  ___________________________


#####  ==========  nohup from SSH:

	_______:  OK!:
admin@NAS2>    nohup cp -a /volumeUSB1/usbshare  ./D05  > copying-D05-nohup.log  2>&1  &

	_______:  NOT-OK!:
admin@NAS2>    nohup "cp -a /volumeUSB1/usbshare  ./D05  > copying-D05-nohup.log  2>&1"  &
##________________________________________  ___________________________


#####  ==========  SSH
- must be activated. default is deactivated ! : control.center --> Terminals & SNMP --> SSH
- explorer--Lx-share:   smb://nas1/daten1/  (in nemo, then loggend in as i1)
- terminal-path by opening from nemo was:  /run/user/1501/gvfs/smb-share:server=nas1,share=daten1/

	_______:  !! USER:
	- ssh  admin@192.168.1.52    bzw.   ssh  admin@nas2   :OK
	-! DIFF:  NAS-Lx-System-Users  <-->  NAS-DMS/Portal-users !!
	   the DMS-generated users (as i1, u1, ...) have in /etc/passwd the entry "nologin" for shell, as in:  i1:x:1026:100:i1-admin:/var/services/homes/i1:/sbin/nologin
	   so they can NOT ssh-login !! --> permission denied!!
	- so for ssh works, as default, ONLY with "admin", as ssh admin@192.168.1.52
	- ssh-login: same PW as the current-PW of the user "admin" ! ALSO as root + same admin-PW !!
##________________________________________  ___________________________


#####  ==========  NFS / Linux mount / iSCSI / ...:
- https://www.synology.com/en-us/knowledgebase/DSM/tutorial/File_Sharing/How_to_access_files_on_Synology_NAS_within_the_local_network_NFS
- must be activated/enabled globally AND must set "NFS Persmissons" per each Schared-Folder ! default is deactivatedi/disabled ! : control.center --> File-Services

	_______:  NFS-mount / mount.nfs:
-! mount-path ist NOT the same as SharedFolder-Path ! see the needed mount-path i n DSM-Portal->Schared-Folder-Peoperties there on the buttom of the page!!
- mount [Synology NAS IP address] : [mount path of shared folder] / [mount point on NFS client]
- root@x13:~#  	mount.nfs  nas1:/volume1/Daten1    /up1/media/nas-d1    ##--> OK! Case-Sensitive for DIR-names !!
##________________________________________  ___________________________


#####  ==========  SMB:
- in nemo/Files-manager:  smb://nas1/daten1/  (needs user-auth!)    ##--> OK! Case-NON-Sensitive for DIR-names !!
##________________________________________  ___________________________


#####  ==========  iSCSI:
https://www.synology.com/en-global/knowledgebase/DSM/tutorial/Virtualization/How_to_set_up_and_use_iSCSI_target_on_Linux
create a LUN on NAS2
apt-get install open-iscsi
vi /etc/iscsi/iscsid.conf    ##---> node.startup = automatic
iscsiadm -m discovery -t st -p 192.168.1.52
	192.168.1.52:3260,0 iqn.2000-01.com.synology:nas2.target-1.ed5358d96c
	169.254.110.96:3260,0 iqn.2000-01.com.synology:nas2.target-1.ed5358d96c
	...
iscsiadm -m node --targetname "iqn.2000-01.com.synology:nas2.target-1.ed5358d96c"   --portal "192.168.1.52:3260,0" --login
--> now is there! see it on your Linux with: fdisk -l , or do mkfs , mount,  ....
....
umount it ...
iscsiadm -m node --targetname "iqn.2000-01.com.synology:nas2.target-1.ed5358d96c"   --portal "192.168.1.52:3260,0" --logout
iscsiadm -m discovery --portal "192.168.1.52:3260,0"  --op=delete
