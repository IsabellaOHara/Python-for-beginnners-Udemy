from datetime import *

d = date(2023, 1, 26)
t = time(10, 12)

dt = datetime.combine(d, t)
print(dt)

