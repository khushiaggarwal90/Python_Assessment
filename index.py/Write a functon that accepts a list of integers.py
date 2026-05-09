# Function to return factorials of only even numbers
# from a list of integers.

# Function to calculate factorial
def factorial(number):

    fact = 1

    for i in range(1, number + 1):
        fact *= i

    return fact


# Function to process even numbers
def even_factorials(numbers):

    factorial_list = []

    for num in numbers:

        # Checking even number
        if num % 2 == 0:

            factorial_list.append(factorial(num))

    return factorial_list


# Taking input from the user
numbers = list(map(int, input("Enter integers separated by space: ").split()))

# Function call
result = even_factorials(numbers)

# Displaying result
print("\nFactorials of Even Numbers:")
print(result)

# Expected Output
"""
Example Input:
Enter integers separated by space: 2 3 4 5 6

Expected Output:
Factorials of Even Numbers:
[2, 24, 720]
"""