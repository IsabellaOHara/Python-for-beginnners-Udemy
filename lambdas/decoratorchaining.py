def square(fun):
    def inner():
        n = fun()
        return n*n
    return inner


def half(fun):
    def inner():
        n = fun()
        return n/2
    return inner


@square
@half #this will happen first
def num():
    return 10


print(num())

