import random

import time
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.svm import LinearSVC
from sklearn import metrics
import csv
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.cross_validation import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.grid_search import GridSearchCV

def get_topic_list(topic_name):
    with open('csv/' + topic_name + '.csv','rb') as f:
        reader = csv.reader(f)
        return [tuple(row) for row in reader]

def get_full_list(topics):
    full_list = []
    for topic in topics:
        topic_list = get_topic_list(topic)
        full_list += topic_list

    return full_list

def split_train_test(full_list):
    # sample = random.sample(full_list, 33000)
    # X = [sent[0] for sent in sample]
    # y = [sent[1] for sent in sample]

    X = [sent[0] for sent in full_list]
    y= [sent[1] for sent in full_list]


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    return (X_train, y_train, X_test, y_test)


topics = ['tech', 'sport', 'entertainment', 'business', 'society']
time0 = time.time()
full_list = get_full_list(topics)
(X_train, y_train, X_test, y_test) = split_train_test(full_list)

print("--- %s preprocess time ---" % (time.time() - time0))

# vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english')
vectorizer = TfidfVectorizer(max_df=0.3, stop_words='english')

""" Pipeline: raw text ==> TFIDF ==> Linear SVM ==> banner """
pl = Pipeline([
   ('vectorizer', TfidfVectorizer(stop_words='english')),
   ('classifier', MultinomialNB(alpha=.01))
   ])

parameters = {'vectorizer__use_idf':[False, True],
              # 'vectorizer__ngram_range':[(1,3)],
              'vectorizer__max_df':[0.3, 0.4, 0.5, 0.8],
              # 'vectorizer__sublinear_tf':[True, False]
              }

""" GridSearch w/ cross-validation """
n_cores = 1
grid_search = GridSearchCV(pl, parameters)
grid_search.fit(X_train, y_train)  #Search the best parameter setting

print 'f1 score : %.2f%%' % (grid_search.best_score_*100)
print("Best parameter set:")
best_parameters = grid_search.best_estimator_.get_params()
for param_name in sorted(parameters.keys()):
    print("\t%s: %r" % (param_name, best_parameters[param_name]))

clf_best = grid_search.best_estimator_

