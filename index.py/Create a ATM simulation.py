# Contact Management System using list and dictionary

# List to store contacts
contacts = []

while True:

    # Displaying menu
    print("\n===== Contact Management System =====")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    # Add contact
    if choice == 1:

        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        contact = {
            "Name": name,
            "Phone": phone
        }

        contacts.append(contact)

        print("Contact added successfully!")

    # Update contact
    elif choice == 2:

        search_name = input("Enter name to update: ")

        found = False

        for contact in contacts:

            if contact["Name"] == search_name:

                new_phone = input("Enter new phone number: ")

                contact["Phone"] = new_phone

                found = True

                print("Contact updated successfully!")

        if not found:
            print("Contact not found!")

    # Search contact
    elif choice == 3:

        search_name = input("Enter name to search: ")

        found = False

        for contact in contacts:

            if contact["Name"] == search_name:

                print(contact)

                found = True

        if not found:
            print("Contact not found!")

    # Delete contact
    elif choice == 4:

        search_name = input("Enter name to delete: ")

        found = False

        for contact in contacts:

            if contact["Name"] == search_name:

                contacts.remove(contact)

                found = True

                print("Contact deleted successfully!")

                break

        if not found:
            print("Contact not found!")

    # Exit
    elif choice == 5:

        print("Exiting Contact Management System...")
        break

    else:
        print("Invalid Choice!")

# Expected Output
"""
===== Contact Management System =====
1. Add Contact
2. Update Contact
3. Search Contact
4. Delete Contact
5. Exit
"""