import codecs
import re
from nltk import word_tokenize

stop_words = []
with open('stop-word-list.txt') as f:
    content = f.readlines()

stop_words = [x.strip() for x in content]
appostophes = [u"\'s", u"\'ve", u"\'re", u"n\'t", u"\'t", u"\'ll", u"\'m",
               u"\u201c", u"\u201d", u"\u2019", u"\u2014", u"\u2018"]

stop_words += appostophes
# stop_words = set(stop_words)
# print(stop_words)

def clean_text(topic_name):
    with open(topic_name + '.txt', 'r') as file:
        text = file.read().decode("utf8")

    # text1 = " ".join(re.findall('[A-Z][^A-Z]*', text1))
    # text1 = re.sub("^\d+\s|\s\d+\s|\s\d+$", " ", text1)
    # print re.sub(r'\b\d+(?:\.\d+)?\s+', '', text1)
    print(repr(text))
    # text = re.sub(u"(\u2018|\u2019)", "'", text)ort

    text = ' '.join([word for word in word_tokenize(text) if word not in stop_words])
    print(repr(text))
    # for a in appostophes:
    #     text = text.replace(a, '')


    # print(repr(text))
    # print(text)
    text = text.encode('ascii','ignore')
    out = open(topic_name + '_.txt', 'w')
    out.write(text)

clean_text('tech')