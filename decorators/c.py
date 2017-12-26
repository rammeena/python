import time
def outer_deco(f):
    print("Inside function %s" % globals()['outer_deco'])
    print("Received argument function %s" % vars()['f'])

    def inner_deco(x, y):
        print("Loging starting time %s" % time.time())
        print("Received arguments\nx:%s\ny:%s" % (vars()['x'], vars()['y']))
        print("Logging returning time %s" % time.time())
        return  f(x, y)

    return inner_deco
