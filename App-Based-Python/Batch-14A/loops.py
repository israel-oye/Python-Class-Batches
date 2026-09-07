print("App")

items = ['ball', 'soap', 'plate', 'perfume']

while True:
    option = input("1. View Items\n2. Add Items\n3. Quit\nEnter: ")

    if option == '1':
        print(f"All items:...\n{items}\n")
    elif option == '2':
        new_item = input("Add item: ")
        items.append(new_item)
        print(f"Added <{new_item}>\n")
    elif option == '3':
        print("Exiting...\n")
        break
    else:
        print("Invalid Option\n")