class SomeMetaClass:
    def __init__(cls, name, bases, body):
        print("called: __init__")

    def __new__(cls, name, bases, body):
        print("called: __new__")

class SomeClass(metaclass=SomeMetaClass):
    pass
