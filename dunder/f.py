class Celsius:
    "Fundamental Temprature descriptor"

    def __init__(self, value=0.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        print("In __get__ for Celsius")
        return self.value

    def __set__(self, instance, value):
        print("In __set__ for Celsius")
        self.value = float(value)


class Farenheit:
    "Requires that the owner have a 'celcius' attribute"

    def __get__(self, instance, owner):
        print("In __get__ for Farenheit")
        return instance.celsius * 9 / 5 * 32

    def __set__(self, instance, value):
        print("In __set__ for Farenheit")
        instance.celsius = (float(value) - 32) * 5

class Temperature:
    celsius = Celsius()
    farenheit = Farenheit()
