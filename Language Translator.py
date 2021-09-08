# Required Module:- pip install translate

from translate import Translator

Text = input("Enter Your Text: ")

# fr = french
translator = Translator(to_lang="fr")

translation = translator.translate(Text)

print("Translated Text: ", translation)

# OUTPUT:-
# Enter Your Text: hello
# Translated Text:  salut