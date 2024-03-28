class Student:
    major = "CSE"

    def __init__(self,rollNo,name):
        self.rollNo = rollNo
        self.name = name

s1 = Student(1,"Akhil")
s2 = Student(2,"Ranga")
print(s1.major)
print(s2.major)
print(s1.name)
print(s2.name)
print(Student.major)