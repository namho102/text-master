import csv
import time
import random
from textblob.classifiers import NaiveBayesClassifier


def classify(news_list):
    news_list = random.sample(news_list, 1000)
    # news_list = random.sample(news_list, len(news_list))
    length = int(round(len(news_list)*0.7))
    train = news_list[:length]
    test = news_list[length:]

    # print len(train)
    print('Tring . . .')
    start_time = time.time()

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

    print("--- %s classify time ---" % (time.time() - start_time))

    start_time = time.time()
    print(cl.accuracy(test))  # 93%
    print("--- %s accuracy time ---" % (time.time() - start_time))



with open('news.csv', 'rb') as f:
    reader = csv.reader(f)
    news_list = []
    for row in reader:
        news_list.append(tuple(row))

    classify(news_list)








# start_time = time.time()
#
# # print len(train)
# print('Modelling . . .')
#
# cl = NaiveBayesClassifier(train)
#
# print("--- %s train time ---" % (time.time() - start_time))
# # cl.show_informative_features(5)
# start_time = time.time()
#
# print(cl.classify("Yesterday, Amazon and Whole Foods ruined a perfectly slow news day on a Friday in June with the announcement that Amazon intends to buy Whole Foods for almost $14 billion."))
# print(cl.classify("Whenever a product is updated, there inevitably are people who grumble about change and wish things had stayed the same."))
# print(cl.classify("He'll sell you solar rooftop tiles to generate electricity, a giant battery to store all that energy and an electric car to suck it up."))
# print(cl.classify("Giroud scored 16 goals last season, but started only 11 Premier League matches with manager Arsene Wenger preferring to deploy Alexis Sanchez in a central striking role."))
# print(cl.classify("A bidding war is set to break out as Cristiano Ronaldo's Bernabeu exit beckons."))
# print(cl.classify("Instead, there could be two periods of 30 minutes with the clock stopped whenever the ball goes out of play."))
#
# print("--- %s classify time ---" % (time.time() - start_time))
#
# start_time = time.time()
# print(cl.accuracy(test)) # 93%
# print("--- %s accuracy time ---" % (time.time() - start_time))