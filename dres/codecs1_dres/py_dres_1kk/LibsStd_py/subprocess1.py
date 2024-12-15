""" 
Py3/Doc/html/library/subprocess.html /:240917  
https://python.land/operating-system/python-subprocess
------
- cmds/args: list better than str! : args is required for all calls and should be a string, or a sequence of program arguments. Providing a sequence of arguments is generally preferred, as it allows the module to take care of any required escaping and quoting of arguments (e.g. to permit spaces in file names). If passing a single string, either shell must be True (see below) or else the string must simply name the program to be executed without specifying any arguments.  Py3/Doc/html/library/subprocess.html#frequently-used-arguments
- stdout/err/... handles:  If encoding or errors are specified, or text (also known as universal_newlines) is true, the file objects stdin, stdout and stderr will be opened in text mode using the encoding and errors specified in the call ! otherwise bytes!

--- capture_output=True:
If capture_output is true, stdout and stderr will be captured. When used, the internal Popen object is automatically created with stdout=PIPE and stderr=PIPE. The stdout and stderr arguments may not be supplied at the same time as capture_output. If you wish to capture and combine both streams into one, use stdout=PIPE and stderr=STDOUT instead of capture_output. : pcdoc
retturned.stdout/.stderr of a run(), if captured, is bytes as default, but is str if  run() was called with an encoding, errors, or text=True. it is  None if stdout was not captured. see subprocess.CompletedProcess StdLibDocs!

--- shell=True :
- shell: If shell is True, the specified command will be executed through the shell! security considerations !!  If shell is True, it is recommended to pass args as a string rather than as a sequence.
- On POSIX with shell=True, the shell defaults to /bin/sh. If args is a string, the string specifies the command to execute through the shell. This means that the string must be formatted exactly as it would be when typed at the shell prompt. This includes, for example, quoting or backslash escaping filenames with spaces in them. If args is a sequence, the first item specifies the command string, and any additional items will be treated as additional arguments to the shell itself.

--- securitys:  Py3/Doc/html/library/subprocess.html#security-considerations  :
- ! user FULL-/absolute-Path of executables! find it with shutil.which(cmd1)
- ! is possible, NOT using shell=True !
- ! prefere list-cmd to str-cmd ! as: cmd1 = ["echo", "aaa", "bbb", "ccc"]  instead  cmd1 = "echo aa bb cc"
"""

import subprocess

def simple_cmds1():
    print ("\n====================  simple  cmds ======================================================")
    # -NOT:  cmd1 = ["echo aa bb cc"]
    cmd1 = ["echo", "aaa", "bbb", "ccc"]  # -1ok:
    cmd1 = "echo aa bb cc"   # -1ok! not needed 'aa bb ...'
    ret1 = subprocess.run(cmd1, stdout=subprocess.PIPE, check=True)
    print("-- ret1-simple-cmd:  ", ret1)
    print("-- ret1-simple-cmd:  ", ret1.stdout)
    print("-- ret1-simple-cmd:  ", ret1.stdout.decode())
    print()

    # --- cmds+args, as ls -xt :
    cmd1 = ["ls", "-la"]  # -1ok
    cmd1 = ["ls", "-x", "-t"]
    ret1 = subprocess.run(cmd1, stdout=subprocess.PIPE, check=True)
    print("-- ret1-simple-cmd-with args:  ", ret1.stdout)
    print("-- ret1-simple-cmd-with args:\n", ret1.stdout.decode())


def multiple_cmds1():
    print ("\n====================  mutiple cmds in one shot: =========================================")
    # NOT && , just & ! in && then one & will be interpreted as ; and second one as background job !
    # -not: cmd1 = "echo  aaa ; echo bbb ; date" ; ret1 = subprocess.run(cmd1, capture_output=True) ; print("\n-- ret1-shell:  ", ret1.stdout)
    # -not: cmd1 = ["echo  aaa ; echo bbb ; date"]
    # -not: cmd1 = ["date", ";", "echo", "aaa", "bbb"]
    # -not: cmd1 = ["date", "ls"]
    cmd1 = ["echo", "aaa aa", "&", "pwd", "&", "uname", "-a", "&", "echo", "bbb bb"]  # -1ok !
    cmd1 = "echo aaa aa aa & pwd & uname -a & echo bbb bb" ;  # -1ok!
    # -I also added the option encoding=’UTF-8′. If you don’t, subprocess.run assumes the output is a stream of bytes because it doesn’t have this information. Alternatively, you can also use the option text=True without specifying the encoding.
    # ret1 = subprocess.run(cmd1, capture_output=True, encoding='UTF-8')
    ret1 = subprocess.run(cmd1, capture_output=True, encoding='UTF-8')
    print("-- ret1-captureOut1_multi:  ", ret1)
    print("-- ret1-captureOut1_multi:\n", ret1.stdout)
    print()

    # -I no encoding arg:
    ret1 = subprocess.run(cmd1, capture_output=True)
    print("-- ret1-captureOut1_multi-no-encoding:  ", ret1)
    print("-- ret1-captureOut1_multi-no-encoding:\n", ret1.stdout)
    print()

    # -/OR with check_out() :
    ret1 = subprocess.check_output(cmd1)
    print("-- ret1-multi1:  ", ret1)
    print("-- ret1-multi1:\n", ret1.decode())

def capture_out1():
    print ("\n====================  capture cmd output: ===============================================")
    ret1 = subprocess.run(['python', '--version'], capture_output=True, encoding='UTF-8')
    print("-- ret1-captureOut1:  ", ret1)
    print("-- ret1-captureOut1:  ", ret1.stdout)
    print()

    print("----- ret1-multi2:  NOT-captured-stdout:")
    ret1 = subprocess.run(['python', '--version'])  # -NOT-captured-stdout!
    print("-- ret1-captureOut1_No:  ", ret1)
    print("-- ret1-captureOut1_No:  ", ret1.stdout)
    print()


def input1():
    print ("\n====================  input1: ============================================================")
    in1 = "aaa"
    ret1 = subprocess.run("tr a x", input=in1, capture_output=True, encoding='UTF-8')
    print("-- ret1-captureOut1_multi:  ", ret1)
    print("-- ret1-captureOut1_multi:\n", ret1.stdout)


def shell_cmds1():
    print ("\n====================  shell-cmds, also multiple-cmds + captured-out : ====================")
    print("----!! Security warning! if possible do NOT use shell=True, due to command-injection danger!! instead feed the command in a list as other examples!")
    print("----- ret1-multi4:  seq. multiple shell commands + captured-out:")
    cmd1 = "echo aaa aa aa & pwd & echo bbb" ;  # -1ok
    cmd1 = ["echo", "aa bb cc", "&", "pwd", "&", "echo", "xx yy"]
    ret1 = subprocess.run(cmd1, shell=True, capture_output=True, encoding='UTF-8') # -!-without shell=true NOT working fine!
    print("-- ret1-captureOut1_multi:  ", ret1)
    print("-- ret1-captureOut1_multi:\n", ret1.stdout)

    print("----- ret1-multi5:  piped multiple shell commands + captured-out + vars inkl. :")
    ii = 2
    cmd1 = f'ls -al | tail -n {ii}'  # -!-NOT as list! list not worked!
    ret1 = subprocess.run(cmd1, shell=True, capture_output=True, encoding='UTF-8') # -!-without shell=true NOT working fine!
    print("-- ret1-captureOut1_multi-piped:  ", ret1)
    print("-- ret1-captureOut1_multi-piped:\n", ret1.stdout)


# =====================================================================================
def main():
    #__  simple_cmds1()
    multiple_cmds1()
    #__ capture_out1()
    #__ input1()
    #__ shell_cmds1()

if __name__ == "__main__":
    main()

