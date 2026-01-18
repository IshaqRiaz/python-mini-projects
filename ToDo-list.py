# simple Python console-based To-Do List app. Users can view, add, and remove tasks through an interactive menu. The program displays tasks with numbering, prevents errors when the list is empty, and offers options to quit anytime. Lightweight and beginner-friendly project.

# Initialize an empty ToDo list
todo_list = []

# Run the program in an infinite loop until the user chooses to quit
while True:
    # Check if the ToDo list is empty
    if len(todo_list) == 0:
        print("Your ToDo list is empty:")
    else:
        # Print all tasks with their index numbers
        index = 1
        for task in todo_list:
            print(f"{index}. {task}")
            index += 1

    # Display menu options to the user
    print("Options:")
    print("1) Add Task")
    print("2) Remove Task")
    print("3) Quit")

    # Take input from the user for action
    choice = input("Please Choose 1, 2 or 3: ")

    # Option 1 → Add a new task
    if choice == "1":
        print("Adding Task")
        new_task = input("Enter the task: ")
        todo_list.append(new_task)  # Add the entered task to the list
        print("Task has been added")

    # Option 2 → Remove the last task from the list
    elif choice == "2":
        print("Removing Task")
        if len(todo_list) > 0:
            remove_task = todo_list.pop()  # Removes the last added task (LIFO order)
            print(f"Task '{remove_task}' has been removed")
        else:
            print("ToDo list is empty, nothing to remove")

    # Option 3 → Exit the program
    elif choice == "3":
        print("Quitting")
        break  # Exit the while loop and end the program

    # If user enters an invalid option
    else:
        print("Invalid choice, please try again")
