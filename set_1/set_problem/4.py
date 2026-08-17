# 4. Remove a number from set

numbers = {10, 20, 30, 40, 50}

num = int(input("Enter number to remove: "))

if num in numbers:
    numbers.remove(num)
    print("Updated set:", numbers)
else:
    print("Number not found")