# Program to print a pyramid pattern of numbers
# and calculate the sum of all printed numbers.

# Taking number of rows
rows = int(input("Enter number of rows: "))

current_number = 1
total_sum = 0

# Printing pyramid pattern
for i in range(1, rows + 1):

    for j in range(i):

        print(current_number, end=" ")

        total_sum += current_number
        current_number += 1

    print()

# Displaying total sum
print("\nSum of all printed numbers:", total_sum)

# Expected Output
"""
Example Input:
Enter number of rows: 4

Expected Output:
1
2 3
4 5 6
7 8 9 10

Sum of all printed numbers: 55
"""