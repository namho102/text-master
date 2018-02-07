import random
import time
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import csv
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib


def get_topic_list(topic_name):
    with open('validated_csv/' + topic_name + '.csv', 'rb') as f:
        reader = csv.reader(f)
        return [tuple(row) for row in reader]


def get_full_list(topics):
    full_list = []
    for topic in topics:
        topic_list = get_topic_list(topic)
        full_list += topic_list

    return full_list


def split_train_test(full_list, ratio):
    sample = random.sample(full_list, len(full_list))
    X = [sent[0] for sent in sample]
    y = [sent[1] for sent in sample]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=ratio)
    return X_train, y_train, X_test, y_test


topics = ['business', 'culture', 'society', 'sport', 'tech']

full_list = get_full_list(topics)
list_len = len(full_list)

(X_train, y_train, X_test, y_test) = split_train_test(full_list, 0.3)


vectorizer = TfidfVectorizer(max_df=0.3, stop_words='english')
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

joblib.dump(vectorizer, 'model_dump/vectorizer.pk')

clf = MultinomialNB(alpha=.01)

clf.fit(X_train, y_train)

joblib.dump(clf, 'model_dump/finalized_model.sav')



