import random
import time


from textblob.classifiers import NaiveBayesClassifier

start_time = time.time()

file1 = open('sport.txt', 'r')
text1 = file1.read().decode('utf-8').encode("ascii", "ignore")

file2 = open('tech.txt', 'r')
text2 = file2.read().decode('utf-8').encode("ascii", "ignore")


# sport_list = text1.strip().replace('\n', '').split('.')
# tech_list = text2.strip().replace('\n', ' ').split('.')
sport_list = text1.strip().split('.')
tech_list = text2.strip().split('.')
# print(sport_list[15:100])
# print(len(sport_list))
# print(len(tech_list))

arr = []
for i in range(0, 5000, 3):
    arr.append((sport_list[i] + ' ' + sport_list[i + 1] + ' ' + sport_list[i + 2], 'Sport'))
    arr.append((tech_list[i] + ' ' + tech_list[i + 1] + ' ' + tech_list[i + 2], 'Tech'))
#
# arr = []
# for i in range(0, 5000, 2):
#     arr.append((sport_list[i] + sport_list[i + 1], 'Sport'))
#     arr.append((tech_list[i] + tech_list[i + 1], 'Tech'))

sample = random.sample(arr, 2000)
train = sample[0:300]
test = sample[1900:2000]

# test = []
# for i in range(4000, 4300, 3):
#     test.append((sport_list[i], 'Sport'))
#     test.append((tech_list[i], 'Tech'))

# train = sample[0:1500]
# test = sample[1900:2000]

# train = sample[0:500]
# test = sample[1900:2000]


# print len(train)
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

print("--- %s classify time ---" % (time.time() - start_time))

start_time = time.time()
print(cl.accuracy(test)) # 93%
print("--- %s accuracy time ---" % (time.time() - start_time))