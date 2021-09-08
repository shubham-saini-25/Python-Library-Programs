# Import the os Module
import os

# print the options
print("1. Shutdown Your Computer.")
print("2. Restart Your Computer.")

choice = int(input())

if choice == 1:
    # It Shutdown your Computer
    os.system("shutdown /s /t 1")
    
elif choice == 2:
    # It Restart your Computer
    os.system("shutdown /r")