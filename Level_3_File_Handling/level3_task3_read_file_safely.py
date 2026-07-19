filename = input("Enter the file name: ")

try:
    with open(filename, "r") as file:
        print("\nFile Contents:\n")

        for line in file:
            print(line.strip())

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied to access the file.")

except Exception as e:
    print("An unexpected error occurred:", e)
input("\nPress Enter to exit...")
