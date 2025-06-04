def calculate_product(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

# Example usage:
my_tuple = (2, 3, 4)
result = calculate_product(my_tuple)
print("Product of numbers in the tuple:", result)
