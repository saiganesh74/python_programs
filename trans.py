import string
text = "Hello, World! How are you today? #feelinggood"
translator = str.maketrans('', '', string.punctuation)
no_punct = text.translate(translator)
print(no_punct)