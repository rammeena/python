import abc

class Bird(abc.ABC):
    @abc.abstractmethod
    def fly(self):
        pass

class Parrot(Bird):
    
    def fly(self):
        print('Flying as Bird')

p = Parrot()

class chooper(Bird):
    
    def fly(self):
        print('Flying as plane or helicopter')

p = Parrot()
a = chooper()
