# Pandas program to read employee data from a CSV file
# and display department-wise average salary
# and highest salary employee.

import pandas as pd

# Creating sample employee data
employee_data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Rahul", "Priya", "Aman", "Sneha", "Rohit"],
    "Department": ["HR", "IT", "IT", "Finance", "HR"],
    "Salary": [40000, 60000, 55000, 70000, 45000]
}

# Creating DataFrame
df = pd.DataFrame(employee_data)

# Saving data to CSV file
df.to_csv("employee_data.csv", index=False)

# Reading CSV file
employee_df = pd.read_csv("employee_data.csv")

# Displaying employee data
print("Employee Data:\n")
print(employee_df)

# Calculating department-wise average salary
average_salary = employee_df.groupby("Department")["Salary"].mean()

print("\nDepartment-wise Average Salary:\n")
print(average_salary)

# Finding highest salary employee
highest_salary_employee = employee_df.loc[employee_df["Salary"].idxmax()]

print("\nHighest Salary Employee:\n")
print(highest_salary_employee)

# Expected Output
"""
Department-wise Average Salary:

Department
Finance    70000.0
HR         42500.0
IT         57500.0

Highest Salary Employee:

Employee_ID        104
Name             Sneha
Department      Finance
Salary            70000
"""