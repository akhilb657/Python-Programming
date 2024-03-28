class Student:
    """
    def __init__(self):
        self.__id = 9
        self.__name = "Ranga"

    def display(self):
        print(self.__id)
        print(self.__name)
    """
    def setId(self,id):
        self.id = id

    def getId(self):
        return self.id

    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name



s = Student()
s.setId(9)
s.setName("Ranga")
print(s.getId())
print(s.getName())

"""
#s.display()
print(s._Student__id)
print(s._Student__name)
"""