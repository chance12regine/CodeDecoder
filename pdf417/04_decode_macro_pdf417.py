#!/usr/bin/env python3
"""
PDF417 decoder for Image-01.png
Requirements:
    pip install opencv-python pyzbar
"""

import cv2
from pyzbar.pyzbar import decode, ZBarSymbol
import sys
from pathlib import Path

# -------------------------------------------------
# Configuration
# -------------------------------------------------
IMAGE_PATH = Path("image1.png")   # <-- put your image here
SHOW_IMAGE = True                   # set False to run head-less

# -------------------------------------------------
# Helper: enhance contrast (optional but helps)
# -------------------------------------------------
def enhance_image(img):
    """Simple contrast stretch + slight blur to reduce noise."""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Histogram equalization (CLAHE)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    equalized = clahe.apply(gray)

    # Optional: mild Gaussian blur to smooth speckles
    blurred = cv2.GaussianBlur(equalized, (3, 3), 0)
    return blurred

# -------------------------------------------------
# Main decoding routine
# -------------------------------------------------
def decode_pdf417(image_path):
    if not image_path.exists():
        print(f"Error: Image not found: {image_path}")
        sys.exit(1)

    img = cv2.imread(str(image_path))
    if img is None:
        print("Error: Could not read the image (check file format).")
        sys.exit(1)

    # Enhance for better detection
    processed = enhance_image(img)

    # Decode – restrict to PDF417 only (faster & avoids false positives)
    barcodes = decode(processed, symbols=[ZBarSymbol.PDF417])

    if not barcodes:
        print("No PDF417 barcode detected.")
        if SHOW_IMAGE:
            cv2.imshow("Processed image (no barcode)", processed)
            cv2.waitKey(0)
        return

    # Usually there is only one PDF417 on a driver’s license / ID
    for barcode in barcodes:
        data = barcode.data.decode("utf-8")
        print("\n--- PDF417 decoded successfully! ---")
        print(data)

        # Optional: draw a green rectangle around the barcode
        if SHOW_IMAGE:
            (x, y, w, h) = barcode.rect
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, "PDF417", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    if SHOW_IMAGE:
        cv2.imshow("Original + detection", img)
        cv2.imshow("Enhanced (grayscale)", processed)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# -------------------------------------------------
# Run
# -------------------------------------------------
if __name__ == "__main__":
    decode_pdf417(IMAGE_PATH)