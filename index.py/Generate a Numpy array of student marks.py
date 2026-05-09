# Program to generate NumPy array of student marks
# and convert it into a Pandas DataFrame.

import numpy as np
import pandas as pd

# Creating NumPy array
marks = np.array([
    [85, 78, 92],
    [88, 76, 95],
    [90, 82, 89],
    [70, 68, 80]
])

# Creating DataFrame
df = pd.DataFrame(
    marks,
    columns=["Math", "Science", "English"],
    index=["Student1", "Student2", "Student3", "Student4"]
)

# Displaying DataFrame
print("Student Marks DataFrame:\n")
print(df)

# Highest marks
print("\nHighest Marks in Each Subject:")
print(df.max())

# Average marks
print("\nAverage Marks in Each Subject:")
print(df.mean())

# Subject-wise statistics
print("\nSubject-wise Statistics:")
print(df.describe())

# Expected Output
"""
Highest Marks in Each Subject:
Math       90
Science    82
English    95
"""