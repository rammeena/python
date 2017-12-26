class ReversedString:
    def __get__(self, instance, name):
        print("Called : __get__ in ReversedString class")
        return self

    def __set__(self, instance, value):
        print("Called : __set__ in ReversedString class")
        return instance._some_string = value
    def __delete(self):
        print("Called : __delete__ in ReversedString class")

