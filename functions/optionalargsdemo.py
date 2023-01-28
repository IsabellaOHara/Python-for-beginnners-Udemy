# *args is an optional argument - can be any number of args
# **kwargs for keyword args
# names don't matter just the *'s
def myfun(x, *args, **kwargs):
    print(x)
    for each_arg in args:
        print(each_arg)
    for key, value in kwargs.items():
        print(key, value)
    modified_args = args+(50, )
    my_fun2(*modified_args, **kwargs)


def my_fun2(*args, **kwargs):
    print(args)
    print(kwargs)

myfun(10, 20, 30, 40, name="Bella", age=22)

