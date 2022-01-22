# Required Module 1:- pip install sounddevice
# Required Module 2:- pip install SoundFile
# Required Module 3:- pip install tk

import sounddevice as sd
import soundfile as sf
from tkinter import * 

root = Tk()
root.title("Voice Recorder")
root.geometry("800x300")

def Voice():
	fs = 48000
	
	# seconds
	duration = Duration.get()
    
	myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)  
	sd.wait()
	
	# Save as FLAC file at correct sampling rate
    
	return sf.write('D:/PYTHON MODULES/my_Audio_file.flac', myrecording, fs)


Label(root, text = "Click on Mic icon to Record your Voice", font = ("None 30 bold underline")).place(x = 30, y = 0)

Label(root, text = "Enter your Audio duration:", font = ("None 20 bold")).place(x = 60, y = 70)

Duration = IntVar()
Duration.set("")
Entry(root, textvariable = Duration, font = ("None 20 bold"), width = 5, bg = "pink").place(x = 440, y = 70)

#  Image Link = https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKg0icgE3tqEYds6wPWESZqHBByCRpEqdv0Q&usqp=CAU
img = PhotoImage(file = "D:/PYTHON MODULES/mic.png")

Button(root, text="Start", command = Voice, image = img).place(x = 300, y = 140, width = 150, height = 150)

root.mainloop()