x = 0
def outer():
    x = 1
    def inner():
        x = 2
        print('inner x:', x)

    inner()
    print('outer x:', x)

outer()
print("global:", x)

# inner x: 2
# outer x: 1
# global x: 0


x = 0
def outer():
    x = 1
    def inner():
        nonlocal x
        x = 2
        print('inner x:', x)

    inner()
    print('outer x:', x)

outer()
print("global:", x)

# inner x: 2
# outer x: 2
# global x: 0

x = 0
def outer():
    x = 1
    def inner():
        global x
        x = 2
        print('inner x:', x)

    inner()
    print('outer x:', x)

outer()
print("global:", x)

# inner x: 2
# outer x: 1 
# global x: 2
