from pyzbar.pyzbar import decode
from PIL import Image

# Load the QR image
image = Image.open("qrcode.png")

# Decode it
decoded_objects = decode(image)

# Print all detected codes
if decoded_objects:
    for obj in decoded_objects:
        print("Type:", obj.type)
        print("Data:", obj.data.decode("utf-8"))
else:
    print("No QR code detected.")
