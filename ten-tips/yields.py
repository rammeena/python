#yields.py

# Fibonacci number
# 1,1,2,3,5,8,13,21....

def classic_fibonacci(limit):
    nums = []
    current, nxt = 0, 1

    while current < limit:
        current, nxt = nxt, nxt + current
        nums.append(current)
    return nums

# Fib by generator

def generator_fib():
    current, nxt = 0, 1

    while True:
        current, nxt = nxt, nxt + current
        yield current

# Even number fibonacci

def even_gen_fib():
    for m in generator_fib():
        if m % 2 == 0:
            yield m

#generator support composition, consume above both generators as pipeline here.

def composed_generator():
    for e in even_gen_fib():
        if e % 3 == 0:
            yield e


if __name__ == '__main__':
    print("Classic")
    for m in classic_fibonacci(100):
        print(m, end=', ')
    print()
    print(classic_fibonacci(10))
    print()
    print()
    print("generator")
    for m in generator_fib():
        print(m, end=', ')
        if m > 100:
            break
    print()
    print("even generator fibonacci")
    for m in even_gen_fib():
        print(m, end=', ')
        if m > 100:
            break
    print()
    print("composed")
    for m in composed_generator():
        print(m, end=', ')
        if m > 1000000:
            break
    print()

