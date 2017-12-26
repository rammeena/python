#properties.py

class Square:
    def __init__(self, side):
        self.side = side

    def aget(self):
        return self.side ** 2

    def aset(self, value):
        print('No set allowed!')

    def adel(self, value):
        print('No del allowed')


    area = property(aget, aset, adel, doc='area')




