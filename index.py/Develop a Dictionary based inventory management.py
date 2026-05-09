# Inventory Management System using Dictionary

# Dictionary to store inventory
inventory = {}

while True:

    # Displaying menu
    print("\n===== Inventory Menu =====")
    print("1. Add Product")
    print("2. Update Quantity")
    print("3. Search Product")
    print("4. Display Low Stock Items")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    # Add Product
    if choice == 1:

        product = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))

        inventory[product] = quantity

        print("Product added successfully!")

    # Update Quantity
    elif choice == 2:

        product = input("Enter product name: ")

        if product in inventory:

            quantity = int(input("Enter new quantity: "))
            inventory[product] = quantity

            print("Quantity updated successfully!")

        else:
            print("Product not found!")

    # Search Product
    elif choice == 3:

        product = input("Enter product name to search: ")

        if product in inventory:
            print(product, "Quantity:", inventory[product])

        else:
            print("Product not found!")

    # Display Low Stock Items
    elif choice == 4:

        print("\nLow Stock Items (Quantity less than 5):")

        for product, quantity in inventory.items():

            if quantity < 5:
                print(product, ":", quantity)

    # Exit
    elif choice == 5:

        print("Exiting Inventory System...")
        break

    else:
        print("Invalid Choice!")

# Expected Output
"""
===== Inventory Menu =====
1. Add Product
2. Update Quantity
3. Search Product
4. Display Low Stock Items
5. Exit
"""