# Program to count total words, lines, and characters
# in a text file with file handling exceptions.

try:

    # Taking file name from user
    file_name = input("Enter file name: ")

    # Opening file
    file = open(file_name, "r")

    # Reading file content
    content = file.read()

    # Counting characters
    character_count = len(content)

    # Counting words
    words = content.split()
    word_count = len(words)

    # Counting lines
    file.seek(0)
    lines = file.readlines()
    line_count = len(lines)

    # Closing file
    file.close()

    # Displaying results
    print("\nFile Analysis:")
    print("Total Lines:", line_count)
    print("Total Words:", word_count)
    print("Total Characters:", character_count)

# Handling file not found error
except FileNotFoundError:
    print("Error: File not found.")

# Handling other exceptions
except Exception as error:
    print("An error occurred:", error)

# Expected Output
"""
Example Input:
Enter file name: sample.txt

Expected Output:
File Analysis:
Total Lines: 5
Total Words: 48
Total Characters: 250
"""