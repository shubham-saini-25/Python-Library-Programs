# Python Program to Get IP Address

import socket

Hostname = socket.gethostname()

IP_Address = socket.gethostbyname(Hostname)

print("Your Computer Name is: ", Hostname)

print("Your Computer IP Address is: ", IP_Address)

# Output:-
# Hostname: DESKTOP-A0PM5GD
# IP Address: 192.168.43.15