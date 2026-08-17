dict1 = {
    "a": 10,
    "b": 20
}

dict2 = {
    "c": 30,
    "d": 40
}

merged = dict1.copy()
merged.update(dict2)

print("Merged dictionary:", merged)