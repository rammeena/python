class Base:
    def __init__(self, val):
        print()
        print("Calling class 'Base'......")
        print("Inside __init__ of class named 'Base'...")
        print("Printing value of 'val' variable passed to 'Base' class")
        print(val)
        print("Setting up instance variable 'self.val'...")
        self.val = val
        print()
        print(self.val)
        print("Value of 'self.val' has been setup.")
        print("Getting out of __init__ of class 'Base'...")

    @classmethod
    def make_obj_in_Base(cls, val):
        print()
        print("Inside method 'make_obj_in_Base' of class named 'Base'...")
        print("Value of variable 'val' passed to classmethod 'make_obj_in_Base'..")
        print(val)
        print("Returning process started in 'make_obj_in_Base'...")
        return cls(val+1)

class Derived(Base):
    def __init__(self, val):
        print()
        print("Calling class 'Derived'......")
        print()
        print("Inside __init__ of class named 'Derived'...")
        print("Printing value of 'val' variable passed to 'Derived' class")
        print(val)
        print("calling super in class 'Derived' by increasing the value of val wth 2....")
        super().__init__(val+2)
        print("Getting out of __init__ of class 'Derived'...")

    @classmethod
    def make_obj_in_Derived(cls, val):
        print()
        print("Inside method 'make_obj_in_Derived' of class named 'Derived'...")
        print("Parameters passed 'val' and value is below...")
        print(val)
        print("calling super in classmethod 'make_obj_in_Derived' in class 'Derived'......")
        return super().make_obj_in_Base(val)
