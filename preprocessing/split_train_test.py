import random
import csv


def get_topic_list(topic_name):
    with open('csv/' + topic_name + '.csv', 'rb') as f:
        reader = csv.reader(f)
        return [tuple(row) for row in reader]


def get_full_list(topics):
    full_list = []
    for topic in topics:
        topic_list = get_topic_list(topic)
        full_list += topic_list
    return full_list


def split_train_test(full_list, ratio=0.9):
    random.shuffle(full_list)

    list_len = len(full_list)
    with open('data/train.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)

        for row in full_list[:int(list_len*ratio)]:
            writer.writerow((row[0], row[1]))

    with open('data/test.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)

        for row in full_list[int(list_len*ratio):]:
            writer.writerow((row[0], row[1]))


topics = ['business', 'culture', 'society', 'sport', 'tech']


split_train_test(get_full_list(topics))
