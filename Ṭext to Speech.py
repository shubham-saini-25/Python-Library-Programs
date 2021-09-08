# Required Module:- pip install gTTS

from gtts import gTTS
import os

# Enter your text here
audio_text = "Hello Python Programmers"

audio = gTTS(text=audio_text, lang='en', slow=False)

# Save the converted audio file 
audio.save("audio.mp3")

# Playing the converted file
os.system("audio1.mp3")