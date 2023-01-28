s = input("enter a sentence")

temp = s.split()
result = []
i = 0

while i < len(temp):
    result.append(temp[i][::-1])
    i = i+1
output = ' '.join(result)
print(output)
