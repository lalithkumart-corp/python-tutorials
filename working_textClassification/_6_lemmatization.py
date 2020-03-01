from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

def doLemmatization():
    print(lemmatizer.lemmatize("cats"))