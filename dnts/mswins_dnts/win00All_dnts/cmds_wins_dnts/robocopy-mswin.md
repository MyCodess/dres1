##________________________________________  ___________________________


#####  ==========  RoboCopy is rsync on win7:
see:  http://technet.microsoft.com/en-us/library/cc733145(v=ws.10).aspx
   bzw. robocopy /?

	_______:  simulate sync-ing from Ref-Dir "w-rf"  to target dir w-cp :
  robocopy  w-rf  w-cp  /mir  /L
  (/L == only-logging/reportin/simulationg without copying ;  /mir  ==  mirror-ing from source to target dir)
  eg:  robocopy  C:\up1\w\docs_m\WPads_All\WPad    C:\up1\w_CP\docs_m\WPads_All\WPad   /mir  /L
  Achtung: im Gegenteil zu rsync werden die immer die inhalte der letzten DIRs sync-ed !
##=============== MsWin-Sync for w_RF :
	dir  C:\up1\w  T:\t1_loc\w_CP
	dry-run:	robocopy C:\up1\w  T:\t1_loc\w_CP   /mir /r:3 /w:3 /dst  /ndl /L    ##--> dst : ignore one hour difference (vo17 / commer-winter) ; if needed also add /fft for fat systems! ; /L : dry-run only listing!
	copying:	robocopy C:\up1\w  T:\t1_loc\w_CP   /mir /r:3 /w:3 /dst  /ndl       ##--> dst : ignore one hour difference (vo17 / commer-winter) ; if needed also add /fft for fat systems!

	_______:  w_RF sync done:
    robocopy C:\up1\w  T:\t1_loc\w_CP   /mir /r:3 /w:3 /np    ##--> 207.932 MegaBytes/min.
##=============== 
##=============== 
