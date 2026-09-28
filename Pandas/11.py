import pandas as pd

age = pd.Series({
    101: 45,
    102: 65,
    103: 70,
    104: 35,
    105: 62
})

print("Average age:", age.mean())

print("\nOldest patient:")
print(age.idxmax(), age.max())

print("\nYoungest patient:")
print(age.idxmin(), age.min())

print("\nPatients above 60:")
print(age[age > 60])