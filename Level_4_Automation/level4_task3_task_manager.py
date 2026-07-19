while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")

        file = open("tasks.txt", "a")
        file.write(task + "\n")
        file.close()

        print("Task Saved!")

    elif choice == "2":
        try:
            file = open("tasks.txt", "r")

            print("\nYour Tasks:")
            print("------------")

            for line in file:
                print(line.strip())

            file.close()

        except FileNotFoundError:
            print("No tasks found.")

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid Choice")