class ShoppingCart:
    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.products = []

    def add_product(self, product, price):
        self.products.append([product, price])
        print(product, "added to cart.")

    def remove_product(self, product):
        for item in self.products:
            if item[0] == product:
                self.products.remove(item)
                print(product, "removed from cart.")
                return

        print("Product not found.")

    def total_bill(self):
        total = 0

        for item in self.products:
            total = total + item[1]

        print("Total Bill:", total)

    def __del__(self):
        print("Shopping cart object destroyed.")


cart = ShoppingCart("Sanjay", 101)

print("Customer Name:", cart.customer_name)
print("Cart ID:", cart.cart_id)

cart.add_product("Laptop", 50000)
cart.add_product("Mouse", 1000)
cart.add_product("Keyboard", 2000)

cart.remove_product("Mouse")

cart.total_bill()

del cart