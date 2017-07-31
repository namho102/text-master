import random

import csv

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

    split_length = int(round(len(sample) * 0.7))

    train_data = sample[0:split_length]
    test_data = sample[split_length:]

    return (train_data, test_data)

topics = ['tech', 'sport', 'entertainment', 'business', 'society']

full_list = get_full_list(topics)
(train_data, test_data) = split_train_test(full_list, len(full_list))

def write_text(corpus, name):
    out = open('text/' + name + '.txt', 'w')

    for c in corpus:
        out.write('__label__' + c[1])
        out.write(' ')
        out.write(c[0])
        out.write('\n')


write_text(train_data, 'train')
write_text(test_data, 'test')

