import pandas as pd

data = {
    "Order_ID": [1, 2, 3, 4, 5],
    "Customer": ["Amit", "Priya", "Rahul", "Sneha", "Neha"],
    "Product": ["Laptop", "Mobile", "TV", "Printer", "Tablet"],
    "Quantity": [1, 2, 1, 3, 2],
    "Price": [60000, 25000, 40000, 10000, 20000],
    "Discount": [5000, 2000, 3000, 1000, 1500]
}

df = pd.DataFrame(data)

df["Final_Amount"] = (df["Quantity"] * df["Price"]) - df["Discount"]

print("All Orders:")
print(df)

print("\nOrders above 5000:")
print(df[df["Final_Amount"] > 5000])

print("\nHighest-value order:")
print(df.loc[df["Final_Amount"].idxmax()])

print("\nAverage order value:")
print(df["Final_Amount"].mean())