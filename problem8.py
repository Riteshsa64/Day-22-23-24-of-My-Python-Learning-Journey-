#Write a program to demonstrate encapsulation by making a variable private and accessing it using a method.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # private variable

    def show(self):
        print("Name:", self.name)
        print("Age:", self.__age)

p1 = Person("Ritesh", 20)
p1.show()

# Trying to access private variable (will cause error)
# print(p1.__age)
