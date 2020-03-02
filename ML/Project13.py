from string import punctuation , digits
import numpy as np


def extract_words(input_string):
    """
    Helper function for bag_of_words()
    Inputs a text string
    Returns a list of lowercase words in the string.
    Punctuation and digits are separated out into their own words.
    """
    for c in punctuation + digits:
        input_string = input_string.replace(c, ' ' + c + ' ')

    return input_string.lower().split()
#pragma: coderesponse end


#pragma: coderesponse template
def bag_of_words(texts):
    """
    Inputs a list of string reviews
    Returns a dictionary of unique unigrams occurring over the input

    Feel free to change this code as guided by Problem 9
    """
    # Your code here
    dictionary = {} # maps word to unique index
    with open("C:\Users\PradeepP\Documents\Masssssss\RandomStuff\ML\Home Work 1\sentiment_analysis\stopwords.txt", 'r') as myfile:
        stopwords1 = myfile.read()
    stopwordlist = extract_words(stopwords1) 

    for word in stopwordlist:
            while word in texts:
                try:
                    texts.remove(word)  
                except:
                    pass 

    for text in texts:
        word_list = extract_words(text)
        
        for word in word_list:
            if word not in dictionary:
                dictionary[word] = len(dictionary)
    return dictionary