class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price


p1 = Product("Laptop", 50000)
p2 = Product("Mobile", 30000)

if p1 == p2:
    print("Both products have the same price")
else:
    print("Products have different prices")

if p1 > p2:
    print(p1.name, "is more expensive than", p2.name)
else:
    print(p2.name, "is more expensive than", p1.name)