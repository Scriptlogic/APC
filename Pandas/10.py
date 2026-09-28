import pandas as pd

price = pd.Series({
    "Laptop": 60000,
    "Mobile": 30000,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Mouse": 800
})

print("Products and Prices:")
print(price)

price = price * 1.10

print("\nPrices after 10% increase:")
print(price)

print("\nMost expensive product:")
print(price.idxmax(), price.max())

print("\nProducts costing more than 1000:")
print(price[price > 1000])