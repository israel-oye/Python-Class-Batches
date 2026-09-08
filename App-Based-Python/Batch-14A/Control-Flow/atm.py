print("----------ATM------------------")

PIN = '1234'
main_balance = 0.0

user_pin = input("Enter your pin: ")
if user_pin != PIN:
    print("Invalid pin...")
else:
    print("Welcome user...")
    while True:
        option = input("1️⃣. Check Balance\n2️⃣. Deposit\n3️⃣. Withdraw\n4️⃣. Exit\nOption: ")

        if option == '1':
            print(f"Bal: ₦{main_balance:.2f}\n")
        elif option == '2':
            amount = float(input("Enter amount: "))
            main_balance += amount
            print(f"Credit: ₦{amount:.2f}\tBal: ₦{main_balance:.2f}\n")
        elif option == '3':
            withdrawal_amount = float(input("How much do you want to withdraw? "))
            if withdrawal_amount > main_balance:
                print("INSUFFICIENT FUNDS...\n")
            else:
                main_balance -= withdrawal_amount
                print(f"Debit ₦{withdrawal_amount:.2f}\tBal: ₦{main_balance:.2f}\n")
        elif option == '4':
            print("Exiting...")
            break
        else:
            print("Invalid input. Enter between 1️⃣-4️⃣")