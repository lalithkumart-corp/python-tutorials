
# Refererred from ggogle page: https://github.com/kk7nc/Text_Classification
# 
from nltk.tokenize import word_tokenize

def doTextTokenization():
    text = "After sleeping for four hours, he decided to sleep for another four"
    print(text)
    tokens = word_tokenize(text)
    print(tokens)