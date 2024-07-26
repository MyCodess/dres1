_____________ Users-Mgm, login, ...________________________________
##________________________________________  ___________________________


#####  ==========  locking/disabling a user acc:

	_______:  loc acc:
	- passwd -l ; 
	- usermod -L : no-login-anymore, but still ssh/... possible! it locks an account by placing a ! in the encrypted password. If the user has another means to log in, such as with an SSH key, using usermod -L will not prevent their login. 
	  same as put an ! in /etc/shadow in front of his password-field-entry

	_______:  unlock:
	usermod -U  ; 
	passwd  -u ;

	_______:  disable acc:
	- usermod --expiredate 1 ; ##--see man passwd: To disable the account, administrators should use usermod --expiredate 1 (this set the account's expire date to Jan 2, 1970).
	- chage -E 1 userX

	_______:  disable all new logins (eg for maintenance,...):
	- /etc/nologin  :  nobody except root can login/ssh/...; the text inside will be shown! eg:  echo "__NO_LOGIN_NOW__" >>   /etc/nologin   ;

	_______:  nts:
	-- man shadow :
	- Note that an account expiration differs from a password expiration. In case of an account expiration, the user shall not be allowed to login. In case of a password expiration, the user is not allowed to login using her password. ## man shadow
	- If the password field contains some string that is not a valid result of crypt(3), for instance ! or *, the user will not be able to use a unix password to log in (but the user may log in the system by other means).
##________________________________________  ___________________________


#####  ==========  qckys 1coll uMgm:
	- who is now logged in and which terminal...?	:   loginctl , w , who
	- my login session features??	:  loginctl show-session $XDG_SESSION_ID
