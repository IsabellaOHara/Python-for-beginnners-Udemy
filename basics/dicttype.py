# key value pairs
dict1 = {1:"john", 2:"bob", 3:"bill"}
print(dict1)


print(dict1.items())

# to access the keys
k = dict1.keys()
for i in k:
    print(i)

# to access the values
v = dict1.values()
for i in v:
    print(i)

# this isn't passing in an index - passing in the key!
print(dict[3])

# delete the element at the specified key
del dict[2]