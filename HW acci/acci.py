# Take character input
char = input("Enter a single character: ")

# Check if it's a single character
if len(char) != 1:
    print("Please enter only ONE character.")
else:
    ascii_value = ord(char)
      # Get ASCII value
    print("Character:", char)
    print("ASCII Value:", ascii_value)

    # Check type of character
    if char.isalpha():
        print("It's a letter.")
        if char.isupper():
            print("It's an uppercase letter.")
        elif char.islower():
            print("It's a lowercase letter.")
    elif char.isdigit():
        print("It's a digit.")
    else:
        print("It's a special character or symbol.")
