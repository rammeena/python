#library.py
class BaseMeta(type):
    def __new__(cls, name, bases, body):
        print('\nInside MetaClass: BaseMeta and method: __new__\n', '\nclasss-name:',cls,'\nname:',
                name,'\nbases:',bases, '\nbody:',body)
        if name == 'Derived' and not 'bar' in body:
            raise TypeError("You are not doing it rigth!!")

        return super().__new__(cls, name, bases, body)

class Base(object, metaclass=BaseMeta):
    def foo(self):
        return self.bar()
