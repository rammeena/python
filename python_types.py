#
# Testing isinstance and issubclass
#
class C1:
    def __init__(self):
        object.__init__(self)

class B1:
    def __init__(self):
        object.__init__(self)

class B2(B1):
    def __init__(self):
        B1.__init__(self)

class CB1(C1,B1):
    def __init__(self):
        # not sure about this for multiple inheritance
        C1.__init__(self)
        B1.__init__(self)
