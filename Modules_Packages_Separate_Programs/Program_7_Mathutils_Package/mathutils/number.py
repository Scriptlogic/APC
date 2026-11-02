# Program 7: Number Operations

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_armstrong(n):
    s = str(n)
    return n == sum(int(d) ** len(s) for d in s)

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]
