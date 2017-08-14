from sklearn.externals import joblib
import random
import time
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.svm import LinearSVC
from sklearn import metrics
import csv
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.cross_validation import train_test_split

def get_topic_list(topic_name):
    with open('new_new_csv/' + topic_name + '.csv','rb') as f:
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
    #
    # X = [sent[0] for sent in full_list]
    # y= [sent[1] for sent in full_list]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)
    return (X_train, y_train, X_test, y_test)


topics = ['tech', 'sport', 'entertainment', 'business', 'society']
time0 = time.time()
full_list = get_full_list(topics)
(X_train, y_train, X_test, y_test) = split_train_test(full_list)
# print(len(y_train))
# print(len(y_test))

print("--- %s preprocess time ---" % (time.time() - time0))

vectorizer = TfidfVectorizer(max_df=0.3, stop_words='english')
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test )

joblib.dump(vectorizer, 'vectorizer2.pk')

# clf = BernoulliNB(alpha=.01)
clf = MultinomialNB(alpha=.01)
# clf = LinearSVC(penalty='l2', dual=False, tol=1e-3)
time1 = time.time()
clf.fit(X_train, y_train)

filename = 'finalized_model2.sav'
joblib.dump(clf, filename)






