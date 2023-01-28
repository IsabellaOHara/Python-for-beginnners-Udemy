# way 1
s = input("enter a string to reverse")
print(s[::-1])

# way 2
s = input("enter a string to reverse")

i = len(s)-1
result = ''

while i >= 0:
    result = result+s[i]
    i = i-1
print(result)

# way 3

d = '-'.join(['a', 'b', 'c'])
print(d)

s = input("enter a string to reverse")
print(''.join(reversed(s)))

