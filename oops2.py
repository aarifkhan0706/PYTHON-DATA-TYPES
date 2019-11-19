class grocery:
    no_of_groceries=0
    def __init__(self,name,price):
        self.name=name
        self.price=price
        grocery.no_of_groceries+=1#using dot as we are using class method
    def show_groceries(self):
        print("The name of the grocery",self.name)
        print("The price of the {} is ".format(self.name),self.price,"\n")
b1=grocery("cornflakes","150rupees")
b2=grocery("cadbury","100rupees")
b3=grocery("horlicks","250rupees")
b1.show_groceries()
b2.show_groceries()
b3.show_groceries()


