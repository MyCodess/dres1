#!/usr/bin/env  python3

""" Multiple Inheritance,  Diamond Problem , ...:
    http://www.srikanthtechnologies.com/blog/python/mro.aspx
    comment-in the super() line in A and check the Diff !!
"""

class A(object):
    def process(self):
        print('A process()')
        ##--I- comment-in and see the DIFF!! :   super().process()


class B(object):
    def process(self):
        print('B process()')


class C(A, B):
    def process(self):
        print('C process()')
        super().process()
        print('C process()--explicit calls of super')
        super(C, self).process()
#       super(C, self).process()
#       super(C).process()


class D(C,B): pass


obj = D()
obj.process()

print(C.mro())
print(D.mro())

