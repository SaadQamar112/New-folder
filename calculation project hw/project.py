# Program to count the number of digits in an integer using a while loop

# Get input from the user and convert it to an integer
num = int(input("Enter an integer: "))

# Handle negative numbers
num = abs(num)

# Initialize digit count
count = 0

# Special case for 0
if num == 0:
    count = 1
else:
    # Use while loop to count digits
    while num > 0:
        num = num // 10
        count += 1

print("Number of digits:", count)
