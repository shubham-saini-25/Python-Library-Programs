# importing tkinter module and choosecolor package

from tkinter import *
from tkinter import colorchooser

root = Tk()
root.geometry("150x150")

# create a function to choose color
def choose_color():
    
	color_code = colorchooser.askcolor(title ="Choose color")
	print(color_code)

# Create Button
Button(root, text = "Select color",command = choose_color).pack(pady= 30)

root.mainloop()