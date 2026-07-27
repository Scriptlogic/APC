# Program to compute cos(x) using the cosine series

x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms: "))

sum = 1
fact = 1
sign = -1

for i in range(2, n + 1, 2):
    fact *= i * (i - 1)      # Computes i!
    term = (x ** i) / fact
    sum += sign * term
    sign *= -1               # Changes the sign of the next term

print("cos(", x, ") =", sum)