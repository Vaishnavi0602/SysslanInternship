# Level 1 - Task 2
# Check whether a number exists in the grid

grid = []

print("Enter 9 numbers for the 3x3 grid:")

for i in range(3):
    row = []

    for j in range(3):
        num = int(input(f"Enter number at row {i+1}, column {j+1}: "))
        row.append(num)

    grid.append(row)

search_num = int(input("\nEnter the number to search: "))

found = False

for row in grid:
    for num in row:
        if num == search_num:
            found = True

if found:
    print("Number found in the grid.")
else:
    print("Number not found in the grid.")
input("\nPress Enter to exit...")