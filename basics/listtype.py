# creating a list []
# can add different types of data

lst = [10, 20, "bella", -10, 30.5]
print(lst)

# indexing, slicing, repetition etc
print(lst[3])
print(lst[3:5])
print(lst*4)
print(len(lst))

# adding and removing list element
list.append(40)
list.remove("bella")
del(lst[1])
print(lst)

# clears all the elements from the list
# lst.clear()

print(max(lst))
print(min(lst))

# insert in particular position (index, value)
lst.insert(3, 99)

# sorts lowest to highest
lst.sort()

# highest to lowest
lst.sort(reverse=True)