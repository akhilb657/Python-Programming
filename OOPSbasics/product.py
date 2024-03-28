class Product:
    def __init__(self):
        self.name = "MAC"
        self.description = 'Amazing'
        self.price = 900

    def __del__(self):
        print("Destructor")

    def display(self):
        print(self.name)
        print(self.description)
        print(self.price)

p1 = Product()
p1.display()
p1 = None

p2 = Product()
p2.display()
p2 = None