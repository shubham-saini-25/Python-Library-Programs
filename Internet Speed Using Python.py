# Required Module:- pip install speedtest-cli

import speedtest

spd = speedtest.Speedtest()

down_spd = spd.download()

up_spd = spd.upload()

# Display Your Download Speed
print("Your Download Speed is:", down_spd) 

# Display Your Upload Speed
print("Your Upload Speed is:", up_spd)