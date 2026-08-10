numbers = [10, 20, 10, 30, 40, 20, 50, 30]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("Original list:", numbers)
print("Unique elements:", unique_numbers)