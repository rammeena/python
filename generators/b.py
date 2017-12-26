def YN_f1():
    pass
def DYN_f2():
    pass
def DYN_f3():
    pass

class GenClass:
    def __init__(self, fields):
        self.fields = fields

    def get_dynamic_fields_names(self):
        for field in self.fields:
            if field.__qualname__.startswith('DYN'):
                yield field.__qualname__

if __name__ == '__main__':
    x = [YN_f1,DYN_f2,DYN_f3]
    myobj = GenClass(x)
    genobj =  myobj.get_dynamic_fields_names()
    print(next(genobj))
