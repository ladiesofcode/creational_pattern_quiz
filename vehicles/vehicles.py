class Vehicle:
    def drive(self):
        pass

class Truck(Vehicle):
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        return "Car driving"

class Toyota(Car):
    def drive(self):
        return "Toyota driving"

class Ford(Car):
    def drive(self):
        return "Ford driving"

class Iveco(Truck):
    def drive(self):
        return "Iveco driving"

class Man(Truck):
    def drive(self):
        return "Man driving"


vehicles = [Man(), Iveco(), Ford(), Toyota()]

for veh in vehicles:
    print(veh.drive())


# Run:
# python vehicles/vehicles.py