# Program to identify students enrolled
# in multiple courses using tuples and sets.

# Tuples containing student names and courses
course1 = ("Rahul", "Aman", "Sneha", "Priya")
course2 = ("Aman", "Priya", "Rohit", "Karan")
course3 = ("Sneha", "Rahul", "Karan", "Anjali")

# Converting tuples into sets
set1 = set(course1)
set2 = set(course2)
set3 = set(course3)

# Finding students enrolled in multiple courses
multiple_courses = (set1 & set2) | (set2 & set3) | (set1 & set3)

# Displaying result
print("Students Enrolled in Multiple Courses:")
print(multiple_courses)

# Expected Output
"""
Students Enrolled in Multiple Courses:
{'Rahul', 'Aman', 'Priya', 'Sneha', 'Karan'}
"""