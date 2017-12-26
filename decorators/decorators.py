import functools

def add(first, second):
    """Return the sum of two arguments."""
    return first + second

def trace_function(func):
    """Adds tracing before and after a function"""
    @functools.wraps(func)
    def new_func(*args):
        """The new function"""
        print('Called func({!r})'.format(args))
        result = func(*args)
        print('Returning {!r}'.format(result))
        return result
    return new_func
