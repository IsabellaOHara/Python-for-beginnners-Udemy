import logging

logging.basicConfig(filename="mylog.log", level=logging.DEBUG)


class OverTheLimitException(Exception):
    def __init__(self, msg):
        self.msg = msg


def withdraw(amount):
    if(amount > 500):
        raise OverTheLimitException("you cannot withdraw more then $500 per day")


withdraw(600)

