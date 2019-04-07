# https://www.toptal.com/machine-learning/nlp-tutorial-text-classification

# Dataset
# https://www.kaggle.com/zynicide/wine-reviews

# Naive Bayes

import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfTransformer

df = pd.read_csv('winemag-data-130k-v2.csv')

df.head()

df.info()

counter = Counter(df['variety'].tolist())
top_10_varieties = {i[0]: idx for idx, i in enumerate(counter.most_common(10))}
df = df[df['variety'].map(lambda x: x in top_10_varieties)]

description_list = df['description'].tolist()
varietal_list = [top_10_varieties[i] for i in df['variety'].tolist()]
varietal_list = np.array(varietal_list)

count_vect = CountVectorizer()
x_train_counts = count_vect.fit_transform(description_list)

tfidf_transformer = TfidfTransformer()
x_train_tfidf = tfidf_transformer.fit_transform(x_train_counts)

X_train, X_test, y_train, y_test = train_test_split(x_train_tfidf, varietal_list, test_size=0.3)

clf = MultinomialNB().fit(X_train, y_train)
# clf = SVC(kernel='linear').fit(X_train, y_train)
y_score = clf.predict(X_test)

n_right = 0
for i in range(len(y_score)):
    if y_score[i] == y_test[i]:
        n_right += 1

print('Accuracy: %.2f%%' % ((n_right / float(len(y_test)) * 100)))

# Building Deep Learning Model

from nltk import word_tokenize
from collections import defaultdict

def count_top_x_words(corpus, top_x, skip_top_n):
    count = defaultdict(lambda: 0)
    for c in corpus:
        for w in word_tokenize(c):
            count[w] += 1

    count_tuples = sorted([(w, c) for w, c in count.items()], key=lambda x: x[1], reverse=True)
    return [i[0] for i in count_tuples[skip_top_n: skip_top_n + top_x]]

def replace_top_x_words_with_wectors(corpus, top_x):
    topx_dict = {top_x[i]: i for i in range(len(top_x))}

    return [
        [topx_dict[w] for w in word_tokenize(s) if w in topx_dict]
        for s in corpus
    ], topx_dict

def filter_to_top_x(corpus, n_top, skip_top_n=0):
    top_x = count_top_x_words(corpus, n_top, skip_top_n)
    return replace_top_x_words_with_wectors(corpus, top_x)

from keras.models import Sequential
from keras.layers import Dense, Conv1D, Flatten
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from keras.utils import to_categorical
import pandas as pd
from collections import Counter
from sklearn.model_selection import train_test_split

df2 = pd.read_csv('winemag-data-130k-v2.csv')

counter = Counter(df2['variety'].tolist())
top_10_varieties = {i[0]: idx for idx, i in enumerate(counter.most_common(10))}
df2 = df2[df2['variety'].map(lambda x: x in top_10_varieties)]

description_list = df2['description'].tolist()
mapped_list, word_list = filter_to_top_x(description_list, 2500, 10)
varietal_list_o = [top_10_varieties[i] for i in df2['variety'].tolist()]
varietal_list = to_categorical(varietal_list_o)

max_review_length = 150

mapped_list = sequence.pad_sequences(mapped_list, maxlen=max_review_length)
X_train, X_test, y_train, y_test = train_test_split(mapped_list, varietal_list, test_size=0.3)

max_review_length = 150

embedding_vector_length = 64
model = Sequential()

model.add(Embedding(2500, embedding_vector_length, input_length=max_review_length))
model.add(Conv1D(50, 5))
model.add(Flatten())
model.add(Dense(100, activation='relu'))
model.add(Dense(max(varietal_list_o) + 1, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=3, batch_size=64)

y_score = model.predict(X_test)
y_score = [[1 if i == max(sc) else 0 for i in sc] for sc in y_score]
n_right = 0
for i in range(len(y_score)):
    if all(y_score[i][j] == y_test[i][j] for j in range(len(y_score[i]))):
        n_right += 1

print('Accuracy: %.2f%%' % ((n_right / float(len(y_test)) * 100)))