def outer():
    def myfunc():
        fname = 'Ram'
        lname = 'Meena'
        fullname = fname + lname
        print(locals())
        print(myfunc.__dict__)
        print(vars())
    myfunc()

outer()
