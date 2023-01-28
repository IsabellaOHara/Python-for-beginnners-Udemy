try:
    num = int(input("enter an even number"))
    assert num % 2 == 0, "invalid input"
except AssertionError as obj:
    print(obj)

print("after the assertion")

