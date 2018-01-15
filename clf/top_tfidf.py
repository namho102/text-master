import csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from collections import defaultdict
import pandas as pd


def get_topic_list(topic_name):
    with open('csv/' + topic_name + '.csv','rb') as f:
        reader = csv.reader(f)
        news_list = []
        for row in reader:
            news_list.append(tuple(row))
        return news_list

def top_tfidf_feats(row, features, top_n=25):
    ''' Get top n tfidf values in row and return them with their corresponding feature names.'''
    topn_ids = np.argsort(row)[::-1][:top_n]
    top_feats = [(features[i], row[i]) for i in topn_ids]
    df = pd.DataFrame(top_feats)
    df.columns = ['feature', 'tfidf']
    return df

def selection(topic):
    X = [sent[0] for sent in get_topic_list(topic)]
    vec_pipe = TfidfVectorizer(max_df=0.3, stop_words='english')

    Xtr = vec_pipe.fit_transform(X)
    # vec = vec_pipe.named_steps['vec']
    features = vec_pipe.get_feature_names()

    row = np.squeeze(Xtr[0].toarray())
    print top_tfidf_feats(row, features, 25)


selection('culture')