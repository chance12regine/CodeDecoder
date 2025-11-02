from pyzbar.pyzbar import decode
from PIL import Image

# Load the image
image = Image.open("barcode.png")  # change to your image path

# Decode the barcode
decoded_objects = decode(image)

# Print the result
if decoded_objects:
    for obj in decoded_objects:
        print("Type:", obj.type)
        print("Data:", obj.data.decode("utf-8"))
else:
    print("No barcode detected.")
