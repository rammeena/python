class Ractangle():
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return "__repr__ method implementd successfully"

    def __str__(self):
        return "name of this module is %s"% __name__

if __name__ == '__main__':
  r1 = Ractangle(10, 20)
  print(r1)
  print('widht: %s\nheight: %s'%(r1.width, r1.height))
