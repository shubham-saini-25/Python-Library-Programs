# Required Module:- pip install qrcode

import qrcode

# Enter Data for QR code
data = "Hello Python Developers"

# Creting QR code
img = qrcode.make(data)

# Save the  file
img.save('QRCode.png')