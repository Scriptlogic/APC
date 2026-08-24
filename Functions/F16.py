def second_largest(numbers):
    numbers = list(set(numbers))
    numbers.sort()

    return numbers[-2]

numbers = [10, 50, 30, 40, 20]

print("Second largest =", second_largest(numbers))