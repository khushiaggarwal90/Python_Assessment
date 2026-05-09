# Program to validate voting eligibility
# and handle invalid inputs.

try:

    # Taking age input
    age = int(input("Enter your age: "))

    # Checking negative age
    if age < 0:
        print("Invalid age entered.")

    # Checking voting eligibility
    elif age >= 18:
        print("You are eligible to vote.")

    else:
        print("You are not eligible to vote.")

# Handling non-numeric input
except ValueError:
    print("Error: Please enter a valid numeric age.")

# Handling other exceptions
except Exception as error:
    print("An error occurred:", error)

# Expected Output
"""
Example Input:
Enter your age: 20

Expected Output:
You are eligible to vote.
"""