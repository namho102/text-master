import codecs
import csv
import random


def write_csv(topic):
    with open(topic + '.txt','r') as f:
        text = f.read().decode('utf-8').encode("ascii", "ignore")

        nums = [1, 1, 2, 2, 3, 3, 5]
        # random.choice(mylist)
        with open(topic + '.csv', 'wb') as csvfile:
            writer = csv.writer(csvfile)

            setence_list = text.strip().replace('\n', '').split('.')

            cnt = 0
            while (cnt < len(setence_list)):
                para = ''
                number_setence = random.choice(nums)
                for i in range(cnt, number_setence + cnt):
                    para += setence_list[i]
                cnt += number_setence
                if len(para):
                    writer.writerow([para, number_setence])

write_csv('sport')