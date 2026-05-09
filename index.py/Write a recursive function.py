# Recursive Approach
def sum_digits_recursive(n):
    if n == 0:
        return 0
    return (n % 10) + sum_digits_recursive(n // 10)

# Iterative Approach
def sum_digits_iterative(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total

# Main Program
num = int(input("Enter a number: "))

print("Recursive Sum:", sum_digits_recursive(num))
print("Iterative Sum:", sum_digits_iterative(num))# Recursive Approach
def sum_digits_recursive(n):
    if n == 0:
        return 0
    return (n % 10) + sum_digits_recursive(n // 10)

# Iterative Approach
def sum_digits_iterative(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total

# Main Program
num = int(input("Enter a number: "))

print("Recursive Sum:", sum_digits_recursive(num))
print("Iterative Sum:", sum_digits_iterative(num))