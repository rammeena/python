class Property:
    "Emulate PyProerty type in objects/descriptors.c"

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.doc = doc


    def __get__(self, obj, objtype=None):
        print("Entering __get__ in descriptor")
        print("obj: {}".format(obj))
        print("objtype: {}".format(objtype))
        if obj is None:
            return self

        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(obj)

    def __set__(self, obj, value):
        print("Entering __set__ in descriptor")
        print("obj: {}".format(obj))
        print("value: {}".format(value))
        if self.fset is None:
            raise AttributeError("Can't set attribute")

        self.fset(obj, value)

    def __delete__(self, obj):
        print("Entering __delete__ in descriptor")
        if self.fdel is None:
            raise AttributeError("Can't delete attribute")

        self.fdel(obj)
