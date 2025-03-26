# Py3/Doc/html/library/collections.html#collections.namedtuple  :


import os, argparse
from collections import ChainMap

def cmdlineargs_read1():
    """
    default-params < os-envvar < cmdline-arg :
    Example of letting user specified command-line arguments take precedence over environment variables which in turn take precedence over default values:
    USAGE: try is with:   python chainmap_cmdlineargs.py  / -u xx1 / export user1=yyy
    """

    defaults = {'color': 'red', 'user1': 'guest'}

    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--user1')
    parser.add_argument('-c', '--color')
    namespace = parser.parse_args()
    command_line_args = {k: v for k, v in vars(namespace).items() if v is not None}

    combined = ChainMap(command_line_args, os.environ, defaults)
    print(combined['color'])
    print(combined['user1'])

##################################### main ##########################################
cmdlineargs_read1()

