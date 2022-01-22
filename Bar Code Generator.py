# Required Module:- pip install python-barcode

from barcode import EAN13
from barcode.writer import ImageWriter
import random

# Pass a number for Barcode
bar_num = str(random.randint(149894280329384, 948278712938723))

# pass the number with the ImageWriter() 
my_code = EAN13(bar_num, writer = ImageWriter())

# save the Barcode
my_code.save("my_barcode")

# Print the Message
print("Your BarCode Saved Successfully.")