l1 = eval(input("enter a list of elements"))
l2 = []
for eachValue in l1:
    if eachValue not in l2:
        l2.append(eachValue)
    print(l2)

s1 = set(l1)
print(s1)
