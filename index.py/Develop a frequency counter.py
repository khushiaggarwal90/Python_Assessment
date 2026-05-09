# Program to count frequency of each word
# and display the most repeated word.

# Taking paragraph input
paragraph = input("Enter a paragraph: ")

# Converting paragraph to lowercase
paragraph = paragraph.lower()

# Splitting paragraph into words
words = paragraph.split()

# Dictionary to store word frequency
word_frequency = {}

# Counting frequency of each word
for word in words:

    # Removing punctuation marks
    cleaned_word = word.strip(".,!?;:")

    if cleaned_word in word_frequency:
        word_frequency[cleaned_word] += 1

    else:
        word_frequency[cleaned_word] = 1

# Displaying word frequency
print("\nWord Frequency:\n")

for word, count in word_frequency.items():
    print(word, ":", count)

# Finding most repeated word
most_repeated_word = max(word_frequency, key=word_frequency.get)

print("\nMost Repeated Word:")
print(most_repeated_word, "-", word_frequency[most_repeated_word], "times")

# Expected Output
"""
Example Input:
Enter a paragraph:
Python is great. Python is easy and Python is powerful.

Expected Output:
python : 3
is : 3
great : 1
easy : 1
and : 1
powerful : 1

Most Repeated Word:
python - 3 times
"""