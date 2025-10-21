#Write a program to demonstrate single inheritance using a Parent and Child class.
class Parent:
    def display_parent(self):
        print("This is the parent class")

class Child(Parent):
    def display_child(self):
        print("This is the child class")

obj = Child()
obj.display_parent()
obj.display_child()
