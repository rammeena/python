#e.py
"""A typical data descriptor"""

class DataDescriptor:
    """A Simple Data Descriptor.
    """
    def __init__(self):
        self.value = 0

    def __get__(self, instance, cls):
        print('data descriptor __get__')
        return self.value

    def __set__(self, instance, value):
        print('data descriptor __set__')
        try:
            self.value = value.upper()
        except AttributeError:
            self.value = value

    def __delete__(self):
        print('data descriptor __delete__')
        print("Dont delete")

class mycls:
    myattr = DataDescriptor()

    def __getattribute__(self, name):
        print("Getting attribute")

    def __getattr__(self, name):
        print("Getting attr")
        print(myattr)

