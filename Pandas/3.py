import pandas as pd

data = {
    "Product_ID": [1, 2, 3, 4, 5],
    "Product_Name": ["Laptop", "Mobile", "Keyboard", "Monitor", "Mouse"],
    "Category": ["Electronics", "Electronics", "Accessories", "Electronics", "Accessories"],
    "Price": [60000, 30000, 1500, 12000, 800],
    "Quantity": [2, 3, 10, 4, 20]
}

df = pd.DataFrame(data)

df["Total_Amount"] = df["Price"] * df["Quantity"]

print(df)

print("\nProduct with highest total sales:")
print(df.loc[df["Total_Amount"].idxmax()])