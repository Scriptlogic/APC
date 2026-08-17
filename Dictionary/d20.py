data = {
    "d": 40,
    "a": 10,
    "c": 30,
    "b": 20
}

sorted_data = dict(sorted(data.items()))

print("Dictionary in ascending order:")

for key, value in sorted_data.items():
    print(key, ":", value)