''' simple calculator (with safety checks) problem : create a calculator that performs addition , substraction,multiplication,or division'''
num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))
operation = input("enter operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero is not allowed.")
        exit()
else:
    print("Error: Invalid operation.")
    exit()

print("Result:", result)