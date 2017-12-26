def myfunc():
    print("step: 0") # In First call it will start here
    yield '0'        # For first call it will return here
    print("step: 1") # In second call it will start here
    yield '0'        # For second call it will return here
    print("step: 2") # In third call it will start here
    yield '2'        # For third call it will return here
    print("step: 3") # SO ON ......
    yield '3'
