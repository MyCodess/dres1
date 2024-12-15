# import required module 
import inspect 

# create classes 
class A(object): 
    pass

class B(A): 
    pass

class C(B): 
    pass

print(inspect.getclasstree([C]))
print("=============")
print(inspect.getclasstree([C], unique=True))
print("=============")

# nested list of tuples 
for i in (inspect.getclasstree(inspect.getmro(C))): 
    print(i) 
    print("-------")


