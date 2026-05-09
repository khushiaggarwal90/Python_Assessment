# Menu-driven mathematical utility program

# Function to calculate factorial
def factorial(number):

    fact = 1

    for i in range(1, number + 1):
        fact *= i

    return fact


# Function to check prime number
def is_prime(number):

    if number <= 1:
        return False

    for i in range(2, number):

        if number % i == 0:
            return False

    return True


# Function to check Armstrong number
def is_armstrong(number):

    original = number
    digits = len(str(number))

    total = 0

    while number > 0:

        digit = number % 10
        total += digit ** digits

        number = number // 10

    return total == original


# Menu-driven program
while True:

    print("\n===== Mathematical Utility Menu =====")
    print("1. Factorial")
    print("2. Prime Checking")
    print("3. Armstrong Number Checking")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    # Factorial
    if choice == 1:

        number = int(input("Enter a number: "))

        print("Factorial:", factorial(number))

    # Prime checking
    elif choice == 2:

        number = int(input("Enter a number: "))

        if is_prime(number):
            print(number, "is a Prime Number.")

        else:
            print(number, "is not a Prime Number.")

    # Armstrong checking
    elif choice == 3:

        number = int(input("Enter a number: "))

        if is_armstrong(number):
            print(number, "is an Armstrong Number.")

        else:
            print(number, "is not an Armstrong Number.")

    # Exit
    elif choice == 4:

        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")

# Expected Output
"""
===== Mathematical Utility Menu =====
1. Factorial
2. Prime Checking
3. Armstrong Number Checking
4. Exit
"""