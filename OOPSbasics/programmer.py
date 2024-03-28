class Programmer:
    def setName(self,n):
        self.name = n
    def getName(self):
        return self.name

    def setSalary(self,s):
        self.salary = s
    def getSalary(self):
        return self.salary

    def setTechnologies(self,skills):
        self.technologies = skills
    def getTechnologies(self):
        return self.technologies

p1 = Programmer()
p1.setName("Akhil")
p1.setSalary(7500)
p1.setTechnologies(["JavaScript","Angular","Python","Django"])
print(p1.getName())
print(p1.getSalary())
print(p1.getTechnologies())