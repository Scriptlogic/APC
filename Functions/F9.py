def largest(numbers):
    large = numbers[0]

    for n in numbers:
        if n > large:
            large = n

    return large

numbers = [10, 25, 5, 40, 15]

print("Largest =", largest(numbers))