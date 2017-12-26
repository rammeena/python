"""Use a decorator to allow nested properties
"""
#print("checking if function 'nested_property' is defined:{}".format(nested_property))
def nested_property(func):
    """Make defining properties simpler.
    """
    print("Inside function 'nested_property'")
    print()
    print("name of passed func to decorator is: {}".format(func.__name__))
    print()
    print("checking the dict of decorated passed function:{!r}".format(func.__dict__))
    print("checking if function 'area' is defined:{}".format(func))
    names = func()
    print()
    print("printing names the return value of passed func 'area' to this decorator")
    print()
    print(names)
    # We want docstring from docorated function.
    # If we do not set 'doc', we get the docstring from 'fget'
    names['doc'] = func.__doc__
    print()
    print()
    print("printing the doc string of decorated function")
    print(names['doc'])
    x = property(**names)
    print("printing x:", x)
    return x

print("checking if function 'nested_property' is defined:{}".format(nested_property))

class Square:
    """A square using properties with decorators.
    """
    print("Starting the creation of class Squre")
    print()
    def __init__(self, side, x=print("Initializing the class Square, inside __init__ method")):
        print("Calling __init__ of class 'Square'")
        self.side = side
 
    print()
    print("Next statement is decorator 'nested_property'")
    print()
    @nested_property
    def area():
        """Property that defines is methods nested.
        """
        print("Inside function 'area' which is passed to deco 'nested_property'")

        def fget(self):
            """
            Calculate the area of square
            when the attribute is accessed
            """
            print("Inside function 'fget'")
            return self.side * self.side

        def fset(self, value):
            """Don't allow setting.
            """
            print("Inside function 'fset'")
            print("Can't set the area.")

        def fdel(self):
            """Dont' allow deleting"""
            print("Inside function 'fdel'")
            print("Can't delete the area.")

        print("returning locals() inside function area")
        return locals()

if __name__ == '__main__':
    print()
    print("Inside if __name__ == '__main__'")
    print()
    print("Creating instance object of class Square with vlaue of side=5")
    square = Square(5)
    print('area:', square.area)
    print('try to set')
    square.area = 10
    print('area:', square.area)
    print('try to delete')
    del square.area
    print('area:', square.area)
    print(Square.area.__doc__)
