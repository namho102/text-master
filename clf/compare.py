import time
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
import csv

def get_data(type, ratio=1):
    x = []
    y = []

    row_count = 0
    with open('data/' + type + '.csv', 'rb') as f:
        reader = csv.reader(f)
        row_count = sum(1 for row in reader)
        if ratio != 1:
            row_count = int(row_count*ratio)
    with open('data/' + type + '.csv', 'rb') as f:
        reader = csv.reader(f)
        count = 0
        for row in reader:
            if count < row_count:
                x.append(row[0])
                y.append(row[1])
                count = count + 1

        return x, y



X_train, y_train = get_data('train', 0.7)
# X_train, y_train = get_data('train')
X_test, y_test = get_data('test')
print(len(y_train))
print(len(y_test))

vectorizer = TfidfVectorizer(max_df=0.3, stop_words='english')
# vectorizer = CountVectorizer(max_df=0.3, stop_words='english')
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

clf = MultinomialNB(alpha=.01)
time1 = time.time()
clf.fit(X_train, y_train)

print("--- %s train time ---" % (time.time() - time1))
pred = clf.predict(X_test)

score = metrics.accuracy_score(y_test, pred)
print("accuracy:   %0.3f" % score)




