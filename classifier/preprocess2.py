
import csv
import random


def write_csv(topic):
    with open(topic + '.txt','r') as f:
        text = f.read().decode('utf-8').encode("ascii", "ignore")

        nums = [1, 1, 2, 2, 3, 3, 5]
        # random.choice(mylist)
        with open('news.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)

            setence_list = text.strip().replace('\n', '').split('.')

            cnt = 0

            while (cnt + 5 < len(setence_list)):
                para = ''
                number_sentence = random.choice(nums)
                for i in range(cnt, number_sentence + cnt):
                    para += setence_list[i] + ' '
                cnt += number_sentence
                if len(para.strip(' ')) > 0:
                    if para[0].isalpha() and para[0].isupper():
                        writer.writerow((para, topic))

write_csv('sport')