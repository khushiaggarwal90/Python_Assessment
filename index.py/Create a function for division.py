# Function for division with exception handling

# Function definition
def divide_numbers(a, b):

    try:

        result = a / b
        return result

    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

    except TypeError:
        return "Error: Invalid input type."


# Taking input from user
try:

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Function call
    output = divide_numbers(num1, num2)

    print("Result:", output)

except ValueError:
    print("Error: Please enter valid numeric values.")

# Expected Output
"""
Example Input:
Enter first number: 20
Enter second number: 0

Expected Output:
Result: Error: Division by zero is not allowed.
"""