import pandas as pd

students = {}

# Add Student
def add_student():
    try:
        roll = int(input("Enter Roll Number: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        students[roll] = {
            "Name": name,
            "Marks": marks
        }

        print("Student Added Successfully!")

    except ValueError:
        print("Invalid Input!")

# View Students
def view_students():
    if students:
        for roll, details in students.items():
            print(f"Roll No: {roll}")
            print(f"Name: {details['Name']}")
            print(f"Marks: {details['Marks']}")
            print("-------------------")
    else:
        print("No records found.")

# Save to File
def save_to_file():
    try:
        with open("students.txt", "w") as file:
            for roll, details in students.items():
                file.write(f"{roll},{details['Name']},{details['Marks']}\n")

        print("Data saved to file.")

    except Exception as e:
        print("Error:", e)

# Generate Report using Pandas
def generate_report():
    df = pd.DataFrame.from_dict(students, orient='index')
    print("\nStudent Report")
    print(df)

# Menu
while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Save to File")
    print("4. Generate Report")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        save_to_file()

    elif choice == "4":
        generate_report()

    elif choice == "5":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")