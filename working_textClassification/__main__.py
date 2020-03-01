from _1_textTokenization import doTextTokenization
from _2_stopWords import removeStopWords
from _3_noiseRemoval import removeNoise
from _4_autoCorrect import doAutocorrectSomewords
from _5_stemming import doStemming
from _6_lemmatization import doLemmatization
from _dataPreprocessing import readAndPreprocess
class MyController:
    def initialize(self):
        print('=====TOKENIZATION=====')
        doTextTokenization() #1
        
        print('=====Removing stop Words=====')
        removeStopWords() #2
        
        print('=====Removing Noise=====')
        print(removeNoise("I have n't used <head>whatsapp</head>. Haven't been there. Hey! are you coming to party 2night?")) #3

        # print('=====AutoCorrection=====')
        # doAutocorrectSomewords()

        print('=====Stemming=====')
        doStemming()

        print('=====Lemmatization====')
        #doLemmatization()

        print('=====Data Preprocessing=====')
        readAndPreprocess()

if __name__ == '__main__':
    ctlr = MyController()
    ctlr.initialize()