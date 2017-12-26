class PeopleHeight:

    def __init__(self, height = 150):
        print("Executing __init__ method of class PeopleHeight....")
        print("Setting up self.height variable....")
        self.height = height
        print("printing value of self.height")
        print("self.height : ", self.height)

    def convert_to_inches(self):
        return (self.height * .3937)

    def get_height(self):
        print("Inside the getter method")
        return self._height

    def set_height(self, value):
        if value < 0:
            raise ValueError("Height can not be negative")
        print("Inside the setter method")
        self._height = value

    height = property(get_height, set_height)




