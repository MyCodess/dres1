________Startup-Files for ksh(88):_______________________
- for case scripts see this file buttom /OR ora92@v880b01:/autofs/orashare/prj/bin/startupTests/ksh88/
##________________________________________  ___________________________


#####  ==========  scenarios per shell:
- each case with:
	1.1  ENV not set
	1.2  ENV set
1- interactive-login 		(eg: fisrtlogin)
2- interactive-non-login	(eg: from prompt: ksh)
3- non-interactive			(eg: script)
##________________________________________  ___________________________


#####  ==========  Summary (short):
-- interactive-login-shell:		/etc/ptofile  --> ~/.profile --> $ENV
-- interactive-NON-login-shell:	$ENV
-- NON-interactive-shell:		- Nothing basically (except if eg. ENV=~/myenv.sh script1.sh and script1.sh firstline is #!/bin/ksh)
		- in ksh93 $ENV is executed ONLY for interactive-shells!!
##________________________________________  ___________________________


#####  ==========  KSH88 StartupFiles Scanarios and logs/protocolls (long):
# in protocolls, first ignore lines with: ^env...:  they are just for checking of exports....;

	_______:  -- 1. Case: NO ENV set in .profile:
- login shell:
=== .profile done
$ ksh
$  ./tests/s1    #(without first line #!/bin/ksh)
prof1 : pp11
env1  :
envu1  :

	_______:  s1 done.
$  ./tests/s1    #(first line:   #!/bin/ksh)
prof1 : pp11
env1  :
envu1  :

	_______:  s1 done.
$

	_______:  1.2 non-interacctive: per ssh (so not from inside current shell):  --> so nothing is done: no .profile , no .kshrc ...:
a101ac9@u011ua01:/export/home/a101ac9 :00$ ssh ora01w@v880b01.i001.finanzit.sko.de './tests/s1'
prof1 :
env1  :
envu1  :

	_______:  s1 done.
a101ac9@u011ua01:/export/home/a101ac9 :00$ ssh ora01w@v880b01.i001.finanzit.sko.de '. ./.profile ; ./tests/s1'
=== .profile done
prof1  : pp11
env1   :
envu1  :
term   :   , is set in /etc/profile
sysProfileDone :
  #System-Profile==1 means  /etc/profile is done

	_______:  s1 done.
a101ac9@u011ua01:/export/home/a101ac9 :00$ ssh ora01w@v880b01.i001.finanzit.sko.de 'ENV=${HOME}/kshu1 ./tests/s1'  # s1-firtline:  #!/bin/ksh
=== kshu1 done.
prof1  :
env1   :
envu1  : u1u1u1
term   :   , is set in /etc/profile
sysProfileDone :
  #System-Profile==1 means  /etc/profile is done

	_______:  s1 done.
a101ac9@u011ua01:/export/home/a101ac9 :00$ ssh ora01w@v880b01.i001.finanzit.sko.de 'ENV=${HOME}/kshu1 ./tests/s1'  # s1-Without-firstline #!...
prof1  :
env1   :
envu1  :
term   :   , is set in /etc/profile
sysProfileDone :
  #System-Profile==1 means  /etc/profile is done

	_______:  s1 done.

	_______:  ---------------------------------------

	_______:  -- 2.case: with ENV set in .profile :  export ENV=${HOME}/kshu1
- login and interactive shells:
sysProfileDone : 1
=== .profile done
=== kshu1 done.
$ ksh
=== kshu1 done.
$ ./tests/s1      #(without first line #!/bin/ksh)
prof1  : pp11
env1   :
envu1  : u1u1u1
term   : vt100  , is set in /etc/profile
sysProfileDone : 1
  System-Profile==1 means  /etc/profile is done

	_______:  s1 done.
$
$ ./tests/s1      #(first line:   #!/bin/ksh)
=== kshu1 done.
prof1  : pp11
env1   :
envu1  : u1u1u1
term   : vt100  , is set in /etc/profile
sysProfileDone : 1
  System-Profile==1 means  /etc/profile is done

	_______:  s1 done.
$
-- 2.2 NON-interactive: per ssh (so not from inside current shell):
a101ac9@u011ua01:/export/home/a101ac9 :00$ ssh ora01w@v880b01.i001.finanzit.sko.de './tests/s1'
prof1 :
env1  :
envu1  :

	_______:  s1 done.
a101ac9@u011ua01:/export/home/a101ac9 :00$ ssh ora01w@v880b01.i001.finanzit.sko.de '. ./.profile ; ./tests/s1'   # with ENV=${HOME}/kshu1 set in .profile
=== .profile done
=== kshu1 done.
prof1 : pp11
env1  :
envu1  : u1u1u1

	_______:  s1 done.

	_______:  man ksh88/Solari8:
- Invocation
     If the shell is invoked by exec(2), and the first  character
     of  argument zero ($0) is -, then the shell is assumed to be
     a login shell and commands are read  from  /etc/profile  and
     then  from  either  .profile  in  the  current  directory or
     $HOME/.profile, if either file exists.  Next,  commands  are
     read  from  the file named by performing parameter substitu-
     tion on the value of the environment  variable  ENV  if  the
     file  exists. If the -s flag is not present and arg is, then
     a path search is performed on the first arg to determine the
     name of the script to execute. The script arg must have read
     permission and  any  setuid  and  setgid  settings  will  be
     ignored.   If  the  script  is not found on the path, arg is
     processed as if it named a builtin command or function
- ENV  
       This variable, when the shell is invoked, is subjected
       to  parameter expansion by the shell and the resulting
       value is used as a pathname of a file containing shell
       commands  to  execute  in the current environment. The
       file need not be executable.  If the expanded value of
       ENV  is  not  an  absolute  pathname,  the results are
       unspecified. ENV will be ignored if  the  user's  real
       and effective user IDs or real and effective group IDs
       are different.
       This variable can be used to  set  aliases  and  other
       items  local  to  the  invocation of a shell. The file
       referred to by ENV differs  from  $HOME/.profile    in
       that   .profile   is  typically  executed  at  session
       startup, whereas the  ENV  file  is  executed  at  the
       beginning  of  each shell invocation. The ENV value is
       interpreted in a manner similar to a  dot  script,  in
       that the commands are executed in the current environ-
       ment and the file needs to be readable, but  not  exe-
       cutable.  However, unlike dot scripts, no PATH search-
       ing is performed. This is used as a guard against Tro-
       jan Horse security breaches.
####################### Test-Scripts-KSH88: ########################
- each time modified a bit, if ENV is set or not,...
# ------- ~/.profile:
# export ENV=${HOME}/kshu1
export prof1=pp11
echo "sysProfileDone : $sysProfileDone"
echo "=== .profile done
# ------- ~/.kshrc :
export env1=ee11
echo "=== .kshrc done."
# ------- ~/kshu1 :
export envu1=u1u1u1
echo "=== kshu1 done."
# ------- ~/tests/s1 :
#!/bin/ksh
echo "prof1  : $prof1"
echo "env1   : $env1"
echo "envu1  : $envu1"
echo "term   : $TERM  , is set in /etc/profile"
echo "sysProfileDone : $sysProfileDone"
echo "  System-Profile==1 means  /etc/profile is done"
echo "--- s1 done."
###################### END-Test-Scripts-KSH88
