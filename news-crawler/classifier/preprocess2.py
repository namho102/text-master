import codecs
import csv
import random


def write_csv(topic):
    with codecs.open('topic' + '.txt','r',encoding='utf8') as f:
        text = f.read()

    nums = [1, 1, 2, 2, 3, 3, 5]
    # random.choice(mylist)
    with open('topic' + '.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile)
        for i in range(0, 100):
            writer.writerow(random.choice(nums), 55)

