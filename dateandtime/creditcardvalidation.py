from datetime import datetime, date


def validateCard(expDate):
    if expDate > datetime.now().date():
        print("valid")
    else:
        print("expired")


validateCard(date(2022,8,1))

