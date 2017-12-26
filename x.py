class parent:
    class_var = "I am a class variable in parent class"
    def __init__(self):
        self.init_var = "I am a method varable inside __init__ method"
        print("Executing __init__ method of check_it class")

    def second_method_in_parent_class(self):
        pass

class child(parent):
    child_var = "I am a class variable in child class"
    def child_method(self):
        child_method_var = "I am a method variable inside child_method in child class"
        print("I am printing inside child_method of child class")

    def second_method_in_child_class(self):
        pass
