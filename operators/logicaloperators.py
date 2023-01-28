# and or not => operate with boolean values

x = 20
y = 30

print((x == 20 and y == 30))
print((x == 25 and y == 30))

print((x == 25 or y == 30))

print(not(x == 25 or y == 31)) # the not makes it true even though it is false
