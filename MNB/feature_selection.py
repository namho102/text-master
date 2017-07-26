
import csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

cvec = CountVectorizer(stop_words='english', min_df=1, max_df=0.5, ngram_range=(1,2))
tf = TfidfVectorizer(analyzer='word', min_df = 0, stop_words = 'english')

def get_topic_list(topic_name):
    with open('csv/' + topic_name + '.csv','rb') as f:
        reader = csv.reader(f)
        news_list = []
        for row in reader:
            news_list.append(tuple(row))
        return news_list

def selection(topic):
    corpus = [sent[0] for sent in get_topic_list(topic)]
    tfidf_matrix = tf.fit_transform(corpus)
    feature_names = tf.get_feature_names()
    print(len(feature_names))




# topics = ['tech', 'sport', 'entertainment', 'business', 'society']
# for topic in topics:
#     selection(topic)

selection('business')