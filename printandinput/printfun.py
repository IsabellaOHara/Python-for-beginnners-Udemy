print("Hello"*3)
print("HI")
print("on separate \n lines")

a, b = 10, 20
print(a, b)
# to add a separator between
print(a, b, sep=',')

name = 'john'
marks = 94.5678

print('Name:', name, 'Marks:', marks)
print('Name is %s, Marks are %.2f' % (name, marks))

print("Name is {}, Marks are {}".format(name, marks))

print("Name is {0}, Marks are {1}".format(name, marks))
