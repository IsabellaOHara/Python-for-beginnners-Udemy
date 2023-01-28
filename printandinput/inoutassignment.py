number = int(input('Enter a number of your choice: '))
primeFlag = False
for n in range(2, number):
    if number % n == 0:
        primeFlag = False
        break
    else:
        primeFlag = True

if primeFlag:
    print('number is prime')
else:
    print('number is not prime')
    