import cv2

# Load the image
image = cv2.imread("aztec.png")

# Initialize detector
detector = cv2.QRCodeDetector()

# Try decoding (it also supports Aztec Codes)
data, points, _ = detector.detectAndDecode(image)

if data:
    print("Aztec Code Data:", data)
else:
    print("No Aztec code detected.")
