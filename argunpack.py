def show_args(arg1, arg2, arg3="THREE"):
    print('\narg1: ', arg1)
    print('arg2: ', arg2)
    print('arg3: ', arg3)
    print(arg1, arg2, arg3)

some_args = range(3)
more_args = {
        "arg1": "ONE",
        "arg2": "TWO",
        "arg3": "Three"
        }

print("Unpacking a sequence:", end=" ")
show_args(*some_args)

print("Unpacking a dict:", end=" ")
show_args(**more_args)
