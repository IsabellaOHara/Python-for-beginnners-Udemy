import threading
from threading import *


def oddNumberThread():
    for i in range(100):
        if i%2==0: print(i)


def evenNumberThread():
    for i in range(100):
        if i%2 != 0:
            print(i)


def allNumber():
    for i in range(100):
        print(i)


t1 = Thread(target=oddNumberThread)
t1.start()
t2 = Thread(target=evenNumberThread)
t2.start()
allNumber()
