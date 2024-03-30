from threading import *

def evenNumberThread():
    for i in range(2,101,2):
        print(i)

def oddNumberThread():
    for i in range(1,100,2):
        print(i)

t1 = Thread(target=evenNumberThread)
t2 = Thread(target=oddNumberThread)

t1.start()
t2.start()

print("Printing numbers from 1 to 10 in Main Thread")
for i in range(1,11):
    print(i)