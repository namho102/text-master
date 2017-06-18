import random
import time


from textblob.classifiers import NaiveBayesClassifier

file1 = open('sport.txt', 'r')
text1 = file1.read().decode('utf-8').encode("ascii", "ignore")

file2 = open('tech.txt', 'r')
text2 = file2.read().decode('utf-8').encode("ascii", "ignore")

sport_list = text1.strip().split('.')
tech_list = text2.strip().split('.')


arr = []
for i in range(0, 5000):
    arr.append((sport_list[i], 'Sport'))
    arr.append((tech_list[i], 'Tech'))

sample = random.sample(arr, 2000)

train = sample[0:1899]
test = sample[1900:2000]

# print len(train)
start_time = time.time()
cl = NaiveBayesClassifier(train)
print("--- %s seconds ---" % (time.time() - start_time))
cl.show_informative_features(5)

print(cl.classify("Reply threads on Facebook are about to get a lot more animated."))
print(cl.classify("Russia can build on opening day win"))
print(cl.accuracy(test)) # 93%
