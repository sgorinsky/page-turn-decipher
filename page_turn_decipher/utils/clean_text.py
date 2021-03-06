import numpy as np

import spacy
import pandas as pd
import os
import re
import string

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer

from nltk import ngrams, FreqDist

from page_turn_decipher.utils.stopwords import stop_words, valid_words

# Only run this once, they will be downloaded.
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('words')
nltk.download('omw-1.4')

#functions used to process text and create the required TFIDF and text2vec Matrices
def clean_text(text):
    #split textument into individual words
    tokens = text.split()
    re_punc = re.compile('[%s]' % re.escape(string.punctuation))
    # remove punctuation from each word
    tokens = [re_punc.sub('', w) for w in tokens]
    # remove remaining tokens that are not alphabetic
    tokens = [word for word in tokens if word.isalpha()]
    # filter out short tokens
    tokens = [word for word in tokens if len(word) > 4]
    #lowercase all words
    tokens = [word.lower() for word in tokens]
    # filter out stop words and invalid words using lookup vars from previous cell
    tokens = [w for w in tokens if not w in stop_words and w in valid_words]
    # word stemming
    ps = PorterStemmer()
    tokens = [ps.stem(word) for word in tokens]
    # lemmatize
    wnl = WordNetLemmatizer()
    tokens = [wnl.lemmatize(token) for token in tokens]

    return ' '.join(tokens)
