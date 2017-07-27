
import csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from collections import defaultdict

cvec = CountVectorizer(stop_words='english', min_df=1, max_df=0.5, ngram_range=(1,2))
tf = TfidfVectorizer(analyzer='word', min_df = 0, stop_words = 'english')

def get_topic_list(topic_name):
    with open('csv/' + topic_name + '.csv','rb') as f:
        reader = csv.reader(f)
        news_list = []
        for row in reader:
            news_list.append(tuple(row))
        return news_list

def get_full_list(topics):
    full_list = []
    for topic in topics:
        topic_list = get_topic_list(topic)
        full_list += topic_list

    return full_list

def selection(topic):
    corpus = [sent[0] for sent in get_topic_list(topic)]
    tfidf_matrix = tf.fit_transform(corpus)
    feature_names = tf.get_feature_names()
    features_by_gram = defaultdict(list)

    for f, w in zip(feature_names, tf.idf_):
        features_by_gram[len(f.split(' '))].append((f, w))

    top_n = 1000

    for gram, features in features_by_gram.iteritems():
        top_features = sorted(features, key=lambda x: x[1], reverse=True)[:top_n]
        top_features = [f[0] for f in top_features]
        print '{}-gram top:'.format(gram), top_features

# topics = ['tech', 'sport', 'entertainment', 'business', 'society']
# for topic in topics:
#     selection(topic)

selection('tech')