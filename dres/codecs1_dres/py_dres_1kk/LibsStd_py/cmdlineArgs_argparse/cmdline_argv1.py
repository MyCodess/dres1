import sys

def main():
    print(str(sys.argv))
    for nr, arg1 in enumerate(sys.argv):
        print(nr, ".  ", arg1, sep='')

if __name__ == '__main__':
    main()
