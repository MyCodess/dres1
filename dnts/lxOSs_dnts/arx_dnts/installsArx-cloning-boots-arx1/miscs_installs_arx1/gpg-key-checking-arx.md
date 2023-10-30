______________________ Sec-Ency, gpg, sha1, md5 , .... ________________________________________
##________________________________________  ___________________________


#####  ==========  .sig files verifying /  gpg2  --verify ... : 

	_______:  1kk-on-ubt--190400 :
gpg2  --keyserver hkp://keys.gnupg.net:80 --keyserver-options auto-key-retrieve --http-proxy ""  --verify archlinux-2019.03.01-x86_64.iso.sig
gpg2  --keyserver hkp://keys.gnupg.net:80 --keyserver-options auto-key-retrieve  --verify archlinux-2019.03.01-x86_64.iso.sig
gpg2  --keyserver hkp://pgp.mit.edu:80/  --keyserver-options auto-key-retrieve  --verify archlinux-2019.03.01-x86_64.iso.sig

	_______:  eg, http://mailutils.org/download.html  /_190400 :
You can use the signature file to verify that the corresponding file (without the .sig suffix) is intact.
First, be sure to download both the .sig file and the corresponding tarball. Then, run a command like this:
 	gpg --verify mailutils-3.6.tar.gz.sig
If that command fails because you don't have the required public key, then run this command to import it:
  gpg --keyserver keys.gnupg.net --recv-keys 3602B07F55D0C732
and rerun the `gpg --verify' command.
##________________________________________  ___________________________


#####  ==========  
