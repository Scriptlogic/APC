def average(numbers):
    total = 0

    for n in numbers:
        total = total + n

    return total / len(numbers)

numbers = [10, 20, 30, 40, 50]

print("Average =", average(numbers))