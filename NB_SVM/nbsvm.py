import sys
import os
import pandas as pd
import argparse
from sklearn.pipeline import Pipeline
from scipy.sparse import csr_matrix
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score

import six
from abc import ABCMeta
import numpy as np
from scipy import sparse
from scipy.sparse import issparse
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils import check_X_y, check_array
from sklearn.utils.extmath import safe_sparse_dot
from sklearn.preprocessing import normalize, binarize, LabelBinarizer
from sklearn.svm import LinearSVC
import random
import csv
import time

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




class NBSVM(six.with_metaclass(ABCMeta, BaseEstimator, ClassifierMixin)):
    def __init__(self, alpha=1.0, C=1.0, max_iter=10000):
        self.alpha = alpha
        self.max_iter = max_iter
        self.C = C
        self.svm_ = []  # fuggly

    def fit(self, X, y):
        X, y = check_X_y(X, y, 'csr')
        _, n_features = X.shape

        labelbin = LabelBinarizer()
        Y = labelbin.fit_transform(y)
        self.classes_ = labelbin.classes_
        if Y.shape[1] == 1:
            Y = np.concatenate((1 - Y, Y), axis=1)

        # LabelBinarizer().fit_transform() returns arrays with dtype=np.int64.
        # so we don't have to cast X to floating point
        Y = Y.astype(np.float64)

        # Count raw events from data
        n_effective_classes = Y.shape[1]
        self.class_count_ = np.zeros(n_effective_classes, dtype=np.float64)
        self.ratios_ = np.full((n_effective_classes, n_features), self.alpha,
                               dtype=np.float64)
        self._compute_ratios(X, Y)

        # flugglyness
        for i in range(n_effective_classes):
            X_i = X.multiply(self.ratios_[i])
            svm = LinearSVC(C=self.C, max_iter=self.max_iter)
            Y_i = Y[:, i]
            svm.fit(X_i, Y_i)
            self.svm_.append(svm)

        return self

    def predict(self, X):
        n_effective_classes = self.class_count_.shape[0]
        n_examples = X.shape[0]

        D = np.zeros((n_effective_classes, n_examples))

        for i in range(n_effective_classes):
            X_i = X.multiply(self.ratios_[i])
            D[i] = self.svm_[i].decision_function(X_i)

        return self.classes_[np.argmax(D, axis=0)]

    def _compute_ratios(self, X, Y):
        """Count feature occurrences and compute ratios."""
        if np.any((X.data if issparse(X) else X) < 0):
            raise ValueError("Input X must be non-negative")

        self.ratios_ += safe_sparse_dot(Y.T, X)  # ratio + feature_occurrance_c
        normalize(self.ratios_, norm='l1', axis=1, copy=False)
        row_calc = lambda r: np.log(np.divide(r, (1 - r)))
        self.ratios_ = np.apply_along_axis(row_calc, axis=1, arr=self.ratios_)
        check_array(self.ratios_)
        self.ratios_ = sparse.csr_matrix(self.ratios_)

        # p_c /= np.linalg.norm(p_c, ord=1)
        # ratios[c] = np.log(p_c / (1 - p_c))


def f1_class(pred, truth, class_val):
    n = len(truth)

    truth_class = 0
    pred_class = 0
    tp = 0

    for ii in range(0, n):
        if truth[ii] == class_val:
            truth_class += 1
            if truth[ii] == pred[ii]:
                tp += 1
                pred_class += 1
                continue;
        if pred[ii] == class_val:
            pred_class += 1

    precision = tp / float(pred_class)
    recall = tp / float(truth_class)

    return (2.0 * precision * recall) / (precision + recall)


def semeval_senti_f1(pred, truth, pos=2, neg=0):
    f1_pos = f1_class(pred, truth, pos)
    f1_neg = f1_class(pred, truth, neg)

    return (f1_pos + f1_neg) / 2.0;


def main(train_file, test_file, ngram=(1, 3)):
    print('loading...')

    topics = ['tech', 'sport', 'entertainment', 'business', 'society']
    full_list = get_full_list(topics)
    print(len(full_list))
    (X_train, y_train, X_test, y_test) = split_train_test(full_list, 50000)

    print('vectorizing...')
    vect = CountVectorizer()
    classifier = NBSVM()

    # create pipeline
    clf = Pipeline([('vect', vect), ('nbsvm', classifier)])
    params = {
        'vect__token_pattern': r"\S+",
        'vect__ngram_range': ngram,
        'vect__binary': True
    }
    clf.set_params(**params)

    # X_train = vect.fit_transform(train['text'])
    # X_test = vect.transform(test['text'])



    print('fitting...')
    time1 = time.time()
    clf.fit(X_train, y_train)
    print("--- %s fitting time ---" % (time.time() - time1))

    print('classifying...')
    pred = clf.predict(X_test)

    print('testing...')
    acc = accuracy_score(y_test, pred)
    # f1 = semeval_senti_f1(pred, y_test)
    print('NBSVM: acc=%f' % acc)
    # print('NBSVM: acc=%f, f1=%f' % (acc, f1))
    my_test = [
        "Yesterday, Amazon and Whole Foods ruined a perfectly slow news day on a Friday in June with the announcement that Amazon intends to buy Whole Foods for almost $14 billion.",
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
    my_pred = clf.predict(my_test)
    print my_pred

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run NBSVM.')
    parser.add_argument('--train', help='path of the train tsv')
    parser.add_argument('--test', help='path of the test tsv')
    parser.add_argument('--ngrams', help='N-grams considered e.g. 1,3 is uni+bi+tri-grams')
    args = parser.parse_args()

    if args.ngrams:
        ngrams = tuple([int(x) for x in args.ngrams.split(',')])
    else:
        ngrams = (1, 3)

    if not args.train or not args.test:
        print('try --help')

    main(args.train, args.test, ngrams)