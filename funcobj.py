def first_function():
    print("The Function '{}'was called".format(first_function.__qualname__))

first_function.description = "A silly function - first_function"

def second_function():
    print("The Function '{}'was called".format(second_function.__qualname__))

second_function.description = "A sillier function - second_function"

def third_function(function):
    print("The description:", end=" ")
    print(function.description)
    print("The name:", end=" ")
    print(function.__name__)
    print("The class:", end=" ")
    print(function.__class__)
    print("Now I'll call the function passed in")
    function()
    
