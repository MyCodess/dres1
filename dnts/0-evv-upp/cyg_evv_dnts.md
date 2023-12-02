________________________ cygwin-setup of evv/upp on mswins __________________________



#####  ==========  evv-cyg-configs (on devpc1-vw /ofc1 ) , /:231000 :
    - ! vi /etc/fstab    :  mount C:\cg-dir to the "/" so that NO-prefixes at all !

    --- .bashrc-evv-call-cyg:
    cat <<-"EEE"  >> ~/.bashrc
    ################# 1evv-addies: ####################################
    shopt  -s  nocaseglob
    shopt  -s  nocasematch
    ##-- export  q_Host1full=$(hostname)  ##--for now set it manually to devpc1 /OR ofc1devpc1 ...!
    export  HOME=${USERPROFILE}     ##--OK1:  export HOME="${HOMEDRIVE}/${HOMEPATH}"
    source  ${USERPROFILE}/up1/.ev13/etc/profile.sh
    EEE
    
    ---  vi $INPUTRC  ##--for case-insensitive-completions, so in evv vi ~/up1/.ev13/etc/inputrc  :
    cat <<-"EEE"  >>  $INPUTRC
    #####  ==========  MsWins/CygWins :
    [[ -a ~/.inputrc ]] &&  $include  ~/.inputrc  ||  echo "##__ not-file:  ~/.inputrc !!"
    set  completion-ignore-case  On
    EEE
###________________________________________  ___________________________


#####  ==========  evv-cyg-configs /:231016 :  on Lv13-mswin:

	- ! assume you have limited rights, similar to office! so not defininf new mount-points,... ! but just as power-user! (Dev-VDI):
    - ! vi /etc/fstab    :  mount C:\cg-dir to the "/" so that NO-prefixes at all !
    ---
	- unpack in /c/Users/a1/up1
	- cd /c/Users/a1/up1 ;
	- links-recreate (if other pathes! you could also change their targets in up1/mnt/ but so here shorter links...) rm t1 varu w1 optu 
	- ! NO-slash at path-end !! :
	--
	ln -s  /t/t1_RF   t1
	ln -s ./t1/varu
	ln -s  /c/Progs2  optu2
	ln -s  /t/T1_HD1/Progs3   optu3
	ln -s  ./t1/w1_RF     w1
	---
	cd ;  vide-org   ~/.bashrc  ;  echo "source  ${HOMEPATH}/up1/.ev13/etc/profile.sh"  >>  ~/.bashrc  ; 
	restart cyg-term !
##________________________________________  ___________________________

#####  ==========  cmds/Allg-nts,...
	--- pathes (converting...):
	cygpath --windows  $PWD
	cygpath --windows ~/.bashrc
	cygpath --unix C:/cygwin/bin/ls.exe
	cygpath --unix C:\\cygwin\\bin\\ls.exe
	https://cygwin.com/faq.html#faq.using.converting-paths

	---
##________________________________________  ___________________________

