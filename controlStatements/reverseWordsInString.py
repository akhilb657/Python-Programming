s = input("Enter a string: ")
t = s.split()
#print(t)

s1 = []

i = len(t)-1

while(i>=0):
    s1.append(t[i])
    i -= 1
print(' '.join(s1))
