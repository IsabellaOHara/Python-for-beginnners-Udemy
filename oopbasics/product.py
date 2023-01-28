class Product:

    # the constructor initialises the fields - values are hard coded here
    def __init__(self):
        self.name = 'IPhone'
        self.description = 'awesome'
        self.price = 1000.00

    # good for deleting files, closing db connections etc
    def __del__(self):
        print("inside the destructor")

    def display(self):
        print(self.name)
        print(self.price)
        print(self.description)

# instantiate an object of this class
p1 = Product()

p1.display()


p2 = Product()

print(p2.name)
print(p2.description)
print(p2.price)
