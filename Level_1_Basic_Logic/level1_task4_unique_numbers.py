# Level 1 - Task 4
# Check if all numbers are unique

grid = []

print("Enter 9 numbers for the 3x3 grid:")

for i in range(3):
    row = []

    for j in range(3):
        num = int(input(f"Enter number at row {i+1}, column {j+1}: "))
        row.append(num)

    grid.append(row)

all_numbers = []

for row in grid:
    for num in row:
        all_numbers.append(num)

unique = True

for i in range(len(all_numbers)):
    for j in range(i + 1, len(all_numbers)):
        if all_numbers[i] == all_numbers[j]:
            unique = False

if unique:
    print("All numbers in the grid are unique.")
else:
    print("Duplicate numbers found in the grid.")
input("\nPress Enter to exit...")
