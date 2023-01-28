import threading

print('Current thread:', threading.current_thread().name)

if threading.current_thread() == threading.main_thread():
    print('Main thread')
else:
    print("other thread")



