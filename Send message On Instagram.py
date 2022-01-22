# required Module:- pip install instabot

# import Bot from instabot library
from instabot import Bot

bot = Bot()

# enter the username and password of Sender
bot.login(username="Username", password="Password")

# enter the message and Reciever name
bot.send_message("Hello Buddy", ["Receiver's Username"])