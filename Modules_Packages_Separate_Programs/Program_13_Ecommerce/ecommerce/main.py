# Program 13: Ecommerce Main Program

from Products.product import add_product
from Products.stock import check_stock
from Customers.customer import create_customer
from Customers.address import add_address
from Orders.order import create_order
from Orders.total import order_total
from Payments.payment import make_payment
from Payments.receipt import generate_receipt

product = add_product("Laptop", 50000)
customer = create_customer("Amit")
address = add_address("Pune")
order = create_order(product, 1)
total = order_total(product["price"], 1)

print(product)
print("Stock Available =", check_stock(5))
print(customer)
print(address)
print(order)
print(make_payment(total))
print(generate_receipt(total))
