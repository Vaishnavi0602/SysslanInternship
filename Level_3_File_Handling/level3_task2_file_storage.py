# Save and Retrieve Records using File Handling

filename = "records.txt"

while True:
    print("\n===== MENU =====")
    print("1. Save Record")
    print("2. View Records")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        try:
            name = input("Enter Student Name: ")
            age = int(input("Enter Age: "))
            marks = float(input("Enter Marks: "))

            with open(filename, "a") as file:
                file.write(f"{name},{age},{marks}\n")

            print("Record saved successfully!")

        except ValueError:
            print("Invalid input! Please enter the correct data type.")

    elif choice == "2":
        try:
            with open(filename, "r") as file:
                records = file.readlines()

                if not records:
                    print("No records found.")
                else:
                    print("\n--- Student Records ---")
                    for record in records:
                        data = record.strip().split(",")

                        if len(data) == 3:
                            name, age, marks = data
                            print(f"Name : {name}")
                            print(f"Age  : {age}")
                            print(f"Marks: {marks}")
                            print("-" * 20)
                        else:
                            print("Invalid record:", record)

        except FileNotFoundError:
            print("No records file found.")
        except Exception as e:
            print("Error:", e)

    elif choice == "3":
        print("Exiting Program...")
        break

    else:
        print("Invalid choice! Please select between 1 and 3.")

input("\nPress Enter to exit...")