cart = []

def add_item(item):
    cart.append(item)
    print(f"'{item}' added to the cart.")

def remove_item(item):
    if item in cart:
        cart.remove(item)
        print(f"'{item}' removed from the cart.")
    else:
        print(f"'{item}' is not in the cart.")

def search_item(item):
    if item in cart:
        print(f"'{item}' is in the cart.")
    else:
        print(f"'{item}' is not in the cart.")

def display_cart():
    print("Current Cart:", cart)

def count_items():
    print("Total items in cart:", len(cart))
add_item("Apple")
add_item("Milk")
add_item("Bread")

display_cart()
count_items()

search_item("Milk")
remove_item("Milk")

display_cart()
count_items()