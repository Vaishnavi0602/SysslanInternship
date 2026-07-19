grid = []

print("Enter 9 numbers:")

for i in range(3):
    row = []
    for j in range(3):
        num = int(input(f"Enter element [{i+1}][{j+1}]: "))
        row.append(num)
    grid.append(row)

print("\n3×3 Number Grid:")
for row in grid:
    print(*row)

input("\nPress Enter to exit...")