
import argparse

description1 = """
    syncronization of two folders, from the source folder into the replica folder
    periodically in certain time intervals! logging the actions into a logfile !
    reading the required pathes as command line arguments !
    """

usage1 = """
    positional argumenets:  <source-folder-path>  <replica-folder-path>  <logfile-path> <time-interval/seconds>
    optional   argumenets:  [--verbose]
    example:  ... ./source1  ./replica1  ./log1.txt   3600  --verbose
    ALL positional arguments are MANDATORY ! There are NO defaults !
    help with:   -h / --help
    """

def cmdline_argsParser1():
    parser1 = argparse.ArgumentParser(usage = usage1, description=description1)
    parser1.add_argument("src1", help="source folder path", type=str)
    parser1.add_argument("rep1", help="replica/target folder path", type=str)
    parser1.add_argument("log1", help="logfile path", type=str)
    parser1.add_argument("time1", help="time periods/intervals for synchronizations", type=int)
    parser1.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    args1 = parser1.parse_args()
    if args1.verbose:
        print ("Verbosity is turned on !")
        print ("your call: ", args1.src1, args1.rep1, args1.log1, args1.time1)

cmdline_argsParser1()

