maths = int(input("Please enter your grade for maths:"))
physics = int(input("Please enter your grade for physics:"))
chem = int(input("Please enter your grade for chemistry:"))

average = (maths + physics + chem)/3

if (maths or physics or chem) <= 35:
    print("oh no, you failed")
elif average <= 59:
    print("you passed! your final grade is: C, your score was: ", average)
elif average <= 69:
    print("you passed! your final grade is: B, your score was: ", average)
else:
    print("you passed! your final grade is: A, your score was: ", average)
