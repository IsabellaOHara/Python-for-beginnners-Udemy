num = int(input("Please enter an integer:"))

for i in range(0, num):
    if i % 10 == 0:
        continue
    elif i > 100:
        break
    else:
        print(i)
