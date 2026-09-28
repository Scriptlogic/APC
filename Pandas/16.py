import pandas as pd

# Read CSV file
df = pd.read_csv("Pandas/weather.csv")

# Display complete data
print("Weather Data:")
print(df)

# Maximum temperature
print("\nMaximum Temperature:")
print(df["Temperature"].max())

# Minimum temperature
print("\nMinimum Temperature:")
print(df["Temperature"].min())

# Average temperature
print("\nAverage Temperature:")
print(df["Temperature"].mean())

# Records where temperature is above 35
print("\nRecords where Temperature is above 35°C:")
print(df[df["Temperature"] > 35])

# City-wise average temperature
print("\nCity-wise Average Temperature:")
print(df.groupby("City")["Temperature"].mean())