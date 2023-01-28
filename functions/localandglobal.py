x = 123  # global


def display():
    x = 476
    y = 678  # local
    print(x, y)
    print(globals()['x'])


# assign function to a variable
z = display
z()
