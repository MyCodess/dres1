________________________ SSHs: OpenSSHs / .... dnts : _________________________________

#####  ==========  docs ...:
	https://wiki.archlinux.org/title/OpenSSH
	https://wiki.archlinux.org/title/Secure_Shell
	man ssh  sshd  ssh_config
##________________________________________  ___________________________

#####  ==========  NWs / setups ...:
	- service-/daemon-check:   systemctl   list-unit-files | grepi ssh ##--if-not-running:  sudo  systemctl  start sshd.service ;
	- port-check: is ssh port open/listening?? :   sudo lsof -i:22  ##-must see sshd ! #/OR: sudo ss -tulpn | grepi listen ;  
	- check if sshd litening at port ...??:  sudo  ss  --tcp  --listening -n  ##-/OR: sudo  lsof -i:22  ##-/OR: telnet localhost 22 #...
##________________________________________  ___________________________

#####  ==========  keys / key-gen / key-enc-methods ...:

	_______:  key-encs-methods (key-gen -t ):  Choosing the authentication key type  : https://wiki.archlinux.org/title/SSH_keys#Choosing_the_authentication_key_type :
	--> prefered:  Ed25519  ! (with  ssh-keygen -t ed25519 ) :
	- Ed25519 (more secure + faster)  :  best security ! but requires recent versions of client & server > OpenSSH 6.5 of January 2014 !
	- ECDSA  (same, but politicaly suspect! NSA-case) :   is likely more compatible than Ed25519 (though still less than RSA), but suspicions exist about its security !
	- RSA (default + most-compatible) :  greatest portability between SSHDs ! ssh-keygen defaults to RSA ! more security with higher key-size/bitrates / -b  BUT performance-drawbacks!! default: 3072 ! eg: ssh-keygen -b 4096 ! GnuPG FAQ: If you need more security than RSA-2048 offers, the way to go for ECC (ECDSA / Ed25519) !
	- DSA deprecated+insecure  :  OpenSSH 7.0 deprecated and disabled support for DSA keys due to discovered vulnerabilitie ! so, only: RSA or one of the two types of ECC (ECDSA and Ed25519)

	_______:  steps to setup-key-login:
	- ssh-keygen  [ -C "ev1-pubkey-$(date -I)" ]  --> generate your keys !
	- add your pub-key to REMOTE-user-authorized-keys as:
		ssh-copy-id -i ~/.ssh/id_ed25519.pub   remote-user-name@remote-server [ -p 9991]
		-- OR manually:
		if remote-.ssh-dir not exists, on remote-pc:  mkdir ~/.ssh ; chmod 700 ~/.ssh ; cat ~/id_ecdsa.pub >> ~/.ssh/authorized_keys ; rm ~/id_ecdsa.pub ; chmod 600 ~/.ssh/authorized_keys ;
		scp ~/.ssh/id_ecdsa.pub username@remote-server.org: #got-to-remote-server : cat ~/id_ecdsa.pub >> ~/.ssh/authorized_keys
		/OR  got-somehow-to-remote-pc-with your pub--key and:  cat my-PUB-key >>  ~/.ssh/authorized_keys (on the remote-server)

	_______:  keygen :
	- add comments to pub-key (grep/find it easier,...): ssh-keygen -C "$(whoami)@$(uname -n)-$(date -I)--l1nw"

	_______:  modifyings/ managing / querying / miscs... keys:
	-! non-default-filename/filepath of your private-key, then must use "-i" ,eg:  ssh -i id_rsa_server1 user@server1
	-! changing PW/passphrase of priv-key, without changing the private key itselt with:  ssh-keygen -f ~/.ssh/<priv-key> -p ..."   /OR also changing  encoding format  ##--man ssh-keygen : -p      Requests changing the passphrase of a private key file instead of creating a new private key ...
	- multiple keys configs ...:  vi ~/.ssh/config ; add ther: Match host=xxx , IdentityFile ~/.ssh/id_rsa_IDENTITY1 ; ... ##--see arx-ssh_key !
	-! ssh -T <pub-key> user1@server1  ##-checkt/test if  works shh-login with the key-pair of this pub-key for this server !?  eg: ssh -T git@github.com
##________________________________________  ___________________________

#####  ==========  ssh-agent :

	_______:  nts:
	-!! see https://wiki.archlinux.org/title/SSH_keys#SSH_agents
	- GitHub key-forwarding : https://docs.github.com/en/authentication/connecting-to-github-with-ssh/using-ssh-agent-forwarding
	- ssh-agent is the default agent included with OpenSSH. It can be used directly or serve as the back-end to a few of the front-end solutions ...
	- ssh-add : is  used to add/remove/query keys to/from ssh-agent !

	_______:  setps:
	- start it (/=R autostart, see u.):   eval $(ssh-agent)  ##--to get as ENVs its PID/Socket/... !
	- ssh-add  ~/.ssh/id_ed25519  ##--so add your PRIVATE key to its agents cache ! 
	- git/other-apps using agent:  To make all ssh clients, including git ..., store keys in the agent on first use, add the configuration setting AddKeysToAgent yes to ~/.ssh/config. Other possible values are confirm, ask and no (default).

	_______:  autostart methods of  ssh-agent  :
	--- autostart ~/.bashrc of ssh-agent in by login:   https://wiki.archlinux.org/title/SSH_keys#Choosing_the_authentication_key_type  :
		In order to start the agent automatically and make sure that only one ssh-agent process runs at a time, add the following to your ~/.bashrc:
		-# The lifetime of the unlocked keys is set to 1 hour :
		if ! pgrep -u "$USER" ssh-agent > /dev/null; then
			ssh-agent -t 1h > "$XDG_RUNTIME_DIR/ssh-agent.env"
		fi
		if [[ ! -f "$SSH_AUTH_SOCK" ]]; then
			source "$XDG_RUNTIME_DIR/ssh-agent.env" >/dev/null
		fi
	--- autostart systemd/user of ssh-agent by login (regardless of X11):   https://wiki.archlinux.org/title/SSH_keys#Choosing_the_authentication_key_type  : .. see there!
	--- autostart X-cmd of ssh-agent as a wrapper for X : ssh-agent startx  ##bzw. startxfce4 ...
	--- autostart other methods: Keychain (one-time by booting !!) , GnuPG Agent, GNOME/Keyring (#Disable keyring daemon components) , x11-ssh-askpass , Kwallet, KeePass2, ....

	_______:  configs usu. of clients for ssh-agent :
	- vi ~/.ssh/config  :
	AddKeysToAgent yes/ask/confirm   ##-man ssh_config , make all other ssh clients/apps (as git, gh, ...) do store the key in the ssh-agent on first use ...

	_______:  querying/modifying/adding/... agent:  all with:  ssh-add ... :
	-! the SSH_xxx ENVs must be set for these cmds!!
	- add new priv-key to agent-cache:  ssh-add -f <priv-key-FP> ...
	- delete all cached keys from agent: ssh-add  -D      ##-Deletes all identities from the agent.
	- delete a key from cache:  ssh-add -d <pub-key>
	- listing-all-priv-keys-cu in agent-cache:  ssh-add -L
	- listing-all-fingerprints-cu in agent-cache:  ssh-add -l
##________________________________________  ___________________________


#####  ==========  X-forwarding (running GUIs on server/sshd and getting its windows on client/ssh):
    --- X-forwarding (eg openning a terminal on the server/raspi1 and get its window on the clien/arx1 opened):
    - X-forwarding MUST be activated on both sides, client/ssh + server/sshd:
    - server/sshd/raspi1:  On the server side, X11Forwarding yes must be specified in /etc/ssh/sshd_config
    - server:   the xauth program must be installed on the server side.
    - client/arx1:  call ssh -X ...  /OR configure it as your ssh-client-default:  ForwardX11 yes in ~/.ssh/config
    - client, if needed:   xhost +   ##--/OR xhost <only your-server...>...
    - !! NO DISPLAY setting required!:  Note that you do not need to set any environment variables on the server. DISPLAY and XAUTHORITY will automatically be set to their proper v
    - check it with -v if problems ...:  ssh  -X  -v   u1@192.168.43.113
    --- so: To get X11 forwarding working over SSH, you'll need three things in place:
        1- Your client must be set up to forward X11.
        2- Your server must be set up to allow X11 forwarding.
        3- Your server must be able to set up X11 authentication.
        --- so:
        1- Server/sshd:
        -  On your server, make sure /etc/ssh/sshd_config contains: X11Forwarding yes  ,   X11DisplayOffset 10
        - restart sshd  ##/OR: cat /var/run/sshd.pid | xargs kill -1
        - On your server, make sure you have xauth installed.  If you do not have xauth installed, you will run into the empty DISPLAY environment variable problem
        2- client/ssh:
        - ssh -X [-v]  u1@host1 ##/OR as default : vi  ~/.ssh/config ; ForwardX11=yes



##________________________________________  ___________________________

#####  ==========  client-configs (OpenSSH):

	_______:  config-files:
	- man ssh_config    ##-for OpenSSH client configuration file
	- order-configs:   cmdline-params  >  ~/.ssh/config  >  /etc/ssh/ssh_config
	-! the FIRST obtained value will be used in the config-files! so put the defaults at the ends and your preferences at the beginning of the config-file !

	_______:  permissions (MUST):
	-! The configuration directory ~/.ssh, its contents should be accessible only by the user (check this on both the client and the server), and the user's home directory should only be writable by the user:
	chmod go-w ~ ; chmod 700 ~/.ssh ; chmod 600 ~/.ssh/* ; chown -R $USER ~/.ssh ;   ##--https://wiki.archlinux.org/title/OpenSSH

	_______:  Troubleshooting /problems of client connections:
	https://wiki.archlinux.org/title/OpenSSH#Troubleshooting  : Checklist
##________________________________________  ___________________________

#####  ==========  GitHub-SSH-client :

	_______:  
	-! see :  https://docs.github.com/en/authentication/connecting-to-github-with-ssh :
	- DSA NOT supported any more !! deprecated ! insecure !
	- RSA keys ONLY with SHA-2 signatures !

	_______:  steps:
	- upload your pub-key to GitHub through web: user-login -> acc-setings --> ssh+GPG --> ssh-keys : "new ssh key" button and copy your pub-key to it !
	- ssh  -i  ~/.ssh/id_ed25519 -T  git@github.com  ##--if ok: Hi ... ! You've successfully authenticated, but GitHub does not provide shell access.
##________________________________________  ___________________________

#####  ==========  server-configs (OpenSSH):

	_______:  config-files:
	- man sshd_config    ##-for OpenSSH client configuration file
	- order-configs:   cmdline-params  >    /etc/ssh/sshd_config
	-! the FIRST obtained value will be used in the config-files! so put the defaults at the ends and your preferences at the beginning of the config-file !

	_______:  
	ss  --tcp  --listening -n   ##--on server: is sshd listening on ??
##________________________________________  ___________________________

#####  ==========  exp cmdline calls:

	_______:  ssh calls:
	- ssh user@server git init --bare mysite ##--create new git-repo on the remote server !
	- executing several cmds with ssh-login :  ssh   ssh://t1@2209arx   "cd ./.cache/ ; ls -la"
	- pipe loc-cmds into remote ones:          cat ~/.ssh/id_rsa.pub | ssh   user@remoteserver 'cat >> .ssh/authorized_keys'
	- pipe remote-cmds into local ones:        ssh root@remoteserver 'tcpdump -c 1000 -nn -w - not port 22' | wireshark -k -i -

	_______:  scp calls:
	scp fileName user@remotehost:/home/username/destination

	_______:  misc/cmds on remote-server per ssh/scp:
	-! vim scp://user@remoteserver//etc/hosts   ##--eitd it directly ! it creates a file in /tmp on the local system and then copies it back once we write the file in vim with :w ...
##________________________________________  ___________________________

#####  ==========  ########### 1coll: #######################################################
##________________________________________  ___________________________

#####  ==========  ########### trys-evv : ###################################################
##________________________________________  ___________________________


#####  ==========  /:230324 :
    ssh-keygen -C "evv-u1@2209arx-try1-sshkey"
    ssh-keygen -C "evv-u1@2209arx-try1-sshkey-ed25" -t ed25519
    - t1 user: mkdir ~/.ssh ; chmod 700 ~/.ssh ; cat <u1 id_ed25519.pub ...> >> /.ssh/authorized_keys ; chmod 600 ~/.ssh/* ;
##________________________________________  ___________________________
