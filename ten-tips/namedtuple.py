def myfunc(x):
    if isinstance(x, str):
        print('I am str')
        field_names = x.replace(',',' ').split()

    print(field_names)
