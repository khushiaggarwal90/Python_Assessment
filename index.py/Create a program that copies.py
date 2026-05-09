# Program to copy contents from one file to another
# and count total words copied.

try:

    # Taking file names
    source_file = input("Enter source file name: ")
    destination_file = input("Enter destination file name: ")

    # Opening source file
    file1 = open(source_file, "r")

    # Reading content
    content = file1.read()

    file1.close()

    # Opening destination file
    file2 = open(destination_file, "w")

    # Writing content
    file2.write(content)

    file2.close()

    # Counting words
    word_count = len(content.split())

    # Displaying result
    print("\nFile copied successfully!")
    print("Total Words Copied:", word_count)

# Handling file not found
except FileNotFoundError:
    print("Error: Source file not found.")

# Handling other exceptions
except Exception as error:
    print("An error occurred:", error)

# Expected Output
"""
Example Output:
File copied successfully!
Total Words Copied: 120
"""