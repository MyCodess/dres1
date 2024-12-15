from abc import ABC, abstractmethod

class C1(ABC):
    @abstractmethod
    def m1(self, ii): print("-- C1.m1 :", ii)

class K1(C1):
    def m1(self, ii):
        print("-- K1.m1 :", ii)
        super().m1(ii+10)   ##--I-now it works and can call even the upper-abstract-method, since the method is once here implemented !

##--2try--error:  xx = C1()
xx = K1()
xx.m1(5)

