class InvalidPasswordException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def displayMessage(self):
        print(self.msg)

try:
    password = input("Please enter a password")

    if len(password) < 8:
        raise InvalidPasswordException("password must be at least 8 characters")
except InvalidPasswordException as e:
    e.displayMessage()
else:
    print("Password accepted")


