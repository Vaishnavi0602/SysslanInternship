import csv

filename = input("Enter file name: ")

try:
    with open(filename, "r") as file:
        print("\nStudent Records:\n")

        for line in file:
            print(line.strip())

except FileNotFoundError:
    print("File not found.")
except FileNotFoundError:
    print("Error: File not found.")

except Exception as e:
    print("Error:", e)
input("\nPress Enter to exit...")