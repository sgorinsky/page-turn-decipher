import ssl
from nltk.corpus import words, stopwords

ssl._create_default_https_context = ssl._create_unverified_context

# Set of stop words from nltk
stop_words = set(stopwords.words('english'))
# Set of valid words from nltk
valid_words = set(words.words())
