BASH-Startup-Files
==============================
    - /:210100


#####  ==========  Types of shells and their BASH-Startup-Files :

    _______:  see/docs:
    - ! see : INVOCATION section of man bash 
    - ! see  https://wiki.archlinux.org/title/Bash#Configuration_files  --> table there !
    - ! see  https://www.gnu.org/software/bash/manual/html_node/Bash-Startup-Files.html  bzw.  https://www.gnu.org/software/bash/manual/bash.html#Bash-Startup-Files
    - ! see  LPIC1-exam_102--learning-materials/102-500/    :  learning.lpi.org/en/learning-materials/102-500/105/105.1/105.1_01/index.html

    _______:  DIFF: shell-invocation-types :
	1- login+interactive-shell , as login into a tty (ps shows tty/x) , or invoke bash -l ; echo $0 must show "-bash" , so with dash !
		eg: ctrl-alt-<F3> + login , /or bash -l ,/OR  su - u2 bzw. su -l u2 , /OR sudo -i -s -u u2  , ... 
	2- Non.login+interactive-shell , as starting xWin and opening new gnome-terminals in xWin (ps whows pts/x for pseudo-terminal); $- must contain "i" for interactive-shel! 
		eg:  in xWin: open just a terminl , /OR in terminal: bash /OR  su u2 /OR  sudo -s -u u2 , ...
	3- non.login+non.interactive ,   as running any scripts-shell , t1.sh),
	4- login-non.interactive (not common, but as #!/bin/bash -l  in a script) ! : 
	- !nts : $0  :  for login-interactive-shell is "-bash"  , for Non.login-interactive-shell is "bash" , for non.login-non.interactive/script is script-name as t1.sh ,  ...

	_______:  verifying/querying the shell-type :
	- is my shell a login-shell??:
		- echo $0 must show "-bash" , so with dash! for nonlogin-interactive shells is "bash" !
	- is my shell an  interactive-shell??:
		-  the $- must contain "i" for interactive-shel! so nonInteractive: [[ $- != *i* ]]  
		as in /etc/bash.bashrc  arx:     [[ $- != *i* ]] && return   # If not running interactively, don't do anything
	- ans so, to verify the other types, just combine the above verifications appropriately !

	_______:  nts to startup-files:
    - /etc/profile file gets executed for all login+interactive shells !
    - /etc/bash.bashrc file gets executed for all interactive shells — whether login or not  -->!! depends on the distro-kernel-compilation if: -DSYS_BASHRC="/etc/bash.bashrc" ! see https://wiki.archlinux.org/title/Bash#Configuration_files !

	_______:  startup-files:
	for more details see:   see  https://www.gnu.org/software/bash/manual/html_node/Bash-Startup-Files.html
	1- login+interactive-shell (/OR bash -l / --login):   
	/etc/profile + first-one-of  ~/.bash_profile, ~/.bash_login, and ~/.profile, in that order ; by exit then:  ~/.bash_logout
	bash  --noprofile option can inhibit executing them!
	2- Non.login+interactive-shell : ~/.bashrc only!
	but /etc/bash.bashrc ist pre-executed in all distros !
	bash  --norc option  can inhibit executing them! The --rcfile  option  force ash to read and execute commands from file instead of ~/.bashrc.
	3- non.login+non.interactive ,   as running any scripts-shell , t1.sh :
	NO startup-files! but, the script ooks for the variable BASH_ENV to execute its filepath!
	/OR int the script do:  #!/bin/bash --login  ;then it executes the login-startup-files
##________________________________________  ___________________________

##############################  trys/logs/protocols : ############################################
#####  ==========  /:230716 :  bash-profiles-protocolling on debian/raspi  230714rpi / 192.168.43.113 :

    - !! tha lines of "--- calling ... from ... " are NOT default-bash-calls, but from the distro-profiles-entries!!
    - ! for the other possible/alternative profile-filenames see man bash ! here for better legibility not mentioned !

    _______:   login + interactive  shell (u1 ssh-login into raspi from arx on terminal):
        so:  /etc/profile  --> /home/u1/.profile  ##-protoc:

    Sun 16 Jul 10:52:45 CEST 2023
    [u1@2209arx wks]$ ssh  u1@192.168.43.113
    ===--  /etc/profile  ---------__1STA____
        __ ---- calling /etc/bash.bashrc by /etc/profile : ---
        ===--  /etc/bash.bashrc ---------__1STA____
        ===--  /etc/bash.bashrc  ---------__1END____
    ===--  /etc/profile  ---------__1END____
    ===--  /home/u1/.profile  ---------__1STA____
        --- calling /home/u1/.bashrc from /home/u1/.profile : ---
        ===--  /home/u1/.bashrc  ---------__1STA____
        ===--  /home/u1/.bashrc  ---------__1END____
    ===--  /home/u1/.profile  ---------__1END____
    u1@230714rpi:~ $

    _______:  interactive-chell  (NON-login):
        so:  /etc/bash.bashrc  -->  /home/u1/.bashrc
        - !?!? obv. man pages say only: ~/.bashrc !! maybe this from distro !?!? but could not fine any lines in distro-profiles for that!? maybe ENVs or bash-compiled-ver ...!?!?

    1@230714rpi:~ $ bash
    ===--  /etc/bash.bashrc ---------__1STA____
    ===--  /etc/bash.bashrc  ---------__1END____
    ===--  /home/u1/.bashrc  ---------__1STA____
    ===--  /home/u1/.bashrc  ---------__1END____
    u1@230714rpi:~ $

    _______:  NON-interactive-shell (script):
        looks for the variable BASH_ENV in the environment to execute !
##________________________________________  ___________________________

