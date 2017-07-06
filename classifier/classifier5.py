import random

import time
from nltk import tokenize
from textblob.classifiers import NaiveBayesClassifier
from re import sub

topics = ['sport', 'entertainment', 'tech']

def read_file(topic_name):
    with open(topic_name + '.txt','rU') as f:
        raw = f.read().decode('utf-8').encode("ascii", "ignore")
        sentence_list = tokenize.sent_tokenize(raw)
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

def get_full_list(topics):
    full_list = []
    for topic in topics:
        topic_list = read_file(topic)
        full_list += topic_list

    return full_list


start_time = time.time()

full_list = get_full_list(topics)
print(len(full_list))
sample = random.sample(full_list, 1000)
split_length = int(round(len(sample)*0.7))
# train - test 7/3
train = sample[0:split_length]
test = sample[split_length:]

print("--- %s preprocess time ---" % (time.time() - start_time))

start_time = time.time()

print('Modelling . . .')

cl = NaiveBayesClassifier(train)

print("--- %s train time ---" % (time.time() - start_time))
# cl.show_informative_features(5)
start_time = time.time()

print(cl.classify("Yesterday, Amazon and Whole Foods ruined a perfectly slow news day on a Friday in June with the announcement that Amazon intends to buy Whole Foods for almost $14 billion."))
print(cl.classify("Whenever a product is updated, there inevitably are people who grumble about change and wish things had stayed the same."))
print(cl.classify("He'll sell you solar rooftop tiles to generate electricity, a giant battery to store all that energy and an electric car to suck it up."))
print(cl.classify("Giroud scored 16 goals last season, but started only 11 Premier League matches with manager Arsene Wenger preferring to deploy Alexis Sanchez in a central striking role."))
print(cl.classify("A bidding war is set to break out as Cristiano Ronaldo's Bernabeu exit beckons."))
print(cl.classify("Instead, there could be two periods of 30 minutes with the clock stopped whenever the ball goes out of play."))
print(cl.classify("If you've been watching any of the hottest TV properties this season, you might have noticed that bludgeoning is kind of the new black."))
print(cl.classify("Adele Fans Unite for Tribute Performances of Her Songs After She Cancels Concerts"))
print(cl.classify("Hit the road: your art on the theme of transportation"))

print("--- %s classify time ---" % (time.time() - start_time))
#
start_time = time.time()
print(cl.accuracy(test)) # 74.6
print("--- %s accuracy time ---" % (time.time() - start_time))
