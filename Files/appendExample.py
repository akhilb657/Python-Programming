f = open("sample.txt","a+")

print("Cursor is at:",f.tell())

f.write("Django is a web framework\n")

f.seek(0)

a = []
for l in f:
    a.append(l)

print(a)

f.close()