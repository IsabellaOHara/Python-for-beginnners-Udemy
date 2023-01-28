lst = [20, 30, 40, 234]

# converting a list into bytes
b = bytes(lst)

# can't add elements to bytes

b1 = bytearray(lst)

# can add elements to a bytearray
b1[2] = 33

# no slicing or repetiton allowed on either