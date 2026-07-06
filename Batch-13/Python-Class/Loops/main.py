print("Welcome to App")

while True:
    user_option = int(input("1. Display\n2. Exit\nOption: "))

    if user_option == 1:
        print("Displaying...")
    elif user_option == 2:
        print("Exiting...")
        break
    else:
        print("Invalid option.")