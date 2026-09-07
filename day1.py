from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.stem import PorterStemmer



# User input
query = input("Enter sentence: ")

#1. tokenisation
token_word= word_tokenize(query, language="english", preserve_line=True) 
print("\nTokens: ", token_word)

#2 Stopwords
stopword =  stopwords.words('english')
print("\nStopwords: ", stopword)

#3. stemming
user = input("Enter a  word for Stemming and lemmatizing: ")
stemmer = PorterStemmer()
print("\nStemming: ", stemmer.stem(word=user, to_lowercase=True))

lemmatizer = WordNetLemmatizer()
word = lemmatizer.lemmatize(word=user)
print("\nLemmatizer: ",word)
