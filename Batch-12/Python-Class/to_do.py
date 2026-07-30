tasks = ["wash the car", "eat the door", "read a pot"]
# Create a To-do list application with the following menu options
while True:
    print("\nOptions:\n1-Add\n2-Remove\n3-View All tasks\n0-Exit\n")
    choice = input("Select an option: ")
    if choice == "1":
        new_task = input("Enter a task: ")
        tasks.append(new_task)
        print("Added task\n")
    elif choice == "2":
        index_to_be_removed = int(input("Enter the S/N of the task you want to delete")) - 1
        if 0 <= index_to_be_removed < len(tasks):
            removed_task = tasks.pop(index_to_be_removed)
            print(f"Removed '{removed_task}'\n")
        else:
            print(f"No task at No.{index_to_be_removed + 1}. Try again\n")
    elif choice == "3":
        print("Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task.title()}")
    elif choice == '0':
        print("Quitting...")
        import time
        time.sleep(1.5)
        break