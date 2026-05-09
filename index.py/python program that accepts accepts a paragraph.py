# Program to count uppercase letters, lowercase letters,
# digits, spaces, and special characters in a paragraph.

# Taking paragraph input from the user
paragraph = input("Enter a paragraph: ")

# Initializing counters
uppercase_count = 0
lowercase_count = 0
digit_count = 0
space_count = 0
special_char_count = 0

# Checking each character in the paragraph
for char in paragraph:

    # Count uppercase letters
    if char.isupper():
        uppercase_count += 1

    # Count lowercase letters
    elif char.islower():
        lowercase_count += 1

    # Count digits
    elif char.isdigit():
        digit_count += 1

    # Count spaces
    elif char.isspace():
        space_count += 1

    # Count special characters
    else:
        special_char_count += 1

# Storing results in a dictionary
result = {
    "Uppercase Letters": uppercase_count,
    "Lowercase Letters": lowercase_count,
    "Digits": digit_count,
    "Spaces": space_count,
    "Special Characters": special_char_count
}

# Sorting the result in descending order based on frequency
sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)

# Displaying the result
print("\nCharacter Count (Descending Order):")

for category, count in sorted_result:
    print(category, ":", count)

# Expected Output
"""
Example Input:
Enter a paragraph: Hello World! Python 3.11

Expected Output:
Character Count (Descending Order):
Lowercase Letters : 15
Spaces : 3
Uppercase Letters : 3
Digits : 3
Special Characters : 2
"""