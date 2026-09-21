class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_vehicle(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type, price):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.price = price

    def display_car(self):
        self.display_vehicle()
        print("Fuel Type:", self.fuel_type)
        print("Price:", self.price)

    def discounted_price(self, discount):
        discount_amount = self.price * discount / 100
        final_price = self.price - discount_amount
        print("Discounted Price:", final_price)


c = Car("Toyota", "Innova", "Diesel", 2000000)

c.display_car()

c.discounted_price(10)