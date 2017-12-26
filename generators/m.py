def generator1():
    for i in range(10):
        print("In Loop1 generator1")
        yield i

    for j in range(10,20):
        print("In Loop 2 generator1")
        yield j

def generator2():
    for i in range(10):
        print("In Loop in generator2")
        yield i


def generator3():
    for i in range(10,20):
        print("In Loop in generator3")
        yield i

def generator():
    for i in generator2():
        yield i

    for j in generator3():
        yield j

def yieldfromgen():
    yield from generator2()
    yield from generator3()

from itertools import chain

def newgen():
    for v in chain(generator2(),  generator3()):
        yield v
