from collections import Counter
import csv


def export_vocabulary(topic):

    file = open('text/' + topic + '_.txt', 'r')
    text = file.read().decode('utf-8')

    topic_word = text.replace('.', " ").split()


    word_count = Counter(topic_word)
    word_count = dict(word_count.items())

    print(len(word_count))
    # print(word_count)

    # for pair in sorted(word_count, key=lambda k: k[1]) :
    #     print pair


    bigrams = []
    for i in range(len(topic_word) - 1):
        bigrams.append(topic_word[i:i+2])

    # print(bigrams[:10])

    str_bigrams = [' '.join(x) for x in bigrams]
    # print(str_bigrams[:10])
    # print(len(str_bigrams))

    gram_count = Counter(str_bigrams)

    print(len(list(gram_count.items())))
    print(gram_count.most_common(10))

    pair_count = {}


    for x in list(gram_count.items()):
        pair = x[0].split()

        if pair_count.has_key(pair[0]):
            if pair_count[pair[0]]['count'] < x[1]:
                pair_count[pair[0]] = {'follower': pair[1], 'count': x[1]}

        else:
            pair_count[pair[0]] = {'follower': pair[1], 'count': x[1]}

    print(pair_count['artificial'])
    print(len(list(pair_count.items())))
    print(list(pair_count.items())[:10])



    with open('vocabulary2/' + topic + '.csv', 'wb') as outcsv:
        writer = csv.writer(outcsv)
        writer.writerow(["Word", "Follower", "Count"])

        for pair in list(pair_count.items()):
            writer.writerow([pair[0].encode('utf-8'), pair[1]["follower"].encode('utf-8'), word_count[pair[0]]])


topics = ['tech', 'sport', 'entertainment', 'business', 'society']

for topic in topics:
    export_vocabulary(topic)
