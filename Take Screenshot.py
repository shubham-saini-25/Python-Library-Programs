# Required Module:- pip install pyscreenshot

import pyscreenshot

try:
    image = pyscreenshot.grab()
    
    image.save("Pictures/ScreenShot.png")
    
    print("Your Screenshot Saved Successfully.")
    
except:
    print("Path Not Found.")