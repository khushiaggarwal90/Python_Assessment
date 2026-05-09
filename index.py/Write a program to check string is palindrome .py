# Program to check whether a string is a palindrome
# after removing spaces and punctuation marks.

import string

# Taking input from the user
text = input("Enter a string: ")

# Removing spaces and punctuation
cleaned_text = ""

for char in text:

    if char.isalnum():
        cleaned_text += char.lower()

# Checking palindrome
if cleaned_text == cleaned_text[::-1]:
    print("The string is a palindrome.")

else:
    print("The string is not a palindrome.")

# Expected Output
"""
Example Input:
A man, a plan, a canal: Panama

Expected Output:
The string is a palindrome.
"""