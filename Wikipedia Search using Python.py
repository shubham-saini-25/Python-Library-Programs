# Required Module:- pip install wikipedia

import wikipedia

# input search material from user
Text = input("Enter your Text: ")

# wikipidea find details about search
result = wikipedia.summary(Text) 
  
# printing the result
print(result)