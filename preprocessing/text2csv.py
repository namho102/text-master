import csv
import random
from nltk import sent_tokenize
import re


def write_csv(topic):
    with open('fixed/' + topic + '.txt', 'r') as f:
        text = f.read().decode('utf-8').encode("ascii", "ignore")

        nums = [2, 3, 4]
        # random.choice(mylist)
        with open('master_csv/' + topic + '.master_csv', 'wb') as csvfile:
            writer = csv.writer(csvfile)

            sentence_list = sent_tokenize(text)

            cnt = 0

            while (cnt + 5 < len(sentence_list)):
                para = ''
                number_sentence = random.choice(nums)
                for i in range(cnt, number_sentence + cnt):
                    para += sentence_list[i] + ' '
                cnt += number_sentence
                # if len(para.strip(' ')) > 0:
                # row = para.strip(' ')
                # if row[0].isalpha() or row[0] == '"':
                #     writer.writerow((row, topic))
                # print re.sub(r"^\W+|\W+$", "", para)
                writer.writerow((re.sub(r"^\W+|\W+$", "", para), topic))


topics = ['business', 'culture', 'society', 'sport', 'tech']
for topic in topics:
    write_csv(topic)
