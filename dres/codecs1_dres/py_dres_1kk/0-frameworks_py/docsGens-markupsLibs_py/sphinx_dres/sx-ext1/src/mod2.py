
def f1(n):
    """
    - this f1 docs example !
    - this f1 docs example !
    """
    return int(n) + 10


def f2(n):
    """
    - this f2() returns just int(param1) - 10
    - this f2() returns just int(param1) - 10
    """
    return int(n) - 10


class C1:
    """Just a dummy class C1 !"""

    def f11(n):
        """This C1.f2() returns just int(param1) + 5
        """
        return int(n) + 5


"""
docstring-testingsQA :
------------------------------

- call a docstring-tests-module as:
- python -m doctest  <mod1> [-v]    ##--then NOT needed  the last lines here as __main__ for doctest-mod-call !
- python <myname1>  [-v]            ##--then it requires the last lines here as __main__ for doctest-mod-call !
- without -v it shows ONLY failed-tests without ! "-v"  : shows ALSO the passed/not-failed test-caese!!
- Note: NOT: python -v ... !! but -v is for the doctest-module!
- just change an expected result below and WATCH the failed test result !!

testingsQA1-routines here for the module itself:
______________________________________________________

    >>> f1(f2(20.3))
    20
    >>> f2(f1(20.3))
    40
    >>> f1(20.3) + f2(20.3) == 20+20 == 40
    True
    >>> f1(20.3) - f2(20.3) == 20
    True
    >>> for ii in 10,20,-30: f1(ii)-f2(ii) == 20
    ...
    True
    True
    True

"""

# #__  if __name__ == "__main__": import doctest; doctest.testmod()
