#a.py
"""Basic dunder methods"""

class Car:
    """Class to demonstrate basic dunder methods"""

    def __init__(self, color, mileage):
        """Object initializer method"""
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return 'A Car of color: {}'.format(self.color)

    def __repr__(self):
        return "{}('{}',{})".format(type(self).__name__, self.color, self.mileage)
