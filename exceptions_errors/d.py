def funny_division(number):
    try:
        if number == 13:
            raise ValueError("{} is an unlucky number".format(number))
        return 100 / number
    except (ZeroDivisionError, TypeError):
        return "Enter the number other than Zero"


for val in (0, "hello", 50.0, 13):

    print("Testing {}:".format(val), end=" ")
    print(funny_division(val))
