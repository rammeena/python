class slotcls:
    __slots__ = ('a', 'b')

    def __init__(self, t, p, q):
        self.a = t
        self.b = p
        self.c = q

    def add(self):
        self.c = self.a + self.b
        return self.c

class mycls:
    def __init__(self, t, p, q):
        self.a = t
        self.b = p
        self.c = q

    def add(self):
        self.c = self.a + self.b
        return self.c
