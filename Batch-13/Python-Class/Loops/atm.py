# ATM
pin = "1234"
balance = 300.5

user_pin = input("Enter PIN: ")

if user_pin == pin:
    while True:
        selected_menu = input("Menu\n1. Withdraw\n2. View balance\n3. Exit\nOption: ")

        if selected_menu == "1":
            amount_to_withdraw = float(input("How much to withdraw: "))
            if amount_to_withdraw > balance:
                print("INSUFFICIENT FUNDS...\n")
            else:
                balance -= amount_to_withdraw
                print(f"Withdrew: ₦{amount_to_withdraw}\tBal: ₦{balance:.2f}\n")
        elif selected_menu == "2":
            print(f"Bal: ₦{balance:.2f}\n")
        elif selected_menu == "3":
            print("Exiting ATM. Thanks for banking with Nexus")
            break
        else:
            print("Invalid menu selected. Enter 1, 2, 3: ")
else:
    print("Invalid PIN.")
