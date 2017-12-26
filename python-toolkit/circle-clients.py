#circle-clients.py
""" Client Applications for Circuitious - An Advance Circle analytics Tool.
"""
from circutious import Circle, Tires

#=========================================================================
#Customer-1
print("Circutious version: {}".format(Circle.version))
c = Circle(10)
print()
print("A circle of radious: {}".format(c.radius))
print()
print("This circle area is: {:0.2f}".format(c.area()))
print('=' * 100)
print()
print()
#=========================================================================
#Customer-2
from random import random, seed
seed(8675309)
print("Using Circuitous(tm) version: {}".format(Circle.version))
n = 100000000
circles = [Circle(random())for i in range(n)]
print()
print("The average area of ", n, " random circles", end=" ")
avg = sum([c.area() for c in circles])
print("is %.2f" % avg)
print('=' * 100)
#=========================================================================
#Customer-3: Rubber sheet company

cuts = [0.1, 0.7, 0.8]

circles = [Circle(r) for r in cuts]

for c in circles:
    print("A Circle with the radius of {}".format(c.radius))
    print("has a perimeter of {}".format(c.perimeter()))
    print("and a cold area of {}".format(c.area()))
    c.radius *= 1.1
    print("and a warm area of {}".format(c.area()))
print()
print('=' * 100)
#=========================================================================
#Customer-4: National Tire Company
t = Tires(22)
print("A Tire of radius, %s"% t.radius)
print("has an inner area of %s" % t.area())
print("and an odometer corrected perimeter of %s" % t.perimeter())
print()
print('=' * 100)

print()
# From alternative constructor method
print("From alternative constructor method")
print()
t = Tires.from_bbd(45)
print("A Tire of radius, %s"% t.radius)
print("has an inner area of %s" % t.area())
print("and an odometer corrected perimeter of %s" % t.perimeter())
print()
print('=' * 100)
#=========================================================================
#Customer-5: National Graphics Company

#bbd = 25.1
#c = Circle(bbd_to_radius(bbd))
#print("A circle with a bbd of %d " % bbd)
#print("has radius of %d " % c.radius)
#print("has an area of %d " % c.area())
#print()
#print('=' * 100)

#Customer-5: Alternative constructor method instead using own func

c = Circle.from_bbd(25.1)
print("A circle with a bbd of 25.1 ")
print("has radius of %d " % c.radius)
print("has an area of %d " % c.area())
print()
print('=' * 100)
