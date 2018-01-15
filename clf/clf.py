import random
import time
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
import csv
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split


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
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)
    return X_train, y_train, X_test, y_test


topics = ['business', 'culture', 'society', 'sport', 'tech']
time0 = time.time()
full_list = get_full_list(topics)
# (X_train, y_train, X_test, y_test) = split_train_test(full_list)
list_len = len(full_list)

(X_train, y_train, X_test, y_test) = split_train_test(full_list, 0.3)
print(len(y_train))
print(len(y_test))

print("--- %s preprocess time ---" % (time.time() - time0))

vectorizer = TfidfVectorizer(max_df=0.3, stop_words='english')
# vectorizer = CountVectorizer(max_df=0.3, stop_words='english')
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

# clf = BernoulliNB(alpha=.01)
clf = MultinomialNB(alpha=.01)
# clf = LinearSVC(penalty='l2', dual=False, tol=1e-3)
time1 = time.time()
clf.fit(X_train, y_train)

print("--- %s train time ---" % (time.time() - time1))
pred = clf.predict(X_test)


# print("test time:  %0.3fs" % test_time)

score = metrics.accuracy_score(y_test, pred)
print("accuracy:   %0.3f" % score)

print(classification_report(y_test, pred, target_names=topics))
print(confusion_matrix(y_test, pred))

my_test = ["VR's mind tricks can teleport you into a Pixar-like world where your role and smart characters suck you deeper into the story.",
           "Nuclear radiation rearranges the electrons in insulators such as brick, glass and porcelain.",
           "He'll sell you solar rooftop tiles to generate electricity, a giant battery to store all that energy and an electric car to suck it up.",
           "Giroud scored 16 goals last season, but started only 11 Premier League matches with manager Arsene Wenger preferring to deploy Alexis Sanchez in a central striking role.",
           "A bidding war is set to break out as Cristiano Ronaldo's Bernabeu exit beckons.",
           "Instead, there could be two periods of 30 minutes with the clock stopped whenever the ball goes out of play.",
           "If you've been watching any of the hottest TV properties this season, you might have noticed that bludgeoning is kind of the new black.",
           "Adele Fans Unite for Tribute Performances of Her Songs After She Cancels Concerts",
           "A fortnight ago, fashion's glitterati were saluting the enduring legacy of Alexandra Shulman at Vogue.",
           "Founded in Malaysia in 2012, it offers private car, motorbike, taxi, and carpooling services and holds 95% market share of third-party taxi hailing in the region, operating nearly 3 million daily rides.",
           "The company suffered a year-on-year decrease in operating profits of 2.19 trillion won ($1.93 billion) in the third quarter of the 2016 fiscal year.",
           "Carillion's shares plunged after the company announced that results would be below expectations, and that CEO Richard Howson was stepping down.",
           "U.S. issues travel advisory for India amid fears of Islamic State attacks",
           "Kaine on Thursday voted to give Mattis a waiver that will allow him to bypass the requirement that Defense secretaries be out of uniform for at least seven years.",
           "Leaders are expected to brief rank-and-file Republican senators Tuesday during their weekly lunch on revisions they have made to the legislation."
           ]


my_pred = clf.predict(vectorizer.transform(my_test))
print my_pred


