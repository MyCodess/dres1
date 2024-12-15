_____ SSHs __________________________
-! see Linux Security Cookbook.chm--Ch.6
##________________________________________  ___________________________


#####  ==========  ssh2-configs:

	_______:  global configs:
	- man sshd_config
	- howto-configs:  !! after modifying glob-configs, RESTART sshd !!
		-Restricting Access to an SSH Server by Account: add to /etc/ssh/sshd_config ,eg "AllowUsers smith jones" ; see Recipe 3.14--lxSecCook.chm
		-Allow SSH connections from remote.example.com to the smith account, but no other incoming SSH connections: AllowUsers smith@remote.example.com ; see Recipe 3.14--lxSecCook.chm
##________________________________________  ___________________________


#####  ==========  Distributing/Executing to all per SSH/SCP:

	_______:  checking before executing for all:
	 for srv in $sshLoginAll  ; do ssh $srv 'hostname && id -a '; done
- scp to all:  for srv in $sshLoginAll  ; do scp -dr ~/uu1  ${srv}: ; done
- removing from all:   for srv in $sshLoginAll  ; do ssh $srv 'hostname && rm -rf ${HOME}/uu1 '; done
- checkspace-all-WitDB-UxServers:  ./checkSpaceDB_all.sh | tee ${HOME}/log/`date +%y%m%d_%H%M`_checkSpaceDB_All.log | egrep '[89][0-9] *$'

	_______:  ! once full synch/distribute for uu1 (current, old uu1-DIRs, and all DB-servers):
	- old (if wanted):		mv uu1 old/`date +%y%m%d_%H%M`_`hostname`_uu1
	- current:	 scp -dr ${HOME}/uu1   target   (eg: ora92@w0012ac7:)
	- current:	remove from all DB-servers (!):   for srv in $sshLoginAll  ; do ssh $srv 'hostname && rm -rf ${HOME}/uu1 '; done
	- current: distribulte/copy to all:
		- for srv in $sshLoginAll  ; do echo "------  ${srv} ----" && scp -rd ${HOME}/uu1 ${srv}: ; done
		- if wanted for witsbTest:  for srv in $sshLoginWitsbTest   ; do echo "------  ${srv} ----" && scp -rd ${HOME}/uu1 ${srv}: ; done
		- /OR to all from admSrv: for srv in $sshLoginAll $sshLoginWitsbTest  ora92@w0012ac7 do echo "------  ${srv} ----" && scp -rd ${HOME}/uu1 ${srv}: ; done
	--- /OR only the last line if not caring about bup,...

	_______:  OLD distributing:
	--- distributing files to all with ssh ,OK (ora817 for some other servers):
		- WitDB:	for srv in $uxServersWitdb; do scp -dr ./uu1 ora92@${srv}: ; done
		- WitSB-t: needs PW:	for srv in $uxServersWitsb; do scp -dr ./uu1 ora92@${srv}: ; done
		- GateX:	for srv in $uxServersGatex; do scp -dr ./uu1 ora817@${srv}: ; done
		- Fonet:	for srv in $uxServersFonet; do scp -dr ./uu1 ora817@${srv}: ; done
		-- test-echo:   for srv in $uxServersWitdb; do echo "scp -dr ./uu1 ora92@${srv}:" ; done
	- mkdir in WitDB:  for srv in $uxServersWitdb; do ssh ora92@${srv}  'mkdir ~/old ~/log ~/tmp' ; done
##________________________________________  ___________________________


#####  ==========  Remote-SSH-Commanding (eg for SQLs):
- running one direct sql-statement on one server remotely, eg:
	ssh2 ora92@witsbt1.t-zssb.finanzit.sko.de '. ${HOME}/.profile && sqlplus -S "/ as sysdba"  @${HOME}/tmp/t1.sql ' (!! so only on current oracle_sid in profile !!)
-!! /OR runnig sqlplus remotely directly from remote-cmdline, eg:
ssh2 ora92@witsbt1.t-zssb.finanzit.sko.de '. ${HOME}/.profile && sqlplus -S "/ as sysdba"  <<EEE
> select * from dual;
> exit
> EEE
> '
-!! /OR with " instead ':
  ssh2 ora92@witsbt1.t-zssb.finanzit.sko.de  ". ./.profile && sqlplus -S \" / as sysdba\" <<EEE
> select * from dual;
> exit
> EEE
> "
##________________________________________  ___________________________


#####  ==========  SSH2-Setups : ===============================================
##________________________________________  ___________________________


#####  ==========  SSH2-Putty-Ux:
	!!! RSA does NOT work for admsrv-ssh-version !! only DSA !!!
	!! admsrv-ssh2 is the older one/worse one! so take preferabaly admsrv-ssh to avoid prblems !!
	!! admsrv-ssh2 has got naming constrains!! a public key with the SAME name as the priv-key in identefication-file plus ".pub" suffix MUST be in .ssh2-Dir of the client! you can change the file names
	! so private-keys of putty and admsrv-ssh ARE different (putty's one is the imported/converted version of admsrv-priv-key) but public-key is the same !

	_______:  ---- setup:
1- first generate keys on Ux-adminsrv with DEFAULT params (admsrv-SSH can NOT RSA; only DSA !!!):
	 ssh-keygen2 khod1_ss2
2- copy both keys to Win
3- import priv-key into PUTTYGEN.EXE and save public+priv.-keys
	you need really only the private-key from putty; public key have standard format (but not priv-keys)!
	so use everywhere only public-key from admsrv-ssh
4- distribute the admsrv-public-key to all receivers (eg w00112ac7, admsrv1 itself,...)
5- regeister its public-key in authorization-file of the receivers/servers.
6- add admsrv-priv-key to the identification-file of admsrv (as client)
7- add putty-priv-key to Pageant or invoke putty with -i "putty-priv-key"
##________________________________________  ___________________________


#####  ==========  SSH2-notes:
- Client:  User-PrivateKeys/IDs (==client) used by ssh-connection/client are listen in : $HOME/.ssh2/identification.
	:filenames of private keys that are  used  in  authentication are  set  in $HOME/.ssh2/identification
- Server:  server checks  $HOME/.ssh2/authorization  for  filenames of matching public keys
==== SSH2-Setup (ohne putty; Ux-admsrv1):

	_______:  ----- einmalig, key-generating and instalation:
720     ssh-keygen2
721     cd .ssh2
725     scp id_dsa_1024_a.pub  ora92@w0012ac7:.ssh2/a101ac9.pub
731     ssh2 -l ora92 w0012ac7
	--> with ora92-PW ; do on remote-server (w0012ac7): echo "Key a101ac9.pub" >> ~.ssh2/authorization
_______ finished installation!!

	_______:  ---- execute:
742     eval `ssh-agent2`  # only with eval !!!!
743     ssh-add2   # input phrase, once only!
744     ssh2 -l ora92 w0012ac7  # login WIHTHOUT PW

	_______:  
##________________________________________  ___________________________


#####  ==========  openSSH-setup
	- openssh: witsbt1 + witsbt2
	- open-ssh-procedure: generating pub-key from a ssh2.com-pub-key and installing:
			(see: Recipe 6.7 Authenticating by Public Key (SSH2 Client, OpenSSH Server) /LinuxSecurityCookbook_Ore_0305.chm)
			on remoteServerHost: 	cd ~/.ssh  &&
			- generating open-ssh-key from ssh2-pub-key:
				- interactively:  ssh-keygen -i > a101ac9_openssh.pub ; ... Enter file in which the key is (/home/smith/.ssh/id_rsa): a101ac9_dsa1024_ssh2.pub
				- non-interactive:   ssh-keygen -i -f  ../.ssh2/a101ac9_dsa1024_ssh2.pub >  a101ac9_dsa1024_openssh.pub
			- Install the new public key by appending a line to ~/.ssh/authorized_keys on remoteServerHost: cat a101ac9_openssh.pub >> ~/.ssh/authorized_keys
##________________________________________  ___________________________


#####  ==========  END-SSH2-Setups : ======================================
