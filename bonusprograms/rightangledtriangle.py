n = int(input('enter number of rows'))

# way 1
for i in range(1, n+1):
    for j in range(1, i+1):
        print("* ", end="")
    print()

# way 2
n = int(input('enter number of rows'))

for i in range(1, n+1):
    print("* "*i)

