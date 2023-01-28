s = input("enter a sentence to reverse")

temp = s.split()

result = []

i = len(temp)-1
while i >= 0:
    result.append(temp[i])
    i = i - 1
print(result)
output = ' '.join(result)
print(output)
