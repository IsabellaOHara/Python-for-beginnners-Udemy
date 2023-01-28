lst = [1, 2, 3, 4, 214, 254, 465, 3251]

result = list(filter(lambda x: x % 2 == 0, lst))
print(result)

for i in result:
    print(i)

