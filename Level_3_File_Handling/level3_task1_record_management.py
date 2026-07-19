# Simple Student Record Management System

records = []

while True:
    print("\n1. Add Record")
    print("2. View Records")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = input("Enter student marks: ")

        student = {
            "Name": name,
            "Marks": marks
        }

        records.append(student)
        print("Record Added Successfully!")

    elif choice == "2":
        print("\nStudent Records")

        for student in records:
            print(student)

    elif choice == "3":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")