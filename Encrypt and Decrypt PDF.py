# Required Module:- pip install pikepdf

########------ENCRYPT THE PDF------#############
import pikepdf

# Open the PDF
pdf = pikepdf.open("D:/My_Pdf.pdf")   

# Encrypt the Given PDF and make two different Passwords as Public Key & Private Key
encrypt =  pikepdf.Encryption(owner = "123456", user = "654321", R = 4)

# Save the Encrypted PDF
pdf.save('D:/Encrypted PDF.pdf', encryption = encrypt) 

# Print a Message
print("Your PDF Encrypted Successfully.")

# Close the PDF
pdf.close()

#*#*#*#*#*#*#*#*#*#*#*#*#*#**#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

########------DECRYPT THE PDF------#############
import pikepdf

# Open the encrypted PDF and Decrypt it using given Password
pdf = pikepdf.open('D:/hard.pdf', password='329890')

# Save the Decrypted PDF
pdf.save('D:/Decrypted PDF.pdf')

# Print a Message
print("Your PDF Decrypted Successfully.")