import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

tfidf = TfidfVectorizer(max_df=0.5, stop_words='english')
t = "Chinese Beijing Chinese. Chinese Chinese Shanghai. Chinese Macao. Tokyo Japan Chinese"
y = np.array([1, 1, 1, 0])
tfs = tfidf.fit_transform(t.split("."))
print tfs.toarray()
# print tfs
print '---'
str = 'Chinese Chinese Chinese Tokyo Japan'
response = tfidf.transform([str])
print response.toarray()

clf = MultinomialNB()
clf.fit(tfs, y)

print(clf.predict(response))
