def calculate_circumference(radius):
    pi = 3.14159
    circumference = 2 * pi * radius
    return circumference

# Example usage:
r = float(input("Enter the radius of the circle: "))
result = calculate_circumference(r)
print("Circumference of the circle is:", result)
