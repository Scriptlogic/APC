class FoodOrder:
    def __init__(self, order_id, customer_name, food_item, quantity, price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price

    def total_bill(self):
        subtotal = self.quantity * self.price
        tax = subtotal * 0.05
        total = subtotal + tax

        print("Subtotal:", subtotal)
        print("Tax:", tax)
        print("Total Bill:", total)

    def __del__(self):
        print("Order completed.")


order = FoodOrder(101, "Sanjay", "Pizza", 2, 250)

print("Order ID:", order.order_id)
print("Customer Name:", order.customer_name)
print("Food Item:", order.food_item)
print("Quantity:", order.quantity)
print("Price:", order.price)

order.total_bill()

del order