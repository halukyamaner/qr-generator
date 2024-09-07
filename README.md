# QR Generator
## Overview

QR Generator is a Python library designed to quickly create QR codes from any text or URL. It simplifies the process of QR code generation with easy customization options, making it ideal for applications ranging from marketing to event management. The library outputs high-quality PNG files, suitable for both digital and print media.

## Features

- **Direct Input Conversion**: Transforms text or URLs directly into QR codes, facilitating easy data embedding.
- **Customizable Options**: Allows users to adjust QR code size, error correction level, and colors to suit specific needs.
- **High-Quality Output**: Produces PNG files that maintain clarity even at large sizes or when printed.
- **Detailed Logging**: Logs each step of the QR code generation process, useful for debugging and ensuring quality.
- **Error Handling**: Effectively manages exceptions and errors, providing clear feedback and instructions to resolve common issues.

## Requirements

- Python 3.x
- `qrcode` library (version 6.1 or higher)
- `Pillow` library for image processing

## Usage

To generate a QR code using the QR Generator library, follow these steps:

```python
from qr_generator import QRGenerator

# Create an instance of QRGenerator
qr = QRGenerator()

# Input the data and specify the filename for the output
data = "https://www.example.com"
filename = "exampleQR"

# Generate and save the QR code
qr.generate(data, filename)
qr.save(f"{filename}.png")
