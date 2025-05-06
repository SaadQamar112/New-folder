# Input for number of rows
rows = int(input("Enter the number of rows: "))

# Loop to print the triangle
for i in range(1, rows + 1):
    # Print spaces first
    for j in range(rows - i):
        print(" ", end="")
    # Print stars
    for k in range(i):
        print("*", end="")
    print()  # New line after each row
