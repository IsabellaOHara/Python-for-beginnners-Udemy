import time
from datetime import date

startTime = time.perf_counter()

l = []

d1 = date(2016, 4, 12)
d2 = date(2017, 4, 12)
d3 = date(2018, 4, 12)
l.append(d1)
l.append(d2)
l.append(d3)

l.sort()

time.sleep(3)

for d in l:
    print(d)

endTime = time.perf_counter()

print("execution time: ", endTime - startTime)
