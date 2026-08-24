products = [
    ("Laptop", 50000, 2),
    ("Mouse", 500, 3),
    ("Keyboard", 1500, 2),
    ("Monitor", 10000, 1)
]


total = list(map(lambda x: (x[0], x[1] * x[2]), products))
print("Total value =", total)


expensive = list(filter(lambda x: x[1] > 1000, products))
print("Products above 1000 =", expensive)


sorted_products = sorted(
    products,
    key=lambda x: x[1] * x[2]
)

print("Sorted products =", sorted_products)