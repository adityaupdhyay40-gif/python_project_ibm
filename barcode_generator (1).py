import barcode
from barcode.writer import ImageWriter

# Input data
number = input("Enter Barcode Number: ")

# Barcode type
code128 = barcode.get_barcode_class('code128')

# Generate barcode
my_barcode = code128(number, writer=ImageWriter())

# Save barcode image
my_barcode.save("generated_barcode")

print("Barcode Generated Successfully")