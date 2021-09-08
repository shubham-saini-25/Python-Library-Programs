# 1. Required Module:- pip install requests
# 2. Required Module:- pip install bs4

import requests
from bs4 import BeautifulSoup

search = input("Enter a City Name: ")

url = f"https://www.google.com/search?&q=weather+in+{search}"

r = requests.get(url)

s = BeautifulSoup(r.text, "html.parser")

weather = s.find("div", class_="BNeawe").text

print(f"The Current Temperature of {search} is:", weather) 