# Program to read student marks from a file
# and display topper, average marks,
# and students scoring below average.

# Creating sample file
file = open("student_marks.txt", "w")

file.write("Rahul 85\n")
file.write("Aman 72\n")
file.write("Priya 90\n")
file.write("Sneha 65\n")
file.write("Rohit 78\n")

file.close()

# Reading file data
file = open("student_marks.txt", "r")

students = []

for line in file:

    data = line.split()

    name = data[0]
    marks = int(data[1])

    students.append((name, marks))

file.close()

# Finding topper
topper = students[0]

total_marks = 0

for student in students:

    total_marks += student[1]

    if student[1] > topper[1]:
        topper = student

# Calculating average
average_marks = total_marks / len(students)

# Displaying results
print("Topper:", topper[0], "-", topper[1])

print("Average Marks:", average_marks)

print("\nStudents Scoring Below Average:")

for student in students:

    if student[1] < average_marks:
        print(student[0], "-", student[1])

# Expected Output
"""
Topper: Priya - 90
Average Marks: 78.0

Students Scoring Below Average:
Aman - 72
Sneha - 65
"""