def display(name):
    def message():
        return "hello "
    return message


fun = display()
print(fun())

