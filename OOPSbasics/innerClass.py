class Car:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year

    class Engine:
        def __init__(self,n):
            self.n = n
        def start(self):
            print("Engine Started")

c = Car("Toyata",2024)

e = c.Engine(111)
e.start()
