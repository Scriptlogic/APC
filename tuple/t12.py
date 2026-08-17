numbers = []

for i in range(5):
    num = int(input("Enter number: "))
    numbers.append(num)

t = tuple(numbers)

print("Tuple:", t)