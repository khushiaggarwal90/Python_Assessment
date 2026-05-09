# Program to separate vowels and consonants
# from a sentence.

# Taking input from user
sentence = input("Enter a sentence: ")

# Lists to store vowels and consonants
vowels = []
consonants = []

# Vowel characters
vowel_letters = "aeiouAEIOU"

# Processing sentence
for char in sentence:

    # Checking alphabet characters
    if char.isalpha():

        if char in vowel_letters:
            vowels.append(char)

        else:
            consonants.append(char)

# Displaying results
print("\nVowels:")
print(vowels)

print("\nConsonants:")
print(consonants)

# Expected Output
"""
Example Input:
Enter a sentence: Python Programming

Expected Output:
Vowels:
['o', 'o', 'a', 'i']

Consonants:
['P', 'y', 't', 'h', 'n', 'P', 'r', 'g', 'r', 'm', 'm', 'n', 'g']
"""