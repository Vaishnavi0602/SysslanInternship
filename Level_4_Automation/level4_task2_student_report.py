try:
    n = int(input("Enter the number of students: "))

    if n <= 0:
        print("Please enter a positive number.")

    else:
        print("\n----- Student Report -----")

        for i in range(n):
            print(f"\nStudent {i + 1}")

            name = input("Enter Name: ")

            while True:
                try:
                    marks = float(input("Enter Marks: "))

                    if marks < 0 or marks > 100:
                        print("Marks should be between 0 and 100.")
                        continue
                    break

                except ValueError:
                    print("Invalid input! Please enter numeric marks.")

            if marks >= 90:
                grade = "A"
            elif marks >= 75:
                grade = "B"
            elif marks >= 60:
                grade = "C"
            elif marks >= 40:
                grade = "D"
            else:
                grade = "F"

            print("Name :", name)
            print("Marks:", marks)
            print("Grade:", grade)

except ValueError:
    print("Invalid input! Please enter a valid number of students.")
input("\nPress Enter to exit...")
