def init(self, amount):
    self.amount = amount

def add(self, value):
    return self.amount + value

Number = type(
        'Number', # The name of the class
        (object,),
        {'__version__': '1.0', '__init__': init, 'add': add} #dict of the class contents
        )

number2 = Number(2)
