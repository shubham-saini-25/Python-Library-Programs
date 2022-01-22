# Required Module:- pip install pywhatkit

import pywhatkit

# Give your text here
text = "Python_with_Shubham"

# convert text into handwritig
pywhatkit.text_to_handwriting(text, save_to="handwriting.png")

# print message
print("Your Text Successfully Converted into Handwriting.")