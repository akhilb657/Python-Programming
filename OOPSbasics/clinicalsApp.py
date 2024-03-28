class Patient:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.clinical = []

    def addClinicalData(self,clinical):
        self.clinical.append(clinical)



class Clinical:
    def __init__(self,componentName, componentValue):
        self.componentName = componentName
        self.componentValue = componentValue

p = Patient("Satya", 33)

c1 = Clinical("BP", '80/112')
p.addClinicalData(c1)

c2 = Clinical("Heart rate",80)
p.addClinicalData(c2)

print(p.name)
for i in p.clinical:
    print(i.componentName)
    print(i.componentValue)

