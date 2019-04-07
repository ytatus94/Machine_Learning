# The dataset that we are going to use for this article can be downloaded from the Cornell Natural Language Processing Group
# http://www.cs.cornell.edu/people/pabo/movie-review-data/review_polarity.tar.gz

'''
Following are the steps required to create a text classification model in Python:

1. Importing Libraries
2. Importing The dataset
3. Text Preprocessing
4. Converting Text to Numbers
5. Training and Test Sets
6. Training Text Classification Model and Predicting Sentiment
7. Evaluating The Model
8. Saving and Loading the Model
'''

# Importing Libraries
import numpy as np
import re
import nltk
from sklearn.datasets import load_files
import pickle
from nltk.corpus import stopwords

# Importing the Dataset
movie_data = load_files(r'/Users/ytshen/Desktop/review_polarity/txt_sentoken')
X, y = movie_data.data, movie_data.target

# Text Preprocessing
documents = []

from nltk.stem import WordNetLemmatizer

stemmer = WordNetLemmatizer()

for sen in range(0, len(X)):
    # Remove all the special characters
    document = re.sub(r'\W', ' ', str(X[sen]))

    # Remove all single characters
    document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)

    # Removing single characters from the start
    document = re.sub(r'\^[a-zA-Z]\s+', ' ', document)

    # Substituting multiple spaces with single space
    document = re.sub(r'\s+', ' ', document, flags=re.I)

    # Removing prefixed 'b'
    document = re.sub(r'^b\s+', '', document)

    # Converting to Lowercase
    document = document.lower()

    # Lemmatization
    document = document.split()

    document = [stemmer.lemmatize(word) for word in document]

    document = ' '.join(document)

    documents.append(document)

# Bag of Words
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(max_features=1500, min_df=5, max_df=0.7, stop_words=stopwords.words('english'))

X = vectorizer.fit_transform(documents).toarray()

# Finding TFIDF
# Term frequency (TF) = (Number of Occurrences of a word) / (Total words in the document)
# Inverse Document Frequency (IDF) = Log((Total number of document) / (Number of documents containing the word))

from sklearn.feature_extraction.text import TfidfTransformer

Tfidfconverter = TfidfTransformer()

X = Tfidfconverter.fit_transform(X).toarray()

# Convert text documents into TFIDF directly
from sklearn.feature_extraction.text import TfidfVectorizer

TfidfVectorizer = TfidfVectorizer(max_features=1500, min_df=5, max_df=0.7, stop_words=stopwords.words('english'))

X2 = TfidfVectorizer.fit_transform(documents).toarray()

# Training and Testing Sets

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Model

from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=1000, random_state=0)

classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

# Evaluating the Model

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
print(accuracy_score(y_test, y_pred))

# Saving and Loading the Model

with open('text_classifier', 'wb') as picklefile:
    pickle.dump(classifier, picklefile)

with open('text_classifier', 'rb') as training_model:
    model = pickle.load(training_model)

y_pred2 = model.predict(X_test)

print(confusion_matrix(y_test, y_pred2))
print(classification_report(y_test, y_pred2))
print(accuracy_score(y_test, y_pred2))