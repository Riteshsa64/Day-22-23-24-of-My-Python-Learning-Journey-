#Write a Python program to demonstrate constructor (__init__) usage in a class.
class Person:
    def __init__(self, name):
        self.name = name
        print("Hello", self.name)

p1 = Person("Ritesh")
