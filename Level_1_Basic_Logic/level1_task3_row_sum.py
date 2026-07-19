# Level 1 - Task 3
# Calculate the sum of each row

grid = []

print("Enter 9 numbers for the 3x3 grid:")

for i in range(3):
    row = []

    for j in range(3):
        num = int(input(f"Enter number at row {i+1}, column {j+1}: "))
        row.append(num)

    grid.append(row)

print("\nRow Sums:")

for i in range(3):
    row_sum = 0

    for num in grid[i]:
        row_sum += num

    print(f"Sum of Row {i+1}: {row_sum}")
input("\nPress Enter to exit...")
