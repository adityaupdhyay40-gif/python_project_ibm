import qrcode

# Data to store
text = input("Enter text for QR Code: ")

# Generate QR
img = qrcode.make(text)

# Save image
img.save("generated_qr.png")

print("QR Code Generated Successfully")