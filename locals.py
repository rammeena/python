def my_func():
    a = 1
    b = 2
    huh = locals()
    c = 3
    print()
    print('printing huh')
    print(huh)
    print()
    huh['d']= 4
    print()
    print('printing huh again after one assignment in huh dict')
    print(huh)
    print()
    #print('printing locals() dirctly again after a new assignment to huh dict')
    #print(locals())
    print()
    #print('printing directly')
    #print(d)
    print()
    print('printing vars()')
    print(vars())


my_func()

