import pickle,student

f = open("student.dat","wb")
s = student.Student(11,"Ranga",99)

pickle.dump(s,f)

f.close()

