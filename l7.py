numbers = []

for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)

sum = 0

for num in numbers:
    sum = sum + num

average = sum / 10

print("Sum =", sum)
print("Average =", average)