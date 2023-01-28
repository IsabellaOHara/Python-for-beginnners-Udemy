s = input()
print(s)

s = input("Enter your name:")
print(s)

# typecast to convert to different datatypes
i = int(input("Enter an integer: "))
print(i)

# splits by spaces
lst = [x for x in input("enter 3 numbers separated by a space:").split()]
print(lst)

# split by a comma and typecast to ints
lst2 = [int(x) for x in input("enter 3 numbers separated by a comma:").split(',')]
print(lst2)
