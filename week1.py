# Basic Calculator Program

# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter operation (+, -, *, /): ")

# Perform calculation
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
if operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
if operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
if operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: impossible")