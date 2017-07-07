import codecs
import re

stop_words = []
with open('stop-word-list.txt') as f:
    content = f.readlines()

stop_words = [x.strip() for x in content]
appostophes = ["\'s", "\'ve", "\'re", "\'t", "\'ll", "\'m"]
# appostophes = ["\'s", "\'ve", "\'re", "\'t", "\'ll", "\'m", u"\u2018", u"\u2019", u"\u2019s", u"\u2019ve", u"\u2019re",
#                u"\u2019\t", u"\u2019ll", u"\u2019m"]
# stop_words += appostophes
# stop_words = set(stop_words)
# print(stop_words)

def clean_text(topic_name):
    with open(topic_name + '.txt', 'r') as file:
        text = file.read().decode("utf8")

    # text1 = " ".join(re.findall('[A-Z][^A-Z]*', text1))
    # text1 = re.sub("^\d+\s|\s\d+\s|\s\d+$", " ", text1)
    # print re.sub(r'\b\d+(?:\.\d+)?\s+', '', text1)
    print(repr(text))
    text = re.sub(u"(\u2018|\u2019)", "'", text)
    text = ' '.join([word for word in text.split() if word not in stop_words])
    for a in appostophes:
        text = text.replace(a, '')


    print(repr(text))
    print(text)
    text = text.encode('ascii','ignore')
    out = open(topic_name + '_.txt', 'w')
    out.write(text)

clean_text('text')