
##-- pyCookBK-3ed--8.7. Calling a Method on a Parent Class :
##--- also see BKlein-descp for explanations ! python-course.eu/python3_multiple_inheritance.php.html

# Tricky initialization problem involving multiple inheritance.
# Uses super()

class Base:
    def __init__(self):
        print('Base.__init__')

class A(Base):
    def __init__(self):
        print('A.__init__')
        super().__init__()
        print('A.__init__done!')

class B(Base):
    def __init__(self):
        print('B.__init__')
        super().__init__()
        print('B.__init__done!')

class C(A,B):
    def __init__(self):
        print('C.__init__')
        super().__init__()     # Only one call to super() here
        print('C.__init__done!')

if __name__ == '__main__':
    # Observe that each class initialized only once
    c = C()
    print ("MRO-of-C: ", C.__mro__)   ##--:  C-A-B-Base

