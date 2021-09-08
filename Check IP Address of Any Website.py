# Get IP Adress of any Website

import socket

# Give website link here
website_url = "google.com"

# Found IP Address of above given website
IP_Adress = socket.gethostbyname(website_url)

# Print IP Adress of Given website
print("IP Adress is: ", IP_Adress)