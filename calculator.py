# Simple Calculator Program

def calculator():
    print("Welcome to Simple Calculator!")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Taking inputs from the user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    choice = input("Enter operation (+, -, *, /): ")

    # Performing operation
    if choice == '+':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is: {result}")
    elif choice == '-':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is: {result}")
    elif choice == '*':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is: {result}")
    elif choice == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is: {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation! Please choose +, -, * or /")

# Call the function
calculator()
