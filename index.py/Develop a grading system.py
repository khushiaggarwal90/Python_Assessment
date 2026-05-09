# Program to calculate percentage, assign grade,
# and check scholarship eligibility using nested if-else.

# Taking marks input for 5 subjects
subject1 = float(input("Enter marks of Subject 1: "))
subject2 = float(input("Enter marks of Subject 2: "))
subject3 = float(input("Enter marks of Subject 3: "))
subject4 = float(input("Enter marks of Subject 4: "))
subject5 = float(input("Enter marks of Subject 5: "))

# Calculating total marks
total_marks = subject1 + subject2 + subject3 + subject4 + subject5

# Calculating percentage
percentage = (total_marks / 500) * 100

# Displaying percentage
print("\nTotal Marks:", total_marks)
print("Percentage:", percentage, "%")

# Assigning grade using nested if-else
if percentage >= 90:
    grade = "A+"

    if percentage >= 95:
        scholarship = "Eligible for Full Scholarship"
    else:
        scholarship = "Eligible for Partial Scholarship"

elif percentage >= 75:
    grade = "A"

    if percentage >= 85:
        scholarship = "Eligible for Partial Scholarship"
    else:
        scholarship = "Not Eligible for Scholarship"

elif percentage >= 60:
    grade = "B"
    scholarship = "Not Eligible for Scholarship"

elif percentage >= 40:
    grade = "C"
    scholarship = "Not Eligible for Scholarship"

else:
    grade = "Fail"
    scholarship = "Not Eligible for Scholarship"

# Displaying grade and scholarship status
print("Grade:", grade)
print("Scholarship Status:", scholarship)

# Expected Output
"""
Example Input:
Enter marks of Subject 1: 85
Enter marks of Subject 2: 90
Enter marks of Subject 3: 88
Enter marks of Subject 4: 92
Enter marks of Subject 5: 87

Expected Output:
Total Marks: 442.0
Percentage: 88.4 %
Grade: A
Scholarship Status: Eligible for Partial Scholarship
"""