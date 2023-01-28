class ATMConstants:
    withdraw = 1
    deposit = 2
    balance_check = 3


option = 1

match option:
    case ATMConstants.withdraw:
        print("withdraw")
    case ATMConstants.deposit:
        print("deposits")
    case ATMConstants.balance_check:
        print("balance check")
    case _:
        print("invalid option")

