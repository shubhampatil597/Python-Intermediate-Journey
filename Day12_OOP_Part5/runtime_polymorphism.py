class Vehicle:

    def start(self):

        print("Vehicle Started")


class Car(Vehicle):

    def start(self):

        print("Car Started")


class Bike(Vehicle):

    def start(self):

        print("Bike Started")


vehicles = [
    Car(),
    Bike()
]

for vehicle in vehicles:

    vehicle.start()