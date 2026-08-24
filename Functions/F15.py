def unique_elements(numbers):
    result = []

    for n in numbers:
        if n not in result:
            result.append(n)

    return result

numbers = [10, 20, 10, 30, 20, 40]

print("Unique elements =", unique_elements(numbers))