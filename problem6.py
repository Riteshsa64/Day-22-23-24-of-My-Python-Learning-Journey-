#Write a program to demonstrate the use of class variables and instance variables in Python.
class Student:
    school = "ABC School"   # class variable

    def __init__(self, name):
        self.name = name    # instance variable

s1 = Student("Ritesh")
s2 = Student("Amit")

print(s1.name, s1.school)
print(s2.name, s2.school)
