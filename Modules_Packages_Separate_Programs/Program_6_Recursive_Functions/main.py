# Program 6: Main Program for Recursive Functions Module

import recursive_utils

n = int(input("Enter a number: "))

print("Factorial =", recursive_utils.factorial(n))

print("Fibonacci Series:")
for i in range(n):
    print(recursive_utils.fibonacci(i), end=" ")

print()
print("Sum of Digits =", recursive_utils.sum_of_digits(n))

binary = recursive_utils.binary_conversion(n)
print("Binary =", binary if binary else "0")
