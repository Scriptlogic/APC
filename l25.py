numbers = [10, 20, 10, 30, 40, 20, 50]

unique_list = []
for item in numbers:
    if item not in unique_list:
        unique_list.append(item)

print("Original List:", numbers)
print("Unique List (order preserved):", unique_list)