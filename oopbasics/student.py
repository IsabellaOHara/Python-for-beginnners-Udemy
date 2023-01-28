class Student:

    # static field
    major = "CSE"

    def __init__(self, rollno, name):
        # __ this makes rollno field private
        self.__rollno = rollno
        self.name = name

    def display(self):
        print(self.__rollno)


s1 = Student(1, "Bill")
s2 = Student(2, "Ben")
print(s1.major)
print(s2.major)
print(s1.name)
print(s2.name)

s1.display()

# name mangling to view private field
print(s2._Student__rollno)


print(Student.major)


