#!/usr/bin/env  python3


########################################################################
##--see:  BKleien:  /python-course.eu/python3_decorators.php.html
print ("---------- OwnDecorators defining (usage like @property decorator): ----------")

class chatty_property:
    """ emulation of the property class for educational purposes """

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        print("\n--- chatty_property.__init__ called with:")
        print(f"fget={fget}, fset={fset}, fdel={fdel}, doc={doc}")
        if doc is None and fget is not None:
            print(f"doc set to docstring of {fget.__name__} method")
            doc = fget.__doc__
        self.__doc__ = doc

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(obj)

    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel, self.__doc__)

    def setter(self, fset):
        print("'__ setter: city' will be set")
        print(type(self))
        return type(self)(self.fget, fset, self.fdel, self.__doc__)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel, self.__doc__)


########################################################################
class Robot:
    """ using the above own-decorator here in an unrelated class: """ 
    def __init__(self, city):
        self.city = city

    @chatty_property
    def city(self):
        """ city attribute of Robot """
        print("__ The Property 'city' will be returned now:")
        return self.__city

    @city.setter
    def city(self, city):
        print("'__ city' will be set")
        self.__city = city

########################################################################
robo = Robot("Berlin")

