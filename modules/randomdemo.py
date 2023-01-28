from random import *

# print random number between 0-1
print(random())

# to get 10 random numbers
for i in range(10):
    print(random())

for i in range(10):
    print(randint(1, 50))

# floats
for i in range(10):
    print(uniform(1, 50))

# start, stop , step
for i in range(10):
    print(randrange(1, 12, 2))

lst = ["java", "python", "devops", "aws"]
for i in range(10):
    print(choice(lst))
