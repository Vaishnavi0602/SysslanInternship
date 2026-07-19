filename = "notes.txt"

while True:
    print("\n===== PERSONAL NOTES MANAGER =====")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Search Note")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        note = input("Enter your note: ")

        with open(filename, "a") as file:
            file.write(note + "\n")

        print("Note saved successfully!")

    elif choice == "2":
        try:
            with open(filename, "r") as file:
                notes = file.readlines()

                if not notes:
                    print("No notes available.")
                else:
                    print("\nYour Notes:")
                    for i, note in enumerate(notes, start=1):
                        print(f"{i}. {note.strip()}")

        except FileNotFoundError:
            print("No notes file found.")

    elif choice == "3":
        keyword = input("Enter keyword to search: ")

        try:
            found = False

            with open(filename, "r") as file:
                for note in file:
                    if keyword.lower() in note.lower():
                        print(note.strip())
                        found = True

            if not found:
                print("No matching note found.")

        except FileNotFoundError:
            print("No notes file found.")

    elif choice == "4":
        print("Thank you! Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")