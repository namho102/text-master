import random
import time
from textblob.classifiers import NaiveBayesClassifier


def get_topic_list(topic_name):
    topic_list = []
    with open(topic_name + '.txt','r') as f:
        text = f.read().decode('utf-8').encode("ascii", "ignore")
        nums = [1, 1, 2, 2, 3, 3, 4]
        sentence_list = text.strip().replace('\n', '').split('.')
        cnt = 0

        while (cnt + 5 < len(sentence_list)):
            para = ''
            number_sentence = random.choice(nums)
            for i in range(cnt, number_sentence + cnt):
                para += sentence_list[i] + ' '
            cnt += number_sentence
            if len(para.strip(' ')) > 0:
                if para[0].isalpha() and para[0].isupper():
                    topic_list.append((para, topic_name))

        return topic_list


tech_list = get_topic_list('tech')
sport_list = get_topic_list('sport')

full_list = tech_list + sport_list

sample = random.sample(full_list, 1000)
split_length = int(round(len(sample)*0.7))
# train - test 7/3
train = sample[0:split_length]
test = sample[split_length:]

start_time = time.time()

print('Modelling . . .')

cl = NaiveBayesClassifier(train)

print("--- %s train time ---" % (time.time() - start_time))
# cl.show_informative_features(5)
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

while True:
    print "Enter a sentence:",
    sentence = raw_input()
    print(cl.classify(sentence))
