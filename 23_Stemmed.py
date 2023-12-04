from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

stemmer = PorterStemmer()

sentence = "He was running very fast, but he was still tired."

tokens = word_tokenize(sentence)

stemmed_tokens = [stemmer.stem(token) for token in tokens]

stemmed_sentence = " ".join(stemmed_tokens)

print("Original sentence:", sentence)
print("Stemmed sentence:", stemmed_sentence)
