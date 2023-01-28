class TooYoungException(Exception):
    def __init__(self, msg):
        self.msg = msg


class TooOldException(Exception):
    def __init__(self, msg):
        self.msg = msg


age = int(input("enter your age"))
if age < 18:
    raise TooYoungException("You need to be over 18 to apply for this")
elif age > 90:
    raise TooOldException("you must be younger than 90 ")
else:
    print("you are eligible")
