class A:
    __slots__ = ('x', 'y')
    version = 0.1

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

class B:
    version = 0.1
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y


objA = A(1,2)
objB = B(2,3)

print("objA.__dict__ ", objA.__dict__)
print("objB.__dict__ ", objB.__dict__)

objA.z = 10
objB.z = 10
print("After setting up new attrs")
print("objA.__dict__ ", objA.__dict__)
print("objB.__dict__ ", objB.__dict__)

