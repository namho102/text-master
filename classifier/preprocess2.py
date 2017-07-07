
import csv
import random


def write_csv(topic):
    with open(topic + '.txt','r') as f:
        text = f.read().decode('utf-8').encode("ascii", "ignore")

        nums = [1, 1, 2, 2, 3, 3, 5]
        # random.choice(mylist)
        with open('news.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)

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
                        writer.writerow((para, topic))

write_csv('sport')