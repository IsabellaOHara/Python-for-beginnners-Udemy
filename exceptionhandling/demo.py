import logging

logging.basicConfig(filename="mylog.log", level=logging.DEBUG)

try:
    f = open("myfile", "w")
    a, b = [int(x) for x in input("enter 2 numbers:").split()]
    logging.info("Division in progress")
    c = a/b
    f.write("writing %d into file" %c)
except ZeroDivisionError:
    print("division by 0 is not allowed")
    print("please enter a non zero number")
    logging.error("division by zero")
else:
    print("you have entered a non zero number")
finally:
    f.close()
    print("file closed")

