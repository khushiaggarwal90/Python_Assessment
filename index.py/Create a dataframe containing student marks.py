# Program to create a DataFrame containing student marks,
# calculate total marks, percentage,
# and assign grades using apply() function.

import pandas as pd

# Creating student data
data = {
    "Name": ["Rahul", "Priya", "Aman", "Sneha"],
    "Math": [85, 92, 76, 88],
    "Science": [78, 95, 80, 84],
    "English": [90, 89, 70, 91]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Calculating total marks
df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)

# Calculating percentage
df["Percentage"] = df["Total"] / 3

# Function to assign grades
def assign_grade(percentage):

    if percentage >= 90:
        return "A+"

    elif percentage >= 75:
        return "A"

    elif percentage >= 60:
        return "B"

    elif percentage >= 40:
        return "C"

    else:
        return "Fail"

# Applying function
df["Grade"] = df["Percentage"].apply(assign_grade)

# Displaying DataFrame
print(df)

# Expected Output
"""
     Name  Math  Science  English  Total  Percentage Grade
0  Rahul    85       78       90    253   84.33      A
1  Priya    92       95       89    276   92.00      A+
"""