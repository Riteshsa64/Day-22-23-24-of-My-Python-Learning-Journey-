#Create a class Student with attributes name and marks. Create an object and display the details.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

s1 = Student("Ritesh", 90)
s1.display()
