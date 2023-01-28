from threading import Thread
import threading


def displayNumbers():
    i = 0
    print('Current thread:', threading.current_thread().name)
    while i <= 10:
        print(i)
        i += 1


print('Current thread:', threading.current_thread().name)
t = Thread(target=displayNumbers)
t.start()

