# no duplicates allowed
# {}

s = {10, 20, 30, "xyz"}

print(s)
print(type(s))

# to add elements - set has no order guaranteed so they'll just be placed anywhere
s.update([88, 99])
print(s)

# no indexing or splicing or repetition allowed

# removing element
s.remove(30)
print(s)

# to convert to a frozen set (can't update/remove)
f = frozenset(s)



