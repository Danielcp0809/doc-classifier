import nltk

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

from sklearn.feature_extraction.text import TfidfVectorizer

def preprocess_text(text):
    # Lowercase
    text = text.lower()

    # Punctuation removal
    text = ''.join([char for char in text if char.isalnum() or char.isspace()])

    # Tokenization
    tokens = word_tokenize(text)

    # Stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    # Lematización
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatizer(word) for word in tokens]

    return ' '.join(tokens)

def tokenize(docs):
    vectorizer = TfidfVectorizer();
    vectors = vectorizer.fit_transform(docs)

    # return the vectors and the vocabulary
    return vectors, vectorizer.vocabulary_
    