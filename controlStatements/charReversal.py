s = "Python is powerful"
temp = s.split()
#print(temp)
s1 = []
i = 0
while i< len(temp):
    s1.append(temp[i][::-1])
    i += 1
print(" ".join(s1))

