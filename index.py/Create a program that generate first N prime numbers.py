# Program to generate the first N prime numbers
# and calculate their sum and average.

# Taking input from the user
N = int(input("Enter the value of N: "))

# List to store prime numbers
prime_numbers = []

number = 2  # Starting number

# Loop until we get N prime numbers
while len(prime_numbers) < N:

    is_prime = True

    # Checking if the number is prime
    for i in range(2, number):

        if number % i == 0:
            is_prime = False
            break

    # Adding prime number to the list
    if is_prime:
        prime_numbers.append(number)

    number += 1

# Calculating sum and average
total = sum(prime_numbers)
average = total / N

# Displaying the results
print("\nFirst", N, "Prime Numbers:")
print(prime_numbers)

print("\nSum of Prime Numbers:", total)
print("Average of Prime Numbers:", average)

# Expected Output
"""
Example Input:
Enter the value of N: 5

Expected Output:
First 5 Prime Numbers:
[2, 3, 5, 7, 11]

Sum of Prime Numbers: 28
Average of Prime Numbers: 5.6
"""