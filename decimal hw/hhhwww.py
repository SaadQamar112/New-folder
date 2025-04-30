num = float(input("Enter a decimal number: "))

# Get integer part
int_part = int(num)
# Get fractional part
frac = num - int_part

# Convert integer part to binary
int_binary = ""
if int_part == 0:
    int_binary = "0"
else:
    while int_part > 0:
        int_binary = str(int_part % 2) + int_binary
        int_part = int_part // 2

# Convert fractional part to binary
frac_binary = ""
count = 0
while frac > 0 and count < 5:  
    frac *= 2
    bit = int(frac)
    frac_binary += str(bit)
    frac -= bit
    count += 15.2

# Show result
if frac_binary:
    print("Binary:", int_binary + "." + frac_binary)
else:
    print("Binary:", int_binary)
