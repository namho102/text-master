import random

import time
from nltk import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.svm import LinearSVC
from sklearn import metrics

def get_topic_list(topic_name):
    with open(topic_name + '.txt','rU') as f:
        raw = f.read().decode('utf-8').encode("ascii", "ignore")
        # very simple tokenize
        # sentence_list = raw.split('.')

        sentence_list = sent_tokenize(raw)
        group_number = 3
        cnt = 0
        group_sentences = []
        while (cnt + group_number < len(sentence_list)):
            para = ''
            for i in range(cnt, group_number + cnt):
                para += sentence_list[i] + ' '
            cnt += group_number
            # group_sentences.append((sub(' +', ' ', para), topic_name))
            group_sentences.append((" ".join(para.split()), topic_name))

        # print group_sentences[:10]
        return group_sentences

        # return [(s, topic_name) for s in sentence_list]

def get_full_list(topics):
    full_list = []
    for topic in topics:
        topic_list = get_topic_list(topic)
        full_list += topic_list

    return full_list

def split_train_test(full_list, size):

    sample = random.sample(full_list, size)
    # sample = full_list
    split_length = int(round(len(sample) * 0.7))

    train_data = sample[0:split_length]
    test_data = sample[split_length:]
    X_train = [sent[0] for sent in train_data]
    y_train = [sent[1] for sent in train_data]
    X_test = [sent[0] for sent in test_data]
    y_test = [sent[1] for sent in test_data]
    return (X_train, y_train, X_test, y_test)


topics = ['tech', 'sport', 'entertainment', 'business', 'society']
time0 = time.time()
full_list = get_full_list(topics)
(X_train, y_train, X_test, y_test) = split_train_test(full_list, len(full_list))

print("--- %s preprocess time ---" % (time.time() - time0))
# print(X_test[:10])
# print(y_test[:10])

vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english')
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test )

# clf = BernoulliNB(alpha=.01)
clf = MultinomialNB(alpha=.01)
# clf = LinearSVC(penalty='l1', dual=False, tol=1e-3)
time1 = time.time()
clf.fit(X_train, y_train)

print("--- %s train time ---" % (time.time() - time1))
pred = clf.predict(X_test)

# print("test time:  %0.3fs" % test_time)

score = metrics.accuracy_score(y_test, pred)
print("accuracy:   %0.3f" % score)

my_test = ["Yesterday, Amazon and Whole Foods ruined a perfectly slow news day on a Friday in June with the announcement that Amazon intends to buy Whole Foods for almost $14 billion.",
           "Whenever a product is updated, there inevitably are people who grumble about change and wish things had stayed the same.",
           "He'll sell you solar rooftop tiles to generate electricity, a giant battery to store all that energy and an electric car to suck it up.",
           "Giroud scored 16 goals last season, but started only 11 Premier League matches with manager Arsene Wenger preferring to deploy Alexis Sanchez in a central striking role.",
           "A bidding war is set to break out as Cristiano Ronaldo's Bernabeu exit beckons.",
           "Instead, there could be two periods of 30 minutes with the clock stopped whenever the ball goes out of play.",
           "If you've been watching any of the hottest TV properties this season, you might have noticed that bludgeoning is kind of the new black.",
           "Adele Fans Unite for Tribute Performances of Her Songs After She Cancels Concerts",
           "A fortnight ago, fashion's glitterati were saluting the enduring legacy of Alexandra Shulman at Vogue.",
           "Koch Brothers Net Worth: How Much Money Do Political Donors Have?",
           "The company suffered a year-on-year decrease in operating profits of 2.19 trillion won ($1.93 billion) in the third quarter of the 2016 fiscal year.",
           "Carillion's shares plunged after the company announced that results would be below expectations, and that CEO Richard Howson was stepping down.",
           "U.S. issues travel advisory for India amid fears of Islamic State attacks",
           "Kaine on Thursday voted to give Mattis a waiver that will allow him to bypass the requirement that Defense secretaries be out of uniform for at least seven years.",
           "Leaders are expected to brief rank-and-file Republican senators Tuesday during their weekly lunch on revisions they have made to the legislation."
           ]



my_pred = clf.predict(vectorizer.transform(my_test))
print my_pred


