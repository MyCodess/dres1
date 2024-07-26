________________ virtualENv_py, venv, alternative-venvs, ...: ______________________________


##############################  "venv" in stdLib : ###############################################
#####  ==========  venv-urls/docs :
	- ! venv-pimer:   https://realpython.com/python-virtual-environments-a-primer/
	https://docs.python.org/3/tutorial/venv.html
	https://packaging.python.org/en/latest/tutorials/installing-packages/#creating-virtual-environments
	https://docs.python.org/3.10/library/site.html
	! https://docs.python.org/3/library/sys_path_init.html   :  The initialization of the sys.path module search path /  PYTHONPATH /  PYTHONHOME
	-  pydoc  venv ,  pydoc  site
	- venv is subset of "Virtualenv", but integrated into py-std-install) :  pydoc  venv , https://peps.python.org/pep-0405/
##________________________________________  ___________________________


#####  ==========  venv-nts-Allg/-concepts/Infs / how it works :
    - ! https://realpython.com/python-virtual-environments-a-primer/#how-does-a-virtual-environment-work :
    --- ! nts-structure: 
        - Python virtual environment is just a folder structure with a settings file (./pyvenv.cfg) :
        - Python virtual environment in its simplest form would consist of nothing more than a copy or symlink of the Python binary accompanied by a pyvenv.cfg file and a site-packages directory. see https://www.python.org/dev/peps/pep-0405/#specification
    --- site-packages :
        - ! as long as your virt-env is active, ALL things/insalls/... will be done in your virtEnv ! so also python and pip cmds act in your virtEnv !
        - (venv1)  python -m pip list    ##--: you see, it lists ONLY pkgs of your venv! not the system ones, if asked in your venv !
        - site-packages concept, see pydoc site ,  and also 
    --- sys.prefix (venv-DIR) /  sys.base_prefix ("base"-/system-/OS-DIR) !! DIFF of both :
        - in venv the sys.prefix ist set to your venv1_DP ! check it in py-shell for both venv1 + system !
        - standard-library modules (also The site and sysconfig ) are modified such that the standard library and header files are found relative to sys.base_prefix (1kk: so, the system-installation), while "site-package" directories […] are still found relative to sys.prefix (1kk: so, the venv1-tree). see :  https://peps.python.org/pep-0405/#specification
        - sys.prefix feature, which is defined based on the start-DIR of python! so it changes the path for python-executable with a link in the new venv-dir/bin ! then:
	    - so, If Python is run in a virtual environment (as described at Virtual Environments and Packages) then prefix and exec_prefix are specific to the virtual environment. 
        - “pyvenv.cfg”  existance effekt:  If a file named “pyvenv.cfg” exists one directory above sys.executable (so, above ./bin/python, so in the root of newly created dir for venv!), sys.prefix and sys.exec_prefix are set to that directory and it is also checked for site-packages (sys.base_prefix and sys.base_exec_prefix will always be the “real” prefixes of the Python installation).   : https://docs.python.org/3.10/library/site.html
	    - so If a pyvenv.cfg file is found alongside the main executable, OR in the directory one level above the executable, ...
        - see also:  https://docs.python.org/3/library/sys_path_init.html#virtual-environments  :
        - also dementsprechend check sys.path in both py-shells (venv + OS) ; sys.path determine which locations Python can import modules from.
##________________________________________  ___________________________


#####  ==========  venv-usages:
    _______:  creation/setup/start your virtEnv (eg "Tut1" dir):
    - python -m venv Tut1 --prompt="venv-tut1" --upgrade-deps ;  Tut1/bin/activate ; deactivate ;   ##see script Tut1/bin/activate !
    - params for venv cration : see pydoc venv : __init__(self, system_site_packages=False, clear=False, symlinks=False, upgrade=False, with_pip=False, prompt=None, upgrade_deps=False)
    - without --upgrade-deps param then usu. basic-libs (so, also pip, setuptools,...) in your venv1 are already outdated (venv takes the org-cpython-installation-versions without connecting to the internet! )
    - pip upgrade : usu. your pip in venv1 is already outdated ! so upgrade it:  (venv) $ python -m pip install --upgrade pip  ##--see:  https://realpython.com/python-virtual-environments-a-primer/#update-the-core-dependencies
    - upgrading the whole venv1 if needed (eg system newly upgraded,...): cd <your-venv1-parent> ;  python3 -m venv venv1 --upgrade
    - reproduce/COPY your venv1 : (venv1) $ python -m pip freeze > requirements.txt ; ... ; (new-venv) $ python -m pip install -r requirements.txt
        BUT this does NOT contain infs about prj-base-pyCore  and also sub-dependencies !
##________________________________________  ___________________________


#####  ==========  venv-manually copying/migrating a venv-dir to a new one
    - ! nts: Python virtual environment is just a folder structure with a settings file (./pyvenv.cfg) !
    - ! https://realpython.com/python-virtual-environments-a-primer/#how-does-a-virtual-environment-work :

    _______:  
    - here  src-venv-dir tut1 , new-target-dir tut2 :
    cp -a tut1  tut2 ;
    cdlla tut2 ;  grep -iRl tut1  ##--just-to-see/check
    sed -i.sd1 -e 's@tut1@tut2@' $( grep -iRl tut1 )
    if needed vi pyvenv.cfg  ##--....

    _______: more:
    - not really needed ./bin/activ* : they set ONLY PATH + PROMPT ! so export PATH=<venv-absolute_DP>/bin:$PATH , and PS1="(tut2) ${PS1:-}"
    - if you call:  (tut2) $ ./bin/python bzw. ./bin/pip  , it works also without PATH adaptions !
    - using also system-site-pkgs : either  vi pyvenv.cfg : include-system-site-packages = true ; /OR generate venv with:  python -m venv venv --system-site-packages
    
    _______:  activate[.sh] script bzw.  withOUT-activate-script using venv1 :
    - ! activate[.sh] does only two things: PATH + PROMPT ! so:   export PATH=<venv-abs_DP>/bin:$PATH , and PS1="(tut2) ${PS1:-}"
    - so to use your venv1 wihtOUT calling activate script: either export PATH=<venv-abs_DP>/bin:$PATH  #/OR ie even sufficient if you call the absolute-path-of-python-in-your-venv1 as /up1/varu/varau/wks/py_venv1/tut1/bin/python ... !
    - ! so, just using the absolute-path-of-python-executable (bzw. abs-pip-path) in your venv1 is sufficient ! the rest is done by python-inerpreter !
    just call th "python"-executable (link) of you venv, eg: /up1/varu/varau/wks/py_venv1/tut1/bin/python
    due to existing  ../pyvenv.cfg then python switches to your venv-python-env ! see here notes to  pyvenv.cfg !
    -  which python-executable am I using? :  import sys; sys.executable ;
##________________________________________  ___________________________


#####  ==========  venv-configs /-customizing :
    - ! see also here section: venv-nts/-concepts !
##________________________________________  ___________________________




##############################  other virtEnvs: virtualenv, ... , utils/libs-virtEnvs :#########################################
#####  ==========  "virtualenv" :
	- virtualenv is a superset of venv
    - https://virtualenv.pypa.io/
	- https://packaging.python.org/tutorials/installing-packages/  :  Installing packages using pip and virtual environments
##________________________________________  ___________________________


#####  ==========  libs/utils/... for py-ENVs-mgm , py-installs-magm ... , Alternative-virtualenvs_py :
    - pyenv : Simple Python Version Management: pyenv , https://github.com/pyenv/pyenv
	- Pipenv : automatically creates and manages a virtualenv for your projects, as well as adds/removes packages from your Pipfile as you install/uninstall packages. ... https://pipenv.pypa.io/
    --- other virtEnvs :
    - Conda offers package, dependency, and environment management for Python and other languages.  https://docs.conda.io/
##________________________________________  ___________________________

