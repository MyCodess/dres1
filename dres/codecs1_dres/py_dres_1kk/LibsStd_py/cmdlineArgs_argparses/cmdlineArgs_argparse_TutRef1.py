"""
    pyStdLib-tut:  Py3/Doc/html/howto/argparse.html#argparse-tutorial
"""
import argparse

parser = argparse.ArgumentParser(description="calculate X to the power of Y")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")  # -option that takes no value (action)! is only flag/bool on/off! 
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base")         # option that takes a value !
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x**args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print(f"{args.x} to the power {args.y} equals {answer}")
else:
    print(f"{args.x}^{args.y} == {answer}")

