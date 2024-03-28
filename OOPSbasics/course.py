class Course:
    def __init__(self,name,ratings):
        self.name = name
        self.ratings = ratings

    def average(self):
        numberOfRatings = len(self.ratings)
        avg = sum(self.ratings)/numberOfRatings
        print("Average ratings for ",self.name,"is ",avg)

c1 = Course("Python",[1,2,3,4,5])
print(c1.name)
print(c1.ratings)
c1.average()

c2 = Course("Django",[5,5,4,5])
print(c2.name)
print(c2.ratings)
c2.average()
