___________________ PyCore-installs/setups/configs/... on system/user ...... _______________________________________________


#####  ==========  OSs/arx-adapts...:
    - /:230831  :  pip user problem, then:  mvi /usr/lib/python3.11/EXTERNALLY-MANAGED /usr/lib/python3.11/EXTERNALLY-MANAGED_1org
##________________________________________  ___________________________


#####  ==========  docs-installs / modules-installs :
    Installing Python Modules/PyPkgs :  https://docs.python.org/3/installing/index.html
    packages-installs:   https://packaging.python.org/tutorials/installing-packages/
    setuptools  :  https://setuptools.readthedocs.io/en/latest/
    Python Setup and Usage  :  https://docs.python.org/3/using/index.html
    pydoc  setuptools
##________________________________________  ___________________________


#####  ==========  manually install pyCore + pip in user-dir without sudo /OR in-system-parallel-to-other-py-versions  ...:
    --- 2chk/not-tryed!
    
    --- pyCore-install/compile, no sudo:
    - so basically have to download py-src, do ./configure prefix=... and make it, and set PATH , as:
    wget https://www.python.org/ftp/python/3.6.10/Python-3.6.10.tgz : tar -xzvf xxx ;
    ?? find ./Python-3.6.10/Python -type d | xargs chmod 0755
    cd ./Python-3.6.10 ;
    ./configure --prefix=$PWD/Python-3.6.10/Python ; make ; make install ;
    export PATH=$CWD:$PATH ;
    - see  https://gist.github.com/sumanthratna/17a265ffbcc846259ee7e59e80c2b8a4

    --- pipCore-install/compile, no sudo:
    see pip_dnts !
##________________________________________  ___________________________


#####  ==========  parallel-instalations of pyCores:
    - see here section for manually install pyCore !
    - also possible by using virtualenv / venv !

    _______: pyenv :
    - !  https://realpython.com/intro-to-pyenv/  : Managing Multiple Python Versions With pyenv
    pyenv is a tool for managing multiple Python versions 
    pyenv install 3.9v  ##--eg parallel to existing 3.11 version !
##________________________________________  ___________________________



#####  ==========  configs-of-pyCore:
    - pydoc sysconfig : Access to Python's configuration information :
    eg:  import sysconfig ; sysconfig.get_path("purelib") ; sysconfig.get_path("platlib") ; ...
##________________________________________  ___________________________

#####  ==========  site / site-packages : Customization of of-install per User/System:
    --- docs ...:
    - https://docs.python.org/3.9/library/site
    - pydoc  site
    - RefTutDocs  :  16.1.4. The Customization Modules  , https://docs.python.org/3/tutorial/appendix.html#the-customization-modules
    ---
    - path of site-packages?:  import sysconfig ; sysconfig.get_path("purelib") ; sysconfig.get_path("platlib") ;
    - customizes py-install-libs for yourself /OR wohole OS/system, so: Append module search paths for third-party packages to sys.path :
    - !!  python -m site [ --user-site ]
    -  ~/.local/lib/python3.9/site-packages   :  to install libs/pkgs ONLY for the USER (not-SYSTEM)
    - user site-packages directory normally appears before the system site-packages directory on sys.path. Thus, packages you install using this technique take priority over SYSTEM-wide ones!
    - force USER-insllas eg:   python3  setup.py  install --user <pkg>  ; ##-OR-libs:   pip  install  --user  packagename
##________________________________________  ___________________________


#####  ==========  Startups/Setups-py ...:
    PYTHONSTARTUP envVar-value-filepath is for interactive-shell like .profile-for-bash ! see man python : This file is only read in interactive sessions, not when Python reads commands from a script, and not when /dev/tty is given as the explicit source of commands (which otherwise behaves like an interactive session). 
##________________________________________  ___________________________


#####  ==========  distributing own Apps/libs, so make them available to others (eg in PyPi):
    -! see pyCookBK--10.15  +  docsRF--An Introduction to Distutils !
    - files in the pkg-root-dir  :  setup.py and MANIFEST.in 
##________________________________________  ___________________________

