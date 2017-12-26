def funny_division_error(divider):
    try:
        return 100/divider
    except ZeroDivisionError:
        return "Zero is not a good idea"
