# Program 3: Main Program for Number Utility Module

from number_utils import is_prime, is_palindrome, is_armstrong, is_perfect

n = int(input("Enter a number: "))

print("Prime =", is_prime(n))
print("Palindrome =", is_palindrome(n))
print("Armstrong =", is_armstrong(n))
print("Perfect =", is_perfect(n))
