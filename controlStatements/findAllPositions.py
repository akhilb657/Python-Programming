s = input("Enter a string")
s1 = "Akhil"
temp = False
p = -1
while(True):
    p = s.find(s1,p+1,len(s))
    if p == -1:
        break
    print("found at ",p)
    temp=True

if temp == False:
    print("given substring not found")