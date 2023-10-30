
"""
Checking if a Variable is None :
There are two ways to check if a variable is None.
- One way can be performed by using the is keyword.
- Another is using the == syntax.
Both comparison methods are different, and you'll see why later:
- With basic types they are same.
- However with objects/classes they can be different, if the Class overwrites __eq__() func, relevenat for == comparison !
So using the is-keyword is the right one to query! :")
https://www.pythoncentral.io/python-null-equivalent-none/
"""

print("========== Is a var None?? two methods: is-keyword /OR == comparison: ====================")
print("\n--- for basic-types both are same:")
null_variable = None
not_null_variable = 'Hello There!'
 
# The is keyword
if null_variable is None:
    print('null_variable is None')
else:
    print('null_variable is not None')
 
if not_null_variable is None:
    print('not_null_variable is None')
else:
    print('not_null_variable is not None')
 
 
# The == operator
if null_variable == None:
    print('null_variable is None')
else:
    print('null_variable is not None')
 
if not_null_variable == None:
    print('not_null_variable is None')
else:
    print('not_null_variable is not None')


####################### None-Objects-comparing: ###########################
print("\n--- for objects both can be different! so is-keyword is the right one to query! :")
class MyClass:
    def __eq__(self, my_object):
        # We won't bother checking if my_object is actually equal
        # to this class, we'll lie and return True. This may occur
        # when there is a bug in the comparison class.
 
        return True
 
my_class = MyClass()
 
if my_class is None:
    print('my_class is None, using the is keyword')
else:
    print('my_class is not None, using the is keyword')
 
if my_class == None:
    print('my_class is None, using the == syntax')
else:
    print('my_class is not None, using the == syntax')

print("\n===== So: using the is-keyword is the right way to query if x is None ! =====\n")
