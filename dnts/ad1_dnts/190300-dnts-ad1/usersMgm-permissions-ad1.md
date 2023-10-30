_______________ rights/permissions/AccessRights/ACLs/Capabilities,  UsersMgm, .... _____________
##________________________________________  ___________________________


#####  ==========  permissions/access-rights :

	_______:  
	- man capabilities , setcap , capsh , ...	 --> capabilities-based !
	- https://forum.xda-developers.com/showpost.php?p=77437874&postcount=6
	- http://man7.org/linux/man-pages/man7/capabilities.7.html

	_______:  adding more rights/capabilities to certain Apps (elevating privileges) :
	- Android restricts all of its (Java) apps from gaining elevated privileges (which can be gained depending on setuid or file capabilities) by setting PR_SET_NO_NEW_PRIVS ... https://forum.xda-developers.com/showpost.php?p=77437874&postcount=6
	- Linux capabilities (and suid-bit) do not have effect when interacted with by ordinary Android apps, because Android JVM process (zygote) uses PR_SET_NO_NEW_PRIVS prctl flag to disable them before running any app code (see man prctl). This means, that ordinary processes (such as Termux UID) can not elevate themselves by using execve (neither with suid, nor with file-caps or SELinux file attributes). https://github.com/termux/termux-app/issues/410
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  
