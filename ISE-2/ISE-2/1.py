
numbers = [2, 4, 3, 5, 7, 8, 1, 6]

target = int(input("Enter the sum: "))

for i in numbers:
    for j in numbers:
        if i + j == target:
            print(i, j)


