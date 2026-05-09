# Calculator program with exception handling

try:

    # Taking inputs
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    operator = input("Enter operation (+, -, *, /): ")

    # Performing operations
    if operator == "+":
        print("Result:", num1 + num2)

    elif operator == "-":
        print("Result:", num1 - num2)

    elif operator == "*":
        print("Result:", num1 * num2)

    elif operator == "/":
        print("Result:", num1 / num2)

    else:
        raise ValueError("Invalid Operation!")

# Handling division by zero
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Handling invalid numeric input
except ValueError as error:
    print("Error:", error)

# Handling any other exception
except Exception:
    print("Something went wrong!")

# Expected Output
"""
Example Input:
Enter first number: 10
Enter second number: 0
Enter operation (+, -, *, /): /

Expected Output:
Error: Division by zero is not allowed.
"""