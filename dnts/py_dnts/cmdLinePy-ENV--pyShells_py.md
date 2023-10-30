"python"-Cmdline-calls  + Py-Interactive-Shell Python interpreter and its interaction with its environment + alternatives/iPython, cmdline calls, run in shell, ENV, ...: ________________
=====================================================================


#####  ==========  cmdline-call + ENV/paths/Libs/... py :
	- ! https://docs.python.org/3/using/cmdline.html  + man python
	- listing of LIBs/py.pathes/... :   alias epylines='echo -e ${PYTHONPATH//:/\\n}'    ##-/OR-just:   echo -e ${PYTHONPATH//:/"\n"}
##________________________________________  ___________________________


#####  ==========  pyShell , py-interactive-interpreter from cmdline "python":     #-see ref.tut--6.2 . ...
	-! startup-config (like .profile in shell):    export PYTHONSTARTUP=<my-startup-filepath>
	   Python will execute the contents of a file identified by the PYTHONSTARTUP environment variable when you start an interactive interpreter. To customize Python even for non-interactive mode, see *The Customization Modules*. #--see ref--tutorial--interactive.txt
	   also for a sample see the aboce doc in tutorial!
	- prompt of py-shell:  import sys; sys.ps1="py--> " ; sys.ps2="py..>" ;
	- sys.path is a list of strings that determines the interpreter’s search path for modules. eg: sys.path.append(’/ufs/guido/lib/python’)
	-! docs of any func/module/... from py.shell:  xxx.__doc__  (or with print xxx.__doc__; for \n ...), as:  print v1.replace.__doc__
##________________________________________  ___________________________


#####  ==========  IPython.shell:
	- http://ipython.org/
	-! withount installation just using: tar -xzvf ipython.src.xxx.tgz ; cd src.xxx ; python ipython.py
	- installation as NO-root: use --install-dir  (or --prefix ??) as in:
	  export PYTHONPATH=${PYTHONPATH}:${HOME}/.py1 ;   easy_install  --install-dir=${HOME}/.py1   ipython[zmq,qtconsole,notebook,test]
##________________________________________  ___________________________


#####  ==========  Python Runtime:
	-! see  pyRefDocs-StdLibs: Python Runtime Services
##________________________________________  ___________________________


#####  ==========  idle (Tk-based-py-shell):
	- py-shelll-Tk-based-GUI, requires Tk (pacman -S tk ) on the system!
	- python-binding-to-Tk (Tkinter) is already in pyStdLib included: pydoc tkinter   #- Tkinter is a Python binding to the Tk GUI toolkit.  https://en.wikipedia.org/wiki/Tkinter
	- idle --help   ##-!- NOT man idle ! (refers to C-headerfile !)
	- https://realpython.com/python-idle/
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________
