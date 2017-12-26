import functools
def better_trace_function(uppercase=False):
    def trace_function(func):
        """Add tracing before and after a function"""
        @functools.wraps(func)
        def new_func(*args):
            """The new function"""
            print('Called {!r} {!r}'.format(func, args))
            result = func(*args)
            print('Returning', result)
            if uppercase:
                return result.upper()
            return result
        return new_func
    return trace_function

