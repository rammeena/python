#user.py
from library import Base

#assert hasattr(Base, 'foo'), "You broke it you fool"

class Derived(Base):
    def bar(self):
    #def bard(self):
        return 'bar'
