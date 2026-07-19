while True:
    try:
        n = int(input("Enter the number of terms: "))

        if n <= 0:
            print("Please enter a positive integer.")
            continue

        break

    except ValueError:
        print("Invalid input! Please enter numbers only.")

a, b = 0, 1

print("\nFibonacci Sequence:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
input("\nPress Enter to exit...")