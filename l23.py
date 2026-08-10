numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
frequency = {}
for item in numbers:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

for key, value in frequency.items():
    print(f"Element {key} appears {value} time(s)")