#Create a class Employee with a class method that counts the total number of employees created.
class Employee:
    count = 0  # class variable

    def __init__(self, name):
        self.name = name
        Employee.count += 1

    @classmethod
    def total_employees(cls):
        print("Total Employees:", cls.count)

e1 = Employee("Ritesh")
e2 = Employee("Amit")
e3 = Employee("Sonal")

Employee.total_employees()
