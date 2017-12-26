#decorator library
from functools import wraps
from time import gmtime, strftime

def func_x(func_y):
    """I am a outer decorator function"""
#    @wraps(func_y)
    def func_z(x, y):
        print("Execution Starts: {}".format(strftime("%Y-%m-%d %H:%M:%S",gmtime())))
        x = func_y(x, y)
        print("Execution Ends: {}".format(strftime("%Y-%m-%d %H:%M:%S",gmtime())))
        return x
    return func_z

