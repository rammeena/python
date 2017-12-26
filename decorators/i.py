def top(x=print("I am top funcs default arg")):
    def f1(f):
        print("I am top most func which takes msg variable")
        def f2():
            print("I am actual decorator which take f as argument")
            def f3(*args, **kwargs):
                print("I am the wrapper which should be returned - may take *args, **kwags")
                print()
                print("printing msg: {}".format(msg))
                print("executing the actual decorated func f")
                return f(*args, **kwargs)
            print("returning f3")
            return f3
        print("returning f2")
        return f2
    print("returning f1")
    return f1

@top()
def add(x, y):
    print("I am add func, I do 2 + 3")
    return x + y 
    


