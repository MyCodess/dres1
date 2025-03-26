# - Py3/Doc/html/library/collections.html#collections.namedtuple :

from collections import namedtuple

def f1():
    print("---------- collections.namedtuple(typename/classname, field_names (as list or csv-str) : ---------")
    Point = namedtuple('Point', ['x', 'y'], defaults=[0, None])   # -default value coulb be also ONLY for y as: [0] ! defaults-list from rightmost!
    p1 = Point(x=1, y=2)
    p3 = Point(3) # OR: if wanted assig to y:   p3 = Point(y=3)
    p5 = Point()
    print(f"-- readable __repr__ with a name=value style:  p1:  {p1} ,  p3:  {p3} ,  p5:  {p5}")
    print("-- index-able like the plain tuple:  ", p1[0] , p1[1])
    a, b = p1;   print("-- unpack like a regular tuple: ", a, b)
    print("-- fields also accessible by name:  ", p1.x , p1.y)
    l1 = [21, 22]
    print("-- _make()   /classmethod : makes a new instance from an existing sequence or iterable:  ", Point._make(l1))
    print("-- _asdict() /instancemethod: : returns a new dict of namedtuple instance:", Point._make(l1)._asdict())
    print("-- _asdict() /instancemethod: : returns a new dict of namedtuple instance:", Point(x=11, y=22)._asdict())
    print("-- _replace() /instancemethod: : ", Point(x=11, y=22)._replace(y=33))
    print("-- _fields : like dict-keys : Useful for introspection and for creating new named tuple types from existing named tuples:  ", Point(x=11, y=22)._fields)
    print("-- _field_defaults /class.member:  ", Point._field_defaults)
    print("-- getattr (if field name as str):  ", getattr(p1, 'x'))
    d1 = {'x': 33, 'y': 44}
    print("-- convert dict --> namedtuple : use ** as:  ", Point(**d1))
    Point3D = namedtuple('Point3D', Point._fields + ('z',))
    print("-- extending fields by subclassing a namedtuple:  ", Point3D(y=2, z=3, x=1))
    print("-- subclassing/extending namedtuple see more in LibStd-docs!")



##############################################################################
if __name__ == '__main__':
    print()
    f1()
    print()

