balance = 5000  
pin = "1234"  
attempts =3

print("Welcome to Python ATM")

while attempts > 0:
    user_pin = input("Enter your 4-digit PIN: ")

    if user_pin == pin:
        print("\nLogin Successful")
        print("1. Balance Inquiry")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("\nEnter your choice (1-4): "))

        if choice == 1:
            print(f"Your current balance is ₹{balance}")

        elif choice == 2:
            amount = int(input("Enter deposit amount: "))
            balance += amount
            print(f"₹{amount} deposited successfully")
            print(f"Updated Balance: ₹{balance}")

        elif choice == 3:
            amount = int(input("Enter withdrawal amount: "))
            if amount <= balance:
                balance -= amount
                print(f"₹{amount} withdrawn successfully ")
                print(f"Remaining Balance: ₹{balance}")
            else:
                print("Insufficient Balance ")

        elif choice == 4:
            print("Thank you for using Python ATM ")
        
        else:
            print("Invalid Choice ")
        break   

    else:
        attempts -= 1
        if attempts > 0:
            print(f"Invalid PIN You have {attempts} attempt(s) left.")
        else:
            print("Account Locked Too many wrong attempts.")

