


def f1(n):
    return int(n) + 10

def f2(n):
    return int(n) - 10
   
#print(__file__)

##__/OR:   if __name__ == "__main__": import doctest; doctest.testfile("./doctest2_separateTestFile.txt")
##__/OR:   if __name__ == "__main__": import doctest, os ; fn1= os.path.basename(__file__).removesuffix(".py") + "_tqa1.txt";   doctest.testfile(fn1)
if __name__ == "__main__":
    import doctest, pathlib ;
    fn1= pathlib.Path(__file__).stem + "_teq1.txt";
    doctest.testfile(fn1)



