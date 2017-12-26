#Circuitous.py
""" Circuitous, LLC -
    An Advance Circle analytics company.
"""
import math

class Circle:
    'An advance circle analytics toookit'
    __slots__ = ['diameter']
    version = '0.1'                   #class variable

    def __init__(self, radius):
        """initializer to populate instances"""
        self.radius = radius              #instance variable

    @property 
    def radius(self):
        'Radius of circle'
        return self.diameter / 2.0
    
    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2.0

    def area(self):
        """Perform quadrature of a shape of uniform radius"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2.0 * math.pi * self.radius

    @classmethod
    def from_bbd(cls, bbd): # alternative constructor
        'Construct a circle from bounding box diagonal'
        print("'cls' : {!r}".format(cls))
        radius = bbd / 2.0 / math.sqrt(2.0)
        return Circle(radius)

    def angle_to_grade(angle):
        'convert angle in degree to percentage grade'
        return math.tan(math.radians(angle)) * 100.0

class Tires(Circle):
    'Tires are circles with a corrected perimeter'

    def perimeter(self):
        return  Circle.perimeter(self) * 1.25
