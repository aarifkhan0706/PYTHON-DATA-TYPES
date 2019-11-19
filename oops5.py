#usig parent class name
class Base(object):
    def __init__(self,x):
        self.x=x
class Derived(Base):
    def __init__(self,x,y):
        Base.x=x
        Base.y=y
    def print(self):