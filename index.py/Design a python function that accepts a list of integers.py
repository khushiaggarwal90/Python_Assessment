# Function to find second largest and second smallest
# element without using built-in sorting functions.

def find_second_elements(numbers):

    # Removing duplicate values
    unique_numbers = []

    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)

    # Checking minimum required elements
    if len(unique_numbers) < 2:
        return "List should contain at least two unique elements."

    # Initializing values
    largest = second_largest = float('-inf')
    smallest = second_smallest = float('inf')

    # Finding largest and second largest
    for num in unique_numbers:

        if num > largest:
            second_largest = largest
            largest = num

        elif num > second_largest:
            second_largest = num

    # Finding smallest and second smallest
    for num in unique_numbers:

        if num < smallest:
            second_smallest = smallest
            smallest = num

        elif num < second_smallest:
            second_smallest = num

    return second_largest, second_smallest


# Taking input from the user
numbers = list(map(int, input("Enter integers separated by space: ").split()))

# Function call
result = find_second_elements(numbers)

# Displaying result
print("\nSecond Largest Element:", result[0])
print("Second Smallest Element:", result[1])

# Expected Output
"""
Example Input:
Enter integers separated by space: 10 20 30 40 50

Expected Output:
Second Largest Element: 40
Second Smallest Element: 20
"""