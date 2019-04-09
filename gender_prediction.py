# https://pythonspot.com/natural-language-processing-prediction/

import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names

def gender_features(word):
    return {'last_letter': word[-1]}

# Data preparation

# Load data
male_names = [(name, 'male') for name in names.words('male.txt')]
female_names = [(name, 'female') for name in names.words('female.txt')]
names = male_names + female_names

# Feature extraction
featureset = [(gender_features(n), g) for (n, g) in names]
train_set = featureset

# Training and prediction
clf = nltk.NaiveBayesClassifier.train(train_set)

# Predict
print(clf.classify(gender_features('Frank')))