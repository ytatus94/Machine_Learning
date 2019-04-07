# https://towardsdatascience.com/machine-learning-nlp-text-classification-using-scikit-learn-python-and-nltk-c52b92a7c73a

# load data

from sklearn.datasets import fetch_20newsgroups

twenty_train = fetch_20newsgroups(subset='train', shuffle=True)

twenty_train.target_names # prints all the categories

print('\n'.join(twenty_train.data[0].split('\n')[:3])) # prints first line of the first data file

# feature extraction

# Bag of words

from sklearn.feature_extraction.text import CountVectorizer

count_vect = CountVectorizer()

X_train_counts = count_vect.fit_transform(twenty_train.data)

X_train_counts.shape

# tf-idf

from sklearn.feature_extraction.text import TfidfTransformer

tfidf_transformer = TfidfTransformer()

X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

X_train_tfidf.shape

# Build model

# Naive Bayes

from sklearn.naive_bayes import MultinomialNB

clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target)

# Building the pipeline

from sklearn.pipeline import Pipeline

text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf', MultinomialNB())
                    ])

text_clf = text_clf.fit(twenty_train.data, twenty_train.target)

# Performance

import numpy as np

twenty_test = fetch_20newsgroups(subset='test', shuffle=True)

predicted = text_clf.predict(twenty_test.data)

np.mean(predicted == twenty_test.target)

# SVM

from sklearn.linear_model import SGDClassifier

text_clf_svm = Pipeline([('vect', CountVectorizer()),
                         ('tfidf', TfidfTransformer()),
                         ('clf_svm', SGDClassifier(loss='hinge',
                                                   penalty='l2', 
                                                   alpha=1e-3,
                                                   n_iter=5,
                                                   random_state=42))
                        ])

_ = text_clf_svm.fit(twenty_train.data, twenty_train.target)

predicted_svm = text_clf_svm.predict(twenty_test.data)

np.mean(predicted_svm == twenty_test.target)

# Grid search

# Naive Bayes

from sklearn.model_selection import GridSearchCV

parameters = {'vect__ngram_range': [(1, 1), (1, 2)],
              'tfidf__use_idf': (True, False),
              'clf__alpha': (1e-2, 1e-3)
            }

gs_clf = GridSearchCV(text_clf, parameters, n_jobs=-1)

gs_clf = gs_clf.fit(twenty_train.data, twenty_train.target)

gs_clf.best_score_

gs_clf.best_params_

# Grid search

# SVM

from sklearn.model_selection import GridSearchCV

parameters_svm = {'vect__ngram_range': [(1, 1), (1, 2)],
                  'tfidf__use_idf': (True, False),
                  'clf_svm__alpha': (1e-2, 1e-3)
                 }

gs_clf_svm = GridSearchCV(text_clf_svm, parameters_svm, n_jobs=-1)

gs_clf_svm = gs_clf_svm.fit(twenty_train.data, twenty_train.target)

gs_clf_svm.best_score_

gs_clf_svm.best_params_

# Remove stopwords

# Naive Bayes

from sklearn.pipeline import Pipeline

text_clf = Pipeline([('vect', CountVectorizer(stop_words='english')),
                     ('tfidf', TfidfTransformer()),
                     ('clf', MultinomialNB())
                    ])

text_clf = text_clf.fit(twenty_train.data, twenty_train.target)

predicted = text_clf.predict(twenty_test.data)

np.mean(predicted == twenty_test.target)

# SVM

text_clf_svm = Pipeline([('vect', CountVectorizer(stop_words='english')),
                         ('tfidf', TfidfTransformer()),
                         ('clf_svm', SGDClassifier(loss='hinge',
                                                   penalty='l2', 
                                                   alpha=1e-3,
                                                   n_iter=5,
                                                   random_state=42))
                        ])

text_clf_svm.fit(twenty_train.data, twenty_train.target)

predicted_svm = text_clf_svm.predict(twenty_test.data)

np.mean(predicted_svm == twenty_test.target)

# Naive Bayes with fit_prior=False

text_clf = Pipeline([('vect', CountVectorizer(stop_words='english')),
                     ('tfidf', TfidfTransformer()),
                     ('clf', MultinomialNB(fit_prior=False))
                    ])

text_clf = text_clf.fit(twenty_train.data, twenty_train.target)

predicted = text_clf.predict(twenty_test.data)

np.mean(predicted == twenty_test.target)

# Stemming

import nltk

nltk.download()

from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer('english', ignore_stopwords=True)

class StemmedCountVectorizer(CountVectorizer):
    def build_analyzer(self):
        analyzer = super(StemmedCountVectorizer, self).build_analyzer()
        return lambda doc: ([stemmer.stem(w) for w in analyzer(doc)])

stemmed_count_vect  = StemmedCountVectorizer(stop_words='english')

# Naive Bayes

text_mnb_stemmed = Pipeline([('vect', stemmed_count_vect),
                             ('tfidf', TfidfTransformer()),
                             ('mnb', MultinomialNB(fit_prior=False))])

text_mnb_stemmed = text_mnb_stemmed.fit(twenty_train.data, twenty_train.target)

predicted_mnb_stemmed = text_mnb_stemmed.predict(twenty_test.data)

np.mean(predicted_mnb_stemmed == twenty_test.target)

# SVM

text_svm_stemmed = Pipeline([('vect', CountVectorizer(stop_words='english')),
                             ('tfidf', TfidfTransformer()),
                             ('clf_svm', SGDClassifier(loss='hinge',
                                                       penalty='l2', 
                                                       alpha=1e-3,
                                                       n_iter=5,
                                                       random_state=42))
                            ])

text_svm_stemmed.fit(twenty_train.data, twenty_train.target)

predicted_svm_stemmed = text_svm_stemmed.predict(twenty_test.data)

np.mean(predicted_svm_stemmed == twenty_test.target)