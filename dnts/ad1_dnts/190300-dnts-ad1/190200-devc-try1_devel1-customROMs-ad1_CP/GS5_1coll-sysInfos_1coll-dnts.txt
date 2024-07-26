__________________ SAMSUNG Galaxy S5 note --coll-- sysinfos ... ___________________________
##________________________________________  ___________________________


#####  ==========  HD/Parts/mounts---GS5 (rooted-org1) /_190225 :
export  PATH=$PATH:/sbin/.magisk/busybox: ;

	_______:  - root@s5neolte:/ # blkid
/dev/block/vold/public:179,33: UUID="3829-15F7" TYPE="vfat"
/dev/block/loop64: UUID="57f8f4bc-abf4-655f-bf67-946fc0f9f25b" TYPE="ext4"
/dev/block/mmcblk1p1: UUID="3829-15F7" TYPE="vfat"
/dev/block/mmcblk0p23: UUID="57f8f4bc-abf4-655f-bf67-946fc0f9f25b" TYPE="ext4"
/dev/block/mmcblk0p22: UUID="57f8f4bc-abf4-655f-bf67-946fc0f9f25b" TYPE="ext4"
/dev/block/mmcblk0p21: UUID="57f8f4bc-abf4-655f-bf67-946fc0f9f25b" TYPE="ext4"
/dev/block/mmcblk0p20: UUID="57f8f4bc-abf4-655f-bf67-946fc0f9f25b" TYPE="ext4"
/dev/block/mmcblk0p18: UUID="57f8f4bc-abf4-655f-bf67-946fc0f9f25b" TYPE="ext4"
/dev/block/mmcblk0p4: UUID="57f8f4bc-abf4-655f-bf67-946fc0f9f25b" TYPE="ext4"
/dev/block/mmcblk0p3: UUID="57f8f4bc-abf4-655f-bf67-946fc0f9f25b" TYPE="ext4"

	_______:  HD-internal-16GB :
root@s5neolte:/ # fdisk -l  /dev/block/mmcblk0
Disk /dev/block/mmcblk0: 15 GB, 15758000128 bytes, 30777344 sectors
1923584 cylinders, 1 heads, 16 sectors/track
Units: sectors of 1 * 512 = 512 bytes
Device             Boot StartCHS    EndCHS        StartLBA     EndLBA    Sectors  Size Id Type
/dev/block/mmcblk0p1    0,0,0       0,0,0                1   30777343   30777343 14.6G ee EFI GPT
root@s5neolte:/ #

	_______:  SDcard-8GB :
root@s5neolte:/ # fdisk -l  /dev/block/mmcblk1
Disk /dev/block/mmcblk1: 7568 MB, 7935623168 bytes, 15499264 sectors
961 cylinders, 256 heads, 63 sectors/track
Units: sectors of 1 * 512 = 512 bytes
Device             Boot StartCHS    EndCHS        StartLBA     EndLBA    Sectors  Size Id Type
/dev/block/mmcblk1p1 *  1023,255,63 1023,255,63       2048   15499263   15497216 7567M  c Win95 FAT32 (LBA)
Partition 1 has different physical/logical start (non-Linux?):
     phys=(1023,255,63) logical=(0,32,33)
Partition 1 has different physical/logical end:
     phys=(1023,255,63) logical=(961,4,4)
root@s5neolte:/ #

	_______:  
shell@s5neolte:/data $ cat /proc/mounts
rootfs / rootfs ro,seclabel 0 0
tmpfs /dev tmpfs rw,seclabel,nosuid,relatime,size=949184k,nr_inodes=237296,mode=755 0 0
devpts /dev/pts devpts rw,seclabel,relatime,mode=600 0 0
proc /proc proc rw,relatime 0 0
sysfs /sys sysfs rw,seclabel,relatime 0 0
selinuxfs /sys/fs/selinux selinuxfs rw,relatime 0 0
/sys/kernel/debug /sys/kernel/debug debugfs rw,relatime 0 0
none /acct cgroup rw,relatime,cpuacct 0 0
none /sys/fs/cgroup tmpfs rw,seclabel,relatime,size=949184k,nr_inodes=237296,mode=750,gid=1000 0 0
tmpfs /mnt tmpfs rw,seclabel,relatime,size=949184k,nr_inodes=237296,mode=755,gid=1000 0 0
tmpfs /mnt/secure tmpfs rw,seclabel,relatime,size=949184k,nr_inodes=237296,mode=700 0 0
tmpfs /mnt/secure/asec tmpfs rw,seclabel,relatime,size=949184k,nr_inodes=237296,mode=700 0 0
none /dev/cpuctl cgroup rw,relatime,cpu 0 0
/dev/block/platform/13540000.dwmmc0/by-name/SYSTEM /system ext4 ro,seclabel,relatime,norecovery 0 0
/dev/block/platform/13540000.dwmmc0/by-name/EFS /efs ext4 rw,seclabel,nosuid,nodev,noatime,discard,journal_checksum,journal_async_commit,noauto_da_alloc,data=ordered 0 0
/dev/block/platform/13540000.dwmmc0/by-name/CACHE /cache ext4 rw,seclabel,nosuid,nodev,noatime,discard,journal_checksum,journal_async_commit,noauto_da_alloc,errors=panic,data=ordered 0 0
/dev/block/platform/13540000.dwmmc0/by-name/USERDATA /data ext4 rw,seclabel,nosuid,nodev,noatime,discard,journal_checksum,journal_async_commit,noauto_da_alloc,data=ordered 0 0
/dev/block/platform/13540000.dwmmc0/by-name/PERSDATA /persdata/absolute ext4 rw,seclabel,nosuid,nodev,relatime,data=ordered 0 0
/dev/block/platform/13540000.dwmmc0/by-name/CPEFS /cpefs ext4 rw,seclabel,nosuid,nodev,noatime,data=ordered 0 0
tmpfs /storage tmpfs rw,seclabel,relatime,size=949184k,nr_inodes=237296,mode=755,gid=1000 0 0
tmpfs /sbin tmpfs rw,seclabel,relatime,size=949184k,nr_inodes=237296 0 0
/dev/block/platform/13540000.dwmmc0/by-name/SYSTEM /sbin/.magisk/mirror/system ext4 ro,seclabel,relatime,norecovery 0 0
/dev/block/platform/13540000.dwmmc0/by-name/USERDATA /sbin/.magisk/mirror/bin ext4 rw,seclabel,nosuid,nodev,noatime,discard,journal_checksum,journal_async_commit,noauto_da_alloc,data=ordered 0 0
/sbin/.magisk/block/loop08 /sbin/.magisk/img ext4 rw,seclabel,noatime,data=ordered 0 0
/data/knox/tmp_sdcard /mnt/knox sdcardfs rw,seclabel,nosuid,nodev,relatime,mask=0077 0 0
/data/knox/sdcard /mnt/knox/default/knox-emulated sdcardfs rw,seclabel,nosuid,nodev,relatime,low_uid=1000,low_gid=1000,gid=9997,multi_user,mask=0006 0 0
/data/knox/sdcard /mnt/knox/read/knox-emulated sdcardfs rw,seclabel,nosuid,nodev,relatime,low_uid=1000,low_gid=1000,gid=9997,multi_user,mask=0027 0 0
/data/knox/sdcard /mnt/knox/write/knox-emulated sdcardfs rw,seclabel,nosuid,nodev,relatime,low_uid=1000,low_gid=1000,gid=9997,multi_user,mask=0007 0 0
/data/knox/secure_fs/enc_media /mnt/shell/enc_media sdcardfs rw,seclabel,nosuid,nodev,relatime,low_uid=1000,low_gid=1000,gid=9997,multi_user,reserved=20MB 0 0
/data/media /mnt/runtime/default/emulated sdcardfs rw,seclabel,nosuid,nodev,noexec,relatime,low_uid=1023,low_gid=1023,gid=1015,multi_user,mask=0006,reserved=20MB 0 0
/data/media /storage/emulated sdcardfs rw,seclabel,nosuid,nodev,noexec,relatime,low_uid=1023,low_gid=1023,gid=1015,multi_user,mask=0006,reserved=20MB 0 0
/data/media /mnt/runtime/read/emulated sdcardfs rw,seclabel,nosuid,nodev,noexec,relatime,low_uid=1023,low_gid=1023,gid=9997,multi_user,mask=0027,reserved=20MB 0 0
/data/media /mnt/runtime/write/emulated sdcardfs rw,seclabel,nosuid,nodev,noexec,relatime,low_uid=1023,low_gid=1023,gid=9997,multi_user,mask=0007,reserved=20MB 0 0
/dev/block/vold/public:179,33 /mnt/media_rw/3829-15F7 vfat rw,dirsync,nosuid,nodev,noexec,noatime,nodiratime,uid=1023,gid=1023,fmask=0007,dmask=0007,allow_utime=0020,codepage=437,iocharset=iso8859-1,shortname=mixed,utf8,errors=remount-ro 0 0
/dev/block/vold/public:179,33 /mnt/secure/asec vfat rw,dirsync,nosuid,nodev,noexec,noatime,nodiratime,uid=1023,gid=1023,fmask=0007,dmask=0007,allow_utime=0020,codepage=437,iocharset=iso8859-1,shortname=mixed,utf8,errors=remount-ro 0 0
/mnt/media_rw/3829-15F7 /mnt/runtime/default/3829-15F7 sdcardfs rw,seclabel,nosuid,nodev,noexec,relatime,low_uid=1023,low_gid=1023,gid=1015,mask=0006 0 0
/mnt/media_rw/3829-15F7 /storage/3829-15F7 sdcardfs rw,seclabel,nosuid,nodev,noexec,relatime,low_uid=1023,low_gid=1023,gid=1015,mask=0006 0 0
/mnt/media_rw/3829-15F7 /mnt/runtime/read/3829-15F7 sdcardfs rw,seclabel,nosuid,nodev,noexec,relatime,low_uid=1023,low_gid=1023,gid=9997,mask=0022 0 0
/mnt/media_rw/3829-15F7 /mnt/runtime/write/3829-15F7 sdcardfs rw,seclabel,nosuid,nodev,noexec,relatime,low_uid=1023,low_gid=1023,gid=9997,mask=0022 0 0
shell@s5neolte:/data $

	_______:  
##________________________________________  ___________________________


#####  ==========  Allg-System-GS5-infos:
root@s5neolte:/sbin # uname -a
Linux localhost 3.10.61-10798689 #1 SMP PREEMPT Tue Feb 28 21:14:13 KST 2017 armv8l GNU/Linux
shell@s5neolte:/etc $ cat /proc/version
Linux version 3.10.61-10798689 (dpi@SWHD4908) (gcc version 4.9.x-google 20140827 (prerelease) (GCC) ) #1 SMP PREEMPT Tue Feb 28 21:14:13 KST 2017

	_______:  adb shell ,after-rooting-1--190223 :
shell@s5neolte:/ $ uname -a
Linux localhost 3.10.61-10798689 #1 SMP PREEMPT Tue Feb 28 21:14:13 KST 2017 armv8l
shell@s5neolte:/ $
shell@s5neolte:/data $ id
uid=2000(shell) gid=2000(shell) groups=2000(shell),1004(input),1007(log),1011(adb),1015(sdcard_rw),1028(sdcard_r),3001(net_bt_admin),3002(net_bt),3003(inet),3006(net_bw_stats) context=u:r:shell:s0

	_______:  CPU /Pocessors :
shell@s5neolte:/ $ cat  /proc/cpuinfo
Processor	: AArch64 Processor rev 3 (aarch64)
processor	: 0
Features	: fp asimd aes pmull sha1 sha2 crc32 wp half thumb fastmult vfp edsp neon vfpv3 tlsi vfpv4 idiva idivt
CPU implementer	: 0x41
CPU architecture: 8
CPU variant	: 0x0
CPU part	: 0xd03
CPU revision	: 3
Hardware	: SAMSUNG Exynos7580
##________________________________________  ___________________________


#####  ==========  getprop GS5-rooted1 /190225 :
Mon Feb 25 13:45:19 UTC 2019
root@s5neolte:/data/d11 # getprop
[audioflinger.bootsnd]: [0]
[boot.sfbootcomplete]: [0]
[dalvik.vm.dex2oat-Xms]: [64m]
[dalvik.vm.dex2oat-Xmx]: [512m]
[dalvik.vm.dex2oat-filter]: [speed]
[dalvik.vm.heapgrowthlimit]: [128m]
[dalvik.vm.heapmaxfree]: [8m]
[dalvik.vm.heapminfree]: [2m]
[dalvik.vm.heapsize]: [512m]
[dalvik.vm.heapstartsize]: [8m]
[dalvik.vm.heaptargetutilization]: [0.75]
[dalvik.vm.image-dex2oat-Xms]: [64m]
[dalvik.vm.image-dex2oat-Xmx]: [64m]
[dalvik.vm.image-dex2oat-filter]: [speed]
[dalvik.vm.isa.arm.features]: [default]
[dalvik.vm.isa.arm.variant]: [cortex-a15]
[dalvik.vm.stack-trace-file]: [/data/anr/traces.txt]
[debug.atrace.tags.enableflags]: [0]
[debug.force_rtl]: [0]
[debug.hwc.otf]: [1]
[debug.hwc.winupdate]: [1]
[debug.sf.layerdump]: [0]
[dev.bootcomplete]: [1]
[dev.kies.deviceowner]: [0]
[dev.kies.drivedisplay]: [1]
[dev.kies.drivedisplay.trust]: [0]
[dev.kies.sommode]: [TRUE]
[dev.kiessupport]: [TRUE]
[dev.knoxapp.running]: [false]
[dev.ssrm.app.type]: [false]
[dev.ssrm.appsync3p]: [true]
[dev.ssrm.current]: [NA]
[dev.ssrm.emergencymode]: [false]
[dev.ssrm.hmt_level]: [0]
[dev.ssrm.init]: [1]
[dev.ssrm.lpc_ver]: [1.0.21]
[dev.ssrm.mode]: []
[dev.ssrm.pst]: [193]
[dev.ssrm.smart_switch]: [false]
[dhcp.wlan0.dns1]: [192.168.8.1]
[dhcp.wlan0.dns2]: []
[dhcp.wlan0.dns3]: []
[dhcp.wlan0.dns4]: []
[dhcp.wlan0.domain]: []
[dhcp.wlan0.gateway]: [192.168.8.1]
[dhcp.wlan0.ipaddress]: [192.168.8.106]
[dhcp.wlan0.leasetime]: [86400]
[dhcp.wlan0.mask]: [255.255.255.0]
[dhcp.wlan0.mtu]: []
[dhcp.wlan0.pid]: [3844]
[dhcp.wlan0.reason]: [ROUTERADVERT]
[dhcp.wlan0.result]: [failed]
[dhcp.wlan0.roaming]: [0]
[dhcp.wlan0.server]: [192.168.8.1]
[dhcp.wlan0.vendorInfo]: []
[drm.service.enabled]: [true]
[gsm.current.phone-type]: [1]
[gsm.network.type]: [Unknown]
[gsm.operator.alpha]: []
[gsm.operator.iso-country]: [de]
[gsm.operator.ispsroaming]: [false]
[gsm.operator.isroaming]: [false]
[gsm.operator.numeric]: [26203]
[gsm.sim.operator.alpha]: []
[gsm.sim.operator.iso-country]: []
[gsm.sim.operator.numeric]: []
[gsm.sim.state]: [ABSENT]
[gsm.version.baseband]: [G903FXXU1BQC1]
[gsm.version.ril-impl]: [Samsung RIL v3.0]
[init.svc.BCS-daemon]: [running]
[init.svc.DIAG-daemon]: [running]
[init.svc.DR-daemon]: [running]
[init.svc.SIDESYNC_service]: [running]
[init.svc.SMD-daemon]: [running]
[init.svc.Tr63Njg]: [stopped]
[init.svc.adbd]: [running]
[init.svc.apaservice]: [running]
[init.svc.argos-daemon]: [running]
[init.svc.at_distributor]: [running]
[init.svc.auditd]: [running]
[init.svc.bootanim]: [stopped]
[init.svc.bootchecker]: [stopped]
[init.svc.ccm]: [running]
[init.svc.compact_memory]: [stopped]
[init.svc.cpboot-daemon]: [running]
[init.svc.cs_service]: [running]
[init.svc.debuggerd]: [running]
[init.svc.dhcpcd_wlan0]: [stopped]
[init.svc.drm]: [running]
[init.svc.edmaudit]: [running]
[init.svc.epmlogd]: [stopped]
[init.svc.flash_recovery]: [stopped]
[init.svc.gatekeeperd]: [running]
[init.svc.gpsd]: [running]
[init.svc.healthd]: [running]
[init.svc.icd]: [stopped]
[init.svc.installd]: [running]
[init.svc.ipsec-daemon]: [running]
[init.svc.jackservice]: [running]
[init.svc.keystore]: [running]
[init.svc.lmkd]: [running]
[init.svc.logd]: [running]
[init.svc.logd-reinit]: [stopped]
[init.svc.macloader]: [stopped]
[init.svc.media]: [running]
[init.svc.mobex-daemon]: [running]
[init.svc.mobicore]: [running]
[init.svc.netd]: [running]
[init.svc.otp]: [running]
[init.svc.p2p_supplicant]: [stopped]
[init.svc.powersnd]: [stopped]
[init.svc.prepare_param]: [stopped]
[init.svc.ril-daemon]: [running]
[init.svc.scs]: [stopped]
[init.svc.sdp_cryptod]: [running]
[init.svc.sec-sh]: [stopped]
[init.svc.servicemanager]: [running]
[init.svc.ss_kb_service]: [running]
[init.svc.surfaceflinger]: [running]
[init.svc.swapon]: [stopped]
[init.svc.tnycLGs]: [stopped]
[init.svc.ueventd]: [running]
[init.svc.vold]: [running]
[init.svc.watchdogd]: [running]
[init.svc.zygote]: [running]
[installd.sdcard_manipulate_done]: [0]
[keyguard.no_require_sim]: [true]
[logd.auditd]: [false]
[logd.klogd]: [false]
[net.bt.name]: [Android]
[net.change]: [net.dns2]
[net.dns1]: [fe80::3a37:8bff:fe2f:705%wlan0]
[net.dns2]: [192.168.8.1]
[net.hostname]: [android-8464af9e420aae0f]
[net.knox.shareddevice.version]: [2.6.0]
[net.knoxscep.version]: [2.0.1]
[net.knoxsso.version]: [2.5.0]
[net.knoxvpn.version]: [2.2.4]
[net.qtaguid_enabled]: [1]
[net.smart_switch.disabled]: [1]
[net.streaming.rtsp.uaprof]: [http://wap.samsungmobile.com/uaprof/]
[net.tcp.default_init_rwnd]: [60]
[nfc.fw.downloadmode_force]: [0]
[nfc.fw.rfreg_mode]: [normal]
[nfc.fw.rfreg_ver]: [15/6/25/9.37.53]
[nfc.smartcard.binded]: [true]
[persist.audio.allsoundmute]: [0]
[persist.audio.cpufreq]: [350000]
[persist.audio.finemediavolume]: [1]
[persist.audio.globaleffect]: [1]
[persist.audio.headsetsysvolume]: [9]
[persist.audio.hphonesysvolume]: [9]
[persist.audio.mpseek]: [0]
[persist.audio.mysound]: [1]
[persist.audio.ringermode]: [2]
[persist.audio.soundalivefxsec]: [1]
[persist.audio.stereospeaker]: [0]
[persist.audio.sysvolume]: [9]
[persist.audio.uhqa]: [0]
[persist.audio.voipcpufreq]: [350000]
[persist.bluetooth_fw_ver]: [bcm43455_V0109.0146.hcd]
[persist.demo.hdmirotationlock]: [false]
[persist.keyguard.ucs]: []
[persist.keyguard.ucs.csname]: []
[persist.logd.size]: []
[persist.radio.calldefault.simid]: [0]
[persist.radio.dataprefer.slotId]: [0]
[persist.radio.initphone-type]: [1]
[persist.radio.plmnname_1]: []
[persist.radio.plmnname_2]: []
[persist.radio.sib16_support]: [0]
[persist.ril.modem.board]: [SHANNON310]
[persist.security.ams.enforcing]: [3]
[persist.security.tlc.ccm]: [0]
[persist.security.tlc.otp]: [0]
[persist.security.tlc.tui]: [1]
[persist.service.bdroid.version]: [4.1]
[persist.sys.SUWRebootReason]: []
[persist.sys.ccm.date]: [Tue Feb 28 21:18:15 KST 2017]
[persist.sys.dalvik.vm.lib.2]: [libart.so]
[persist.sys.drs.date]: [Tue Feb 28 21:18:15 KST 2017]
[persist.sys.kap.date]: [Tue Feb 28 21:18:15 KST 2017]
[persist.sys.kap.status]: [NONE]
[persist.sys.locale]: [en-ZA]
[persist.sys.localedefault]: [de-DE]
[persist.sys.profiler_ms]: [0]
[persist.sys.sb.setting.enabled]: [false]
[persist.sys.setupwizard]: [FINISH]
[persist.sys.silent]: [0]
[persist.sys.sm_mode]: [1]
[persist.sys.storage_preload]: [2]
[persist.sys.timezone]: [Europe/Berlin]
[persist.sys.usb.config]: [mtp,adb]
[persist.sys.webview.vmsize]: [104857600]
[ril.CompleteMsg]: [OK]
[ril.ICC_TYPE]: [0]
[ril.RildInit]: [1]
[ril.approved_codever]: [none]
[ril.approved_cscver]: [none]
[ril.approved_modemver]: [none]
[ril.atd_status]: [1_1_0]
[ril.backoffstate]: [1024]
[ril.cbd.boot_done]: [1]
[ril.cbd.dt_revision]: [011]
[ril.cbd.rfs_check_done]: [1]
[ril.cs_svc]: [1]
[ril.ecclist00]: [112,911,999,000,08,110,118,119]
[ril.ecclist_net0]: []
[ril.hasisim]: [0]
[ril.hw_ver]: [MP 0.500]
[ril.ims.ecsupport]: [2]
[ril.ims.ltevoicesupport]: [2]
[ril.model_id]: [QB5889412]
[ril.modem.board]: [SHANNON310]
[ril.official_cscver]: [G903FOXA1BQC1]
[ril.product_code]: [SM-G903FZDADBT]
[ril.radiostate]: [10]
[ril.rfcal_date]: [20150826]
[ril.serialnumber]: [RF8G82FTAFD]
[ril.servicestate]: [2]
[ril.ss.routing]: [0]
[ril.subinfo]: [0:2147483643]
[ril.sw_ver]: [G903FXXU1BQC1]
[ril.timezoneID]: [Europe/Berlin]
[ril.voice.rat]: [3]
[rild.libpath]: [/system/lib/libsec-ril.so]
[rild.libpath2]: [/system/lib/libsec-ril-dsds.so]
[ro.adb.qemud]: [1]
[ro.adb.secure]: [1]
[ro.allow.mock.location]: [0]
[ro.arch]: [exynos7580]
[ro.astcenc.astcsupport]: [1]
[ro.baseband]: [unknown]
[ro.board.platform]: [exynos5]
[ro.boot.boot_salescode]: []
[ro.boot.bootloader]: [G903FXXU1BQC1]
[ro.boot.debug_level]: [0x4f4c]
[ro.boot.emmc_checksum]: [3]
[ro.boot.hardware]: [samsungexynos7580]
[ro.boot.hmac_mismatch]: [0]
[ro.boot.hw_rev]: [11]
[ro.boot.odin_download]: [1]
[ro.boot.sec_atd.tty]: [/dev/ttySAC1]
[ro.boot.security_mode]: [1526595584]
[ro.boot.selinux]: [enforcing]
[ro.boot.serialno]: [330024514e93624b]
[ro.boot.ucs_mode]: [0]
[ro.boot.warranty_bit]: [0]
[ro.boot_recovery]: [unknown]
[ro.bootimage.build.date]: [Tue Feb 28 21:20:50 KST 2017]
[ro.bootimage.build.date.utc]: [1488284450]
[ro.bootimage.build.fingerprint]: [samsung/s5neoltexx/s5neolte:6.0.1/MMB29K/G903FXXU1BQC1:user/test-keys]
[ro.bootloader]: [G903FXXU1BQC1]
[ro.bootmode]: [unknown]
[ro.bt.bdaddr_path]: [/efs/bluetooth/bt_addr]
[ro.build.PDA]: [G903FXXU1BQC1]
[ro.build.changelist]: [10798689]
[ro.build.characteristics]: [phone]
[ro.build.date]: [Tue Feb 28 21:18:15 KST 2017]
[ro.build.date.utc]: [1488284295]
[ro.build.description]: [s5neoltexx-user 6.0.1 MMB29K G903FXXU1BQC1 release-keys]
[ro.build.display.id]: [MMB29K.G903FXXU1BQC1]
[ro.build.fingerprint]: [samsung/s5neoltexx/s5neolte:6.0.1/MMB29K/G903FXXU1BQC1:user/release-keys]
[ro.build.flavor]: [s5neoltexx-user]
[ro.build.hidden_ver]: [G903FXXU1BQC1]
[ro.build.host]: [SWHD4908]
[ro.build.id]: [MMB29K]
[ro.build.official.release]: [true]
[ro.build.product]: [s5neolte]
[ro.build.scafe]: [capuccino]
[ro.build.scafe.cream]: [white]
[ro.build.scafe.shot]: [single]
[ro.build.scafe.size]: [short]
[ro.build.scafe.version]: [2016A]
[ro.build.selinux]: [0]
[ro.build.selinux.enforce]: [1]
[ro.build.tags]: [release-keys]
[ro.build.type]: [user]
[ro.build.user]: [dpi]
[ro.build.version.all_codenames]: [REL]
[ro.build.version.base_os]: []
[ro.build.version.codename]: [REL]
[ro.build.version.incremental]: [G903FXXU1BQC1]
[ro.build.version.preview_sdk]: [0]
[ro.build.version.release]: [6.0.1]
[ro.build.version.sdk]: [23]
[ro.build.version.sdl]: [2301]
[ro.build.version.security_patch]: [2017-03-01]
[ro.carrier]: [unknown]
[ro.chipname]: [exynos7580]
[ro.com.google.clientidbase]: [android-samsung]
[ro.com.google.gmsversion]: [6.0_r10]
[ro.config.alarm_alert]: [Morning_Flower.ogg]
[ro.config.dha_cached_max]: [8]
[ro.config.dha_cached_min]: [4]
[ro.config.dha_empty_init]: [24]
[ro.config.dha_empty_max]: [24]
[ro.config.dha_empty_min]: [6]
[ro.config.dha_lmk_scale]: [1.341]
[ro.config.dha_pwhitelist_enable]: [1]
[ro.config.dha_th_rate]: [1.83]
[ro.config.dmverity]: [true]
[ro.config.kap]: [true]
[ro.config.knox]: [v30]
[ro.config.mdha_ssr_enable]: [true]
[ro.config.media_sound]: [Media_preview_Touch_the_light.ogg]
[ro.config.notification_sound]: [Skyline.ogg]
[ro.config.notification_sound_2]: [S_Charming_Bell.ogg]
[ro.config.ringtone]: [Over_the_Horizon.ogg]
[ro.config.ringtone_2]: [Basic_Bell.ogg]
[ro.config.rkp]: [true]
[ro.config.rm_preload_enabled]: [0]
[ro.config.tima]: [1]
[ro.config.timaversion]: [3.0]
[ro.cp_debug_level]: [unknown]
[ro.crypto.fuse_sdcard]: [true]
[ro.crypto.state]: [unencrypted]
[ro.csc.country_code]: [Germany]
[ro.csc.countryiso_code]: [DE]
[ro.csc.sales_code]: [DBT]
[ro.dalvik.vm.native.bridge]: [0]
[ro.debug_level]: [0x4f4c]
[ro.debuggable]: [0]
[ro.emmc_checksum]: [3]
[ro.error.receiver.default]: [com.samsung.receiver.error]
[ro.expect.recovery_id]: [0xb7a1587fbbc840cc41d3bea87e10ac23a09fb07d000000000000000000000000]
[ro.fmp_config]: [unknown]
[ro.frp.pst]: [/dev/block/persistent]
[ro.hardware]: [samsungexynos7580]
[ro.hmac_mismatch]: [0]
[ro.hwui.drop_shadow_cache_size]: [6]
[ro.hwui.gradient_cache_size]: [2]
[ro.hwui.layer_cache_size]: [34]
[ro.hwui.path_cache_size]: [10]
[ro.hwui.r_buffer_cache_size]: [4]
[ro.hwui.shape_cache_size]: [4]
[ro.hwui.text_large_cache_height]: [1024]
[ro.hwui.text_large_cache_width]: [2048]
[ro.hwui.text_small_cache_height]: [1024]
[ro.hwui.text_small_cache_width]: [1024]
[ro.hwui.texture_cache_flushrate]: [0.4]
[ro.hwui.texture_cache_size]: [50]
[ro.im.param.offset]: [unknown]
[ro.kernel.qemu]: [0]
[ro.kernel.qemu.gles]: [1]
[ro.mct.compressiontype]: [ETC1]
[ro.me.param.offset]: [unknown]
[ro.multisim.simslotcount]: [1]
[ro.nfc.port]: [I2C]
[ro.opengles.version]: [196609]
[ro.pr.param.offset]: [unknown]
[ro.product.board]: [universal7580]
[ro.product.brand]: [samsung]
[ro.product.cpu.abi]: [armeabi-v7a]
[ro.product.cpu.abi2]: [armeabi]
[ro.product.cpu.abilist]: [armeabi-v7a,armeabi]
[ro.product.cpu.abilist32]: [armeabi-v7a,armeabi]
[ro.product.cpu.abilist64]: []
[ro.product.device]: [s5neolte]
[ro.product.locale]: [en-GB]
[ro.product.manufacturer]: [samsung]
[ro.product.model]: [SM-G903F]
[ro.product.name]: [s5neoltexx]
[ro.product_ship]: [true]
[ro.revision]: [0]
[ro.ril.gprsclass]: [10]
[ro.ril.hsxpa]: [1]
[ro.rtn_config]: [unknown]
[ro.runtime.firstboot]: [1551083548119]
[ro.sec.fle.encryption]: [true]
[ro.secure]: [1]
[ro.security.icd.flagmode]: [multi]
[ro.security.reactive.version]: [2.0.9]
[ro.security.vpnpp.release]: [6.1]
[ro.security.vpnpp.ver]: [1.4]
[ro.security_mode]: [1526595584]
[ro.serialno]: [330024514e93624b]
[ro.setupwizard.mode]: [OPTIONAL]
[ro.sf.lcd_density]: [480]
[ro.sku.param.offset]: [unknown]
[ro.smps.enable]: [true]
[ro.sn.param.offset]: [unknown]
[ro.telephony.default_network]: [9]
[ro.warranty_bit]: [0]
[ro.wifi.channels]: []
[ro.zygote]: [zygote32]
[ro.zygote.disable_gl_preload]: [1]
[rw.km_fips_status]: [ready]
[sec.fle.encryption.status]: [Dec NewFile IncludeMedia]
[secmm.player.gp.url]: [true]
[security.ASKS.policy_version]: [161011]
[security.mdpp.mass]: [skmm]
[selinux.policy_version]: [SEPF_SECMOBILE_6.0.1_0034]
[service.bootanim.exit]: [0]
[service.camera.rec.running]: [0]
[service.camera.running]: [0]
[service.media.powersnd]: [1]
[storage.mmc.size]: [15758000128]
[sys.adaptivedisplay.eadon]: [true]
[sys.boot_completed]: [1]
[sys.cameramode.blackbox]: [0]
[sys.cameramode.vtcall]: [0]
[sys.config.samp_spcm_enable]: [true]
[sys.dockstate]: [0]
[sys.enterprise.billing.version]: [1.2.0]
[sys.enterprise.otp.version]: [2.6.0]
[sys.isdumpstaterunning]: [0]
[sys.knox.exists]: [0]
[sys.knox.store]: [0]
[sys.mobicoredaemon.enable]: [true]
[sys.nfc.support]: [1]
[sys.oem_unlock_allowed]: [1]
[sys.settings_global_version]: [5]
[sys.settings_system_version]: [15]
[sys.siop.level]: [0]
[sys.ssrm.mdnie]: [-1]
[sys.sysctl.compact_memory]: [0]
[sys.sysctl.extra_free_kbytes]: [24300]
[sys.sysctl.tcp_adv_win_scale]: [1]
[sys.sysctl.tcp_def_init_rwnd]: [60]
[sys.usb.config]: [mtp,adb]
[sys.usb.configfs]: [0]
[sys.usb.state]: [mtp,adb]
[system.camera.CC.disable]: [0]
[telephony.lteOnCdmaDevice]: [0]
[vold.has_adoptable]: [0]
[vold.post_fs_data_done]: [1]
[vzw.os.rooted]: [false]
[wifi.interface]: [wlan0]
[wlan.driver.status]: [unloaded]
[wlan.p2p.chkintent]: [0]
root@s5neolte:/data/d11 #
##________________________________________  ___________________________


#####  ==========  
