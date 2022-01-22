# Get the Source Code of any website

import requests

url = "https://google.com/"

req = requests.get(url, 'html.parser')

with open("website_code.txt", 'w') as f:
    f.write(req.text)
    f.close()
    