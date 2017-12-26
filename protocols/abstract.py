import abc

class Aeroplane(abc.ABC):

    @abc.abstractmethod
    def fly(self):
        pass

class Boeing(Aeroplane):
    def fly(self):
        print('Boeing Flying')

