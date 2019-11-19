#implementing inheritance
class car():
    def wheels(self):
        print("it has great wheels")
    def engines(self):
        print("it has great engine")
class honda(car):
    def shape(self):
        print("Its a sedan")
t1=car()
t2=honda()

t2.wheels()
t2.engines()
t2.shape()
