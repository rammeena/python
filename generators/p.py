def fib_gen():
    x, y = 1, 1
    while x < 100:
        x, y = y, x + y
        yield x
    return True

print(list(fib_gen()))
