
"""
docstring-testingsQA , call a docstring-tests-module as:
    - python -m doctest  <mod1> [-v]    ##--then NOT needed  the last lines here as __main__ for doctest-mod-call ! shows ONLY failed-tests without -v ! /OR
    - python <myname1>  [-v]            ##--then it requires the last lines here as __main__ for doctest-mod-call ! shows ONLY failed-tests without -v !
    --
    - "-v"  : shows ALSO the passed/not-failed test-caese!! WATCH: NOT: python -v ... !! but -v is for the doctest-module!
    - just change an expected result below and WATCH the failed test result !!

========== testingsQA1-routines here for the module itself:
>>> f1(f2(20.3))
20
>>> f2(f1(20.3))
20
>>> f1(20.3) + f2(20.3) == 20+20 == 40
True
>>> f1(20.3) - f2(20.3) == 20
True
>>> for ii in 10,20,-30: f1(ii)-f2(ii) == 20
... 
True
True
True

========== __1END__testing-routines here:
"""


def f1(n):
    """
    ========== testingsQA1-routines here for the above func:
    >>> f1(2)
    12
    >>> f1(5)
    15
    >>> f1(3.1)
    13
    >>> f1("aa")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 7, in f1
    ValueError: invalid literal for int() with base 10: 'aa'
    >>> f1(5.2)
    15
    >>> [f1(ii) for ii in range(4)] 
    [10, 11, 12, 13]

    ========== __1END__testing-routines here:
    """
    return int(n) + 10

def f2(n):
    """
    ========== testingsQA1-routines here for the above func:
    >>> f2(20)
    10
    >>> f2("bb")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/up1/mnt/VARUfs/varu/varau/prjs/py1/tests/t1.py", line 40, in f2
        return int(n) - 10
    ValueError: invalid literal for int() with base 10: 'bb'
    >>> f2(20.3)
    10

    ========== __1END__testing-routines here:
    """
    return int(n) - 10
    
##__  if __name__ == "__main__": import doctest; doctest.testmod()



