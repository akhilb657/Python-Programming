from numpy import *

a1 = arange(1,10)
a2 = a1.copy()

print("Array_1",a1)
print("Array_2",a2)

a2[2] = 9

print("After modification")
print("Array_1",a1)
print("Array_2",a2)