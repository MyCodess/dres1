#!/bin/bash

##--I-see https://wiki.archlinux.org/index.php/Offline_installation_of_packages  : Offline installation of packages

ARCH='x86_64'
MIRROR='https://ftp.spline.inf.fu-berlin.de/mirrors/archlinux/'
##--org MIRROR='https://mirrors.kernel.org/archlinux/'

set -x
wget "${MIRROR}/community/os/${ARCH}/community.db"
wget "${MIRROR}/core/os/${ARCH}/core.db"
wget "${MIRROR}/extra/os/${ARCH}/extra.db"
wget "${MIRROR}/multilib/os/${ARCH}/multilib.db"
set +x

echo ====================== 1done __________________________________

