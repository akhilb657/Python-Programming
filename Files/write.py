# opens the file for writing
f = open("myFile.txt","w")

print("Enter Text (Type 'done' when you're done)")

s = ''
while s != 'done':
    s = input()
    f.write(s + "\n")

f.close()

