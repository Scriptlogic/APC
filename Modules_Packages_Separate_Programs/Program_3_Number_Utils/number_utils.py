# Program 3: Number Utility Module

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def is_armstrong(n):
    s = str(n)
    return n == sum(int(d) ** len(s) for d in s)

def is_perfect(n):
    if n <= 1:
        return False
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n
