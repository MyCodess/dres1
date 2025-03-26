import sys

# old/conventional sys.argv method! kaum faciities! :
# call eg:   python cmdline_argv1.py 5 6 7

def main():
    print(str(sys.argv))
    for nr, arg1 in enumerate(sys.argv):
        print(nr, ".  ", arg1, sep='')

if __name__ == '__main__':
    main()
