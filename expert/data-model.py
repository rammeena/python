#some behaviour that i want to implement --->  write some __function__(dunder methods)
#top-level function or top-level syntax  --> corresponding __method__

class Polynomial:

    def __init__(self, *coeffs):
        print('calling __init__')
        self.coeffs = coeffs

    def __repr__(self):
        print('calling __repr__')
        return 'Polynomial(*{!r})'.format(self.coeffs)
 
    def __add__(self, other):
        print('calling __add__')
        return  Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))

    def __len__(self):
        print('calling __len__')
        return len(self.coeffs)


p1 = Polynomial(1,2,3)# x² + 2x + 3
p2 = Polynomial(3,4,3)# 3x² + 4x + 3
