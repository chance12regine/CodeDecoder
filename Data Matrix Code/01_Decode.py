from pylibdmtx.pylibdmtx import decode
from PIL import Image

# Load your Data Matrix image
image = Image.open("qrcode.png")

# Decode it
decoded = decode(image)

# Print result
if decoded:
    print(decoded[0].data.decode("utf-8"))
else:
    print("No Data Matrix code found.")
