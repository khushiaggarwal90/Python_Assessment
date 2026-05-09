# Program to check Armstrong numbers entered by the user.

# Taking number of inputs
n = int(input("Enter how many numbers you want to check: "))

# Loop for checking numbers
for i in range(n):

    number = int(input("\nEnter a number: "))

    original_number = number
    digits = len(str(number))

    sum_of_powers = 0

    # Calculating sum of powers
    while number > 0:

        digit = number % 10

        sum_of_powers += digit ** digits

        number = number // 10

    # Checking Armstrong number
    if sum_of_powers == original_number:
        print(original_number, "is an Armstrong Number.")

    else:
        print(original_number, "is not an Armstrong Number.")

# Expected Output
"""
Example Input:
Enter how many numbers you want to check: 2

Enter a number: 153
153 is an Armstrong Number.

Enter a number: 125
125 is not an Armstrong Number.
"""