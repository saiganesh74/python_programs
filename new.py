from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
text = 'running , runner , ran'
words = text.split(",")
stemmed_words = [stemmer.stem(word) for word in words ]
text = ".".join()
print(text)