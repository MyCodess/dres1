##________________________________________  ___________________________


#####  ==========  

	_______:  OK mirroring/rsync a http-DIR , so NOT-downloading again the existings locally, and dw ONLY the newer ones,  OK worked (kind os rsync , but still missing --delete ! so kind of quick mirroring of the directory )
- (try -m instead , if ok !?!? )
- first dry/simulation with  --spider  
cd  /up1/t1/packs/arx_pk/mirror1/core1/os/x86_64
wget   -e robots=off   -N -nd -np -r  --spider        http://ftp.spline.inf.fu-berlin.de/mirrors/archlinux/core/os/x86_64/   ##--dry
wget   -e robots=off   -N -nd -np -r  -o core1.log    http://ftp.spline.inf.fu-berlin.de/mirrors/archlinux/core/os/x86_64/
wget   -e robots=off   -N -nd -np -r  -o extra1.log   http://ftp.spline.inf.fu-berlin.de/mirrors/archlinux/extra/os/x86_64/
[u1@arx1 x86_64]$ date
Fri 10 Jan 2020 02:44:48 PM CET
- OK also with -m (still need -np  !!, otherwise goes uwards ....):
wget   -e robots=off  -nd -np -m  --spider  http://ftp.spline.inf.fu-berlin.de/mirrors/archlinux/core/os/x86_64/       ##--dry
wget   -e robots=off  -nd -np -m            http://ftp.spline.inf.fu-berlin.de/mirrors/archlinux/core/os/x86_64/

	_______:  
[u1@arx1 x86_64]$ wget -e robots=off -np  -r  https://ftp.spline.inf.fu-berlin.de/mirrors/archlinux/core/os/x86_64
[u1@arx1 x86_64]$ date
Thu 09 Jan 2020 02:13:41 PM CET

	_______:  
u1@x13: /media/u1/t1/mirror1/ $date
Fri Jan  3 16:56:47 CET 2020
u1@x13: /media/u1/t1/mirror1/ $wget -e robots=off --no-prox  -r  https://ftp.spline.inf.fu-berlin.de/mirrors/archlinux/core/os/x86_64
u1@x13: /media/u1/t1/mirror1/ $

	_______:  
wget -e robots=off --no-prox -r -np   https://ftp.spline.inf.fu-berlin.de/mirrors/archlinux/iso/latest
