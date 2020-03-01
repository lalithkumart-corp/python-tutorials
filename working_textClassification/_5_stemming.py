from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

def doStemming():
    ps = PorterStemmer()

    example_words = ["python","pythoner","pythoning","pythoned","pythonly", "batteries", "happier"]
    print(example_words)
    for w in example_words:
        print(ps.stem(w))