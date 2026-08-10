n = int(input("Enter a number: "))

num = n
rev = 0

while n > 0:
    rev = rev * 10 + (n % 10)
    n = n // 10

if num == rev:
    print("Palindrome")
else:
    print("Not Palindrome")