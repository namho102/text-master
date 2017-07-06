import random
import time


from textblob.classifiers import NaiveBayesClassifier



def get_topic_list(topic):
    file = open(topic + '.txt', 'r')
    text = file.read().decode('utf-8').encode("ascii", "ignore")
    topic_list = text.strip().split('.')
    return topic_list

def split_train_test(topics):
    full_list = []
    for topic in topics:
        topic_list = get_topic_list(topic)
        full_list += topic_list



# arr = []
# for i in range(0, 5000, 3):
#     arr.append((sport_list[i] + ' ' + sport_list[i + 1] + ' ' + sport_list[i + 2], 'Sport'))
#     arr.append((tech_list[i] + ' ' + tech_list[i + 1] + ' ' + tech_list[i + 2], 'Tech'))
# #
# arr = []
# for i in range(0, 5000, 2):
#     arr.append((sport_list[i] + sport_list[i + 1], 'Sport'))
# #     arr.append((tech_list[i] + tech_list[i + 1], 'Tech'))
#
# sample = random.sample(arr, 2000)
# train = sample[0:300]
# test = sample[1900:2000]
#



if __name__ == "__main__":
    start_time = time.time()
