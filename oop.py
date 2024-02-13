class Fruits:
    def __init__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color

    def onyesha(self):
        print(f"My favourite Fruit is {self.name} "
              f"and its cost Ksh is {self.price} "
              f"and is {self.color} in color")


myobj = Fruits("Oranges", 50 , "orange")
myobj.onyesha()
myobj2 = Fruits("Bananas",69,"yellow")
myobj2.onyesha()



