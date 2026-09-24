#import nltk
from nltk.tokenize import word_tokenize

#nltk.download('punkt')
# nltk.download('punkt_tab')

text = "Welcome to NLTK tokenization example."

tokens = word_tokenize(text)

print(tokens)