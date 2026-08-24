def natural_sum(n):
    sum = 0

    for i in range(1, n + 1):
        sum = sum + i

    return sum

n = int(input("Enter n: "))

print("Sum =", natural_sum(n))