# Get range input from the user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Lists to store even and odd squares
even_squares = []
odd_squares = []

# Loop through the range and compute squares
for num in range(start, end + 1):
    square = num * num
    if square % 2 == 0:
        even_squares.append(square)
    else:
        odd_squares.append(square)

# Print results
print("Even squares:", even_squares)
print("Odd squares:", odd_squares)
