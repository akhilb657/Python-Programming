from numpy import *

a1 = array([10,31,50,70,1001])
a2 = array([20,40,60,80,100])

print(a1>=a2)
print(a1<a2)

print(all(a1 <= a2))

print(logical_or(a1>10,a1<100))

print(where(a1%2 != 0, a1, 0))
print(where(a1>a2,a1,a2))