class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_vehicle(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def display_car(self):
        self.display_vehicle()
        print("Fuel Type:", self.fuel_type)


class Bike(Vehicle):
    def __init__(self, brand, model, engine):
        super().__init__(brand, model)
        self.engine = engine

    def display_bike(self):
        self.display_vehicle()
        print("Engine:", self.engine)


class SportsCar(Car):
    def __init__(self, brand, model, fuel_type, top_speed):
        super().__init__(brand, model, fuel_type)
        self.top_speed = top_speed

    def display_sports_car(self):
        self.display_car()
        print("Top Speed:", self.top_speed, "km/h")


class ElectricBike(Bike):
    def __init__(self, brand, model, engine, battery):
        super().__init__(brand, model, engine)
        self.battery = battery

    def display_electric_bike(self):
        self.display_bike()
        print("Battery:", self.battery, "kWh")


s = SportsCar("BMW", "M4", "Petrol", 280)
e = ElectricBike("Ola", "S1", "Electric", 4)

s.display_sports_car()

print()

e.display_electric_bike()