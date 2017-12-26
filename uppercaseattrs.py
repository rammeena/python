class UppercaseAttributes:
    """
    A class that returns uppercase values on uppercase attribute access.
    """
    #Called only attribute access fails
    def __getattr__(self, name):
        print("Calling {!r}".format(self.__getattr__.__func__))
        if name.isupper():
            print('Entering if condition')
            if name.lower() in self.__dict__:
                return self.__dict__[name.lower()].upper()
        raise AttributeError("'{}' object has no attribute {}.".format(self,name))
