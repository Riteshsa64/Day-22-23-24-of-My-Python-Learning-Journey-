#Create a class Car with a method start() and another class ElectricCar that inherits from it and overrides the start() method.
class Car:
    def start(self):
        print("Car is starting...")

class ElectricCar(Car):
    def start(self):
        print("Electric car is starting silently...")

tesla = ElectricCar()
tesla.start()
