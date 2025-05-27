import math

# Get input from the user
angle_degrees = float(input("Enter the angle in degrees: "))

# Convert degrees to radians
angle_radians = math.radians(angle_degrees)

# Calculate sin, cos, and tan
sin_value = math.sin(angle_radians)
cos_value = math.cos(angle_radians)
tan_value = math.tan(angle_radians)

# Display the results
print(f"sin({angle_degrees}) = {sin_value}")
print(f"cos({angle_degrees}) = {cos_value}")
print(f"tan({angle_degrees}) = {tan_value}")
