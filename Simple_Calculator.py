
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /, %, **): ")

if operator == "+":
    print("Result:", a + b)
elif operator == "-":
    print("Result:", a - b)
elif operator == "*":
    print("Result:", a * b)
elif operator == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
elif operator == "%":
    print("Result:", a % b)
elif operator == "**":
    print("Result:", a ** b)
else:
    print("Invalid operator")
