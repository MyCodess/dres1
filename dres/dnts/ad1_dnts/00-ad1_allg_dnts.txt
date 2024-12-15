##________________________________________  ___________________________


#####  ==========  foratting USB sticks for read-write both on android9 + LX/rx1:

	_______:  ! was ok: USB-32GB, parted+formated on arx1/Lx  as vfat ! (exfat was NOT readable on android9/umidigi) : 
	00_UB32_DataTraveler_Kingston_blackLong_100G3.flg
	gdisk /dev/sdc , ##one part, 0700 / 'Microsoft basic data'
	[root@2004arx varau]# mkfs.vfat  -n  UB32_DT  /dev/sdc1
	mkfs.fat 4.2 (2021-01-31)
	[root@2004arx varau]# date
	2021-10-11T09:10:30 CEST

	_______:  exfat formatting did NOT work !! android9 wanted to reformatt it again !!

	_______:  formatting on android9 as tranfer-media worked also fine! it was formatted by android9 as vfat !
