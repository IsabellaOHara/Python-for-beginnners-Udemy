# tuples use ()
tpl = (20, 30, 40, 20, 50, "hi")
print(tpl)

# to make single element tuple
tpl2 = (3,)

# repetition,
print(tpl*3)

# how often does that element appear
print(tpl.count(20))

print(tpl.index('xyz'))

# slicing and max/min works the same

# converting a list to tuple
lst = [67, 34, "xyz"]
tpl2 = tuple(lst)
