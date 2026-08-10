import math

n = int(input("Enter number: "))
r = int(math.sqrt(n))

prime = True
for i in range(2, r):
    if r % i == 0:
        prime = False

if prime and r > 1:
    print("Square root is prime")
else:
    print("Square root is not prime")