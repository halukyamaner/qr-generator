"""
Library: QR Generator
Author: Haluk YAMANER
Email: haluk@halukyamaner.com
Web: https://www.halukyamaner.com
Version: 1.0

Description:
    QR Generator is a Python library designed to efficiently create QR codes from text or URLs. It simplifies the QR code generation process, making it accessible and customizable, ideal for both developers and non-technical users. With features like variable size, border, and error correction levels, QR Generator fits various applications, from ticketing systems to retail marketing.

Usage:
    To use QR Generator, input the desired text or URL and specify a file name for the output. The library handles encoding and error correction, producing a ready-to-use PNG file.

Requirements:
    Python 3.x
    qrcode>=6.1
    Pillow for image handling

Features:
    - Converts text or URLs directly into QR codes.
    - Allows customization of dimensions, error correction levels, and colors.
    - Outputs high-quality PNG files, suitable for print and digital use.
    - Detailed logging of the generation process aids in troubleshooting and validation.

Potential Use Cases:
    - Marketing tools where QR codes provide links to offers or product details.
    - Event ticketing systems where QR codes serve as digital entry passes.
    - Personal projects for fun or practical QR code applications.

Example:
    Below is a simple example of how to use the QR Generator library:

    from qr_generator import QRGenerator

    # Create an instance of QRGenerator
    qr = QRGenerator()

    # Generate QR code
    qr.generate("https://www.halukyamaner.com", "QRCode")

    # Save and check the QR code
    qr.save("QRCode.png")

    Run the script, and the QR code will be saved as 'QRCode.png'. Detailed output can be monitored in the log file for any steps performed.
"""
import qrcode

# Prompt user for the data to encode
data = input("Enter the text or link to encode in the QR code: ")
filename = input("Enter the filename to save the QR code image (without extension): ")
filename_with_extension = filename if filename.lower().endswith('.png') else filename + '.png'

qr = qrcode.QRCode(
    version=1,  # controls the size of the QR code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls the error correction used
    box_size=30,  # controls how many pixels each “box” of the QR code is
    border=1,  # controls how many boxes thick the border should be
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill='black', back_color='white')

# Save the image to a file with .png extension
img.save(filename_with_extension)

print(f"QR Code generated and saved as '{filename_with_extension}'")
