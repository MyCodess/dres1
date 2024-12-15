##________________________________________  ___________________________


#####  ==========  docs:
	https://wiki.archlinux.org/index.php/Docker
	https://docs.docker.com/
--########## coll: =========================================================
##________________________________________  ___________________________


#####  ==========  20201127-211144 : done-coll:
see:  https://wiki.archlinux.org/index.php/Docker  :
	--- root:
	pacman -Suy  docker
	usermod -a -G docker  u1  ##--!!- u1 must re-login !! check u1 groups in terminal with:  groups 
	[root@2004arx 2So]# systemctl   start    docker.service
	--- u1:
	[u1@2004arx ~]$ docker   --version
	[u1@2004arx ~]$ docker    info
	 docker run -it --rm archlinux bash -c "echo hello world"   ##---> 150 MB image-DW
