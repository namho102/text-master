import random

import time
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.svm import LinearSVC
import csv
from sklearn.cross_validation import train_test_split

def get_topic_list(topic_name):
    with open('new_csv/' + topic_name + '.csv','rb') as f:
        reader = csv.reader(f)
        return [tuple(row) for row in reader]

def get_full_list(topics):
    full_list = []
    for topic in topics:
        topic_list = get_topic_list(topic)
        full_list += topic_list

    return full_list

def split_train_test(full_list):
    sample = random.sample(full_list, len(full_list))
    X = [sent[0] for sent in sample]
    y = [sent[1] for sent in sample]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    return (X_train, y_train, X_test, y_test)


topics = ['tech', 'sport', 'entertainment', 'business', 'society']
full_list = get_full_list(topics)
(X_train, y_train, X_test, y_test) = split_train_test(full_list)


vectorizer = TfidfVectorizer(max_df=0.3, stop_words='english')
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test )

# clf = BernoulliNB(alpha=.01)
clf = MultinomialNB(alpha=.01)
# clf = LinearSVC()

clf.fit(X_train, y_train)

def validate(topic):
    data = get_topic_list(topic)
    print(len(data))
    X = [sent[0] for sent in data]
    my_pred = clf.predict(vectorizer.transform(X))
    with open('new_new_csv/' + topic + '.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile)
        for i in range(0, len(my_pred)):
            if my_pred[i] == topic:
                writer.writerow((data[i][0], topic))


for topic in topics:
    validate(topic)

