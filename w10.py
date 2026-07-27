n = int(input("Enter a number: "))

i = 2

while i < n:
    if n % i == 0:
        print("Not Prime")
        break
    i += 1
else:
    print("Prime")