from numpy import *

a1 = arange(12)
print("Array_1",a1)

a2 = reshape(a1,(4,3))
print("Arryy_2",a2)

a3 = reshape(a1,(2,2,3))
print("Array_3",a3)

print(a3.flatten())

print(eye(2))

print(ones((2,3),int))
print(zeros((2,3),int))