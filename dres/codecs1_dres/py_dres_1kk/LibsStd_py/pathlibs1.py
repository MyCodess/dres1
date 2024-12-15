""" pathlibs ... 
- see/based:  Py3/Doc/html/library/pathlib.html

prereq test-files: mkdir -p /tmp/d1/d11 ; echo "-dummy-text-1" >| /tmp/d1/d11/f11.txt ; echo "-dummy-text-2" >> /tmp/d1/d11/f11.txt ;
"""
from pathlib import Path


# =====================================================================================
def pathes1(p1str: str):
    p1 = Path(p1str)
    p2 = Path('/tmp') / 'd1' / 'd11'  # -concatanate pathes , and resolve-links ...
    p2j = Path('/tmp').joinpath('d1').joinpath('d11')  # -concatanate pathes , and resolve-links ...
    fp2 = p2 / 'f11.txt'

    print("\n-- pathes: ", p1, p2, p2j, fp2, sep=" - ")
    ls1 = [x for x in p1.iterdir()]
    print("\n-- ls1:\n", ls1)
    
    subdirs1 = [x for x in p1.iterdir() if x.is_dir()]
    print("\n-- subdirs1:\n", subdirs1)
    
    # - globbing / regex eg: Listing Python source files recursively in this directory tree!
    # - addition of “**” which means “this directory and all subdirectories, recursively”. In other words, it enables recursive globbing:
    pyFiles1 = [x for x in p1.glob("**/*.py")]
    #_ -longer--list:  print("\n-- pyFiles1:\n", pyFiles1)

    print("\n-- concats1 / parts / parents:\n", p2, p2.absolute(), p2.resolve(), sep=" - ")
    print("Path as str: ", str(fp2))
    print("Path posix /forward slashes (/): ", fp2.as_posix, fp2.as_uri, sep=" - ")
    print("filename: ", fp2.name, " -suffix: ", fp2.suffix,  " -no-suffix/stem: ", fp2.stem, sep=" - ")
    print("parts / subcomponents of a Path: ", fp2.parts)
    print("parents: ", fp2.parent, " -: ", fp2.parents[0], " - ", fp2.parents[1], " - ", fp2.parents[2], " - ", fp2.parents[3])

    print("\n-- open/read a Path:")
    with fp2.open() as fh2: print(fh2.readlines())

    print("\n-- attribs/...:")
    print(fp2.drive, fp2.root, fp2.anchor, fp2.name, sep=" - ")

    print("\n-- querys/status//...:")
    print("querys1: ", p2.exists(), p2.is_dir(), p2.is_absolute(), sep=" - ")

    print("\n-- matches: ")
    # -If pattern is absolute, the path must be absolute, and the whole path must match: If pattern is relative, the path can be either relative or absolute, and matching is done from the right: case-sensitivity follows platform defaults:
    print("match1: ", fp2, fp2.match('*.txt'), fp2.match('*.TXT'), fp2.match('d11/*.txt'), fp2.match('11/*.txt'), fp2.match('/d11/*.txt'), sep=" - ")

    print("\n-- modifs: ")
    print("change-only-filename: ", fp2.with_name("f22.htm"), fp2.with_stem("f33"), fp2.with_suffix(".tgz"), sep=" - ")

    print("\n-- Path-class-methods:")
    print("cu-dir / PWD : ", Path.cwd())
    print("HOME:  ", Path.home())

    print("\n-- Path-obj-methods:")
    print("stat:  ", fp2.stat())

    print("\n-- iterate over a dir (not tree! not recursive!):")
    for ii in (p1.iterdir()): print("-: ", ii)


# =====================================================================================
def main():
    pathes1(".")

if __name__ == "__main__":
    main()
