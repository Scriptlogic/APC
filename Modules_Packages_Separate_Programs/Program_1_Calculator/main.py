# Program 1: Main Program for Calculator Module

import calculator

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
choice = input("Enter operation (+, -, *, /): ")

if choice == "+":
    print("Result =", calculator.add(a, b))
elif choice == "-":
    print("Result =", calculator.subtract(a, b))
elif choice == "*":
    print("Result =", calculator.multiply(a, b))
elif choice == "/":
    print("Result =", calculator.divide(a, b))
else:
    print("Invalid operation")
