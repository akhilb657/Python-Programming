#import numpy as np
from numpy import *

arr = array([1,2,3,4,5,6],int)
carr = array(['a','b','c','d'])
sarr = array(["Python","Django","DRF"],dtype=str)
print(arr)
print(carr)
print(sarr)

print(linspace(0,100))

larr = logspace(1,20)
for i in larr:
    print(i)

print(arange(100,1,-3))

print(zeros(20))
print(ones(9))