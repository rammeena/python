class GetTracer:
    def __getitem__(self, key):
         print('called __getitem__({} {})'.format(type(key), repr(key)))

