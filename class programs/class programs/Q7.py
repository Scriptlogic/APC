class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Storage:", self.storage)
        print("Price:", self.price)

    def discounted_price(self, discount):
        final_price = self.price - (self.price * discount / 100)
        print("Price after", discount, "% discount:", final_price)


m = MobilePhone("Samsung", "Galaxy A55", "128 GB", 30000)

m.display()
m.discounted_price(10)