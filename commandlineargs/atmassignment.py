import sys

lst = sys.argv

accBalance = 10000.00

if lst[1] == "1":
    print("Account Balance:", accBalance)
elif lst[1] == "2":
    withdraw = float(input("Enter the value to withdraw"))
    if withdraw > accBalance:
        print("Denied - insufficient funds");
    else:
        accBalance = accBalance - withdraw
elif lst[1] == "3":
    depositCash = float(input("Enter the value of cash to deposit"))
    accBalance = accBalance + depositCash
elif lst[1] == "4":
    depositCheck = float(input("Enter the value of check to deposit"))
    accBalance = accBalance + depositCheck
else:
    print("invalid option")
