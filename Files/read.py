import os,sys

if os.path.isfile("myFile.txt"):
    f = open("myFile.txt","r")

else:
    print("File does not exist")
    sys.exit()

s = f.read()
print(s)
f.close()