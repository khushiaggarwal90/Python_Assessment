# Menu-Driven Banking Application

# Initial balance
balance = 0

# Infinite loop until user chooses Exit
while True:

    # Displaying menu options
    print("\n===== Banking Menu =====")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Exit")

    # Taking user choice
    choice = int(input("Enter your choice: "))

    # Deposit operation
    if choice == 1:

        deposit_amount = float(input("Enter amount to deposit: "))
        balance += deposit_amount

        print("Amount Deposited Successfully!")
        print("Updated Balance:", balance)

    # Withdraw operation
    elif choice == 2:

        withdraw_amount = float(input("Enter amount to withdraw: "))

        if withdraw_amount <= balance:
            balance -= withdraw_amount

            print("Withdrawal Successful!")
            print("Remaining Balance:", balance)

        else:
            print("Insufficient Balance!")

    # Check balance
    elif choice == 3:

        print("Current Balance:", balance)

    # Exit application
    elif choice == 4:

        print("Thank You for Using Banking Application!")
        break

    # Invalid choice
    else:
        print("Invalid Choice! Please Try Again.")

# Expected Output
"""
===== Banking Menu =====
1. Deposit Money
2. Withdraw Money
3. Check Balance
4. Exit

Enter your choice: 1
Enter amount to deposit: 5000

Amount Deposited Successfully!
Updated Balance: 5000
"""