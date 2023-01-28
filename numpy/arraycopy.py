from numpy import *

a1 = arange(1, 10)
a2 = a1.view()
a3 = a1.copy()
print('a1', a1)
print('a2', a2)
print('a3', a3)
a2[3] = 40
a3[7] = 40

print("-----------")
print('a1', a1)
print('a2', a2)
print('a3', a3)
