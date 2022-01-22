# Required Module:- pip install pyshorteners

import pyshorteners

# Enter your website URL here
url = "https://pythonwithshubham2021.blogspot.com/"

# apply shorting method
shortener = pyshorteners.Shortener()

# short the URL
shorted_url = shortener.tinyurl.short(url)

# print the shorted URL
print(shorted_url)

#### OUTPUT:-  
# => https://tinyurl.com/ye9hbuwy