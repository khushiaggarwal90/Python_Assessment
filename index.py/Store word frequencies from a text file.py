# Program to store word frequencies from a text file
# and display top five most frequently used words.

# Opening file
file = open("sample_text.txt", "w")

file.write("Python is easy and Python is powerful. ")
file.write("Python is widely used in programming. ")
file.write("Programming with Python is fun.")

file.close()

# Reading file
file = open("sample_text.txt", "r")

content = file.read().lower()

file.close()

# Removing punctuation
for symbol in ".,!?":
    content = content.replace(symbol, "")

# Splitting words
words = content.split()

# Dictionary for word frequency
word_frequency = {}

# Counting frequencies
for word in words:

    if word in word_frequency:
        word_frequency[word] += 1

    else:
        word_frequency[word] = 1

# Sorting words by frequency
sorted_words = sorted(
    word_frequency.items(),
    key=lambda item: item[1],
    reverse=True
)

# Displaying top five words
print("Top Five Most Frequent Words:\n")

for word, frequency in sorted_words[:5]:
    print(word, ":", frequency)

# Expected Output
"""
Top Five Most Frequent Words:

python : 4
is : 3
programming : 2
easy : 1
and : 1
"""