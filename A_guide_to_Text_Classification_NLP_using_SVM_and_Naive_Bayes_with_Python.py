# https://medium.com/@bedigunjit/simple-guide-to-text-classification-nlp-using-svm-and-naive-bayes-with-python-421db3a72d34

# Step 1: Add the required libraries

import pandas as pd
import numpy as np

from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn

from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import model_selection, naive_bayes, svm
from sklearn.metrics import accuracy_score

from collections import defaultdict

# Step 2: Set random seed

np. random.seed(500)

# Step 3: Add Corpus

Corpus = pd.read_csv(r'corpus.csv', encoding='latin-1')

# Step 4: Data pre-processing

# a.) Remove blank rows if any
Corpus['text'].dropna(inplace=True)

# b.) Change all text to lower case
Corpus['text'] = [entry.lower() for entry in Corpus['text']]

# c.) Tokenization:
Corpus['text'] = [word_tokenize(entry) for entry in Corpus['text']]

# d.) Remove stop words, non-numeric and perform Word Stemming / Lemmenting

# WordNetLemmatizer requires POS tags to understand if the word is noun or verb or adjective etc.
# By default it is set to Noun
tag_map = defaultdict(lambda : wn.NOUN)
tag_map['J'] = wn.ADJ
tag_map['V'] = wn.VERB
tag_map['R'] = wn.ADV

for index, entry in enumerate(Corpus['text']):
    # Declaring empty list to store the words that follow the rules for this step
    Final_words = []
    # Initialization WordNetLemmatizer()
    word_Lemmatized = WordNetLemmatizer()
    # POS_tag function below will provide the 'tag' i.e. if the word is Noun (N) or Verb (V) or something else.
    for word, tag in pos_tag(entry):
        if word not in stopwords.words('english') and word.isalpha():
            word_Final = word_Lemmatized.lemmatize(word, tag_map[tag[0]])
            Final_words.append(word_Final)
    # The filan processed set of words for each iteration will be stored in 'text_final'
    Corpus.loc[index, 'text_final'] = str(Final_words)

# Step 5: Prepare train and test datasets

X_train, X_test, y_train, y_test = model_selection.train_test_split(Corpus['text_final'], Corpus['label'], test_size=0.3)

# Step 6: Encoding

Encoder = LabelEncoder()
y_train = Encoder.fit_transform(y_train)
y_test = Encoder.fit_transform(y_test)

# Step 7: Word Vectorization

Tfidf_vec = TfidfVectorizer(max_features=5000)
Tfidf_vec.fit(Corpus['text_final'])

X_train_tfidf = Tfidf_vec.transform(X_train)
X_test_tfidf = Tfidf_vec.transform(X_test)

print(Tfidf_vec.vocabulary_)
print(X_train_tfidf)

# Step 7: Use the ML algorithms to predict the outcome

# fit the training dataset on the NB classifier
Naive = naive_bayes.MultinomialNB()
Naive.fit(X_train_tfidf, y_train)

# predict the labels on validation dataset
predictions_NB = Naive.predict(X_test_tfidf)

# Use accuracy_score function to get the accuracy
print('Naive Bayes Accuracy Score ->', accuracy_score(predictions_NB, y_test) * 100)

# Classifier: SVM
# fit the training dataset on the SVM Classifier
SVM = svm.SVC(C=1.0, kernel='linear', degree=3, gamma='auto')
SVM.fit(X_train_tfidf, y_train)

# predict the labels on validation dataset
predictions_SVM = SVM.predict(X_test_tfidf)

# Use accuracy_score function to get the accuracy
print('SVM Accuracy Score->', accuracy_score(predictions_SVM, y_test) * 100)