#Write a program to show how polymorphism works using two classes Dog and Cat with a common method sound()
class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
        print("Cat meows")

for animal in (Dog(), Cat()):
    animal.sound()
