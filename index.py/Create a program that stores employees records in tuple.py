# Program to store employee records in tuples
# and display employees with salary above average.

# List to store employee records
employees = []

# Taking number of employees
n = int(input("Enter number of employees: "))

# Input employee details
for i in range(n):

    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    salary = float(input("Enter Employee Salary: "))

    # Creating tuple
    employee = (emp_id, name, salary)

    employees.append(employee)

# Calculating average salary
total_salary = 0

for emp in employees:
    total_salary += emp[2]

average_salary = total_salary / n

print("\nAverage Salary:", average_salary)

# Displaying employees above average salary
print("\nEmployees with Salary Above Average:")

for emp in employees:

    if emp[2] > average_salary:
        print(emp)

# Expected Output
"""
Average Salary: 45000.0

Employees with Salary Above Average:
(102, 'Rahul', 50000.0)
(103, 'Aman', 60000.0)
"""