# Program 7: Main Program for mathutils Package

from mathutils.basic import add, subtract, multiply, divide
from mathutils.number import is_prime, is_armstrong, is_palindrome
from mathutils.statistics import mean, maximum, minimum

print("Addition =", add(10, 5))
print("Subtraction =", subtract(10, 5))
print("Multiplication =", multiply(10, 5))
print("Division =", divide(10, 5))

n = int(input("Enter a number: "))
print("Prime =", is_prime(n))
print("Armstrong =", is_armstrong(n))
print("Palindrome =", is_palindrome(n))

values = [10, 20, 30, 40]
print("Mean =", mean(values))
print("Maximum =", maximum(values))
print("Minimum =", minimum(values))
