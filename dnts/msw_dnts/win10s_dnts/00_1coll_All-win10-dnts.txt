___________________ 1coll-win1o-ALL, just put in if not classified,...; maybe later sorting,... or not .... __________________________
##________________________________________  ___________________________


#####  ==========  /_220726 : Changing Drive letters Offline :
https://sites.google.com/site/pchelpandhowto/boot-up/changing-drive-letters-offline
In the left pane, click on HKEY_LOCAL_MACHINE to highlight it
Click File | Load Hive...
Browse to \Windows\system32\config of the OS with the messed up drive letters.
Double click on SYSTEM (the one with no extension)
In the Key Name: box type @SYSTEM
navigate to here:
HKEY_LOCAL_MACHINE\@SYSTEM\MountedDevices
Right click MountedDevices and click Permissions...
Make sure the Administrators group has Full Control permission.
Then rename the \DosDevices keys so that the drive letters are changed as desired
NOTE: You must first rename "\DosDevices\C:" to an unused letter, such as "\DosDevices\Z:" and
then rename the other drive letter to C: (such as: \DosDevices\D: --> \DosDevices\C:)
__________________________________________________________________________________________________
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  
