from c import outer_deco

@outer_deco
def myfunc(x,y):
    print("Inside myfunc")
    return x + y
