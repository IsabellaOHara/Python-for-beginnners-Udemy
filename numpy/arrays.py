# import numpy as np
from numpy import *

arr = array([1, 2, 3, 4, 5])
carr = array(['a', 'b', 'c'])
sarr = array(['Python', 'Java', 'React'])
print(arr)
print(carr)
print(sarr)

# default is 50 divisions
print(linspace(0, 100))
# gives log values in specified range
larr = logspace(1,20)
for i in larr:
    print(larr)
# first, last(exclusive), step
print(arange(1,5,2))

print(zeros(20))
print(ones(10))
