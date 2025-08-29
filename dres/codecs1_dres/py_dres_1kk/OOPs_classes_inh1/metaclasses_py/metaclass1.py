"""
    _______:  see:
    - ! see: https://realpython.com/python-metaclasses/#defining-a-class-dynamically
    - python-course.eu/oop/dynamically-creating-classes-with-type.php.html
    - https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python  :  (metaclass=...)
    - pydoc type  ;  type(className, superClasses, attributesDict)  ;

    _______:  type():
    - ! type() has VARIOUS usages!!
    - type(obj1) : returns the type of the obj1
    - type(className, superClasses, attributesDict) : returns/creates-dynamically a class with the name "className", its base-classes "superClasses", its members/attribs: "attributesDict"
"""

import inspect


#####  ==========  
def meta1():
    print("==================== type()-3-args to dynamically create new classes: ====================")
    ii = 0
    print("\n---- type-3-arg eg:")
    INT2 = type ("INT2", (int,) , {"a1": 11, "a2": 22});  in1 = INT2(); print(type(in1), "bases/parents", INT2.__bases__ , "member-values", in1.a1, in1.a2, sep="  ::  ");
    A = type("A", (), {"var1": 3}) ; a1=A(); print(type(a1) , "member-values", a1.var1, sep="  ::  ");

    print("\n---- type-3-arg eg with function creation:")
    def f1(self, n): return n+10;
    Foo=type("Foo", (), {"func1": f1}); a1=Foo();
    print("creating-with-funcs", type(a1) , "member-values", a1.func1(5), sep="  ::  ");

    print("\n---- type-3-arg eg with __init__ :")
    def f2(self): self.v1=33; print("init-done-1")
    Foo=type("Foo", (), {"__init__": f2}); a1=Foo();
    print("creating-with-init", type(a1) , "member-values", a1.v1, sep="  ::  ");

    print("\n---- type-3-arg eg with lambda :")
    Foo = type( 'Foo', (), { 'attr': 10, 'attr_val': lambda x : x.attr + 4 })
    a1 = Foo()
    print("creating-with-func-lambda", type(a1) , "member-values", a1.attr, a1.attr_val(), sep="  ::  ");

##________________________________________  ___________________________


if __name__ == "__main__":
    meta1()
