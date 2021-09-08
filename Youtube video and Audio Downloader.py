# Required Module:- pip install youtube_dl

# Download any Youtube Video
import youtube_dl

link = input("Enter Video Link Here: ")

with youtube_dl.YoutubeDL() as ydl:
    ydl.download([link])

############################################

# Download Audio from Youtube video
from youtube_dl import YoutubeDL

audio = YoutubeDL({'format':'bestaudio'})

link = input("Enter Video Link Here: ") 

audio.extract_info(link)