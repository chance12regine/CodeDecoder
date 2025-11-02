from pyzbar.pyzbar import decode
from PIL import Image

# Load your MaxiCode image
image = Image.open("maxicode.png")  # replace with your image path

# Decode the barcode
decoded_objects = decode(image)

# Display the decoded info
if decoded_objects:
    for obj in decoded_objects:
        print("Type:", obj.type)
        print("Data:", obj.data.decode("utf-8"))
else:
    print("No MaxiCode detected.")
