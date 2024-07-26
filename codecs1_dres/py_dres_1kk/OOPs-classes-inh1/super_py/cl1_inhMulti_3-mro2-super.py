#!/usr/bin/env  python3

##--- see BKlein-descp ! python-course.eu/python3_multiple_inheritance.php.html

print ("\n------------ MOR-in-multiple-Inheritance using super() ! see MRO-dnts ! :---------------------------")
class A(object):
    def m(self): print("m of A called")
class B(A):
    def m(self):
        print("m of B called")
        super().m()
class C(A):
    def m(self):
        print("m of C called")
        super().m()
class D(B,C):
    def m(self):
        print("m of D called")
        super().m()

x = D()
x.m()            ##--:  D-B-C-A
print (D.mro())  ##--:  D-B-C-A

print ("\n---------  see the diff when baseclasses call super().xx or not! compare with above eg! : --------------------")
class A(object):
    pass
class B(A):
    def m(self):
        print("m of B called")
        ##--II-uncomment this and see the DIFF !!:    super().m()
class C(A):
    def m(self):
        print("m of C called")
        ##--II-uncomment this and see the DIFF !!:    super().m()
class D(B,C):
    def m(self):
        print("m of D called")
        super().m()

x = D()
x.m()            ##--:  D-B
print (D.mro())  ##--:  D-B-C-A

print ("-------------------------------------------------")
class A:
  def method(self):
    print("A.method() called")
    ##--II-uncomment this and see the DIFF !!:    super().method()
class B:
  def method(self):
    print("B.method() called")
class C(A, B):
  pass
class D(C, B):  ##--change to (B, C) to get exception !
  pass

d = D()
d.method()       ##--:  A
print (D.mro())  ##--:  D-C-A-B

print ("-------------------------------------------------")
print ("-- mro() nachvollziehen:  so for C1.mro() . just write down all classes from left-to-right--and-each-first-to-Top, and then take the repeated ones out except its last entry !")
class X:pass
class Y: pass
class Z:pass
class A(X,Y):pass
class B(Y,Z):pass
class M(B,A,Z):pass
x=M()
print (M.mro())  ##--:  M-B-A-X-Y-Z


print ("-------------------------------------------------")
