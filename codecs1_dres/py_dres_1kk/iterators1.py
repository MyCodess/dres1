#!/usr/bin/env  python3

print()
##--I-   if you want to add an iterator behavior to your class, you have to add the __iter__ and the __next__ method to your class. The __iter__ method returns an iterator object. If the class contains a __next__, it is enough for the __iter__ method to return self, i.e. a reference to itself! "
print ("========== zu-fuss, an iterable class, without using generators/yield: ================")
class c1:
    def __init__(self, x):
        ##__ if  not hasattr(self, "l1"): self.l1=[]
        self.l1 = []
        self.l1.append(x)
    def add1 (self, x):
        self.l1.append(x)
    def __iter__ (self): return self
    def __next__ (self):
        if len(self.l1):
            return self.l1.pop()
        else:
            raise StopIteration
o1 = c1(20)
o1.add1(21)
o1.add1(22)
print (o1.l1)
it1 = iter (o1)
for ii in it1:     print (ii , end=" - ")
print()
print ("-----------------------------------------")

print()
print ("========== zu-fuss, an iterable class, without using generators/yield: ================")
##--I- We have described how an iterator works. So if you want to add an iterator behavior to your class, you have to add the __iter__ and the __next__ method to your class. The __iter__ method returns an iterator object. If the class contains a __next__, it is enough for the __iter__ method to return self, i.e. a reference to itself:
class Reverse:
    """
    Creates Iterators for looping over a sequence backwards.
    """
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
lst = [34, 978, 42]
lst_backwards = Reverse(lst)
for el in lst_backwards:
    print(el)
print ("-----------------------------------------")


print()
print ("======== a list=obj as iter argument ==================================")
o1.l1=[10,11,12,13]
it2 = iter (o1)
print (next (it2))
print (next (it2))
print (next (it2))
print ("-----------------------------------------")

print()
print ("======== a list=obj as iter argument ===================================")
cities = ["Berlin", "Vienna", "Zurich"]
iterator_obj = iter(cities)
print(iterator_obj)
print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))
print ("-----------------------------------------")


print()
print ("======= check if the argument=obj is iterable??: =========================")
def iterable(obj):
     try:
         iter(obj)
         return True
     except TypeError:
         return False 
for element in [34, [4, 5], (4, 5), {"a":4}, "dfsdf", 4.5]:
    print(element, "iterable: ", iterable(element))
print ("-----------------------------------------")


