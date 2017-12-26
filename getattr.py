class Count:
    def __init__(self, mymin, mymax):
        self.mymin = mymin
        self.mymax = mymax
        #self.current = None

    def __getattr__(self, item):
        print("Calling __getattr__")
        self.__dict__[item] = 0
        return 0

    def __getattribute__(self, item):
        print("Calling __getattribute__")
        if item.startswith('cur'):
            raise AttributeError
        return super().__getattribute__(item)
