class Foo (object):
    def __setattr__( self, name, value ):
        self.bar(name, value)
        object.__setattr__(self, name, value)


    def bar( self, name, value ):
        print('Setting {} to {}.'.format(name, value))
