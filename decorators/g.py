#define a function
def foo(x):
    #inner function "bar"
    def bar(y):
        q = 10
        #inner function "baz"
        def baz(z):
            print("Locals in baz func: ", locals())
            print("Vars in bar func:", vars())
            return x + y + q + z
        return baz
    return bar


