f = open("sample.txt","r")

print(f.read(13))

f.seek(0)
print(f.readline(2))
f.seek(0)
print(f.readlines())

f.close()