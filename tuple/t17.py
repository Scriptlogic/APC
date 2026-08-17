t = (25, 10, 45, 5, 30)

largest = t[0]
smallest = t[0]

for num in t:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("Largest =", largest)
print("Smallest =", smallest)