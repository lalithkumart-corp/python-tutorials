import pandas as pd
import nltk
from bs4 import BeautifulSoup
import string
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

def readAndPreprocess():
    theData = pd.read_csv('amazon_co-ecommerce_sample.csv')
    #df.shape()
    theData.dropna(inplace = True) #It will remove a row if any of its column value is null
    print('--------------')
    print(theData.head())
    print('--------------')
    print(theData.shape)
    print('--------------')
    print(type(theData["product_name"]))#print(theData["uniq_id"].str.split(" ", n = 1, expand = True))
    print('--------------')
    print(pd.Series(theData["product_name"]))
    print('--------------')
    print(pd.Series(theData["product_name"])[0])
    # print('--------------')
    # print(pd.array(theData))
