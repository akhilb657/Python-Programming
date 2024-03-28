class Patient:
    def __init__(self):
        self.__id = None
        self.__name = None
        self.__ssn = None

    def setId(self,id):
        self.__id = id
    def getId(self):
        return self.__id

    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name

    def setSSN(self,ssn):
        self.__ssn = ssn
    def getSSN(self):
        return self.__ssn

p = Patient()
p.setId(1)
print(p.getId())

p.setName("Ravi")
print(p.getName())

p.setSSN(1111)
print(p.getSSN())