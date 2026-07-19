filename = input("Enter file name: ")

try:
    numbers = []

    with open(filename, "r") as file:
        for line in file:
            try:
                num = float(line.strip())
                numbers.append(num)
            except ValueError:
                print(f"Invalid data skipped: {line.strip()}")

    if len(numbers) == 0:
        print("No valid numbers found in the file.")
    else:
        total = sum(numbers)
        average = total / len(numbers)
        maximum = max(numbers)

        print("\nResults")
        print("Total   :", total)
        print("Average :", average)
        print("Maximum :", maximum)

except FileNotFoundError:
    print("Error: File not found.")
input("\nPress Enter to exit...")
